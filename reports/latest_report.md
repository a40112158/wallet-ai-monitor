# 钱包合约信号报告

Time: **2026-07-08 02:00:32 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1226，本轮 warmup 钱包：1195，变动事件：2273
- AI 输入信号：3，虚拟开仓：0，动态评分钱包：132
- 钱包胜率层：enabled=True，新记录=270，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 8，冷却合并 4
- 信号状态：NEW=1，RE_ALERT=0，REPEAT=2，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=0

### 24h运行健康

- runs=36，signals=60，avg_duration=198.5s，AI calls=45，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.11 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.11 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.04 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.99 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.98 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.98 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **ETH LONG** [ACTIVE_REPEAT / 第6轮 / 持续15.5小时 / 冷却剩余7.0小时 / 金额变化4.18x] swing=87.73 AI=- conf=- AI分=None 综合=87.73 delta=$2,479,913 wallets=7 q=57/100 高质=2 样本=4 horizon=3-14
- **NEAR LONG** [ACTIVE_REPEAT / 第4轮 / 持续10.5小时 / 冷却剩余7.0小时 / 金额变化1.39x] swing=86.55 AI=- conf=- AI分=None 综合=86.55 delta=$353,587 wallets=1 q=50/100 高质=0 样本=0 horizon=3-14

### 过滤/短线噪音

- XRP LONG [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=56.78：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. ETH OPEN_LONG / Swing 87.73 / AI评分 None / 综合 87.73 / AI置信度 -

- 钱包数：7，分组：{'smart_money': 4, 'money_printer': 3}，事件：{'FLIP_POSITION': 2, 'INCREASE_POSITION': 4, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$2,479,913，最大单钱包：$1,004,085
- 标记价：1753.65，均价：1756.4，权重分：45.0925，净偏向分：21.8329
- AI独立评分：None，规则评分：87.73，综合开仓评分：87.73，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第6轮 / 持续15.5小时 / 冷却剩余7.0小时 / 金额变化4.18x
- 钱包质量：57/100 高质=2 样本=4，高质量钱包=2，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$1,705,582，冲突比=0.6878
- 市场：funding=1.25e-05，OI=783457.4004000003，oracle=1753.7，15m=-1.301% ，1h=-1.301% ，volRatio=5.2421
- 中长期评分：87.73 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,479,913，6h=$2,479,913，24h=$7,443,221
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.73, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong, volume_expansion
- Top wallets：
  - 0xf9109ada2f73c62e9889b45453065f0d99260a2d smart_money INCREASE_POSITION $1,004,085 score=1.03 grade=B win72=- avg72=-
  - 0x3bcae23e8c380dab4732e9a159c0456f12d866f3 money_printer NEW_POSITION $441,837 score=1.46 grade=NEW win72=- avg72=-
  - 0xca4903c207a0df58bf37d4bc8bbc5210726f53c8 money_printer INCREASE_POSITION $343,547 score=1.00 grade=NEW win72=- avg72=-

### 2. XRP OPEN_LONG / Swing 56.78 / AI评分 None / 综合 56.78 / AI置信度 -

- 钱包数：2，分组：{'smart_money': 2}，事件：{'FLIP_POSITION': 1, 'INCREASE_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$608,128，最大单钱包：$425,533
- 标记价：1.09725，均价：1.104656，权重分：11.874，净偏向分：11.874
- AI独立评分：None，规则评分：56.78，综合开仓评分：56.78，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：61/100 高质=1 样本=1，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=-1.88562e-05，OI=70548946.0，oracle=1.0981，15m=-1.6504% ，1h=-1.6414% ，volRatio=4.5958
- 中长期评分：56.78 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$608,128，6h=$608,128，24h=$608,128
- 评分拆解：{'wallet_resonance': 7.67, 'wallet_quality': 6.11, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, volume_expansion
- Top wallets：
  - 0x9a31f7aff78fd464bbceb398e11b82ba633c6525 smart_money INCREASE_POSITION $425,533 score=1.00 grade=NEW win72=- avg72=-
  - 0x4537e1a5b7bcadd39f6d6211cb757ce431798732 smart_money FLIP_POSITION $182,594 score=1.75 grade=NEW win72=- avg72=-

### 3. NEAR OPEN_LONG / Swing 86.55 / AI评分 None / 综合 86.55 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$353,587，最大单钱包：$353,587
- 标记价：1.91015，均价：1.91954，权重分：7.4905，净偏向分：7.4905
- AI独立评分：None，规则评分：86.55，综合开仓评分：86.55，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第4轮 / 持续10.5小时 / 冷却剩余7.0小时 / 金额变化1.39x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=-9.46621e-05，OI=40668237.800000004，oracle=1.9115，15m=-4.3758% ，1h=-4.3959% ，volRatio=20.7419
- 中长期评分：86.55 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$353,587，6h=$353,587，24h=$1,132,526
- 评分拆解：{'wallet_resonance': 15.33, 'wallet_quality': 5.0, 'multi_window_accumulation': 22.5, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 8.72}
- 风险标签：money_printer_confirmed, swing_strong, volume_expansion
- Top wallets：
  - 0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e money_printer INCREASE_POSITION $353,587 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=22 amount=$22,963,007 score=168.7364 groups={'smart_money': 5, 'money_printer': 17}
- **ETH EXIT_SHORT** wallets=16 amount=$29,468,519 score=130.8542 groups={'smart_money': 2, 'money_printer': 14}
- **HYPE EXIT_SHORT** wallets=4 amount=$1,212,241 score=29.2869 groups={'money_printer': 3, 'smart_money': 1}
- **SOL EXIT_SHORT** wallets=4 amount=$2,959,653 score=28.6363 groups={'smart_money': 2, 'money_printer': 2}
- **NEAR EXIT_SHORT** wallets=3 amount=$362,208 score=21.4758 groups={'money_printer': 3}
- **XRP EXIT_SHORT** wallets=3 amount=$779,467 score=19.4706 groups={'smart_money': 2, 'money_printer': 1}
- **SOL EXIT_LONG** wallets=3 amount=$1,047,044 score=18.7774 groups={'money_printer': 1, 'smart_money': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC LONG 第22轮 amount=$25,516,289 prev=55 exit_ratio=- amount_ratio=19.76x age=269.9m cooldown_left=4.0小时
- **COOLDOWN_MERGED** HYPE LONG 第11轮 amount=$3,087,727 prev=52 exit_ratio=- amount_ratio=4.05x age=390.0m cooldown_left=5.0小时
- **COOLDOWN_MERGED** SOL LONG 第12轮 amount=$2,010,952 prev=59 exit_ratio=- amount_ratio=1.05x age=120.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC SHORT 第29轮 amount=$1,881,899 prev=58 exit_ratio=- amount_ratio=3.45x age=210.0m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第29轮 amount=$22,963,007 prev=58 exit_ratio=5.2806 amount_ratio=3.45x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL LONG 第12轮 amount=$1,047,044 prev=59 exit_ratio=0.971 amount_ratio=1.05x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第-轮 amount=$29,468,519 prev=54 exit_ratio=4.0964 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第-轮 amount=$1,212,241 prev=53 exit_ratio=0.538 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：65 条，方向正确 34，方向错误 31，平均方向收益 0.28%，最好 8.47%，最差 -7.07%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.40885 | 8.47 | 8.34 | 8.47 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.40885 | 8.34 | 8.21 | 8.34 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.91015 | -7.07 | -7.20 | 1.11 | -7.07 |
| 34 | JTO | LONG | 0.77639 | 0.72669 | -6.40 | -6.53 | 0.55 | -6.78 |
| 8 | NEAR | SHORT | 2.0234 | 1.91015 | 5.60 | 5.47 | 5.60 | -2.72 |
| 45 | MON | LONG | 0.025817 | 0.024379 | -5.57 | -5.70 | 0.89 | -7.78 |
| 41 | HYPE | SHORT | 71.902 | 67.9625 | 5.48 | 5.35 | 5.48 | -0.38 |
| 13 | GRAM | SHORT | 1.6858 | 1.5953 | 5.37 | 5.24 | 5.37 | -0.52 |
| 16 | HYPE | LONG | 71.6085 | 67.9625 | -5.09 | -5.22 | 1.59 | -5.09 |
| 28 | HYPE | SHORT | 71.49 | 67.9625 | 4.93 | 4.80 | 4.93 | -1.76 |
| 44 | VVV | SHORT | 11.1805 | 10.6775 | 4.50 | 4.37 | 5.94 | 0.00 |
| 47 | SOL | SHORT | 82.5535 | 78.9225 | 4.40 | 4.27 | 4.40 | -0.08 |
| 4 | HYPE | SHORT | 71.0475 | 67.9625 | 4.34 | 4.21 | 4.34 | -2.39 |
| 56 | LIT | SHORT | 2.50975 | 2.40885 | 4.02 | 3.89 | 4.02 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 78.9225 | -3.79 | -3.92 | 0.71 | -3.79 |
| 37 | ZEC | LONG | 495.815 | 477.155 | -3.76 | -3.89 | 2.90 | -3.76 |
| 14 | kPEPE | LONG | 0.002705 | 0.002612 | -3.44 | -3.57 | 1.44 | -3.44 |
| 5 | SOL | SHORT | 81.6175 | 78.9225 | 3.30 | 3.17 | 3.30 | -1.23 |
| 51 | ZEC | LONG | 493.435 | 477.155 | -3.30 | -3.43 | 0.83 | -3.30 |
| 62 | UNI | LONG | 3.2692 | 3.1661 | -3.15 | -3.28 | 0.00 | -3.15 |
| 7 | XRP | SHORT | 1.13285 | 1.09725 | 3.14 | 3.01 | 3.14 | 0.00 |
| 49 | HYPE | LONG | 70.1565 | 67.9625 | -3.13 | -3.26 | 0.23 | -3.13 |
| 11 | SOL | LONG | 81.4165 | 78.9225 | -3.06 | -3.19 | 1.48 | -3.06 |
| 21 | ZEC | LONG | 463.135 | 477.155 | 3.03 | 2.90 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 477.155 | -3.03 | -3.16 | 1.19 | -10.16 |
| 39 | XRP | SHORT | 1.12915 | 1.09725 | 2.83 | 2.70 | 2.83 | -0.20 |
| 42 | ETH | SHORT | 1803.55 | 1753.65 | 2.77 | 2.64 | 2.77 | -0.39 |
| 9 | TAO | LONG | 213.63 | 207.9 | -2.68 | -2.81 | 1.58 | -2.68 |
| 46 | ETH | LONG | 1801.95 | 1753.65 | -2.68 | -2.81 | 0.48 | -2.68 |
| 53 | HYPE | SHORT | 69.8095 | 67.9625 | 2.65 | 2.52 | 2.65 | -0.73 |

</details>
