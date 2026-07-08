# 钱包合约信号报告

Time: **2026-07-08 04:00:33 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1219，本轮 warmup 钱包：1202，变动事件：1360
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：139
- 钱包胜率层：enabled=True，新记录=174，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 5，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=3
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=40，signals=66，avg_duration=200.0s，AI calls=47，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.05 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.03 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.03 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.02 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.99 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.99 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=13 amount=$8,267,894 score=105.0874 groups={'smart_money': 1, 'money_printer': 12}
- **ETH EXIT_SHORT** wallets=5 amount=$1,328,754 score=41.4726 groups={'money_printer': 5}
- **BTC EXIT_LONG** wallets=4 amount=$1,620,050 score=21.8661 groups={'smart_money': 4}
- **SOL EXIT_SHORT** wallets=2 amount=$754,518 score=16.79 groups={'money_printer': 2}
- **HYPE EXIT_SHORT** wallets=1 amount=$114,026 score=7.7853 groups={'money_printer': 1}
- **XPL EXIT_SHORT** wallets=1 amount=$137,067 score=7.4592 groups={'money_printer': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$376,551 score=5.8105 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC LONG 第25轮 amount=$3,488,852 prev=55 exit_ratio=- amount_ratio=10.85x age=389.9m cooldown_left=2.0小时
- **COOLDOWN_MERGED** SOL LONG 第14轮 amount=$1,193,253 prev=59 exit_ratio=- amount_ratio=1.95x age=240.0m cooldown_left=5.0小时
- **COOLDOWN_MERGED** ETH SHORT 第26轮 amount=$690,015 prev=57 exit_ratio=- amount_ratio=0.89x age=360.1m cooldown_left=3.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第-轮 amount=$376,551 prev=66 exit_ratio=0.524 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第-轮 amount=$8,267,894 prev=58 exit_ratio=1.9013 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：68 条，方向正确 37，方向错误 31，平均方向收益 0.31%，最好 8.64%，最差 -7.60%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.4043 | 8.64 | 8.51 | 8.64 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.4043 | 8.51 | 8.38 | 8.51 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.71742 | -7.60 | -7.73 | 0.55 | -7.60 |
| 31 | NEAR | LONG | 2.05555 | 1.92695 | -6.26 | -6.39 | 1.11 | -7.50 |
| 45 | MON | LONG | 0.025817 | 0.024382 | -5.56 | -5.69 | 0.89 | -7.78 |
| 41 | HYPE | SHORT | 71.902 | 67.9495 | 5.50 | 5.37 | 5.90 | -0.38 |
| 13 | GRAM | SHORT | 1.6858 | 1.59395 | 5.45 | 5.32 | 6.60 | -0.52 |
| 16 | HYPE | LONG | 71.6085 | 67.9495 | -5.11 | -5.24 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 67.9495 | 4.95 | 4.82 | 5.35 | -1.76 |
| 8 | NEAR | SHORT | 2.0234 | 1.92695 | 4.77 | 4.64 | 6.03 | -2.72 |
| 47 | SOL | SHORT | 82.5535 | 78.6575 | 4.72 | 4.59 | 4.72 | -0.08 |
| 4 | HYPE | SHORT | 71.0475 | 67.9495 | 4.36 | 4.23 | 4.76 | -2.39 |
| 56 | LIT | SHORT | 2.50975 | 2.4043 | 4.20 | 4.07 | 4.20 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 78.6575 | -4.12 | -4.25 | 0.71 | -4.12 |
| 14 | kPEPE | LONG | 0.002705 | 0.0026 | -3.88 | -4.01 | 1.44 | -3.88 |
| 5 | SOL | SHORT | 81.6175 | 78.6575 | 3.63 | 3.50 | 3.63 | -1.23 |
| 21 | ZEC | LONG | 463.135 | 479.13 | 3.45 | 3.32 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 479.13 | -3.45 | -3.58 | 1.19 | -10.16 |
| 7 | XRP | SHORT | 1.13285 | 1.09445 | 3.39 | 3.26 | 3.39 | 0.00 |
| 11 | SOL | LONG | 81.4165 | 78.6575 | -3.39 | -3.52 | 1.48 | -3.39 |
| 37 | ZEC | LONG | 495.815 | 479.13 | -3.37 | -3.50 | 2.90 | -3.76 |
| 44 | VVV | SHORT | 11.1805 | 10.8165 | 3.26 | 3.13 | 5.94 | 0.00 |
| 49 | HYPE | LONG | 70.1565 | 67.9495 | -3.15 | -3.28 | 0.23 | -3.55 |
| 39 | XRP | SHORT | 1.12915 | 1.09445 | 3.07 | 2.94 | 3.07 | -0.20 |
| 24 | SOL | SHORT | 81.0475 | 78.6575 | 2.95 | 2.82 | 2.95 | -1.94 |
| 51 | ZEC | LONG | 493.435 | 479.13 | -2.90 | -3.03 | 0.83 | -3.30 |
| 42 | ETH | SHORT | 1803.55 | 1751.35 | 2.89 | 2.76 | 2.89 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1751.35 | -2.81 | -2.94 | 0.48 | -2.81 |
| 48 | BNB | SHORT | 584.295 | 568.41 | 2.72 | 2.59 | 2.72 | 0.00 |
| 9 | TAO | LONG | 213.63 | 207.935 | -2.67 | -2.80 | 1.58 | -2.92 |

</details>
