from __future__ import annotations

"""
激进但带护栏的 AI 自动优化器：
- 收集最近报告/日志/关键代码
- 让 Poe 代码模型生成优化建议和 unified diff
- 默认只保存 patch，不自动应用
- ALLOW_AUTO_PATCH=1 后：校验 patch -> 应用 -> 跑测试 -> 失败自动回滚
- GitHub Actions 可在测试通过后直接推送到当前分支

安全边界：
- 不允许自动交易/下单
- 不读取或修改 .env、密钥、钱包地址文件
- 只允许修改 ALLOWED_PATCH_FILES 中的文件
"""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from dotenv import load_dotenv
from wallet_ai_monitor.budget import estimate_points, usage_from_openai_response
from wallet_ai_monitor.storage import Store

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_PATCH_FILES = {
    "wallet_ai_monitor/main.py",
    "wallet_ai_monitor/hyperliquid.py",
    "wallet_ai_monitor/signals.py",
    "wallet_ai_monitor/storage.py",
    "wallet_ai_monitor/ai.py",
    "wallet_ai_monitor/budget.py",
    "wallet_ai_monitor/config.py",
    "wallet_ai_monitor/pnl.py",
    "wallet_ai_monitor/report.py",
    "wallet_ai_monitor/telegram.py",
    "wallet_ai_monitor/wallets.py",
    "tests/test_addresses.py",
    "tests/test_ai.py",
    "tests/test_budget.py",
    "tests/test_hyperliquid.py",
    "tests/test_pnl.py",
    "tests/test_signals.py",
    "tests/test_storage.py",
    "tests/test_param_optimizer.py",
    "tests/test_param_overrides_config.py",
    "tools/backtest.py",
    "tools/ai_optimizer.py",
    "tools/ai_param_optimizer.py",
    ".github/workflows/wallet-monitor.yml",    ".env.example",
}

READ_CONTEXT_FILES = sorted(ALLOWED_PATCH_FILES | {
    "requirements.txt",
    "config/ai_param_overrides.env",
    ".github/workflows/wallet-monitor.yml",})

FORBIDDEN_PATTERNS = (
    ".env",
    "POE_API_KEY",
    "TELEGRAM_BOT_TOKEN",
    "PRIVATE_KEY",
    "SECRET",
    "exchange.sign",
    "place_order",
    "order(",
    "cancel_order",
    "withdraw",
)


@dataclass
class CmdResult:
    returncode: int
    stdout: str
    stderr: str


def run_cmd(args: list[str], *, check: bool = False) -> CmdResult:
    p = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    res = CmdResult(p.returncode, p.stdout, p.stderr)
    if check and p.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(args)}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}")
    return res


def read_file(path: Path, max_chars: int = 20000) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    return text[-max_chars:]


def latest_files(pattern: str, limit: int = 3, max_chars_each: int = 12000) -> dict[str, str]:
    files = sorted((ROOT / "reports").glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]
    return {str(p.relative_to(ROOT)): read_file(p, max_chars_each) for p in files}


def collect_context() -> dict:
    git_status = run_cmd(["git", "status", "--short"]).stdout if (ROOT / ".git").exists() else ""
    last_test = run_cmd([sys.executable, "-m", "pytest", "-q"])
    files = {f: read_file(ROOT / f, 18000) for f in READ_CONTEXT_FILES}
    state_summary = {}
    db_path = ROOT / os.getenv("DB_PATH", ".state/wallet_monitor.sqlite3")
    if db_path.exists():
        try:
            with Store(db_path) as store:
                now = int(datetime.now(timezone.utc).timestamp())
                state_summary = {
                    "integrity_ok": store.integrity_ok(),
                    "health_24h": store.run_health_summary(now - 86400),
                    "health_7d": store.run_health_summary(now - 7 * 86400),
                    "estimated_points_today": store.estimated_ai_points_since(now - (now % 86400)),
                }
        except Exception as exc:  # noqa: BLE001
            state_summary = {"error": str(exc)}
    optimizer_logs = latest_files("optimizer_*.log", limit=4, max_chars_each=6000)
    return {
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "goal": (
            "优化 Hyperliquid 钱包监控脚本的稳定性、速度、AI 成本、信号质量、收益计算准确性和 GitHub 单工作流稳定性。"
            "可以大胆优化，并允许改动单工作流；但禁止加入自动交易/下单，禁止读取或修改密钥，禁止修改钱包地址文件。"
        ),
        "allowed_patch_files": sorted(ALLOWED_PATCH_FILES),
        "git_status_before": git_status,
        "pytest_before": {
            "returncode": last_test.returncode,
            "stdout": last_test.stdout[-5000:],
            "stderr": last_test.stderr[-5000:],
        },
        "latest_reports": latest_files("latest_*.json", limit=3),
        "latest_signal_json": latest_files("latest_signals.json", limit=1),
        "optimizer_logs": optimizer_logs,
        "state_summary": state_summary,
        "github_context": {
            "run_id": os.getenv("GITHUB_RUN_ID"),
            "run_number": os.getenv("GITHUB_RUN_NUMBER"),
            "ref": os.getenv("GITHUB_REF_NAME"),
            "event": os.getenv("GITHUB_EVENT_NAME"),
        },
        "files": files,
    }


def extract_patch(text: str) -> str:
    # Prefer the final diff code block.
    blocks = re.findall(r"```(?:diff|patch)?\s*\n(.*?)```", text, flags=re.S | re.I)
    diff_blocks = [b.strip() for b in blocks if "diff --git" in b or b.strip().startswith("--- ")]
    if diff_blocks:
        return diff_blocks[-1].strip() + "\n"
    if "diff --git" in text:
        return text[text.find("diff --git"):].strip() + "\n"
    return ""


def iter_patch_paths(patch: str) -> Iterable[str]:
    for line in patch.splitlines():
        if line.startswith("diff --git "):
            parts = line.split()
            for raw in parts[2:4]:
                if raw.startswith("a/") or raw.startswith("b/"):
                    path = raw[2:]
                    if path != "/dev/null":
                        yield path
        elif line.startswith("+++ b/") or line.startswith("--- a/"):
            path = line[6:]
            if path and path != "/dev/null":
                yield path


def validate_patch(patch: str) -> tuple[bool, str]:
    if not patch.strip():
        return True, "empty patch"
    paths = sorted(set(iter_patch_paths(patch)))
    if not paths:
        return False, "patch 里没有识别到文件路径"
    illegal = [p for p in paths if p not in ALLOWED_PATCH_FILES]
    if illegal:
        return False, "patch 试图修改非白名单文件：" + ", ".join(illegal)
    lowered = patch.lower()
    risky_hits = [p for p in FORBIDDEN_PATTERNS if p.lower() in lowered]
    # 允许文档里出现变量名，但不允许 diff 新增/修改真实密钥或交易函数痕迹。
    serious = [h for h in risky_hits if h not in {".env", "poe_api_key", "telegram_bot_token"}]
    if serious:
        return False, "patch 包含高风险关键词：" + ", ".join(serious)
    return True, "ok"


def apply_patch_with_rollback(patch_path: Path) -> tuple[bool, str]:
    before = run_cmd(["git", "diff", "--", *sorted(ALLOWED_PATCH_FILES)]).stdout if (ROOT / ".git").exists() else ""
    check = run_cmd(["git", "apply", "--check", str(patch_path)])
    if check.returncode != 0:
        return False, "git apply --check failed\n" + check.stderr

    apply = run_cmd(["git", "apply", str(patch_path)])
    if apply.returncode != 0:
        return False, "git apply failed\n" + apply.stderr

    tests = run_cmd([sys.executable, "-m", "pytest", "-q"])
    if tests.returncode == 0:
        return True, "Patch applied and tests passed.\n" + tests.stdout

    # Reverse only the generated patch. Never discard unrelated local edits.
    reverse = run_cmd(["git", "apply", "-R", str(patch_path)])
    after_rollback = run_cmd(["git", "diff", "--", *sorted(ALLOWED_PATCH_FILES)]).stdout if (ROOT / ".git").exists() else ""
    msg = (
        "Patch applied but tests failed; rollback attempted.\n"
        f"TEST STDOUT:\n{tests.stdout}\nTEST STDERR:\n{tests.stderr}\n"
        f"ROLLBACK STDERR:\n{reverse.stderr}\n"
    )
    if before != after_rollback:
        msg += "WARNING: rollback diff does not match original clean state; review git status.\n"
    return False, msg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate or safely validate a Poe optimizer patch")
    parser.add_argument(
        "--apply-patch",
        type=Path,
        default=None,
        help="Validate, apply and test an existing patch without requiring an API key",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.apply_patch is not None:
        patch_path = args.apply_patch if args.apply_patch.is_absolute() else ROOT / args.apply_patch
        if not patch_path.is_file():
            print(f"patch not found: {patch_path}", file=sys.stderr)
            return 2
        patch = patch_path.read_text(encoding="utf-8")
        ok, reason = validate_patch(patch)
        if not ok:
            print(reason, file=sys.stderr)
            return 3
        if not patch.strip():
            print("empty patch; nothing to apply")
            return 0
        success, apply_msg = apply_patch_with_rollback(patch_path)
        print(apply_msg)
        return 0 if success else 4

    load_dotenv(ROOT / ".env")
    api_key = os.getenv("POE_API_KEY", "")
    if not api_key:
        print("POE_API_KEY empty; cannot run optimizer", file=sys.stderr)
        return 2

    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        print("openai package is not installed; run: pip install -r requirements.txt", file=sys.stderr)
        return 2

    client = OpenAI(api_key=api_key, base_url=os.getenv("POE_BASE_URL", "https://api.poe.com/v1"))
    model = os.getenv("POE_MODEL_CODE", "Claude-Sonnet-4.6")
    max_tokens = int(os.getenv("AI_OPTIMIZER_MAX_TOKENS", "5000"))
    aggressive = os.getenv("AI_OPTIMIZER_AGGRESSIVE", "1").strip().lower() in {"1", "true", "yes", "on"}

    context = collect_context()
    prompt = (
        "你是严格但敢改的 Python 量化监控系统维护助手。\n"
        "目标：提高钱包监控、信号筛选、收益追踪、Poe AI 成本控制、GitHub 自动运行稳定性。\n"
        "要求：\n"
        "- 输出中文审查结论。\n"
        "- 最后必须给出一个可直接 git apply 的 unified diff，放在 ```diff 代码块。\n"
        "- 只允许修改 allowed_patch_files 中的文件。\n"
        "- 禁止修改 .env、密钥、钱包地址文件。\n"
        "- 禁止加入自动下单、自动交易、私钥签名、提现等功能。\n"
        "- 优先修复真实 bug，其次优化性能/限流/重试/AI 成本/信号质量/测试覆盖。\n"
        "- 如果信息不足，可以做保守改动，但不要编造不存在的 API 字段。\n"
        f"- 当前模式：{'AGGRESSIVE，大胆给出有效 patch' if aggressive else 'CONSERVATIVE，只给必要 patch'}。\n"
        "上下文 JSON：\n"
        + json.dumps(context, ensure_ascii=False)
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你输出中文审查结论，并在最后提供一个 ```diff 代码块。"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.08 if not aggressive else 0.18,
        max_tokens=max_tokens,
    )

    text = resp.choices[0].message.content or ""
    usage = usage_from_openai_response(resp)
    try:
        with Store(ROOT / os.getenv("DB_PATH", ".state/wallet_monitor.sqlite3")) as store:
            points = estimate_points(
                prompt_tokens=usage.get("prompt_tokens"),
                completion_tokens=usage.get("completion_tokens"),
                input_cost_per_million_usd=float(os.getenv("AI_CODE_INPUT_COST_PER_MILLION_USD", os.getenv("AI_SIGNAL_INPUT_COST_PER_MILLION_USD", "2.58"))),
                output_cost_per_million_usd=float(os.getenv("AI_CODE_OUTPUT_COST_PER_MILLION_USD", os.getenv("AI_SIGNAL_OUTPUT_COST_PER_MILLION_USD", "12.88"))),
                points_per_usd=float(os.getenv("AI_POINTS_PER_USD", "33333")),
            )
            store.record_ai_usage(
                ts=int(datetime.now(timezone.utc).timestamp()), model=model, purpose="optimizer", usage=usage,
                estimated_points=points, cached=False, ok=True,
            )
    except Exception:
        pass
    out_dir = ROOT / ".state" / "optimizer"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    report_path = out_dir / "optimizer_report.json"
    report_md_path = out_dir / "optimizer_report.md"
    patch_path = out_dir / "optimizer_patch.diff"
    run_report_path = out_dir / f"optimizer_report_{ts}.json"
    run_report_md_path = out_dir / f"optimizer_report_{ts}.md"
    run_patch_path = out_dir / f"optimizer_patch_{ts}.diff"

    patch = extract_patch(text)
    report_payload = {
        "ts": ts,
        "model": model,
        "usage": usage,
        "text": text,
        "patch_path": str(patch_path.relative_to(ROOT)),
    }
    report_path.write_text(json.dumps(report_payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    run_report_path.write_text(json.dumps(report_payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    report_md_path.write_text(text, encoding="utf-8")
    run_report_md_path.write_text(text, encoding="utf-8")
    patch_path.write_text(patch, encoding="utf-8")
    run_patch_path.write_text(patch, encoding="utf-8")
    print(f"saved {report_path}")
    print(f"saved {report_md_path}")
    print(f"saved {patch_path}")

    ok, reason = validate_patch(patch)
    validation_path = out_dir / "optimizer_validation.log"
    validation_path.write_text(reason + "\n", encoding="utf-8")
    if not ok:
        # AI-generated diffs can occasionally be malformed. This should never block
        # the wallet monitor or report commit path; keep the validation log for
        # later review and exit successfully.
        print("AI optimizer produced an invalid patch; skipped without blocking workflow.", file=sys.stderr)
        print(reason, file=sys.stderr)
        return 0

    if os.getenv("ALLOW_AUTO_PATCH", "0") != "1":
        print("ALLOW_AUTO_PATCH != 1, patch not applied. Review .state/optimizer/optimizer_patch.diff manually.")
        return 0
    if not patch.strip():
        print("empty patch; nothing to apply")
        return 0

    success, apply_msg = apply_patch_with_rollback(patch_path)
    (out_dir / "optimizer_apply.log").write_text(apply_msg, encoding="utf-8")
    print(apply_msg)
    if not success:
        print("AI optimizer patch/apply failed; skipped without blocking workflow.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
