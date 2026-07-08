# 钱包合约信号报告

Time: **2026-07-08 07:00:32 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1216，本轮 warmup 钱包：1205，变动事件：1611
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：143
- 钱包胜率层：enabled=True，新记录=120，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 10，冷却合并 7
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=44，signals=70，avg_duration=207.7s，AI calls=49，AI estimated points=47800

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.14 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.14 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.10 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.03 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 1.98 | 1 | - | - | - | - |
| 0x4ef1c5...a528e3 | smart_money | NEW | 1.98 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **ETH EXIT_SHORT** wallets=9 amount=$3,826,784 score=73.7133 groups={'smart_money': 1, 'money_printer': 8}
- **BTC EXIT_LONG** wallets=7 amount=$1,916,298 score=47.1718 groups={'smart_money': 3, 'money_printer': 4}
- **BTC EXIT_SHORT** wallets=4 amount=$1,330,013 score=32.9156 groups={'money_printer': 4}
- **SOL EXIT_LONG** wallets=4 amount=$919,251 score=26.5719 groups={'smart_money': 2, 'money_printer': 2}
- **SOL EXIT_SHORT** wallets=3 amount=$645,319 score=22.5414 groups={'smart_money': 1, 'money_printer': 2}
- **ETH EXIT_LONG** wallets=3 amount=$4,229,283 score=18.3996 groups={'smart_money': 2, 'money_printer': 1}
- **XRP EXIT_SHORT** wallets=1 amount=$138,711 score=8.3769 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第37轮 amount=$1,158,975 prev=60 exit_ratio=- amount_ratio=0.24x age=390.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** SOL SHORT 第18轮 amount=$422,668 prev=73 exit_ratio=- amount_ratio=0.14x age=59.9m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第17轮 amount=$590,391 prev=70 exit_ratio=- amount_ratio=0.88x age=149.9m cooldown_left=4.5小时
- **COOLDOWN_MERGED** ZEC LONG 第11轮 amount=$359,039 prev=67 exit_ratio=- amount_ratio=0.89x age=270.0m cooldown_left=2.5小时
- **COOLDOWN_MERGED** ETH SHORT 第31轮 amount=$568,168 prev=72 exit_ratio=- amount_ratio=0.26x age=119.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH LONG 第9轮 amount=$354,711 prev=63 exit_ratio=- amount_ratio=0.02x age=300.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** HYPE LONG 第16轮 amount=$306,205 prev=66 exit_ratio=- amount_ratio=0.90x age=270.0m cooldown_left=3.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第31轮 amount=$3,826,784 prev=72 exit_ratio=1.2207 amount_ratio=0.26x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH LONG 第9轮 amount=$4,229,283 prev=63 exit_ratio=1.7054 amount_ratio=0.02x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL LONG 第-轮 amount=$919,251 prev=59 exit_ratio=0.8525 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：73 条，方向正确 39，方向错误 34，平均方向收益 0.25%，最好 8.10%，最差 -9.49%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.702745 | -9.49 | -9.62 | 0.55 | -9.49 |
| 18 | LIT | SHORT | 2.63175 | 2.41865 | 8.10 | 7.97 | 9.22 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.41865 | 7.96 | 7.83 | 9.08 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.9046 | -7.34 | -7.47 | 1.11 | -7.50 |
| 45 | MON | LONG | 0.025817 | 0.024125 | -6.55 | -6.68 | 0.89 | -7.78 |
| 8 | NEAR | SHORT | 2.0234 | 1.9046 | 5.87 | 5.74 | 6.03 | -2.72 |
| 13 | GRAM | SHORT | 1.6858 | 1.5934 | 5.48 | 5.35 | 6.60 | -0.52 |
| 47 | SOL | SHORT | 82.5535 | 78.122 | 5.37 | 5.24 | 5.37 | -0.08 |
| 41 | HYPE | SHORT | 71.902 | 68.0615 | 5.34 | 5.21 | 5.90 | -0.38 |
| 44 | VVV | SHORT | 11.1805 | 10.5885 | 5.29 | 5.16 | 5.94 | 0.00 |
| 16 | HYPE | LONG | 71.6085 | 68.0615 | -4.95 | -5.08 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 68.0615 | 4.80 | 4.67 | 5.35 | -1.76 |
| 40 | SOL | LONG | 82.0335 | 78.122 | -4.77 | -4.90 | 0.71 | -4.77 |
| 5 | SOL | SHORT | 81.6175 | 78.122 | 4.28 | 4.15 | 4.28 | -1.23 |
| 4 | HYPE | SHORT | 71.0475 | 68.0615 | 4.20 | 4.07 | 4.76 | -2.39 |
| 11 | SOL | LONG | 81.4165 | 78.122 | -4.05 | -4.18 | 1.48 | -4.05 |
| 37 | ZEC | LONG | 495.815 | 476.28 | -3.94 | -4.07 | 2.90 | -3.94 |
| 14 | kPEPE | LONG | 0.002705 | 0.0026 | -3.88 | -4.01 | 1.44 | -4.07 |
| 7 | XRP | SHORT | 1.13285 | 1.09005 | 3.78 | 3.65 | 3.96 | 0.00 |
| 56 | LIT | SHORT | 2.50975 | 2.41865 | 3.63 | 3.50 | 4.80 | 0.00 |
| 24 | SOL | SHORT | 81.0475 | 78.122 | 3.61 | 3.48 | 3.61 | -1.94 |
| 51 | ZEC | LONG | 493.435 | 476.28 | -3.48 | -3.61 | 0.83 | -3.48 |
| 39 | XRP | SHORT | 1.12915 | 1.09005 | 3.46 | 3.33 | 3.65 | -0.20 |
| 48 | BNB | SHORT | 584.295 | 565.975 | 3.14 | 3.01 | 3.14 | 0.00 |
| 59 | SOL | LONG | 80.5705 | 78.122 | -3.04 | -3.17 | 0.03 | -3.04 |
| 49 | HYPE | LONG | 70.1565 | 68.0615 | -2.99 | -3.12 | 0.23 | -3.55 |
| 42 | ETH | SHORT | 1803.55 | 1750.55 | 2.94 | 2.81 | 2.99 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1750.55 | -2.85 | -2.98 | 0.48 | -2.90 |
| 21 | ZEC | LONG | 463.135 | 476.28 | 2.84 | 2.71 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 476.28 | -2.84 | -2.97 | 1.19 | -10.16 |

</details>
