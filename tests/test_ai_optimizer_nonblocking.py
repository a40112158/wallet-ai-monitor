from pathlib import Path

import tools.ai_optimizer as opt


def test_invalid_patch_validation_detects_corrupt_patch():
    ok, reason = opt.validate_patch("this is not a valid git patch")
    assert ok is False
    assert "patch" in reason.lower() or "识别" in reason


def test_optimizer_invalid_patch_branch_is_nonblocking_in_source():
    source = Path(opt.__file__).read_text(encoding="utf-8")
    assert "AI optimizer produced an invalid patch; skipped without blocking workflow." in source
    assert "return 0" in source
