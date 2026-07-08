# 钱包合约信号报告

Time: **2026-07-08 06:30:32 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1215，本轮 warmup 钱包：1206，变动事件：1464
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：143
- 钱包胜率层：enabled=True，新记录=126，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 10，冷却合并 7
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=43，signals=70，avg_duration=207.4s，AI calls=49，AI estimated points=47800

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.14 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.14 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.08 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.06 | 1 | - | - | - | - |
| 0xf17de4...2adab2 | money_printer | NEW | 2.03 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 2.00 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=10 amount=$9,519,961 score=64.9882 groups={'smart_money': 5, 'money_printer': 5}
- **SOL EXIT_SHORT** wallets=7 amount=$2,835,057 score=51.5564 groups={'smart_money': 3, 'money_printer': 4}
- **ETH EXIT_SHORT** wallets=4 amount=$2,670,260 score=34.8101 groups={'money_printer': 4}
- **BTC EXIT_SHORT** wallets=4 amount=$1,464,380 score=29.69 groups={'money_printer': 4}
- **XRP EXIT_SHORT** wallets=1 amount=$175,937 score=8.3862 groups={'money_printer': 1}
- **SOL EXIT_LONG** wallets=1 amount=$110,093 score=5.1505 groups={'smart_money': 1}
- **ETH EXIT_LONG** wallets=1 amount=$119,860 score=4.6864 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第36轮 amount=$4,746,344 prev=60 exit_ratio=- amount_ratio=3.72x age=360.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH SHORT 第30轮 amount=$2,192,594 prev=72 exit_ratio=- amount_ratio=1.75x age=89.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** HYPE SHORT 第16轮 amount=$672,642 prev=70 exit_ratio=- amount_ratio=1.17x age=119.9m cooldown_left=5.0小时
- **COOLDOWN_MERGED** SOL SHORT 第17轮 amount=$2,999,249 prev=73 exit_ratio=- amount_ratio=1.05x age=29.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第30轮 amount=$493,155 prev=69 exit_ratio=- amount_ratio=0.12x age=119.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL LONG 第16轮 amount=$439,849 prev=59 exit_ratio=- amount_ratio=0.63x age=390.0m cooldown_left=2.5小时
- **COOLDOWN_MERGED** HYPE LONG 第15轮 amount=$339,292 prev=66 exit_ratio=- amount_ratio=0.37x age=240.0m cooldown_left=3.5小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第17轮 amount=$2,835,057 prev=73 exit_ratio=0.9905 amount_ratio=1.05x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第30轮 amount=$2,670,260 prev=72 exit_ratio=0.8518 amount_ratio=1.75x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第30轮 amount=$9,519,961 prev=69 exit_ratio=0.5876 amount_ratio=0.12x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：73 条，方向正确 40，方向错误 33，平均方向收益 0.32%，最好 9.22%，最差 -8.80%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.3892 | 9.22 | 9.09 | 9.22 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.3892 | 9.08 | 8.95 | 9.08 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.708065 | -8.80 | -8.93 | 0.55 | -8.80 |
| 31 | NEAR | LONG | 2.05555 | 1.90395 | -7.38 | -7.51 | 1.11 | -7.50 |
| 45 | MON | LONG | 0.025817 | 0.0241 | -6.65 | -6.78 | 0.89 | -7.78 |
| 8 | NEAR | SHORT | 2.0234 | 1.90395 | 5.90 | 5.77 | 6.03 | -2.72 |
| 41 | HYPE | SHORT | 71.902 | 67.8585 | 5.62 | 5.49 | 5.90 | -0.38 |
| 13 | GRAM | SHORT | 1.6858 | 1.59495 | 5.39 | 5.26 | 6.60 | -0.52 |
| 47 | SOL | SHORT | 82.5535 | 78.151 | 5.33 | 5.20 | 5.33 | -0.08 |
| 16 | HYPE | LONG | 71.6085 | 67.8585 | -5.24 | -5.37 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 67.8585 | 5.08 | 4.95 | 5.35 | -1.76 |
| 56 | LIT | SHORT | 2.50975 | 2.3892 | 4.80 | 4.67 | 4.80 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 78.151 | -4.73 | -4.86 | 0.71 | -4.73 |
| 4 | HYPE | SHORT | 71.0475 | 67.8585 | 4.49 | 4.36 | 4.76 | -2.39 |
| 44 | VVV | SHORT | 11.1805 | 10.69 | 4.39 | 4.26 | 5.94 | 0.00 |
| 5 | SOL | SHORT | 81.6175 | 78.151 | 4.25 | 4.12 | 4.25 | -1.23 |
| 14 | kPEPE | LONG | 0.002705 | 0.002595 | -4.07 | -4.20 | 1.44 | -4.07 |
| 11 | SOL | LONG | 81.4165 | 78.151 | -4.01 | -4.14 | 1.48 | -4.01 |
| 7 | XRP | SHORT | 1.13285 | 1.08795 | 3.96 | 3.83 | 3.96 | 0.00 |
| 37 | ZEC | LONG | 495.815 | 477.54 | -3.69 | -3.82 | 2.90 | -3.76 |
| 39 | XRP | SHORT | 1.12915 | 1.08795 | 3.65 | 3.52 | 3.65 | -0.20 |
| 24 | SOL | SHORT | 81.0475 | 78.151 | 3.57 | 3.44 | 3.57 | -1.94 |
| 49 | HYPE | LONG | 70.1565 | 67.8585 | -3.28 | -3.41 | 0.23 | -3.55 |
| 51 | ZEC | LONG | 493.435 | 477.54 | -3.22 | -3.35 | 0.83 | -3.30 |
| 21 | ZEC | LONG | 463.135 | 477.54 | 3.11 | 2.98 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 477.54 | -3.11 | -3.24 | 1.19 | -10.16 |
| 48 | BNB | SHORT | 584.295 | 566.495 | 3.05 | 2.92 | 3.05 | 0.00 |
| 59 | SOL | LONG | 80.5705 | 78.151 | -3.00 | -3.13 | 0.03 | -3.00 |
| 42 | ETH | SHORT | 1803.55 | 1749.65 | 2.99 | 2.86 | 2.99 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1749.65 | -2.90 | -3.03 | 0.48 | -2.90 |

</details>
