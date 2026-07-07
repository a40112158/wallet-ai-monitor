# 钱包合约信号报告

Time: **2026-07-07 19:00:28 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1245，本轮 warmup 钱包：1176，变动事件：1715
- AI 输入信号：3，虚拟开仓：0，动态评分钱包：112
- 钱包胜率层：enabled=True，新记录=147，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 5，生命周期事件 8，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=2，REPEAT=1，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=3，观察候选=0

### 24h运行健康

- runs=22，signals=46，avg_duration=187.4s，AI calls=36，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.91 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.91 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.90 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.87 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.74 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.73 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.73 | 1 | - | - | - | - |
| 0x4537e1...798732 | smart_money | NEW | 1.70 | 1 | - | - | - | - |
| 0xe9d199...ecd2d3 | smart_money | NEW | 1.70 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **HYPE LONG** [ACTIVE_REPEAT / 第3轮 / 持续8.5小时 / 冷却剩余7.0小时 / 金额变化0.86x] swing=82.65 AI=- conf=- AI分=None 综合=82.65 delta=$1,530,506 wallets=8 q=31/100 高质=0 样本=4 horizon=3-14
- **ZEC LONG** [RE_ALERT / 第6轮 / 持续6.5小时 / 冷却剩余7.0小时 / 金额变化4.54x] swing=90.31 AI=- conf=- AI分=None 综合=90.31 delta=$1,146,230 wallets=2 q=49/100 高质=0 样本=1 horizon=3-14

### 开空强候选

- **ETH SHORT** [RE_ALERT / 第11轮 / 持续12.0小时 / 冷却剩余7.0小时 / 金额变化17.66x] swing=95.56 AI=- conf=- AI分=None 综合=95.56 delta=$15,631,416 wallets=3 q=50/100 高质=0 样本=0 horizon=3-14

## 本轮开仓/加仓信号

### 1. HYPE OPEN_LONG / Swing 82.65 / AI评分 None / 综合 82.65 / AI置信度 -

- 钱包数：8，分组：{'smart_money': 3, 'money_printer': 5}，事件：{'INCREASE_POSITION': 7, 'FLIP_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$1,530,506，最大单钱包：$367,830
- 标记价：70.1565，均价：70.4027875，权重分：49.3928，净偏向分：29.5819
- AI独立评分：None，规则评分：82.65，综合开仓评分：82.65，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第3轮 / 持续8.5小时 / 冷却剩余7.0小时 / 金额变化0.86x
- 钱包质量：31/100 高质=0 样本=4，高质量钱包=0，低质量钱包=3，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$818,492，冲突比=0.5348
- 市场：funding=1.25e-05，OI=22436361.519999996，oracle=70.216，15m=-2.4653% ，1h=-2.4653% ，volRatio=3.4141
- 中长期评分：82.65 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$1,530,506，6h=$1,530,506，24h=$4,695,974
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 3.06, 'multi_window_accumulation': 22.5, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.09}
- 风险标签：direction_conflict, long_upper_wick_risk, money_printer_confirmed, swing_strong, volume_expansion
- Top wallets：
  - 0x7fdafde5cfb5465924316eced2d3715494c517d1 money_printer INCREASE_POSITION $367,830 score=0.73 grade=C win72=- avg72=-
  - 0xd6e56265890b76413d1d527eb9b75e334c0c5b42 money_printer INCREASE_POSITION $320,231 score=1.00 grade=NEW win72=- avg72=-
  - 0x13640f452a56aaa7a5a5e5a6bd24c45374dacbcc smart_money INCREASE_POSITION $165,663 score=1.00 grade=NEW win72=- avg72=-

### 2. ETH OPEN_SHORT / Swing 95.56 / AI评分 None / 综合 95.56 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 1, 'money_printer': 2}，事件：{'INCREASE_POSITION': 2, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$15,631,416，最大单钱包：$14,732,089
- 标记价：1783.05，均价：1768.94333333，权重分：22.7113，净偏向分：22.7113
- AI独立评分：None，规则评分：95.56，综合开仓评分：95.56，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第11轮 / 持续12.0小时 / 冷却剩余7.0小时 / 金额变化17.66x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=803071.0782，oracle=1782.7，15m=-0.6674% ，1h=-0.6674% ，volRatio=3.4957
- 中长期评分：95.56 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$15,631,416，6h=$33,864,763，24h=$35,684,263
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.0, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 7.56}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, multi_round_accumulation, short_lower_wick_risk, swing_strong, volume_expansion
- Top wallets：
  - 0xa6ee1ed1ae80b8352603654b39f5e7b9bedd5078 money_printer NEW_POSITION $14,732,089 score=1.00 grade=NEW win72=- avg72=-
  - 0x3440f23a87f1950e7a88cd248fd270e92d1132c5 money_printer INCREASE_POSITION $778,936 score=1.00 grade=NEW win72=- avg72=-
  - 0x351126a070c9cadef8064ddd7b2d289fc33163aa smart_money INCREASE_POSITION $120,392 score=1.00 grade=NEW win72=- avg72=-

### 3. ZEC OPEN_LONG / Swing 90.31 / AI评分 None / 综合 90.31 / AI置信度 -

- 钱包数：2，分组：{'smart_money': 1, 'money_printer': 1}，事件：{'INCREASE_POSITION': 1, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$1,146,230，最大单钱包：$989,678
- 标记价：493.435，均价：497.77645，权重分：13.1285，净偏向分：13.1285
- AI独立评分：None，规则评分：90.31，综合开仓评分：90.31，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第6轮 / 持续6.5小时 / 冷却剩余7.0小时 / 金额变化4.54x
- 钱包质量：49/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=475879.16，oracle=493.58，15m=-0.3658% ，1h=-0.3658% ，volRatio=0.4784
- 中长期评分：90.31 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$1,146,230，6h=$3,714,695，24h=$4,247,991
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.86, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 3.45}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xd67ca2c6f8bc84acf4fa4472b82a8740dc0a53ff money_printer NEW_POSITION $989,678 score=1.00 grade=NEW win72=- avg72=-
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $156,552 score=0.88 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **ETH EXIT_SHORT** wallets=14 amount=$12,477,995 score=102.6622 groups={'smart_money': 1, 'money_printer': 13}
- **BTC EXIT_SHORT** wallets=10 amount=$7,277,638 score=67.4985 groups={'smart_money': 2, 'money_printer': 8}
- **SOL EXIT_SHORT** wallets=4 amount=$1,623,191 score=24.0513 groups={'smart_money': 2, 'money_printer': 2}
- **HYPE EXIT_LONG** wallets=4 amount=$9,432,166 score=23.7414 groups={'smart_money': 2, 'money_printer': 2}
- **HYPE EXIT_SHORT** wallets=3 amount=$4,951,475 score=21.6124 groups={'smart_money': 1, 'money_printer': 2}
- **ZEC EXIT_SHORT** wallets=2 amount=$316,465 score=15.2561 groups={'money_printer': 2}
- **SOL EXIT_LONG** wallets=3 amount=$446,090 score=13.794 groups={'smart_money': 3}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** SOL SHORT 第10轮 amount=$639,842 prev=24 exit_ratio=- amount_ratio=0.87x age=330.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC SHORT 第15轮 amount=$2,792,164 prev=26 exit_ratio=- amount_ratio=0.75x age=299.9m cooldown_left=6.5小时
- **COOLDOWN_MERGED** BTC LONG 第10轮 amount=$1,253,808 prev=20 exit_ratio=- amount_ratio=3.36x age=390.1m cooldown_left=4.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第5轮 amount=$818,492 prev=28 exit_ratio=- amount_ratio=0.47x age=292.5m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第10轮 amount=$1,623,191 prev=24 exit_ratio=1.4141 amount_ratio=0.87x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第11轮 amount=$12,477,995 prev=23 exit_ratio=6.6645 amount_ratio=17.66x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第5轮 amount=$4,951,475 prev=28 exit_ratio=6.4621 amount_ratio=0.47x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL LONG 第-轮 amount=$446,090 prev=40 exit_ratio=0.5438 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：51 条，方向正确 20，方向错误 31，平均方向收益 0.01%，最好 6.54%，最差 -6.54%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 493.435 | 6.54 | 6.41 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 493.435 | -6.54 | -6.67 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 493.435 | -5.08 | -5.21 | 0.00 | -8.65 |
| 34 | JTO | LONG | 0.77639 | 0.737995 | -4.95 | -5.08 | 0.55 | -4.95 |
| 18 | LIT | SHORT | 2.63175 | 2.5359 | 3.64 | 3.51 | 3.64 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.5359 | 3.50 | 3.37 | 4.57 | -2.20 |
| 44 | VVV | SHORT | 11.1805 | 10.7955 | 3.44 | 3.31 | 3.44 | 0.00 |
| 13 | GRAM | SHORT | 1.6858 | 1.6323 | 3.17 | 3.04 | 3.17 | -0.52 |
| 41 | HYPE | SHORT | 71.902 | 70.1565 | 2.43 | 2.30 | 2.43 | -0.38 |
| 31 | NEAR | LONG | 2.05555 | 2.01195 | -2.12 | -2.25 | 1.11 | -2.12 |
| 16 | HYPE | LONG | 71.6085 | 70.1565 | -2.03 | -2.16 | 1.59 | -2.03 |
| 45 | MON | LONG | 0.025817 | 0.025295 | -2.02 | -2.15 | 0.89 | -2.02 |
| 28 | HYPE | SHORT | 71.49 | 70.1565 | 1.87 | 1.74 | 1.87 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 81.0475 | 1.82 | 1.69 | 1.82 | -0.08 |
| 7 | XRP | SHORT | 1.13285 | 1.11575 | 1.51 | 1.38 | 1.58 | 0.00 |
| 4 | HYPE | SHORT | 71.0475 | 70.1565 | 1.25 | 1.12 | 1.25 | -2.39 |
| 40 | SOL | LONG | 82.0335 | 81.0475 | -1.20 | -1.33 | 0.71 | -1.20 |
| 39 | XRP | SHORT | 1.12915 | 1.11575 | 1.19 | 1.06 | 1.19 | -0.20 |
| 42 | ETH | SHORT | 1803.55 | 1783.05 | 1.14 | 1.01 | 1.14 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1783.05 | -1.05 | -1.18 | 0.48 | -1.05 |
| 26 | BTC | SHORT | 62945.5 | 63586.5 | -1.02 | -1.15 | 0.00 | -1.93 |
| 27 | ETH | SHORT | 1767.25 | 1783.05 | -0.89 | -1.02 | 0.00 | -2.45 |
| 38 | ETH | LONG | 1797.05 | 1783.05 | -0.78 | -0.91 | 0.75 | -0.78 |
| 36 | ETH | SHORT | 1797.05 | 1783.05 | 0.78 | 0.65 | 0.78 | -0.75 |
| 1 | BTC | SHORT | 63136.5 | 63586.5 | -0.71 | -0.84 | 0.30 | -1.62 |
| 5 | SOL | SHORT | 81.6175 | 81.0475 | 0.70 | 0.57 | 1.18 | -1.23 |
| 43 | BTC | LONG | 64028.5 | 63586.5 | -0.69 | -0.82 | 0.20 | -0.69 |
| 25 | BTC | LONG | 63172.5 | 63586.5 | 0.66 | 0.53 | 1.56 | -0.36 |
| 9 | TAO | LONG | 213.63 | 212.41 | -0.57 | -0.70 | 1.58 | -0.60 |
| 8 | NEAR | SHORT | 2.0234 | 2.01195 | 0.57 | 0.44 | 1.24 | -2.72 |

</details>
