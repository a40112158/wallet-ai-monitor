# 钱包合约信号报告

Time: **2026-07-08 04:30:38 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1218，本轮 warmup 钱包：1203，变动事件：1336
- AI 输入信号：3，虚拟开仓：0，动态评分钱包：140
- 钱包胜率层：enabled=True，新记录=168，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 3，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=1，REPEAT=2，追踪状态=6
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=3，观察候选=0

### 24h运行健康

- runs=41，signals=66，avg_duration=200.3s，AI calls=48，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.01 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.00 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.00 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.00 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.95 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.95 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **BTC LONG** [ACTIVE_REPEAT / 第26轮 / 持续16.0小时 / 冷却剩余7.0小时 / 金额变化4.64x] swing=86.35 AI=- conf=- AI分=None 综合=86.35 delta=$16,202,669 wallets=2 q=44/100 高质=0 样本=1 horizon=3-14
- **ETH LONG** [RE_ALERT / 第8轮 / 持续18.0小时 / 冷却剩余7.0小时 / 金额变化12.72x] swing=87.0 AI=- conf=- AI分=None 综合=87.0 delta=$16,120,579 wallets=1 q=50/100 高质=0 样本=0 horizon=3-14

### 开空强候选

- **HYPE SHORT** [ACTIVE_REPEAT / 第12轮 / 持续21.5小时 / 冷却剩余7.0小时 / 金额变化1.07x] swing=89.48 AI=- conf=- AI分=None 综合=89.48 delta=$644,853 wallets=3 q=65/100 高质=1 样本=2 horizon=3-14

## 本轮开仓/加仓信号

### 1. BTC OPEN_LONG / Swing 86.35 / AI评分 None / 综合 86.35 / AI置信度 -

- 钱包数：2，分组：{'smart_money': 1, 'money_printer': 1}，事件：{'INCREASE_POSITION': 2}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$16,202,669，最大单钱包：$15,969,590
- 标记价：62890.5，均价：62808.45，权重分：14.7089，净偏向分：10.09
- AI独立评分：None，规则评分：86.35，综合开仓评分：86.35，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第26轮 / 持续16.0小时 / 冷却剩余7.0小时 / 金额变化4.64x
- 钱包质量：44/100 高质=0 样本=1，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$6,784,030，冲突比=0.4187
- 市场：funding=1.25e-05，OI=38080.20094，oracle=62893.0，15m=-0.9191% ，1h=-1.1885% ，volRatio=0.4643
- 中长期评分：86.35 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$16,202,669，6h=$16,202,669，24h=$55,910,669
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.35, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, long_upper_wick_risk, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x049bdc370620beab340b01072fa580fd57745e7d money_printer INCREASE_POSITION $15,969,590 score=1.00 grade=NEW win72=- avg72=-
  - 0x8f63c88fccae90c1f9eb8b447f830bce7b71dd74 smart_money INCREASE_POSITION $233,080 score=0.71 grade=NEW win72=- avg72=-

### 2. HYPE OPEN_SHORT / Swing 89.48 / AI评分 None / 综合 89.48 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 1, 'money_printer': 2}，事件：{'FLIP_POSITION': 1, 'INCREASE_POSITION': 2}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$644,853，最大单钱包：$292,883
- 标记价：68.237，均价：67.18553333，权重分：21.3388，净偏向分：5.3347
- AI独立评分：None，规则评分：89.48，综合开仓评分：89.48，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第12轮 / 持续21.5小时 / 冷却剩余7.0小时 / 金额变化1.07x
- 钱包质量：65/100 高质=1 样本=2，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$905,998，冲突比=1.405
- 市场：funding=1.25e-05，OI=21951234.419999998，oracle=68.221，15m=-1.2081% ，1h=-1.915% ，volRatio=0.2217
- 中长期评分：89.48 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$644,853，6h=$644,853，24h=$7,507,951
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 6.48, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00 money_printer INCREASE_POSITION $292,883 score=1.82 grade=S win72=- avg72=-
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money FLIP_POSITION $192,423 score=1.10 grade=B win72=- avg72=-
  - 0x645b2eeaa0a46df3c4211bebda1b2c7703e287b8 money_printer INCREASE_POSITION $159,548 score=1.00 grade=NEW win72=- avg72=-

### 3. ETH OPEN_LONG / Swing 87.0 / AI评分 None / 综合 87.0 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$16,120,579，最大单钱包：$16,120,579
- 标记价：1758.05，均价：1754.3，权重分：9.73，净偏向分：2.4325
- AI独立评分：None，规则评分：87.0，综合开仓评分：87.0，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第8轮 / 持续18.0小时 / 冷却剩余7.0小时 / 金额变化12.72x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$17,463,561，冲突比=1.0833
- 市场：funding=1.25e-05，OI=799410.6640000001，oracle=1757.3，15m=-0.9754% ，1h=-1.3647% ，volRatio=0.8139
- 中长期评分：87.0 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$16,120,579，6h=$18,600,492，24h=$23,563,800
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.0, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x049bdc370620beab340b01072fa580fd57745e7d money_printer INCREASE_POSITION $16,120,579 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=10 amount=$7,372,063 score=64.2275 groups={'smart_money': 6, 'money_printer': 4}
- **ETH EXIT_LONG** wallets=3 amount=$671,818 score=18.2521 groups={'smart_money': 2, 'money_printer': 1}
- **BTC EXIT_SHORT** wallets=2 amount=$325,674 score=13.4172 groups={'money_printer': 2}
- **SOL EXIT_LONG** wallets=1 amount=$202,110 score=7.393 groups={'money_printer': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$101,582 score=6.507 groups={'money_printer': 1}
- **XRP EXIT_SHORT** wallets=1 amount=$151,088 score=5.9986 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第27轮 amount=$17,463,561 prev=57 exit_ratio=- amount_ratio=25.31x age=390.1m cooldown_left=2.5小时
- **COOLDOWN_MERGED** BTC SHORT 第32轮 amount=$6,784,030 prev=58 exit_ratio=- amount_ratio=0.91x age=360.1m cooldown_left=5.0小时
- **COOLDOWN_MERGED** HYPE LONG 第14轮 amount=$905,998 prev=66 exit_ratio=- amount_ratio=1.96x age=120.1m cooldown_left=5.5小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：71 条，方向正确 39，方向错误 32，平均方向收益 0.31%，最好 7.54%，最差 -7.13%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.43335 | 7.54 | 7.41 | 8.64 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.43335 | 7.40 | 7.27 | 8.51 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.721065 | -7.13 | -7.26 | 0.55 | -7.60 |
| 31 | NEAR | LONG | 2.05555 | 1.93325 | -5.95 | -6.08 | 1.11 | -7.50 |
| 13 | GRAM | SHORT | 1.6858 | 1.5953 | 5.37 | 5.24 | 6.60 | -0.52 |
| 45 | MON | LONG | 0.025817 | 0.024474 | -5.20 | -5.33 | 0.89 | -7.78 |
| 41 | HYPE | SHORT | 71.902 | 68.237 | 5.10 | 4.97 | 5.90 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 68.237 | -4.71 | -4.84 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 68.237 | 4.55 | 4.42 | 5.35 | -1.76 |
| 8 | NEAR | SHORT | 2.0234 | 1.93325 | 4.46 | 4.33 | 6.03 | -2.72 |
| 47 | SOL | SHORT | 82.5535 | 78.8795 | 4.45 | 4.32 | 4.72 | -0.08 |
| 21 | ZEC | LONG | 463.135 | 481.765 | 4.02 | 3.89 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 481.765 | -4.02 | -4.15 | 1.19 | -10.16 |
| 4 | HYPE | SHORT | 71.0475 | 68.237 | 3.96 | 3.83 | 4.76 | -2.39 |
| 40 | SOL | LONG | 82.0335 | 78.8795 | -3.84 | -3.97 | 0.71 | -4.12 |
| 44 | VVV | SHORT | 11.1805 | 10.7815 | 3.57 | 3.44 | 5.94 | 0.00 |
| 5 | SOL | SHORT | 81.6175 | 78.8795 | 3.35 | 3.22 | 3.63 | -1.23 |
| 7 | XRP | SHORT | 1.13285 | 1.09585 | 3.27 | 3.14 | 3.39 | 0.00 |
| 11 | SOL | LONG | 81.4165 | 78.8795 | -3.12 | -3.25 | 1.48 | -3.39 |
| 14 | kPEPE | LONG | 0.002705 | 0.002621 | -3.11 | -3.24 | 1.44 | -3.88 |
| 56 | LIT | SHORT | 2.50975 | 2.43335 | 3.04 | 2.91 | 4.20 | 0.00 |
| 39 | XRP | SHORT | 1.12915 | 1.09585 | 2.95 | 2.82 | 3.07 | -0.20 |
| 37 | ZEC | LONG | 495.815 | 481.765 | -2.83 | -2.96 | 2.90 | -3.76 |
| 49 | HYPE | LONG | 70.1565 | 68.237 | -2.74 | -2.87 | 0.23 | -3.55 |
| 24 | SOL | SHORT | 81.0475 | 78.8795 | 2.67 | 2.54 | 2.95 | -1.94 |
| 33 | ZEC | SHORT | 469.59 | 481.765 | -2.59 | -2.72 | 0.00 | -8.65 |
| 48 | BNB | SHORT | 584.295 | 569.245 | 2.58 | 2.45 | 2.72 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1758.05 | 2.52 | 2.39 | 2.89 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1758.05 | -2.44 | -2.57 | 0.48 | -2.81 |
| 68 | LDO | LONG | 0.32029 | 0.32787 | 2.37 | 2.24 | 2.37 | 0.00 |

</details>
