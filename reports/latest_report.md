# 钱包合约信号报告

Time: **2026-07-08 01:30:30 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1224，本轮 warmup 钱包：1197，变动事件：1339
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：131
- 钱包胜率层：enabled=True，新记录=141，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 4，生命周期事件 7，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=35，signals=60，avg_duration=198.4s，AI calls=44，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.99 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.97 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.89 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.86 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.83 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.83 | 1 | - | - | - | - |
| 0xf17de4...2adab2 | money_printer | NEW | 1.80 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=8 amount=$3,861,122 score=56.0205 groups={'smart_money': 1, 'money_printer': 7}
- **SOL EXIT_SHORT** wallets=6 amount=$1,319,013 score=37.0035 groups={'smart_money': 3, 'money_printer': 3}
- **HYPE EXIT_SHORT** wallets=3 amount=$694,416 score=18.3367 groups={'smart_money': 2, 'money_printer': 1}
- **BTC EXIT_LONG** wallets=2 amount=$3,198,821 score=14.7587 groups={'money_printer': 1, 'smart_money': 1}
- **HYPE EXIT_LONG** wallets=2 amount=$804,562 score=10.5644 groups={'smart_money': 2}
- **SOL EXIT_LONG** wallets=1 amount=$1,199,992 score=8.2069 groups={'money_printer': 1}
- **XPL EXIT_SHORT** wallets=1 amount=$146,898 score=7.6108 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** SOL LONG 第11轮 amount=$1,913,974 prev=59 exit_ratio=- amount_ratio=2.35x age=90.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第21轮 amount=$1,291,452 prev=55 exit_ratio=- amount_ratio=0.51x age=239.9m cooldown_left=4.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第11轮 amount=$601,671 prev=53 exit_ratio=- amount_ratio=0.59x age=360.0m cooldown_left=1.0小时
- **COOLDOWN_MERGED** BTC SHORT 第28轮 amount=$545,738 prev=58 exit_ratio=- amount_ratio=0.39x age=179.9m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第28轮 amount=$3,861,122 prev=58 exit_ratio=0.8879 amount_ratio=0.39x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL LONG 第11轮 amount=$1,199,992 prev=59 exit_ratio=1.1128 amount_ratio=2.35x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第-轮 amount=$804,562 prev=49 exit_ratio=0.5257 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：62 条，方向正确 28，方向错误 34，平均方向收益 0.16%，最好 7.00%，最差 -5.81%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.4475 | 7.00 | 6.87 | 7.00 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.4475 | 6.86 | 6.73 | 6.86 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.73127 | -5.81 | -5.94 | 0.55 | -6.78 |
| 45 | MON | LONG | 0.025817 | 0.024669 | -4.45 | -4.58 | 0.89 | -7.78 |
| 13 | GRAM | SHORT | 1.6858 | 1.61145 | 4.41 | 4.28 | 4.41 | -0.52 |
| 21 | ZEC | LONG | 463.135 | 482.515 | 4.18 | 4.05 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 482.515 | -4.18 | -4.31 | 1.19 | -10.16 |
| 41 | HYPE | SHORT | 71.902 | 69.0365 | 3.99 | 3.86 | 3.99 | -0.38 |
| 31 | NEAR | LONG | 2.05555 | 1.97675 | -3.83 | -3.96 | 1.11 | -3.83 |
| 44 | VVV | SHORT | 11.1805 | 10.763 | 3.73 | 3.60 | 5.94 | 0.00 |
| 16 | HYPE | LONG | 71.6085 | 69.0365 | -3.59 | -3.72 | 1.59 | -3.59 |
| 28 | HYPE | SHORT | 71.49 | 69.0365 | 3.43 | 3.30 | 3.43 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 79.9995 | 3.09 | 2.96 | 3.09 | -0.08 |
| 4 | HYPE | SHORT | 71.0475 | 69.0365 | 2.83 | 2.70 | 2.83 | -2.39 |
| 33 | ZEC | SHORT | 469.59 | 482.515 | -2.75 | -2.88 | 0.00 | -8.65 |
| 37 | ZEC | LONG | 495.815 | 482.515 | -2.68 | -2.81 | 2.90 | -3.70 |
| 56 | LIT | SHORT | 2.50975 | 2.4475 | 2.48 | 2.35 | 2.48 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 79.9995 | -2.48 | -2.61 | 0.71 | -2.48 |
| 8 | NEAR | SHORT | 2.0234 | 1.97675 | 2.31 | 2.18 | 2.31 | -2.72 |
| 51 | ZEC | LONG | 493.435 | 482.515 | -2.21 | -2.34 | 0.83 | -3.24 |
| 5 | SOL | SHORT | 81.6175 | 79.9995 | 1.98 | 1.85 | 1.98 | -1.23 |
| 7 | XRP | SHORT | 1.13285 | 1.11045 | 1.98 | 1.85 | 1.98 | 0.00 |
| 14 | kPEPE | LONG | 0.002705 | 0.002656 | -1.81 | -1.94 | 1.44 | -1.81 |
| 11 | SOL | LONG | 81.4165 | 79.9995 | -1.74 | -1.87 | 1.48 | -1.74 |
| 42 | ETH | SHORT | 1803.55 | 1772.85 | 1.70 | 1.57 | 1.76 | -0.39 |
| 39 | XRP | SHORT | 1.12915 | 1.11045 | 1.66 | 1.53 | 1.66 | -0.20 |
| 46 | ETH | LONG | 1801.95 | 1772.85 | -1.61 | -1.74 | 0.48 | -1.68 |
| 49 | HYPE | LONG | 70.1565 | 69.0365 | -1.60 | -1.73 | 0.23 | -1.60 |
| 48 | BNB | SHORT | 584.295 | 576.205 | 1.38 | 1.25 | 1.38 | 0.00 |
| 38 | ETH | LONG | 1797.05 | 1772.85 | -1.35 | -1.48 | 0.75 | -1.41 |

</details>
