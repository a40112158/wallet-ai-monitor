# 钱包合约信号报告

Time: **2026-07-07 18:00:35 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1248，本轮 warmup 钱包：1173，变动事件：1275
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：110
- 钱包胜率层：enabled=True，新记录=102，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 8，冷却合并 5
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=5
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=20，signals=45，avg_duration=182.6s，AI calls=34，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0x00f8da...e7454b | money_printer | NEW | 1.72 | 1 | - | - | - | - |
| 0xd487e2...934982 | money_printer | NEW | 1.72 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.72 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.71 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.71 | 1 | - | - | - | - |
| 0x3da0af...fefe82 | smart_money | NEW | 1.70 | 1 | - | - | - | - |
| 0xbba068...b519d9 | smart_money | NEW | 1.69 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.68 | 2 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=2 amount=$1,104,773 score=14.647 groups={'money_printer': 2}
- **ZEC EXIT_LONG** wallets=2 amount=$775,648 score=14.0839 groups={'money_printer': 2}
- **ETH EXIT_SHORT** wallets=2 amount=$1,121,366 score=10.6647 groups={'smart_money': 2}
- **ZEC EXIT_SHORT** wallets=1 amount=$485,991 score=9.0877 groups={'money_printer': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$137,362 score=6.9361 groups={'money_printer': 1}
- **BTC EXIT_LONG** wallets=1 amount=$101,056 score=6.6471 groups={'money_printer': 1}
- **SOL EXIT_SHORT** wallets=1 amount=$152,816 score=5.1842 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** SOL SHORT 第8轮 amount=$2,236,162 prev=24 exit_ratio=- amount_ratio=0.97x age=270.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** BTC SHORT 第13轮 amount=$1,052,856 prev=26 exit_ratio=- amount_ratio=1.25x age=240.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** ETH SHORT 第9轮 amount=$2,041,771 prev=23 exit_ratio=- amount_ratio=3.94x age=270.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ZEC LONG 第5轮 amount=$252,235 prev=21 exit_ratio=- amount_ratio=0.42x age=330.2m cooldown_left=7.0小时
- **COOLDOWN_MERGED** NEAR LONG 第3轮 amount=$254,091 prev=31 exit_ratio=- amount_ratio=0.99x age=150.1m cooldown_left=4.5小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第9轮 amount=$1,121,366 prev=23 exit_ratio=0.5989 amount_ratio=3.94x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC LONG 第5轮 amount=$775,648 prev=21 exit_ratio=1.4544 amount_ratio=0.42x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第-轮 amount=$485,991 prev=19 exit_ratio=0.7372 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：47 条，方向正确 23，方向错误 24，平均方向收益 -0.26%，最好 8.93%，最差 -8.93%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 504.47 | 8.93 | 8.80 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 504.47 | -8.93 | -9.06 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 504.47 | -7.43 | -7.56 | 0.00 | -8.65 |
| 34 | JTO | LONG | 0.77639 | 0.753935 | -2.89 | -3.02 | 0.55 | -3.32 |
| 8 | NEAR | SHORT | 2.0234 | 2.07845 | -2.72 | -2.85 | 1.24 | -2.72 |
| 27 | ETH | SHORT | 1767.25 | 1810.55 | -2.45 | -2.58 | 0.00 | -2.45 |
| 23 | ETH | SHORT | 1773.75 | 1810.55 | -2.07 | -2.20 | 0.37 | -2.07 |
| 24 | SOL | SHORT | 81.0475 | 82.6195 | -1.94 | -2.07 | 0.49 | -1.94 |
| 26 | BTC | SHORT | 62945.5 | 64159.5 | -1.93 | -2.06 | 0.00 | -1.93 |
| 37 | ZEC | LONG | 495.815 | 504.47 | 1.75 | 1.62 | 2.90 | 0.00 |
| 18 | LIT | SHORT | 2.63175 | 2.58595 | 1.74 | 1.61 | 3.01 | -2.05 |
| 17 | ETH | LONG | 1780.75 | 1810.55 | 1.67 | 1.54 | 1.67 | -0.76 |
| 3 | ETH | SHORT | 1781.15 | 1810.55 | -1.65 | -1.78 | 0.78 | -1.65 |
| 1 | BTC | SHORT | 63136.5 | 64159.5 | -1.62 | -1.75 | 0.30 | -1.62 |
| 13 | GRAM | SHORT | 1.6858 | 1.65875 | 1.60 | 1.47 | 1.76 | -0.52 |
| 6 | LIT | SHORT | 2.6279 | 2.58595 | 1.60 | 1.47 | 4.57 | -2.20 |
| 25 | BTC | LONG | 63172.5 | 64159.5 | 1.56 | 1.43 | 1.56 | -0.36 |
| 11 | SOL | LONG | 81.4165 | 82.6195 | 1.48 | 1.35 | 1.48 | -0.94 |
| 10 | BTC | SHORT | 63245.5 | 64159.5 | -1.45 | -1.58 | 0.47 | -1.45 |
| 14 | kPEPE | LONG | 0.002705 | 0.002744 | 1.44 | 1.31 | 1.44 | -1.37 |
| 12 | BTC | SHORT | 63271.5 | 64159.5 | -1.40 | -1.53 | 0.52 | -1.40 |
| 15 | BTC | SHORT | 63341.5 | 64159.5 | -1.29 | -1.42 | 0.63 | -1.29 |
| 5 | SOL | SHORT | 81.6175 | 82.6195 | -1.23 | -1.36 | 1.18 | -1.23 |
| 2 | BTC | SHORT | 63427.5 | 64159.5 | -1.15 | -1.28 | 0.76 | -1.15 |
| 9 | TAO | LONG | 213.63 | 216.095 | 1.15 | 1.02 | 1.58 | -0.60 |
| 31 | NEAR | LONG | 2.05555 | 2.07845 | 1.11 | 0.98 | 1.11 | 0.00 |
| 22 | BTC | LONG | 63460.5 | 64159.5 | 1.10 | 0.97 | 1.10 | -0.81 |
| 30 | BTC | LONG | 63562.5 | 64159.5 | 0.94 | 0.81 | 0.94 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 64159.5 | -0.94 | -1.07 | 0.00 | -0.94 |
| 44 | VVV | SHORT | 11.1805 | 11.0895 | 0.81 | 0.68 | 0.88 | 0.00 |

</details>
