# 钱包合约信号报告

Time: **2026-07-08 05:30:34 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1215，本轮 warmup 钱包：1206，变动事件：1408
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：140
- 钱包胜率层：enabled=True，新记录=96，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 5，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=43，signals=70，avg_duration=200.1s，AI calls=49，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.11 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.05 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.05 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.03 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.01 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.99 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.95 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=11 amount=$10,640,144 score=94.1658 groups={'money_printer': 10, 'smart_money': 1}
- **ETH EXIT_SHORT** wallets=3 amount=$844,201 score=23.561 groups={'money_printer': 3}
- **XRP EXIT_SHORT** wallets=1 amount=$116,468 score=8.2195 groups={'money_printer': 1}
- **SOL EXIT_LONG** wallets=1 amount=$241,134 score=7.4999 groups={'money_printer': 1}
- **kBONK EXIT_SHORT** wallets=1 amount=$113,053 score=5.0533 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第29轮 amount=$1,251,678 prev=72 exit_ratio=- amount_ratio=0.40x age=30.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第14轮 amount=$605,784 prev=70 exit_ratio=- amount_ratio=1.05x age=59.9m cooldown_left=6.0小时
- **COOLDOWN_MERGED** BTC LONG 第28轮 amount=$1,578,619 prev=69 exit_ratio=- amount_ratio=2.05x age=59.9m cooldown_left=6.0小时
- **COOLDOWN_MERGED** BTC SHORT 第34轮 amount=$1,206,746 prev=60 exit_ratio=- amount_ratio=0.59x age=300.1m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第34轮 amount=$10,640,144 prev=60 exit_ratio=1.2076 amount_ratio=0.59x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：72 条，方向正确 42，方向错误 30，平均方向收益 0.37%，最好 7.40%，最差 -7.31%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.43705 | 7.40 | 7.27 | 8.64 | -2.05 |
| 34 | JTO | LONG | 0.77639 | 0.719605 | -7.31 | -7.44 | 0.55 | -7.60 |
| 6 | LIT | SHORT | 2.6279 | 2.43705 | 7.26 | 7.13 | 8.51 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.92305 | -6.45 | -6.58 | 1.11 | -7.50 |
| 13 | GRAM | SHORT | 1.6858 | 1.59155 | 5.59 | 5.46 | 6.60 | -0.52 |
| 45 | MON | LONG | 0.025817 | 0.02445 | -5.29 | -5.42 | 0.89 | -7.78 |
| 41 | HYPE | SHORT | 71.902 | 68.1715 | 5.19 | 5.06 | 5.90 | -0.38 |
| 8 | NEAR | SHORT | 2.0234 | 1.92305 | 4.96 | 4.83 | 6.03 | -2.72 |
| 47 | SOL | SHORT | 82.5535 | 78.5735 | 4.82 | 4.69 | 4.82 | -0.08 |
| 16 | HYPE | LONG | 71.6085 | 68.1715 | -4.80 | -4.93 | 1.59 | -5.51 |
| 44 | VVV | SHORT | 11.1805 | 10.648 | 4.76 | 4.63 | 5.94 | 0.00 |
| 28 | HYPE | SHORT | 71.49 | 68.1715 | 4.64 | 4.51 | 5.35 | -1.76 |
| 21 | ZEC | LONG | 463.135 | 483.64 | 4.43 | 4.30 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 483.64 | -4.43 | -4.56 | 1.19 | -10.16 |
| 40 | SOL | LONG | 82.0335 | 78.5735 | -4.22 | -4.35 | 0.71 | -4.22 |
| 4 | HYPE | SHORT | 71.0475 | 68.1715 | 4.05 | 3.92 | 4.76 | -2.39 |
| 5 | SOL | SHORT | 81.6175 | 78.5735 | 3.73 | 3.60 | 3.73 | -1.23 |
| 11 | SOL | LONG | 81.4165 | 78.5735 | -3.49 | -3.62 | 1.48 | -3.49 |
| 7 | XRP | SHORT | 1.13285 | 1.09345 | 3.48 | 3.35 | 3.48 | 0.00 |
| 62 | UNI | LONG | 3.2692 | 3.37725 | 3.31 | 3.18 | 3.31 | -3.15 |
| 14 | kPEPE | LONG | 0.002705 | 0.002616 | -3.29 | -3.42 | 1.44 | -3.88 |
| 39 | XRP | SHORT | 1.12915 | 1.09345 | 3.16 | 3.03 | 3.16 | -0.20 |
| 24 | SOL | SHORT | 81.0475 | 78.5735 | 3.05 | 2.92 | 3.05 | -1.94 |
| 33 | ZEC | SHORT | 469.59 | 483.64 | -2.99 | -3.12 | 0.00 | -8.65 |
| 56 | LIT | SHORT | 2.50975 | 2.43705 | 2.90 | 2.77 | 4.20 | 0.00 |
| 49 | HYPE | LONG | 70.1565 | 68.1715 | -2.83 | -2.96 | 0.23 | -3.55 |
| 42 | ETH | SHORT | 1803.55 | 1755.95 | 2.64 | 2.51 | 2.89 | -0.39 |
| 48 | BNB | SHORT | 584.295 | 569.13 | 2.60 | 2.47 | 2.72 | 0.00 |
| 46 | ETH | LONG | 1801.95 | 1755.95 | -2.55 | -2.68 | 0.48 | -2.81 |
| 59 | SOL | LONG | 80.5705 | 78.5735 | -2.48 | -2.61 | 0.03 | -2.48 |

</details>
