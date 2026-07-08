# 钱包合约信号报告

Time: **2026-07-08 03:00:35 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1217，本轮 warmup 钱包：1204，变动事件：1766
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：137
- 钱包胜率层：enabled=True，新记录=168，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 6，冷却合并 4
- 信号状态：NEW=1，RE_ALERT=0，REPEAT=0，追踪状态=5
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=1

### 24h运行健康

- runs=38，signals=65，avg_duration=200.0s，AI calls=47，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.13 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.05 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.05 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.99 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.99 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.97 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.93 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 观察候选

- **LDO LONG** [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=65.83 bucket=WATCHLIST_CANDIDATE AI分=None 综合=65.83 delta=$287,868 q=50/100 高质=0 样本=0 risk=money_printer_confirmed,swing_watch,volume_expansion

## 本轮开仓/加仓信号

### 1. LDO OPEN_LONG / Swing 65.83 / AI评分 None / 综合 65.83 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$287,868，最大单钱包：$287,868
- 标记价：0.32029，均价：0.29195，权重分：7.3699，净偏向分：7.3699
- AI独立评分：None，规则评分：65.83，综合开仓评分：65.83，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=25165057.400000002，oracle=0.3201，15m=3.1768% ，1h=3.1768% ，volRatio=2.0127
- 中长期评分：65.83 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$287,868，6h=$287,868，24h=$287,868
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 5.0, 'multi_window_accumulation': 20.0, 'money_printer_weight': 6.0, 'price_position_health': 12.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 10.0}
- 风险标签：money_printer_confirmed, swing_watch, volume_expansion
- Top wallets：
  - 0x0748e296e5a350ec36c8487a1cea406e1b57d4b2 money_printer INCREASE_POSITION $287,868 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=8 amount=$4,839,485 score=53.1101 groups={'smart_money': 4, 'money_printer': 4}
- **ETH EXIT_SHORT** wallets=5 amount=$1,325,640 score=39.9286 groups={'money_printer': 5}
- **HYPE EXIT_LONG** wallets=5 amount=$894,643 score=31.3977 groups={'smart_money': 2, 'money_printer': 3}
- **BTC EXIT_SHORT** wallets=4 amount=$1,468,335 score=31.3663 groups={'money_printer': 4}
- **SOL EXIT_LONG** wallets=4 amount=$1,533,486 score=28.9702 groups={'money_printer': 4}
- **ETH EXIT_LONG** wallets=3 amount=$543,694 score=16.8142 groups={'smart_money': 3}
- **HYPE EXIT_SHORT** wallets=2 amount=$693,480 score=15.8706 groups={'money_printer': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第31轮 amount=$7,481,932 prev=58 exit_ratio=- amount_ratio=1.64x age=270.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE LONG 第13轮 amount=$461,970 prev=66 exit_ratio=- amount_ratio=0.64x age=30.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH SHORT 第24轮 amount=$414,678 prev=57 exit_ratio=- amount_ratio=0.30x age=300.1m cooldown_left=4.0小时
- **COOLDOWN_MERGED** BTC LONG 第23轮 amount=$1,271,934 prev=55 exit_ratio=- amount_ratio=0.05x age=330.0m cooldown_left=3.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第13轮 amount=$894,643 prev=66 exit_ratio=1.2449 amount_ratio=0.64x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL LONG 第-轮 amount=$1,533,486 prev=59 exit_ratio=1.4221 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：68 条，方向正确 38，方向错误 30，平均方向收益 0.24%，最好 7.23%，最差 -7.29%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.71976 | -7.29 | -7.42 | 0.55 | -7.32 |
| 18 | LIT | SHORT | 2.63175 | 2.44135 | 7.23 | 7.10 | 8.47 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.44135 | 7.10 | 6.97 | 8.34 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.9228 | -6.46 | -6.59 | 1.11 | -7.50 |
| 13 | GRAM | SHORT | 1.6858 | 1.5873 | 5.84 | 5.71 | 6.60 | -0.52 |
| 8 | NEAR | SHORT | 2.0234 | 1.9228 | 4.97 | 4.84 | 6.03 | -2.72 |
| 41 | HYPE | SHORT | 71.902 | 68.3345 | 4.96 | 4.83 | 5.90 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 68.3345 | -4.57 | -4.70 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 68.3345 | 4.41 | 4.28 | 5.35 | -1.76 |
| 21 | ZEC | LONG | 463.135 | 483.555 | 4.41 | 4.28 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 483.555 | -4.41 | -4.54 | 1.19 | -10.16 |
| 47 | SOL | SHORT | 82.5535 | 79.0775 | 4.21 | 4.08 | 4.51 | -0.08 |
| 45 | MON | LONG | 0.025817 | 0.024738 | -4.18 | -4.31 | 0.89 | -7.78 |
| 4 | HYPE | SHORT | 71.0475 | 68.3345 | 3.82 | 3.69 | 4.76 | -2.39 |
| 40 | SOL | LONG | 82.0335 | 79.0775 | -3.60 | -3.73 | 0.71 | -3.91 |
| 14 | kPEPE | LONG | 0.002705 | 0.002617 | -3.25 | -3.38 | 1.44 | -3.81 |
| 5 | SOL | SHORT | 81.6175 | 79.0775 | 3.11 | 2.98 | 3.42 | -1.23 |
| 33 | ZEC | SHORT | 469.59 | 483.555 | -2.97 | -3.10 | 0.00 | -8.65 |
| 11 | SOL | LONG | 81.4165 | 79.0775 | -2.87 | -3.00 | 1.48 | -3.18 |
| 7 | XRP | SHORT | 1.13285 | 1.10045 | 2.86 | 2.73 | 3.26 | 0.00 |
| 56 | LIT | SHORT | 2.50975 | 2.44135 | 2.73 | 2.60 | 4.02 | 0.00 |
| 49 | HYPE | LONG | 70.1565 | 68.3345 | -2.60 | -2.73 | 0.23 | -3.55 |
| 39 | XRP | SHORT | 1.12915 | 1.10045 | 2.54 | 2.41 | 2.94 | -0.20 |
| 37 | ZEC | LONG | 495.815 | 483.555 | -2.47 | -2.60 | 2.90 | -3.76 |
| 42 | ETH | SHORT | 1803.55 | 1759.35 | 2.45 | 2.32 | 2.85 | -0.39 |
| 24 | SOL | SHORT | 81.0475 | 79.0775 | 2.43 | 2.30 | 2.74 | -1.94 |
| 46 | ETH | LONG | 1801.95 | 1759.35 | -2.36 | -2.49 | 0.48 | -2.76 |
| 44 | VVV | SHORT | 11.1805 | 10.9205 | 2.33 | 2.20 | 5.94 | 0.00 |
| 9 | TAO | LONG | 213.63 | 208.86 | -2.23 | -2.36 | 1.58 | -2.92 |
| 48 | BNB | SHORT | 584.295 | 571.45 | 2.20 | 2.07 | 2.38 | 0.00 |

</details>
