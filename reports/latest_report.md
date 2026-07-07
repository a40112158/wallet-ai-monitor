# 钱包合约信号报告

Time: **2026-07-07 21:00:29 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1236，本轮 warmup 钱包：1185，变动事件：1303
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：126
- 钱包胜率层：enabled=True，新记录=123，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 5，生命周期事件 4，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=3
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=26，signals=52，avg_duration=191.0s，AI calls=38，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.15 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.81 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.75 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.75 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.73 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.73 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.71 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.71 | 1 | - | - | - | - |
| 0x4537e1...798732 | smart_money | NEW | 1.67 | 1 | - | - | - | - |
| 0xe9d199...ecd2d3 | smart_money | NEW | 1.67 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=4 amount=$575,279 score=25.2289 groups={'smart_money': 2, 'money_printer': 2}
- **BTC EXIT_SHORT** wallets=3 amount=$494,087 score=21.4264 groups={'money_printer': 3}
- **SOL EXIT_SHORT** wallets=3 amount=$384,659 score=21.245 groups={'money_printer': 3}
- **HYPE EXIT_SHORT** wallets=2 amount=$452,609 score=12.4927 groups={'smart_money': 1, 'money_printer': 1}
- **LIT EXIT_SHORT** wallets=1 amount=$457,034 score=7.2204 groups={'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=1 amount=$334,882 score=7.0481 groups={'money_printer': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$112,027 score=6.8166 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第19轮 amount=$2,848,168 prev=26 exit_ratio=- amount_ratio=1.77x age=419.9m cooldown_left=5.5小时
- **COOLDOWN_MERGED** SOL LONG 第5轮 amount=$355,431 prev=40 exit_ratio=- amount_ratio=0.98x age=300.0m cooldown_left=2.0小时
- **COOLDOWN_MERGED** BTC LONG 第13轮 amount=$458,065 prev=30 exit_ratio=- amount_ratio=0.18x age=359.9m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第-轮 amount=$452,609 prev=28 exit_ratio=0.5907 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：54 条，方向正确 26，方向错误 28，平均方向收益 -0.16%，最好 5.98%，最差 -6.10%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.729045 | -6.10 | -6.23 | 0.55 | -6.10 |
| 21 | ZEC | LONG | 463.135 | 490.835 | 5.98 | 5.85 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 490.835 | -5.98 | -6.11 | 1.19 | -10.16 |
| 45 | MON | LONG | 0.025817 | 0.024616 | -4.65 | -4.78 | 0.89 | -4.65 |
| 33 | ZEC | SHORT | 469.59 | 490.835 | -4.52 | -4.65 | 0.00 | -8.65 |
| 44 | VVV | SHORT | 11.1805 | 10.7985 | 3.42 | 3.29 | 3.44 | 0.00 |
| 13 | GRAM | SHORT | 1.6858 | 1.64275 | 2.55 | 2.42 | 3.17 | -0.52 |
| 31 | NEAR | LONG | 2.05555 | 2.0049 | -2.46 | -2.59 | 1.11 | -2.46 |
| 41 | HYPE | SHORT | 71.902 | 70.2325 | 2.32 | 2.19 | 2.91 | -0.38 |
| 18 | LIT | SHORT | 2.63175 | 2.5801 | 1.96 | 1.83 | 4.48 | -2.05 |
| 16 | HYPE | LONG | 71.6085 | 70.2325 | -1.92 | -2.05 | 1.59 | -2.51 |
| 6 | LIT | SHORT | 2.6279 | 2.5801 | 1.82 | 1.69 | 4.57 | -2.20 |
| 28 | HYPE | SHORT | 71.49 | 70.2325 | 1.76 | 1.63 | 2.35 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 81.246 | 1.58 | 1.45 | 1.82 | -0.08 |
| 26 | BTC | SHORT | 62945.5 | 63777 | -1.32 | -1.45 | 0.00 | -1.93 |
| 7 | XRP | SHORT | 1.13285 | 1.11965 | 1.17 | 1.04 | 1.58 | 0.00 |
| 4 | HYPE | SHORT | 71.0475 | 70.2325 | 1.15 | 1.02 | 1.74 | -2.39 |
| 27 | ETH | SHORT | 1767.25 | 1786.7 | -1.10 | -1.23 | 0.00 | -2.45 |
| 1 | BTC | SHORT | 63136.5 | 63777 | -1.01 | -1.14 | 0.30 | -1.62 |
| 37 | ZEC | LONG | 495.815 | 490.835 | -1.00 | -1.13 | 2.90 | -1.00 |
| 40 | SOL | LONG | 82.0335 | 81.246 | -0.96 | -1.09 | 0.71 | -1.20 |
| 25 | BTC | LONG | 63172.5 | 63777 | 0.96 | 0.83 | 1.56 | -0.36 |
| 42 | ETH | SHORT | 1803.55 | 1786.7 | 0.93 | 0.80 | 1.14 | -0.39 |
| 8 | NEAR | SHORT | 2.0234 | 2.0049 | 0.91 | 0.78 | 1.24 | -2.72 |
| 46 | ETH | LONG | 1801.95 | 1786.7 | -0.85 | -0.98 | 0.48 | -1.05 |
| 39 | XRP | SHORT | 1.12915 | 1.11965 | 0.84 | 0.71 | 1.19 | -0.20 |
| 10 | BTC | SHORT | 63245.5 | 63777 | -0.84 | -0.97 | 0.47 | -1.45 |
| 14 | kPEPE | LONG | 0.002705 | 0.002683 | -0.81 | -0.94 | 1.44 | -1.37 |
| 12 | BTC | SHORT | 63271.5 | 63777 | -0.80 | -0.93 | 0.52 | -1.40 |
| 23 | ETH | SHORT | 1773.75 | 1786.7 | -0.73 | -0.86 | 0.37 | -2.07 |

</details>
