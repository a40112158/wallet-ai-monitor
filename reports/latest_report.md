# 钱包合约信号报告

Time: **2026-07-07 23:00:30 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1227，本轮 warmup 钱包：1194，变动事件：1284
- AI 输入信号：0，虚拟开仓：0，动态评分钱包：129
- 钱包胜率层：enabled=True，新记录=147，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 6，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=0，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=30，signals=56，avg_duration=193.9s，AI calls=41，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.13 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.13 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.12 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 2.05 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.93 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.80 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.75 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.74 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.74 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 1.73 | 1 | - | - | - | - |

## AI 状态

No significant signal met AI trigger

## 本轮开仓/加仓信号

本轮没有达到阈值的开多/开空信号。

## 减仓/平仓风险信号

- **ETH EXIT_SHORT** wallets=6 amount=$1,185,284 score=45.7926 groups={'money_printer': 6}
- **BTC EXIT_LONG** wallets=7 amount=$6,703,099 score=44.8991 groups={'smart_money': 4, 'money_printer': 3}
- **HYPE EXIT_LONG** wallets=5 amount=$1,724,989 score=33.3924 groups={'smart_money': 1, 'money_printer': 4}
- **SOL EXIT_SHORT** wallets=3 amount=$897,301 score=21.5094 groups={'money_printer': 2, 'smart_money': 1}
- **BTC EXIT_SHORT** wallets=3 amount=$751,815 score=20.7915 groups={'smart_money': 1, 'money_printer': 2}
- **ZEC EXIT_SHORT** wallets=1 amount=$160,684 score=7.6235 groups={'money_printer': 1}
- **LIT EXIT_SHORT** wallets=1 amount=$133,950 score=7.5078 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第23轮 amount=$8,596,743 prev=58 exit_ratio=- amount_ratio=1.98x age=29.9m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第8轮 amount=$619,769 prev=53 exit_ratio=- amount_ratio=1.34x age=210.0m cooldown_left=3.5小时
- **COOLDOWN_MERGED** ETH SHORT 第18轮 amount=$3,550,900 prev=42 exit_ratio=- amount_ratio=2.01x age=390.0m cooldown_left=6.0小时
- **COOLDOWN_MERGED** BTC LONG 第16轮 amount=$1,906,425 prev=43 exit_ratio=- amount_ratio=1.05x age=390.0m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第16轮 amount=$6,703,099 prev=43 exit_ratio=0.7613 amount_ratio=1.05x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第-轮 amount=$1,724,989 prev=49 exit_ratio=1.1271 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：58 条，方向正确 26，方向错误 32，平均方向收益 0.10%，最好 5.83%，最差 -5.60%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.47845 | 5.83 | 5.70 | 6.21 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.47845 | 5.69 | 5.56 | 6.07 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.73288 | -5.60 | -5.73 | 0.55 | -6.78 |
| 21 | ZEC | LONG | 463.135 | 486.435 | 5.03 | 4.90 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 486.435 | -5.03 | -5.16 | 1.19 | -10.16 |
| 45 | MON | LONG | 0.025817 | 0.024636 | -4.57 | -4.70 | 0.89 | -7.78 |
| 44 | VVV | SHORT | 11.1805 | 10.6855 | 4.43 | 4.30 | 5.94 | 0.00 |
| 13 | GRAM | SHORT | 1.6858 | 1.62205 | 3.78 | 3.65 | 3.89 | -0.52 |
| 33 | ZEC | SHORT | 469.59 | 486.435 | -3.59 | -3.72 | 0.00 | -8.65 |
| 31 | NEAR | LONG | 2.05555 | 1.9873 | -3.32 | -3.45 | 1.11 | -3.63 |
| 41 | HYPE | SHORT | 71.902 | 69.7035 | 3.06 | 2.93 | 3.94 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 69.7035 | -2.66 | -2.79 | 1.59 | -3.54 |
| 28 | HYPE | SHORT | 71.49 | 69.7035 | 2.50 | 2.37 | 3.38 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 80.8775 | 2.03 | 1.90 | 2.27 | -0.08 |
| 37 | ZEC | LONG | 495.815 | 486.435 | -1.89 | -2.02 | 2.90 | -3.70 |
| 4 | HYPE | SHORT | 71.0475 | 69.7035 | 1.89 | 1.76 | 2.78 | -2.39 |
| 8 | NEAR | SHORT | 2.0234 | 1.9873 | 1.78 | 1.65 | 2.10 | -2.72 |
| 7 | XRP | SHORT | 1.13285 | 1.11515 | 1.56 | 1.43 | 1.94 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1775.45 | 1.56 | 1.43 | 1.76 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1775.45 | -1.47 | -1.60 | 0.48 | -1.68 |
| 51 | ZEC | LONG | 493.435 | 486.435 | -1.42 | -1.55 | 0.83 | -3.24 |
| 40 | SOL | LONG | 82.0335 | 80.8775 | -1.41 | -1.54 | 0.71 | -1.65 |
| 56 | LIT | SHORT | 2.50975 | 2.47845 | 1.25 | 1.12 | 1.65 | 0.00 |
| 39 | XRP | SHORT | 1.12915 | 1.11515 | 1.24 | 1.11 | 1.62 | -0.20 |
| 38 | ETH | LONG | 1797.05 | 1775.45 | -1.20 | -1.33 | 0.75 | -1.41 |
| 36 | ETH | SHORT | 1797.05 | 1775.45 | 1.20 | 1.07 | 1.41 | -0.75 |
| 48 | BNB | SHORT | 584.295 | 578.545 | 0.98 | 0.85 | 1.14 | 0.00 |
| 26 | BTC | SHORT | 62945.5 | 63547.5 | -0.96 | -1.09 | 0.00 | -1.93 |
| 5 | SOL | SHORT | 81.6175 | 80.8775 | 0.91 | 0.78 | 1.18 | -1.23 |
| 14 | kPEPE | LONG | 0.002705 | 0.002682 | -0.85 | -0.98 | 1.44 | -1.52 |

</details>
