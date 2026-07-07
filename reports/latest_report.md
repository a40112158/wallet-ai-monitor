# 钱包合约信号报告

Time: **2026-07-07 23:30:31 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1228，本轮 warmup 钱包：1193，变动事件：1230
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：129
- 钱包胜率层：enabled=True，新记录=69，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 5，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=31，signals=56，avg_duration=195.1s，AI calls=41，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.08 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.07 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.07 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.06 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.88 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.78 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.73 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 1.72 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.72 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=8 amount=$3,628,733 score=57.8412 groups={'money_printer': 8}
- **ETH EXIT_SHORT** wallets=4 amount=$1,103,715 score=32.0555 groups={'money_printer': 4}
- **BTC EXIT_LONG** wallets=3 amount=$3,917,082 score=22.4463 groups={'smart_money': 1, 'money_printer': 2}
- **HYPE EXIT_LONG** wallets=2 amount=$597,581 score=12.5148 groups={'smart_money': 1, 'money_printer': 1}
- **SOL EXIT_SHORT** wallets=1 amount=$117,437 score=7.408 groups={'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=1 amount=$158,894 score=6.9746 groups={'money_printer': 1}
- **LIT EXIT_SHORT** wallets=1 amount=$135,735 score=6.8828 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第24轮 amount=$3,599,245 prev=58 exit_ratio=- amount_ratio=0.42x age=60.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH SHORT 第19轮 amount=$3,560,500 prev=50 exit_ratio=- amount_ratio=1.00x age=270.1m cooldown_left=5.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第9轮 amount=$566,825 prev=53 exit_ratio=- amount_ratio=0.91x age=240.0m cooldown_left=3.0小时
- **COOLDOWN_MERGED** BTC LONG 第17轮 amount=$263,036 prev=55 exit_ratio=- amount_ratio=0.14x age=119.9m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第24轮 amount=$3,628,733 prev=58 exit_ratio=0.8345 amount_ratio=0.42x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：58 条，方向正确 25，方向错误 33，平均方向收益 0.05%，最好 5.29%，最差 -5.29%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 487.615 | 5.29 | 5.16 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 487.615 | -5.29 | -5.42 | 1.19 | -10.16 |
| 18 | LIT | SHORT | 2.63175 | 2.4948 | 5.20 | 5.07 | 6.21 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.4948 | 5.06 | 4.93 | 6.07 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.73958 | -4.74 | -4.87 | 0.55 | -6.78 |
| 45 | MON | LONG | 0.025817 | 0.024661 | -4.48 | -4.61 | 0.89 | -7.78 |
| 44 | VVV | SHORT | 11.1805 | 10.693 | 4.36 | 4.23 | 5.94 | 0.00 |
| 33 | ZEC | SHORT | 469.59 | 487.615 | -3.84 | -3.97 | 0.00 | -8.65 |
| 13 | GRAM | SHORT | 1.6858 | 1.63095 | 3.25 | 3.12 | 3.89 | -0.52 |
| 31 | NEAR | LONG | 2.05555 | 1.98875 | -3.25 | -3.38 | 1.11 | -3.63 |
| 41 | HYPE | SHORT | 71.902 | 69.8415 | 2.87 | 2.74 | 3.94 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 69.8415 | -2.47 | -2.60 | 1.59 | -3.54 |
| 28 | HYPE | SHORT | 71.49 | 69.8415 | 2.31 | 2.18 | 3.38 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 81.0785 | 1.79 | 1.66 | 2.27 | -0.08 |
| 8 | NEAR | SHORT | 2.0234 | 1.98875 | 1.71 | 1.58 | 2.10 | -2.72 |
| 4 | HYPE | SHORT | 71.0475 | 69.8415 | 1.70 | 1.57 | 2.78 | -2.39 |
| 37 | ZEC | LONG | 495.815 | 487.615 | -1.65 | -1.78 | 2.90 | -3.70 |
| 7 | XRP | SHORT | 1.13285 | 1.11665 | 1.43 | 1.30 | 1.94 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1780.25 | 1.29 | 1.16 | 1.76 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1780.25 | -1.20 | -1.33 | 0.48 | -1.68 |
| 51 | ZEC | LONG | 493.435 | 487.615 | -1.18 | -1.31 | 0.83 | -3.24 |
| 40 | SOL | LONG | 82.0335 | 81.0785 | -1.16 | -1.29 | 0.71 | -1.65 |
| 26 | BTC | SHORT | 62945.5 | 63658.5 | -1.13 | -1.26 | 0.00 | -1.93 |
| 39 | XRP | SHORT | 1.12915 | 1.11665 | 1.11 | 0.98 | 1.62 | -0.20 |
| 48 | BNB | SHORT | 584.295 | 578.785 | 0.94 | 0.81 | 1.14 | 0.00 |
| 38 | ETH | LONG | 1797.05 | 1780.25 | -0.93 | -1.06 | 0.75 | -1.41 |
| 36 | ETH | SHORT | 1797.05 | 1780.25 | 0.93 | 0.80 | 1.41 | -0.75 |
| 14 | kPEPE | LONG | 0.002705 | 0.002682 | -0.85 | -0.98 | 1.44 | -1.52 |
| 1 | BTC | SHORT | 63136.5 | 63658.5 | -0.83 | -0.96 | 0.30 | -1.62 |
| 25 | BTC | LONG | 63172.5 | 63658.5 | 0.77 | 0.64 | 1.56 | -0.36 |

</details>
