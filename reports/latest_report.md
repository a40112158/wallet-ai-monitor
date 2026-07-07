# 钱包合约信号报告

Time: **2026-07-07 15:30:30 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1240，本轮 warmup 钱包：1181，变动事件：1506
- AI 输入信号：4，虚拟开仓：0，动态评分钱包：83
- 钱包胜率层：enabled=True，新记录=222，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 45120/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 8，生命周期事件 7，冷却合并 5
- 信号状态：NEW=2，RE_ALERT=2，REPEAT=0，追踪状态=9
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=1

### 24h运行健康

- runs=15，signals=28，avg_duration=169.7s，AI calls=29，AI estimated points=45716

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 1.73 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.73 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0x4e2328...ae20c3 | money_printer | NEW | 1.71 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.69 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.64 | 1 | - | - | - | - |
| 0x48ec00...a79faf | smart_money | NEW | 1.62 | 1 | - | - | - | - |
| 0x3da0af...fefe82 | smart_money | NEW | 1.61 | 1 | - | - | - | - |
| 0x4537e1...798732 | smart_money | NEW | 1.61 | 1 | - | - | - | - |
| 0xe9d199...ecd2d3 | smart_money | NEW | 1.61 | 1 | - | - | - | - |

## AI 状态

AI returned non-json

## 中长期合约开单候选池

### 开多强候选

- **BTC LONG** [RE_ALERT / 第5轮 / 持续3.0小时 / 冷却剩余6.0小时 / 金额变化1.11x] swing=88.62 AI=- conf=- AI分=None 综合=88.62 delta=$3,239,758 wallets=10 q=66/100 高质=3 样本=6 horizon=3-14

### 开空强候选

- **ZEC SHORT** [RE_ALERT / 第2轮 / 持续3.0小时 / 冷却剩余6.0小时 / 金额变化2.14x] swing=86.33 AI=- conf=- AI分=None 综合=86.33 delta=$1,408,324 wallets=4 q=38/100 高质=0 样本=3 horizon=3-14

### 观察候选

- **NEAR LONG** [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余6.0小时 / 金额变化-] swing=72.69 bucket=WATCHLIST_CANDIDATE AI分=None 综合=72.69 delta=$778,939 q=50/100 高质=0 样本=0 risk=money_printer_confirmed,swing_watch

### 过滤/短线噪音

- JTO LONG [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余6.0小时 / 金额变化-] swing=60.83：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. NEAR OPEN_LONG / Swing 72.69 / AI评分 None / 综合 72.69 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 2, 'money_printer': 1}，事件：{'INCREASE_POSITION': 2, 'NEW_POSITION': 1}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$778,939，最大单钱包：$513,888
- 标记价：2.05555，均价：2.04805333，权重分：17.9335，净偏向分：17.9335
- AI独立评分：None，规则评分：72.69，综合开仓评分：72.69，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余6.0小时 / 金额变化-
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.48662e-05，OI=43404162.8，oracle=2.0536，15m=0.8011% ，1h=0.935% ，volRatio=1.3678
- 中长期评分：72.69 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$778,939，6h=$778,939，24h=$778,939
- 评分拆解：{'wallet_resonance': 11.5, 'wallet_quality': 5.0, 'multi_window_accumulation': 20.0, 'money_printer_weight': 6.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 8.19}
- 风险标签：money_printer_confirmed, swing_watch
- Top wallets：
  - 0xad227f63d34e7251c1d0ab65e64eeea07aee4e44 money_printer INCREASE_POSITION $513,888 score=1.00 grade=NEW win72=- avg72=-
  - 0x39b07015ca813075bbce6f475767d5b4b9d518b0 smart_money INCREASE_POSITION $161,181 score=1.00 grade=NEW win72=- avg72=-
  - 0x7083a8e36b44865c8d40379502bc081259a0ba66 smart_money NEW_POSITION $103,871 score=1.00 grade=NEW win72=- avg72=-

### 2. BTC OPEN_LONG / Swing 88.62 / AI评分 None / 综合 88.62 / AI置信度 -

- 钱包数：10，分组：{'smart_money': 8, 'money_printer': 2}，事件：{'INCREASE_POSITION': 6, 'FLIP_POSITION': 4}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$3,239,758，最大单钱包：$1,216,591
- 标记价：63717.5，均价：63634.11，权重分：58.9505，净偏向分：14.7376
- AI独立评分：None，规则评分：88.62，综合开仓评分：88.62，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第5轮 / 持续3.0小时 / 冷却剩余6.0小时 / 金额变化1.11x
- 钱包质量：66/100 高质=3 样本=6，高质量钱包=3，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$10,457,239，冲突比=3.2278
- 市场：funding=1.25e-05，OI=38492.69158，oracle=63730.0，15m=0.0942% ，1h=0.5582% ，volRatio=0.5811
- 中长期评分：88.62 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$6,161,757，6h=$12,212,867，24h=$12,212,867
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 6.62, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x39b07015ca813075bbce6f475767d5b4b9d518b0 smart_money INCREASE_POSITION $1,216,591 score=1.00 grade=NEW win72=- avg72=-
  - 0xcf3f419d08a5bdc2c6e5fbd9ad70904c5420f95f smart_money FLIP_POSITION $459,060 score=0.85 grade=NEW win72=- avg72=-
  - 0x023a3d058020fb76cca98f01b3c48c8938a22355 money_printer INCREASE_POSITION $455,891 score=0.85 grade=NEW win72=- avg72=-

### 3. ZEC OPEN_SHORT / Swing 86.33 / AI评分 None / 综合 86.33 / AI置信度 -

- 钱包数：4，分组：{'smart_money': 1, 'money_printer': 3}，事件：{'INCREASE_POSITION': 3, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$1,408,324，最大单钱包：$581,855
- 标记价：469.59，均价：451.009875，权重分：26.2495，净偏向分：13.4779
- AI独立评分：None，规则评分：86.33，综合开仓评分：86.33，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第2轮 / 持续3.0小时 / 冷却剩余6.0小时 / 金额变化2.14x
- 钱包质量：38/100 高质=0 样本=3，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$913,620，冲突比=0.6487
- 市场：funding=2.75215e-05，OI=489431.74，oracle=469.23，15m=2.0209% ，1h=2.9523% ，volRatio=1.4997
- 中长期评分：86.33 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$1,408,324，6h=$2,067,569，24h=$2,067,569
- 评分拆解：{'wallet_resonance': 19.17, 'wallet_quality': 3.76, 'multi_window_accumulation': 22.5, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 5.9}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, swing_strong
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $581,855 score=0.86 grade=NEW win72=- avg72=-
  - 0x7fdafde5cfb5465924316eced2d3715494c517d1 money_printer INCREASE_POSITION $372,972 score=0.83 grade=NEW win72=- avg72=-
  - 0xd4c1f7e8d876c4749228d515473d36f919583d1d money_printer INCREASE_POSITION $252,156 score=0.47 grade=NEW win72=- avg72=-

### 4. JTO OPEN_LONG / Swing 60.83 / AI评分 None / 综合 60.83 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'NEW_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$251,321，最大单钱包：$251,321
- 标记价：0.77639，均价：0.779952，权重分：5.4002，净偏向分：5.4002
- AI独立评分：None，规则评分：60.83，综合开仓评分：60.83，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余6.0小时 / 金额变化-
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=19367558.0，oracle=0.7761，15m=-0.2509% ，1h=-0.6662% ，volRatio=3.5472
- 中长期评分：60.83 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$251,321，6h=$251,321，24h=$251,321
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 5.0, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 10.0}
- 风险标签：long_upper_wick_risk, volume_expansion
- Top wallets：
  - 0x39b07015ca813075bbce6f475767d5b4b9d518b0 smart_money NEW_POSITION $251,321 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=12 amount=$9,372,676 score=80.4494 groups={'smart_money': 4, 'money_printer': 8}
- **HYPE EXIT_LONG** wallets=5 amount=$1,280,705 score=30.2402 groups={'smart_money': 3, 'money_printer': 2}
- **ETH EXIT_LONG** wallets=2 amount=$369,824 score=12.3724 groups={'smart_money': 1, 'money_printer': 1}
- **BTC EXIT_LONG** wallets=2 amount=$246,115 score=10.1801 groups={'smart_money': 2}
- **POLYX EXIT_LONG** wallets=1 amount=$888,150 score=8.0305 groups={'money_printer': 1}
- **SOL EXIT_SHORT** wallets=1 amount=$107,468 score=6.7922 groups={'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=1 amount=$234,795 score=5.3707 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第4轮 amount=$2,302,231 prev=23 exit_ratio=- amount_ratio=0.39x age=120.1m cooldown_left=4.5小时
- **COOLDOWN_MERGED** SOL SHORT 第3轮 amount=$1,106,449 prev=24 exit_ratio=- amount_ratio=0.96x age=120.1m cooldown_left=4.0小时
- **COOLDOWN_MERGED** HYPE SHORT 第3轮 amount=$1,380,954 prev=28 exit_ratio=- amount_ratio=0.66x age=82.5m cooldown_left=4.6小时
- **COOLDOWN_MERGED** BTC SHORT 第8轮 amount=$10,457,239 prev=12 exit_ratio=- amount_ratio=0.65x age=329.7m cooldown_left=6.0小时
- **COOLDOWN_MERGED** ZEC LONG 第2轮 amount=$913,620 prev=21 exit_ratio=- amount_ratio=1.71x age=180.1m cooldown_left=3.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第8轮 amount=$9,372,676 prev=12 exit_ratio=1.4947 amount_ratio=0.65x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** ETH LONG 第-轮 amount=$369,824 prev=17 exit_ratio=1.2174 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

| id | coin | side | lev | margin | notional | entry | current | pnl% | ROE% | pnl_usd | status | 准备平仓 | reason | AI平仓 | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|
| 1 | BTC | SHORT | 1.0x | $500.00 | $500.00 | 63136.5 | 63717.5 | -0.92 | -0.92 | -4.60 | CLOSED |  | AI_CLOSE | 92: 该BTC SHORT 已触发ACTIVE_SIGNAL_DECAY，且最新市场信 | 0.30 | -0.92 |

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：34 条，方向正确 13，方向错误 21，平均方向收益 -0.18%，最好 1.82%，最差 -2.39%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 4 | HYPE | SHORT | 71.0475 | 72.7485 | -2.39 | -2.52 | 0.00 | -2.39 |
| 18 | LIT | SHORT | 2.63175 | 2.58385 | 1.82 | 1.69 | 3.01 | -2.05 |
| 28 | HYPE | SHORT | 71.49 | 72.7485 | -1.76 | -1.89 | 0.00 | -1.76 |
| 6 | LIT | SHORT | 2.6279 | 2.58385 | 1.68 | 1.55 | 4.57 | -2.20 |
| 16 | HYPE | LONG | 71.6085 | 72.7485 | 1.59 | 1.46 | 1.59 | -0.59 |
| 8 | NEAR | SHORT | 2.0234 | 2.05555 | -1.59 | -1.72 | 1.24 | -1.59 |
| 27 | ETH | SHORT | 1767.25 | 1792.7 | -1.44 | -1.57 | 0.00 | -1.44 |
| 21 | ZEC | LONG | 463.135 | 469.59 | 1.39 | 1.26 | 1.41 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 469.59 | -1.39 | -1.52 | 1.19 | -1.41 |
| 26 | BTC | SHORT | 62945.5 | 63717.5 | -1.23 | -1.36 | 0.00 | -1.23 |
| 23 | ETH | SHORT | 1773.75 | 1792.7 | -1.07 | -1.20 | 0.37 | -1.07 |
| 24 | SOL | SHORT | 81.0475 | 81.904 | -1.06 | -1.19 | 0.49 | -1.06 |
| 1 | BTC | SHORT | 63136.5 | 63717.5 | -0.92 | -1.05 | 0.30 | -0.92 |
| 25 | BTC | LONG | 63172.5 | 63717.5 | 0.86 | 0.73 | 0.86 | -0.36 |
| 10 | BTC | SHORT | 63245.5 | 63717.5 | -0.75 | -0.88 | 0.47 | -0.75 |
| 12 | BTC | SHORT | 63271.5 | 63717.5 | -0.70 | -0.83 | 0.52 | -0.70 |
| 17 | ETH | LONG | 1780.75 | 1792.7 | 0.67 | 0.54 | 0.67 | -0.76 |
| 3 | ETH | SHORT | 1781.15 | 1792.7 | -0.65 | -0.78 | 0.78 | -0.65 |
| 11 | SOL | LONG | 81.4165 | 81.904 | 0.60 | 0.47 | 0.60 | -0.94 |
| 15 | BTC | SHORT | 63341.5 | 63717.5 | -0.59 | -0.72 | 0.63 | -0.59 |
| 7 | XRP | SHORT | 1.13285 | 1.1262 | 0.59 | 0.46 | 1.58 | 0.00 |
| 2 | BTC | SHORT | 63427.5 | 63717.5 | -0.46 | -0.59 | 0.76 | -0.46 |
| 9 | TAO | LONG | 213.63 | 214.6 | 0.45 | 0.32 | 1.58 | -0.60 |
| 22 | BTC | LONG | 63460.5 | 63717.5 | 0.40 | 0.27 | 0.40 | -0.81 |
| 5 | SOL | SHORT | 81.6175 | 81.904 | -0.35 | -0.48 | 1.18 | -0.35 |
| 30 | BTC | LONG | 63562.5 | 63717.5 | 0.24 | 0.11 | 0.24 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 63717.5 | -0.24 | -0.37 | 0.00 | -0.24 |
| 13 | GRAM | SHORT | 1.6858 | 1.6821 | 0.22 | 0.09 | 1.76 | -0.52 |
| 14 | kPEPE | LONG | 0.002705 | 0.002704 | -0.04 | -0.17 | 0.33 | -1.37 |
| 20 | BTC | LONG | 63706.5 | 63717.5 | 0.02 | -0.11 | 0.02 | -1.19 |

</details>
