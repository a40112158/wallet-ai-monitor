# 钱包合约信号报告

Time: **2026-07-07 20:30:34 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1235，本轮 warmup 钱包：1186，变动事件：1330
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：125
- 钱包胜率层：enabled=True，新记录=114，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 5，生命周期事件 9，冷却合并 7
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=25，signals=52，avg_duration=191.3s，AI calls=38，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.18 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.85 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.75 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.75 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.73 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.71 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0x4537e1...798732 | smart_money | NEW | 1.65 | 1 | - | - | - | - |
| 0xe9d199...ecd2d3 | smart_money | NEW | 1.65 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=13 amount=$7,603,015 score=91.834 groups={'smart_money': 2, 'money_printer': 11}
- **SOL EXIT_SHORT** wallets=4 amount=$855,877 score=29.3648 groups={'money_printer': 4}
- **HYPE EXIT_LONG** wallets=2 amount=$572,019 score=12.8296 groups={'smart_money': 1, 'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=2 amount=$1,390,746 score=12.7709 groups={'money_printer': 1, 'smart_money': 1}
- **BTC EXIT_LONG** wallets=2 amount=$4,038,528 score=12.0504 groups={'smart_money': 1, 'money_printer': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$500,259 score=11.8442 groups={'smart_money': 1, 'money_printer': 1}
- **ETH EXIT_LONG** wallets=2 amount=$675,614 score=11.2153 groups={'smart_money': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC LONG 第12轮 amount=$2,569,251 prev=30 exit_ratio=- amount_ratio=2.34x age=330.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH SHORT 第14轮 amount=$687,870 prev=27 exit_ratio=- amount_ratio=0.10x age=390.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** SOL LONG 第4轮 amount=$362,141 prev=40 exit_ratio=- amount_ratio=0.38x age=270.1m cooldown_left=2.5小时
- **COOLDOWN_MERGED** HYPE LONG 第6轮 amount=$777,222 prev=49 exit_ratio=- amount_ratio=1.55x age=90.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ZEC SHORT 第8轮 amount=$804,380 prev=33 exit_ratio=- amount_ratio=0.48x age=300.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC SHORT 第18轮 amount=$1,606,408 prev=26 exit_ratio=- amount_ratio=0.57x age=390.0m cooldown_left=6.0小时
- **COOLDOWN_MERGED** HYPE SHORT 第7轮 amount=$463,306 prev=28 exit_ratio=- amount_ratio=0.21x age=382.6m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第12轮 amount=$4,038,528 prev=30 exit_ratio=1.3821 amount_ratio=2.34x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第8轮 amount=$1,390,746 prev=33 exit_ratio=0.9875 amount_ratio=0.48x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：54 条，方向正确 26，方向错误 28，平均方向收益 -0.16%，最好 6.27%，最差 -6.27%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 492.195 | 6.27 | 6.14 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 492.195 | -6.27 | -6.40 | 1.19 | -10.16 |
| 34 | JTO | LONG | 0.77639 | 0.7323 | -5.68 | -5.81 | 0.55 | -5.68 |
| 33 | ZEC | SHORT | 469.59 | 492.195 | -4.81 | -4.94 | 0.00 | -8.65 |
| 45 | MON | LONG | 0.025817 | 0.02463 | -4.60 | -4.73 | 0.89 | -4.60 |
| 13 | GRAM | SHORT | 1.6858 | 1.6354 | 2.99 | 2.86 | 3.17 | -0.52 |
| 44 | VVV | SHORT | 11.1805 | 10.928 | 2.26 | 2.13 | 3.44 | 0.00 |
| 41 | HYPE | SHORT | 71.902 | 70.3195 | 2.20 | 2.07 | 2.91 | -0.38 |
| 18 | LIT | SHORT | 2.63175 | 2.5799 | 1.97 | 1.84 | 4.48 | -2.05 |
| 31 | NEAR | LONG | 2.05555 | 2.01555 | -1.95 | -2.08 | 1.11 | -2.12 |
| 6 | LIT | SHORT | 2.6279 | 2.5799 | 1.83 | 1.70 | 4.57 | -2.20 |
| 16 | HYPE | LONG | 71.6085 | 70.3195 | -1.80 | -1.93 | 1.59 | -2.51 |
| 28 | HYPE | SHORT | 71.49 | 70.3195 | 1.64 | 1.51 | 2.35 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 81.3165 | 1.50 | 1.37 | 1.82 | -0.08 |
| 26 | BTC | SHORT | 62945.5 | 63730.5 | -1.25 | -1.38 | 0.00 | -1.93 |
| 27 | ETH | SHORT | 1767.25 | 1787.95 | -1.17 | -1.30 | 0.00 | -2.45 |
| 7 | XRP | SHORT | 1.13285 | 1.12105 | 1.04 | 0.91 | 1.58 | 0.00 |
| 4 | HYPE | SHORT | 71.0475 | 70.3195 | 1.02 | 0.89 | 1.74 | -2.39 |
| 1 | BTC | SHORT | 63136.5 | 63730.5 | -0.94 | -1.07 | 0.30 | -1.62 |
| 25 | BTC | LONG | 63172.5 | 63730.5 | 0.88 | 0.75 | 1.56 | -0.36 |
| 40 | SOL | LONG | 82.0335 | 81.3165 | -0.87 | -1.00 | 0.71 | -1.20 |
| 42 | ETH | SHORT | 1803.55 | 1787.95 | 0.86 | 0.73 | 1.14 | -0.39 |
| 23 | ETH | SHORT | 1773.75 | 1787.95 | -0.80 | -0.93 | 0.37 | -2.07 |
| 46 | ETH | LONG | 1801.95 | 1787.95 | -0.78 | -0.91 | 0.48 | -1.05 |
| 10 | BTC | SHORT | 63245.5 | 63730.5 | -0.77 | -0.90 | 0.47 | -1.45 |
| 53 | HYPE | SHORT | 69.8095 | 70.3195 | -0.73 | -0.86 | 0.00 | -0.73 |
| 52 | HYPE | LONG | 69.8095 | 70.3195 | 0.73 | 0.60 | 0.73 | 0.00 |
| 37 | ZEC | LONG | 495.815 | 492.195 | -0.73 | -0.86 | 2.90 | -0.93 |
| 12 | BTC | SHORT | 63271.5 | 63730.5 | -0.73 | -0.86 | 0.52 | -1.40 |
| 39 | XRP | SHORT | 1.12915 | 1.12105 | 0.72 | 0.59 | 1.19 | -0.20 |

</details>
