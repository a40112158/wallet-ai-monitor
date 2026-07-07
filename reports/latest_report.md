# 钱包合约信号报告

Time: **2026-07-07 20:00:27 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1238，本轮 warmup 钱包：1183，变动事件：1404
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：112
- 钱包胜率层：enabled=True，新记录=111，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 9，冷却合并 6
- 信号状态：NEW=0，RE_ALERT=1，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=24，signals=51，avg_duration=190.0s，AI calls=38，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.83 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.81 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.81 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.79 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.73 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.67 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.67 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **ETH SHORT** [RE_ALERT / 第13轮 / 持续13.0小时 / 冷却剩余7.0小时 / 金额变化1.92x] swing=95.89 AI=- conf=- AI分=None 综合=95.89 delta=$7,193,809 wallets=3 q=50/100 高质=0 样本=1 horizon=3-14

## 本轮开仓/加仓信号

### 1. ETH OPEN_SHORT / Swing 95.89 / AI评分 None / 综合 95.89 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 1, 'money_printer': 2}，事件：{'NEW_POSITION': 2, 'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$7,193,809，最大单钱包：$5,369,850
- 标记价：1789.95，均价：1787.78666667，权重分：22.907，净偏向分：22.907
- AI独立评分：None，规则评分：95.89，综合开仓评分：95.89，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第13轮 / 持续13.0小时 / 冷却剩余7.0小时 / 金额变化1.92x
- 钱包质量：50/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=802581.4834，oracle=1789.8，15m=-0.6379% ，1h=-0.6379% ，volRatio=0.4006
- 中长期评分：95.89 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$22,825,225，6h=$39,186,263，24h=$42,878,072
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.96, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 7.93}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, multi_round_accumulation, short_lower_wick_risk, swing_strong
- Top wallets：
  - 0xa6ee1ed1ae80b8352603654b39f5e7b9bedd5078 money_printer INCREASE_POSITION $5,369,850 score=1.00 grade=NEW win72=- avg72=-
  - 0x3bcae23e8c380dab4732e9a159c0456f12d866f3 money_printer NEW_POSITION $1,403,321 score=0.95 grade=NEW win72=- avg72=-
  - 0x2cef0a7f84e722c77b271862da5fe2387028fa20 smart_money NEW_POSITION $420,638 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=10 amount=$4,074,760 score=67.7123 groups={'smart_money': 2, 'money_printer': 8}
- **ETH EXIT_SHORT** wallets=7 amount=$3,056,416 score=50.9203 groups={'money_printer': 6, 'smart_money': 1}
- **HYPE EXIT_LONG** wallets=4 amount=$1,847,261 score=24.4093 groups={'smart_money': 3, 'money_printer': 1}
- **HYPE EXIT_SHORT** wallets=3 amount=$611,221 score=19.9867 groups={'smart_money': 1, 'money_printer': 2}
- **LIT EXIT_SHORT** wallets=2 amount=$234,594 score=13.3525 groups={'money_printer': 2}
- **BTC EXIT_LONG** wallets=2 amount=$864,699 score=12.6128 groups={'smart_money': 1, 'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=2 amount=$476,603 score=12.4051 groups={'money_printer': 1, 'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第17轮 amount=$2,818,068 prev=26 exit_ratio=- amount_ratio=0.29x age=359.9m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ZEC SHORT 第7轮 amount=$1,691,570 prev=33 exit_ratio=- amount_ratio=2.15x age=269.9m cooldown_left=4.5小时
- **COOLDOWN_MERGED** SOL SHORT 第12轮 amount=$347,969 prev=24 exit_ratio=- amount_ratio=0.34x age=390.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE LONG 第5轮 amount=$501,632 prev=49 exit_ratio=- amount_ratio=0.14x age=60.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第11轮 amount=$1,098,147 prev=22 exit_ratio=- amount_ratio=0.88x age=420.0m cooldown_left=3.5小时
- **COOLDOWN_MERGED** ZEC LONG 第8轮 amount=$995,100 prev=37 exit_ratio=- amount_ratio=1.35x age=240.0m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第-轮 amount=$611,221 prev=28 exit_ratio=0.7977 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第5轮 amount=$1,847,261 prev=49 exit_ratio=1.207 amount_ratio=0.14x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第13轮 amount=$3,056,416 prev=23 exit_ratio=1.6324 amount_ratio=1.92x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：54 条，方向正确 27，方向错误 27，平均方向收益 -0.10%，最好 7.43%，最差 -7.43%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 497.55 | 7.43 | 7.30 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 497.55 | -7.43 | -7.56 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 497.55 | -5.95 | -6.08 | 0.00 | -8.65 |
| 34 | JTO | LONG | 0.77639 | 0.734345 | -5.42 | -5.55 | 0.55 | -5.52 |
| 45 | MON | LONG | 0.025817 | 0.024958 | -3.33 | -3.46 | 0.89 | -3.33 |
| 44 | VVV | SHORT | 11.1805 | 10.862 | 2.85 | 2.72 | 3.44 | 0.00 |
| 13 | GRAM | SHORT | 1.6858 | 1.63855 | 2.80 | 2.67 | 3.17 | -0.52 |
| 18 | LIT | SHORT | 2.63175 | 2.5644 | 2.56 | 2.43 | 4.48 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.5644 | 2.42 | 2.29 | 4.57 | -2.20 |
| 41 | HYPE | SHORT | 71.902 | 70.199 | 2.37 | 2.24 | 2.91 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 70.199 | -1.97 | -2.10 | 1.59 | -2.51 |
| 28 | HYPE | SHORT | 71.49 | 70.199 | 1.81 | 1.68 | 2.35 | -1.76 |
| 31 | NEAR | LONG | 2.05555 | 2.0209 | -1.69 | -1.82 | 1.11 | -2.12 |
| 47 | SOL | SHORT | 82.5535 | 81.3315 | 1.48 | 1.35 | 1.82 | -0.08 |
| 26 | BTC | SHORT | 62945.5 | 63831.5 | -1.41 | -1.54 | 0.00 | -1.93 |
| 27 | ETH | SHORT | 1767.25 | 1789.95 | -1.28 | -1.41 | 0.00 | -2.45 |
| 4 | HYPE | SHORT | 71.0475 | 70.199 | 1.19 | 1.06 | 1.74 | -2.39 |
| 1 | BTC | SHORT | 63136.5 | 63831.5 | -1.10 | -1.23 | 0.30 | -1.62 |
| 25 | BTC | LONG | 63172.5 | 63831.5 | 1.04 | 0.91 | 1.56 | -0.36 |
| 7 | XRP | SHORT | 1.13285 | 1.12165 | 0.99 | 0.86 | 1.58 | 0.00 |
| 10 | BTC | SHORT | 63245.5 | 63831.5 | -0.93 | -1.06 | 0.47 | -1.45 |
| 23 | ETH | SHORT | 1773.75 | 1789.95 | -0.91 | -1.04 | 0.37 | -2.07 |
| 12 | BTC | SHORT | 63271.5 | 63831.5 | -0.89 | -1.02 | 0.52 | -1.40 |
| 40 | SOL | LONG | 82.0335 | 81.3315 | -0.86 | -0.99 | 0.71 | -1.20 |
| 51 | ZEC | LONG | 493.435 | 497.55 | 0.83 | 0.70 | 0.83 | -0.45 |
| 15 | BTC | SHORT | 63341.5 | 63831.5 | -0.77 | -0.90 | 0.63 | -1.29 |
| 42 | ETH | SHORT | 1803.55 | 1789.95 | 0.75 | 0.62 | 1.14 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1789.95 | -0.67 | -0.80 | 0.48 | -1.05 |
| 39 | XRP | SHORT | 1.12915 | 1.12165 | 0.66 | 0.53 | 1.19 | -0.20 |
| 2 | BTC | SHORT | 63427.5 | 63831.5 | -0.64 | -0.77 | 0.76 | -1.15 |

</details>
