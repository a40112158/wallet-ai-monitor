# 钱包合约信号报告

Time: **2026-07-07 16:00:27 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1239，本轮 warmup 钱包：1182，变动事件：1845
- AI 输入信号：7，虚拟开仓：0，动态评分钱包：83
- 钱包胜率层：enabled=True，新记录=219，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 45716/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 7，生命周期事件 12，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=5，REPEAT=2，追踪状态=11
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=4，观察候选=3

### 24h运行健康

- runs=16，signals=32，avg_duration=173.9s，AI calls=30，AI estimated points=46078

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.82 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.82 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.80 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.67 | 1 | - | - | - | - |
| 0x48ec00...a79faf | smart_money | NEW | 1.64 | 1 | - | - | - | - |
| 0x50a4d3...0f8168 | smart_money | NEW | 1.64 | 1 | - | - | - | - |
| 0x45ffe9...abff5f | smart_money | NEW | 1.63 | 2 | - | - | - | - |
| 0x3da0af...fefe82 | smart_money | NEW | 1.63 | 1 | - | - | - | - |
| 0x6e8bc7...ffea79 | smart_money | NEW | 1.62 | 1 | - | - | - | - |

## AI 状态

AI returned non-json

## 中长期合约开单候选池

### 开多强候选

- **BTC LONG** [RE_ALERT / 第6轮 / 持续3.5小时 / 冷却剩余6.0小时 / 金额变化1.52x] swing=88.21 AI=- conf=- AI分=None 综合=88.21 delta=$4,930,398 wallets=8 q=62/100 高质=2 样本=5 horizon=3-14

### 开空强候选

- **ETH SHORT** [RE_ALERT / 第5轮 / 持续9.0小时 / 冷却剩余6.0小时 / 金额变化2.37x] swing=87.96 AI=- conf=- AI分=None 综合=87.96 delta=$5,462,689 wallets=9 q=25/100 高质=0 样本=7 horizon=3-14
- **XRP SHORT** [ACTIVE_REPEAT / 第2轮 / 持续9.0小时 / 冷却剩余6.0小时 / 金额变化4.85x] swing=81.83 AI=- conf=- AI分=None 综合=81.83 delta=$574,813 wallets=1 q=50/100 高质=0 样本=0 horizon=3-14
- **HYPE SHORT** [RE_ALERT / 第4轮 / 持续9.0小时 / 冷却剩余6.0小时 / 金额变化1.27x] swing=87.96 AI=- conf=- AI分=None 综合=87.96 delta=$1,753,747 wallets=2 q=31/100 高质=0 样本=2 horizon=3-14

### 观察候选

- **ZEC LONG** [RE_ALERT / 第3轮 / 持续3.5小时 / 冷却剩余6.0小时 / 金额变化2.81x] swing=79.17 bucket=WATCHLIST_CANDIDATE AI分=None 综合=79.17 delta=$2,568,465 q=50/100 高质=0 样本=0 risk=cooldown_realert_large_add,direction_conflict,long_chasing_pump,money_printer_confirmed,price_extended_wait_pullback,swing_watch,volume_expansion
- **ETH LONG** [RE_ALERT / 第2轮 / 持续5.5小时 / 冷却剩余6.0小时 / 金额变化12.37x] swing=77.44 bucket=WATCHLIST_CANDIDATE AI分=None 综合=77.44 delta=$3,758,551 q=56/100 高质=1 样本=1 risk=cooldown_realert_large_add,direction_conflict,high_long_short_conflict,money_printer_confirmed,swing_watch
- **SOL LONG** [ACTIVE_REPEAT / 第2轮 / 持续6.8小时 / 冷却剩余6.0小时 / 金额变化0.47x] swing=68.23 bucket=WATCHLIST_CANDIDATE AI分=None 综合=68.23 delta=$820,335 q=50/100 高质=0 样本=0 risk=direction_conflict,money_printer_confirmed,swing_watch

## 本轮开仓/加仓信号

### 1. BTC OPEN_LONG / Swing 88.21 / AI评分 None / 综合 88.21 / AI置信度 -

- 钱包数：8，分组：{'smart_money': 5, 'money_printer': 3}，事件：{'INCREASE_POSITION': 6, 'FLIP_POSITION': 2}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$4,930,398，最大单钱包：$2,672,499
- 标记价：63930.5，均价：63872.3375，权重分：51.7467，净偏向分：47.1122
- AI独立评分：None，规则评分：88.21，综合开仓评分：88.21，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第6轮 / 持续3.5小时 / 冷却剩余6.0小时 / 金额变化1.52x
- 钱包质量：62/100 高质=2 样本=5，高质量钱包=2，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$588,758，冲突比=0.1194
- 市场：funding=1.25e-05，OI=37987.0134，oracle=63955.0，15m=0.712% ，1h=0.712% ，volRatio=0.66
- 中长期评分：88.21 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$11,092,154，6h=$17,143,265，24h=$17,143,265
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 6.21, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, long_upper_wick_risk, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x469e9a7f624b04c24f0e64edf8d8a277e6bf58a5 money_printer INCREASE_POSITION $2,672,499 score=1.00 grade=NEW win72=- avg72=-
  - 0xcf3f419d08a5bdc2c6e5fbd9ad70904c5420f95f smart_money INCREASE_POSITION $692,355 score=0.84 grade=NEW win72=- avg72=-
  - 0x0c349d9b92fbd172bbb5a17a9db0a673a6a10ad3 money_printer INCREASE_POSITION $494,137 score=1.00 grade=NEW win72=- avg72=-

### 2. ETH OPEN_SHORT / Swing 87.96 / AI评分 None / 综合 87.96 / AI置信度 -

- 钱包数：9，分组：{'smart_money': 1, 'money_printer': 8}，事件：{'FLIP_POSITION': 1, 'INCREASE_POSITION': 7, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$5,462,689，最大单钱包：$2,477,121
- 标记价：1797.05，均价：1760.60666667，权重分：61.4289，净偏向分：29.7297
- AI独立评分：None，规则评分：87.96，综合开仓评分：87.96，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第5轮 / 持续9.0小时 / 冷却剩余6.0小时 / 金额变化2.37x
- 钱包质量：25/100 高质=0 样本=7，高质量钱包=0，低质量钱包=5，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$3,758,551，冲突比=0.688
- 市场：funding=1.25e-05，OI=798725.1523999997，oracle=1797.3，15m=0.8303% ，1h=0.8303% ，volRatio=1.7245
- 中长期评分：87.96 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$11,410,145，6h=$13,282,454，24h=$15,101,954
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 2.46, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 2.5}
- 风险标签：cooldown_realert_large_add, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x3bcae23e8c380dab4732e9a159c0456f12d866f3 money_printer NEW_POSITION $2,477,121 score=0.59 grade=NEW win72=- avg72=-
  - 0x023a3d058020fb76cca98f01b3c48c8938a22355 money_printer INCREASE_POSITION $805,976 score=0.84 grade=C win72=- avg72=-
  - 0x39475d17bcd20adc540e647dae6781b153fbf3b1 money_printer INCREASE_POSITION $392,131 score=1.00 grade=NEW win72=- avg72=-

### 3. ZEC OPEN_LONG / Swing 79.17 / AI评分 None / 综合 79.17 / AI置信度 -

- 钱包数：4，分组：{'smart_money': 1, 'money_printer': 3}，事件：{'NEW_POSITION': 2, 'INCREASE_POSITION': 2}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$2,568,465，最大单钱包：$1,239,538
- 标记价：495.815，均价：476.123875，权重分：28.2665，净偏向分：19.7993
- AI独立评分：None，规则评分：79.17，综合开仓评分：79.17，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第3轮 / 持续3.5小时 / 冷却剩余6.0小时 / 金额变化2.81x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$1,025,836，冲突比=0.3994
- 市场：funding=1.25e-05，OI=483568.0799999998，oracle=495.51，15m=7.8436% ，1h=7.8436% ，volRatio=3.971
- 中长期评分：79.17 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,568,465，6h=$3,101,761，24h=$3,101,761
- 评分拆解：{'wallet_resonance': 19.17, 'wallet_quality': 5.0, 'multi_window_accumulation': 22.5, 'money_printer_weight': 12.0, 'price_position_health': 9.5, 'oi_funding_health': 9.0, 'low_direction_conflict': 2.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, long_chasing_pump, money_printer_confirmed, price_extended_wait_pullback, swing_watch, volume_expansion
- Top wallets：
  - 0xad227f63d34e7251c1d0ab65e64eeea07aee4e44 money_printer INCREASE_POSITION $1,239,538 score=1.00 grade=NEW win72=- avg72=-
  - 0xd487e26c62ed8c28ce3cc70b5791e501c2934982 money_printer INCREASE_POSITION $1,096,539 score=1.00 grade=NEW win72=- avg72=-
  - 0x00897e2d7168165b81558c3cd9257efb007f2410 smart_money NEW_POSITION $126,076 score=1.00 grade=NEW win72=- avg72=-

### 4. ETH OPEN_LONG / Swing 77.44 / AI评分 None / 综合 77.44 / AI置信度 -

- 钱包数：4，分组：{'smart_money': 2, 'money_printer': 2}，事件：{'INCREASE_POSITION': 2, 'NEW_POSITION': 1, 'FLIP_POSITION': 1}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$3,758,551，最大单钱包：$1,797,050
- 标记价：1797.05，均价：1872.8875，权重分：28.3348，净偏向分：7.0837
- AI独立评分：None，规则评分：77.44，综合开仓评分：77.44，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第2轮 / 持续5.5小时 / 冷却剩余6.0小时 / 金额变化12.37x
- 钱包质量：56/100 高质=1 样本=1，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$5,462,689，冲突比=1.4534
- 市场：funding=1.25e-05，OI=798725.1523999997，oracle=1797.3，15m=0.8303% ，1h=0.8303% ，volRatio=1.7245
- 中长期评分：77.44 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$3,758,551，6h=$4,062,332，24h=$4,062,332
- 评分拆解：{'wallet_resonance': 15.33, 'wallet_quality': 5.61, 'multi_window_accumulation': 22.5, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, high_long_short_conflict, money_printer_confirmed, swing_watch
- Top wallets：
  - 0xad227f63d34e7251c1d0ab65e64eeea07aee4e44 money_printer FLIP_POSITION $1,797,050 score=1.00 grade=NEW win72=- avg72=-
  - 0xa516541e599129095d14f7faf8b11ae670c837b0 smart_money NEW_POSITION $1,211,971 score=1.00 grade=NEW win72=- avg72=-
  - 0x48ec0004494081e8332589faf0747d568da79faf smart_money INCREASE_POSITION $536,103 score=1.62 grade=NEW win72=- avg72=-

### 5. XRP OPEN_SHORT / Swing 81.83 / AI评分 None / 综合 81.83 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$574,813，最大单钱包：$574,813
- 标记价：1.12915，均价：1.251393，权重分：5.7595，净偏向分：5.7595
- AI独立评分：None，规则评分：81.83，综合开仓评分：81.83，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第2轮 / 持续9.0小时 / 冷却剩余6.0小时 / 金额变化4.85x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=8.96e-06，OI=70277972.0，oracle=1.1301，15m=0.1865% ，1h=0.1865% ，volRatio=1.8885
- 中长期评分：81.83 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$574,813，6h=$574,813，24h=$693,267
- 评分拆解：{'wallet_resonance': 15.33, 'wallet_quality': 5.0, 'multi_window_accumulation': 22.5, 'money_printer_weight': 6.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 10.0}
- 风险标签：money_printer_confirmed, swing_strong
- Top wallets：
  - 0x7c976f00e84db0b44f945fc6d7fad34b43150a1a smart_money INCREASE_POSITION $574,813 score=1.00 grade=NEW win72=- avg72=-

### 6. SOL OPEN_LONG / Swing 68.23 / AI评分 None / 综合 68.23 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'FLIP_POSITION': 1}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$820,335，最大单钱包：$820,335
- 标记价：82.0335，均价：82.3134，权重分：7.9839，净偏向分：4.6566
- AI独立评分：None，规则评分：68.23，综合开仓评分：68.23，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第2轮 / 持续6.8小时 / 冷却剩余6.0小时 / 金额变化0.47x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$455,829，冲突比=0.5557
- 市场：funding=1.25e-05，OI=5541202.539999998，oracle=82.065，15m=0.7149% ，1h=0.7149% ，volRatio=1.1677
- 中长期评分：68.23 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$820,335，6h=$820,335，24h=$2,581,145
- 评分拆解：{'wallet_resonance': 11.5, 'wallet_quality': 5.0, 'multi_window_accumulation': 22.5, 'money_printer_weight': 6.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 1.23}
- 风险标签：direction_conflict, money_printer_confirmed, swing_watch
- Top wallets：
  - 0xad227f63d34e7251c1d0ab65e64eeea07aee4e44 money_printer FLIP_POSITION $820,335 score=1.00 grade=NEW win72=- avg72=-

### 7. HYPE OPEN_SHORT / Swing 87.96 / AI评分 None / 综合 87.96 / AI置信度 -

- 钱包数：2，分组：{'smart_money': 1, 'money_printer': 1}，事件：{'INCREASE_POSITION': 2}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$1,753,747，最大单钱包：$1,623,380
- 标记价：71.902，均价：69.7413，权重分：11.7802，净偏向分：2.9451
- AI独立评分：None，规则评分：87.96，综合开仓评分：87.96，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第4轮 / 持续9.0小时 / 冷却剩余6.0小时 / 金额变化1.27x
- 钱包质量：31/100 高质=0 样本=2，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$1,775,134，冲突比=1.0122
- 市场：funding=1.25e-05，OI=22530930.279999997，oracle=71.961，15m=-0.243% ，1h=-0.243% ，volRatio=0.7423
- 中长期评分：87.96 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,519,986，6h=$2,519,986，24h=$4,609,768
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 3.1, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 1.86}
- 风险标签：cooldown_realert_large_add, direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $1,623,380 score=0.75 grade=NEW win72=- avg72=-
  - 0xd4c1f7e8d876c4749228d515473d36f919583d1d money_printer INCREASE_POSITION $130,368 score=0.45 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=17 amount=$16,200,897 score=116.8171 groups={'smart_money': 4, 'money_printer': 13}
- **SOL EXIT_SHORT** wallets=5 amount=$2,414,279 score=29.5877 groups={'smart_money': 3, 'money_printer': 2}
- **ZEC EXIT_SHORT** wallets=4 amount=$3,496,205 score=29.5352 groups={'smart_money': 1, 'money_printer': 3}
- **ETH EXIT_SHORT** wallets=4 amount=$1,279,044 score=24.001 groups={'smart_money': 2, 'money_printer': 2}
- **BTC EXIT_LONG** wallets=4 amount=$3,578,999 score=22.8853 groups={'smart_money': 3, 'money_printer': 1}
- **HYPE EXIT_LONG** wallets=3 amount=$1,274,788 score=20.4056 groups={'smart_money': 1, 'money_printer': 2}
- **ETH EXIT_LONG** wallets=3 amount=$680,075 score=17.9404 groups={'smart_money': 2, 'money_printer': 1}
- **XRP EXIT_SHORT** wallets=2 amount=$284,485 score=13.1429 groups={'money_printer': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** HYPE LONG 第2轮 amount=$1,775,134 prev=16 exit_ratio=- amount_ratio=0.56x age=330.8m cooldown_left=29分钟
- **COOLDOWN_MERGED** BTC SHORT 第9轮 amount=$588,758 prev=12 exit_ratio=- amount_ratio=0.06x age=359.7m cooldown_left=6.0小时
- **COOLDOWN_MERGED** ZEC SHORT 第3轮 amount=$1,025,836 prev=19 exit_ratio=- amount_ratio=0.73x age=210.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** SOL SHORT 第4轮 amount=$455,829 prev=24 exit_ratio=- amount_ratio=0.41x age=150.0m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第3轮 amount=$3,496,205 prev=19 exit_ratio=5.3033 amount_ratio=0.73x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第6轮 amount=$3,578,999 prev=20 exit_ratio=3.1708 amount_ratio=1.52x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第9轮 amount=$16,200,897 prev=12 exit_ratio=2.5836 amount_ratio=0.06x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第4轮 amount=$452,274 prev=28 exit_ratio=0.5903 amount_ratio=1.27x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第5轮 amount=$1,279,044 prev=23 exit_ratio=0.6831 amount_ratio=2.37x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第4轮 amount=$2,414,279 prev=24 exit_ratio=2.1032 amount_ratio=0.41x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC LONG 第3轮 amount=$5,128,824 prev=21 exit_ratio=9.6172 amount_ratio=2.81x age=-m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** ETH LONG 第2轮 amount=$680,075 prev=17 exit_ratio=2.2387 amount_ratio=12.37x age=-m cooldown_left=6.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：41 条，方向正确 17，方向错误 24，平均方向收益 -0.23%，最好 7.06%，最差 -7.06%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 495.815 | 7.06 | 6.93 | 7.06 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 495.815 | -7.06 | -7.19 | 1.19 | -7.06 |
| 33 | ZEC | SHORT | 469.59 | 495.815 | -5.58 | -5.71 | 0.00 | -5.58 |
| 18 | LIT | SHORT | 2.63175 | 2.5618 | 2.66 | 2.53 | 3.01 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.5618 | 2.52 | 2.39 | 4.57 | -2.20 |
| 8 | NEAR | SHORT | 2.0234 | 2.06855 | -2.23 | -2.36 | 1.24 | -2.23 |
| 27 | ETH | SHORT | 1767.25 | 1797.05 | -1.69 | -1.82 | 0.00 | -1.69 |
| 26 | BTC | SHORT | 62945.5 | 63930.5 | -1.56 | -1.69 | 0.00 | -1.56 |
| 23 | ETH | SHORT | 1773.75 | 1797.05 | -1.31 | -1.44 | 0.37 | -1.31 |
| 1 | BTC | SHORT | 63136.5 | 63930.5 | -1.26 | -1.39 | 0.30 | -1.26 |
| 24 | SOL | SHORT | 81.0475 | 82.0335 | -1.22 | -1.35 | 0.49 | -1.22 |
| 4 | HYPE | SHORT | 71.0475 | 71.902 | -1.20 | -1.33 | 0.00 | -2.39 |
| 25 | BTC | LONG | 63172.5 | 63930.5 | 1.20 | 1.07 | 1.20 | -0.36 |
| 10 | BTC | SHORT | 63245.5 | 63930.5 | -1.08 | -1.21 | 0.47 | -1.08 |
| 12 | BTC | SHORT | 63271.5 | 63930.5 | -1.04 | -1.17 | 0.52 | -1.04 |
| 15 | BTC | SHORT | 63341.5 | 63930.5 | -0.93 | -1.06 | 0.63 | -0.93 |
| 17 | ETH | LONG | 1780.75 | 1797.05 | 0.92 | 0.79 | 0.92 | -0.76 |
| 3 | ETH | SHORT | 1781.15 | 1797.05 | -0.89 | -1.02 | 0.78 | -0.89 |
| 9 | TAO | LONG | 213.63 | 215.5 | 0.88 | 0.75 | 1.58 | -0.60 |
| 2 | BTC | SHORT | 63427.5 | 63930.5 | -0.79 | -0.92 | 0.76 | -0.79 |
| 11 | SOL | LONG | 81.4165 | 82.0335 | 0.76 | 0.63 | 0.76 | -0.94 |
| 22 | BTC | LONG | 63460.5 | 63930.5 | 0.74 | 0.61 | 0.74 | -0.81 |
| 31 | NEAR | LONG | 2.05555 | 2.06855 | 0.63 | 0.50 | 0.63 | 0.00 |
| 30 | BTC | LONG | 63562.5 | 63930.5 | 0.58 | 0.45 | 0.58 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 63930.5 | -0.58 | -0.71 | 0.00 | -0.58 |
| 28 | HYPE | SHORT | 71.49 | 71.902 | -0.58 | -0.71 | 0.00 | -1.76 |
| 5 | SOL | SHORT | 81.6175 | 82.0335 | -0.51 | -0.64 | 1.18 | -0.51 |
| 16 | HYPE | LONG | 71.6085 | 71.902 | 0.41 | 0.28 | 1.59 | -0.59 |
| 14 | kPEPE | LONG | 0.002705 | 0.002716 | 0.41 | 0.28 | 0.41 | -1.37 |
| 20 | BTC | LONG | 63706.5 | 63930.5 | 0.35 | 0.22 | 0.35 | -1.19 |

</details>
