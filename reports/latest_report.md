# 钱包合约信号报告

Time: **2026-07-08 08:30:38 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1215，本轮 warmup 钱包：1206，变动事件：2053
- AI 输入信号：3，虚拟开仓：0，动态评分钱包：143
- 钱包胜率层：enabled=True，新记录=222，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 8，冷却合并 4
- 信号状态：NEW=1，RE_ALERT=1，REPEAT=1，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=0

### 24h运行健康

- runs=46，signals=64，avg_duration=212.1s，AI calls=51，AI estimated points=47505

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xf17de4...2adab2 | money_printer | NEW | 2.13 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 2.09 | 1 | - | - | - | - |
| 0x4ef1c5...a528e3 | smart_money | NEW | 2.09 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **SOL LONG** [ACTIVE_REPEAT / 第17轮 / 持续23.3小时 / 冷却剩余7.0小时 / 金额变化5.90x] swing=86.38 AI=- conf=- AI分=None 综合=86.38 delta=$2,594,457 wallets=3 q=44/100 高质=0 样本=1 horizon=3-14

### 开空强候选

- **HYPE SHORT** [RE_ALERT / 第20轮 / 持续25.5小时 / 冷却剩余7.0小时 / 金额变化3.77x] swing=89.18 AI=- conf=- AI分=None 综合=89.18 delta=$2,474,918 wallets=4 q=62/100 高质=1 样本=3 horizon=3-14

### 过滤/短线噪音

- kPEPE SHORT [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=51.83：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. HYPE OPEN_SHORT / Swing 89.18 / AI评分 None / 综合 89.18 / AI置信度 -

- 钱包数：4，分组：{'smart_money': 1, 'money_printer': 3}，事件：{'INCREASE_POSITION': 4}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$2,474,918，最大单钱包：$1,435,947
- 标记价：67.7955，均价：67.3577，权重分：29.943，净偏向分：24.7719
- AI独立评分：None，规则评分：89.18，综合开仓评分：89.18，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第20轮 / 持续25.5小时 / 冷却剩余7.0小时 / 金额变化3.77x
- 钱包质量：62/100 高质=1 样本=3，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$569,880，冲突比=0.2303
- 市场：funding=1.25e-05，OI=22094883.160000008，oracle=67.738，15m=-0.3929% ，1h=-0.3666% ，volRatio=2.7559
- 中长期评分：89.18 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,474,918，6h=$3,119,771，24h=$7,893,086
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 6.18, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong, volume_expansion
- Top wallets：
  - 0x645b2eeaa0a46df3c4211bebda1b2c7703e287b8 money_printer INCREASE_POSITION $1,435,947 score=1.10 grade=NEW win72=- avg72=-
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $673,688 score=1.05 grade=B win72=- avg72=-
  - 0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00 money_printer INCREASE_POSITION $224,185 score=1.74 grade=S win72=- avg72=-

### 2. SOL OPEN_LONG / Swing 86.38 / AI评分 None / 综合 86.38 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 1, 'money_printer': 2}，事件：{'INCREASE_POSITION': 2, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$2,594,457，最大单钱包：$2,171,745
- 标记价：77.1995，均价：76.06116667，权重分：20.3826，净偏向分：18.8474
- AI独立评分：None，规则评分：86.38，综合开仓评分：86.38，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第17轮 / 持续23.3小时 / 冷却剩余7.0小时 / 金额变化5.90x
- 钱包质量：44/100 高质=0 样本=1，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$260,548，冲突比=0.1004
- 市场：funding=1.14054e-05，OI=5270478.220000001，oracle=77.23，15m=-1.7599% ，1h=-1.7799% ，volRatio=1.3402
- 中长期评分：86.38 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,594,457，6h=$2,594,457，24h=$6,253,917
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.38, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, long_upper_wick_risk, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xa445a0a15b1d50fa0c4bfe6796d9447e0da5329d money_printer NEW_POSITION $2,171,745 score=1.00 grade=NEW win72=- avg72=-
  - 0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e money_printer INCREASE_POSITION $233,060 score=0.62 grade=NEW win72=- avg72=-
  - 0xdc5289909be4f3ce2604806bdd1448fd307f19f5 smart_money INCREASE_POSITION $189,652 score=1.00 grade=NEW win72=- avg72=-

### 3. kPEPE OPEN_SHORT / Swing 51.83 / AI评分 None / 综合 51.83 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$429,713，最大单钱包：$429,713
- 标记价：0.002581，均价：0.002591，权重分：5.6332，净偏向分：5.6332
- AI独立评分：None，规则评分：51.83，综合开仓评分：51.83，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=6158322526.0，oracle=0.002584，15m=-1.2228% ，1h=-1.2605% ，volRatio=4.3172
- 中长期评分：51.83 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$429,713，6h=$429,713，24h=$429,713
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 5.0, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, volume_expansion
- Top wallets：
  - 0x5eeb5a0cb514bf3843d5f1c24752ee0e3b08f46c smart_money INCREASE_POSITION $429,713 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=17 amount=$7,445,663 score=123.4359 groups={'smart_money': 5, 'money_printer': 12}
- **ETH EXIT_SHORT** wallets=6 amount=$2,279,964 score=47.0593 groups={'smart_money': 1, 'money_printer': 5}
- **BTC EXIT_LONG** wallets=5 amount=$6,361,558 score=28.2359 groups={'smart_money': 4, 'money_printer': 1}
- **HYPE EXIT_LONG** wallets=3 amount=$610,995 score=18.4897 groups={'smart_money': 2, 'money_printer': 1}
- **SOL EXIT_LONG** wallets=2 amount=$948,163 score=14.6182 groups={'smart_money': 1, 'money_printer': 1}
- **ETH EXIT_LONG** wallets=2 amount=$747,033 score=10.1306 groups={'smart_money': 1, 'money_printer': 1}
- **HYPE EXIT_SHORT** wallets=1 amount=$1,694,888 score=8.4093 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC LONG 第32轮 amount=$14,210,857 prev=69 exit_ratio=- amount_ratio=14.87x age=240.0m cooldown_left=5.0小时
- **COOLDOWN_MERGED** ETH SHORT 第34轮 amount=$4,171,153 prev=72 exit_ratio=- amount_ratio=0.79x age=210.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH LONG 第11轮 amount=$4,281,885 prev=63 exit_ratio=- amount_ratio=0.48x age=390.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** BTC SHORT 第40轮 amount=$3,454,400 prev=74 exit_ratio=- amount_ratio=0.58x age=59.8m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第40轮 amount=$7,445,663 prev=74 exit_ratio=0.5949 amount_ratio=0.58x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第34轮 amount=$2,279,964 prev=72 exit_ratio=0.7273 amount_ratio=0.79x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第20轮 amount=$1,694,888 prev=70 exit_ratio=2.6283 amount_ratio=3.77x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第-轮 amount=$610,995 prev=66 exit_ratio=0.8502 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：78 条，方向正确 39，方向错误 39，平均方向收益 0.14%，最好 10.12%，最差 -19.24%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.627035 | -19.24 | -19.37 | 0.55 | -19.24 |
| 18 | LIT | SHORT | 2.63175 | 2.36535 | 10.12 | 9.99 | 10.12 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.36535 | 9.99 | 9.86 | 9.99 | -2.20 |
| 45 | MON | LONG | 0.025817 | 0.023698 | -8.21 | -8.34 | 0.89 | -8.21 |
| 31 | NEAR | LONG | 2.05555 | 1.88885 | -8.11 | -8.24 | 1.11 | -8.11 |
| 13 | GRAM | SHORT | 1.6858 | 1.5678 | 7.00 | 6.87 | 7.00 | -0.52 |
| 44 | VVV | SHORT | 11.1805 | 10.413 | 6.86 | 6.73 | 6.86 | 0.00 |
| 8 | NEAR | SHORT | 2.0234 | 1.88885 | 6.65 | 6.52 | 6.65 | -2.72 |
| 47 | SOL | SHORT | 82.5535 | 77.1995 | 6.49 | 6.36 | 6.49 | -0.08 |
| 40 | SOL | LONG | 82.0335 | 77.1995 | -5.89 | -6.02 | 0.71 | -5.89 |
| 56 | LIT | SHORT | 2.50975 | 2.36535 | 5.75 | 5.62 | 5.75 | 0.00 |
| 41 | HYPE | SHORT | 71.902 | 67.7955 | 5.71 | 5.58 | 5.90 | -0.38 |
| 5 | SOL | SHORT | 81.6175 | 77.1995 | 5.41 | 5.28 | 5.41 | -1.23 |
| 16 | HYPE | LONG | 71.6085 | 67.7955 | -5.32 | -5.45 | 1.59 | -5.51 |
| 37 | ZEC | LONG | 495.815 | 469.84 | -5.24 | -5.37 | 2.90 | -5.24 |
| 11 | SOL | LONG | 81.4165 | 77.1995 | -5.18 | -5.31 | 1.48 | -5.18 |
| 28 | HYPE | SHORT | 71.49 | 67.7955 | 5.17 | 5.04 | 5.35 | -1.76 |
| 51 | ZEC | LONG | 493.435 | 469.84 | -4.78 | -4.91 | 0.83 | -4.78 |
| 24 | SOL | SHORT | 81.0475 | 77.1995 | 4.75 | 4.62 | 4.75 | -1.94 |
| 7 | XRP | SHORT | 1.13285 | 1.07985 | 4.68 | 4.55 | 4.68 | 0.00 |
| 14 | kPEPE | LONG | 0.002705 | 0.002581 | -4.58 | -4.71 | 1.44 | -4.58 |
| 4 | HYPE | SHORT | 71.0475 | 67.7955 | 4.58 | 4.45 | 4.76 | -2.39 |
| 39 | XRP | SHORT | 1.12915 | 1.07985 | 4.37 | 4.24 | 4.37 | -0.20 |
| 59 | SOL | LONG | 80.5705 | 77.1995 | -4.18 | -4.31 | 0.03 | -4.18 |
| 9 | TAO | LONG | 213.63 | 205.115 | -3.99 | -4.12 | 1.58 | -3.99 |
| 42 | ETH | SHORT | 1803.55 | 1732.05 | 3.96 | 3.83 | 3.96 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1732.05 | -3.88 | -4.01 | 0.48 | -3.88 |
| 48 | BNB | SHORT | 584.295 | 562.065 | 3.80 | 3.67 | 3.80 | 0.00 |
| 38 | ETH | LONG | 1797.05 | 1732.05 | -3.62 | -3.75 | 0.75 | -3.62 |
| 36 | ETH | SHORT | 1797.05 | 1732.05 | 3.62 | 3.49 | 3.62 | -0.75 |

</details>
