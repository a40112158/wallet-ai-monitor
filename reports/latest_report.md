# 钱包合约信号报告

Time: **2026-07-08 09:31:03 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1220，本轮 warmup 钱包：1201，变动事件：1632
- AI 输入信号：2，虚拟开仓：0，动态评分钱包：149
- 钱包胜率层：enabled=True，新记录=174，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 7，生命周期事件 6，冷却合并 5
- 信号状态：NEW=1，RE_ALERT=0，REPEAT=1，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=48，signals=68，avg_duration=211.5s，AI calls=52，AI estimated points=47309

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
| 0xf17de4...2adab2 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.19 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 2.08 | 1 | - | - | - | - |
| 0x4ef1c5...a528e3 | smart_money | NEW | 2.08 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **ZEC LONG** [ACTIVE_REPEAT / 第12轮 / 持续21.0小时 / 冷却剩余7.0小时 / 金额变化2.51x] swing=91.83 AI=- conf=- AI分=None 综合=91.83 delta=$902,880 wallets=1 q=53/100 高质=0 样本=1 horizon=3-14

### 过滤/短线噪音

- PAXG LONG [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=60.33：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. ZEC OPEN_LONG / Swing 91.83 / AI评分 None / 综合 91.83 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$902,880，最大单钱包：$902,880
- 标记价：463.81，均价：468.7815，权重分：6.1221，净偏向分：6.1221
- AI独立评分：None，规则评分：91.83，综合开仓评分：91.83，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第12轮 / 持续21.0小时 / 冷却剩余7.0小时 / 金额变化2.51x
- 钱包质量：53/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=457400.8199999999，oracle=464.11，15m=-2.9301% ，1h=-3.643% ，volRatio=1.9612
- 中长期评分：91.83 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$902,880，6h=$902,880，24h=$5,555,165
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.25, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 4.58}
- 风险标签：money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $902,880 score=1.11 grade=B win72=- avg72=-

### 2. PAXG OPEN_LONG / Swing 60.33 / AI评分 None / 综合 60.33 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$606,755，最大单钱包：$606,755
- 标记价：4048.65，均价：4062.888，权重分：5.0359，净偏向分：5.0359
- AI独立评分：None，规则评分：60.33，综合开仓评分：60.33，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：35/100 高质=0 样本=1，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 市场：funding=-1.48416e-05，OI=4887.67，oracle=4051.4，15m=-1.746% ，1h=-1.7126% ，volRatio=8.5601
- 中长期评分：60.33 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$606,755，6h=$606,755，24h=$606,755
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 3.5, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 10.0}
- 风险标签：volume_expansion
- Top wallets：
  - 0x9a31f7aff78fd464bbceb398e11b82ba633c6525 smart_money INCREASE_POSITION $606,755 score=0.48 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **ETH EXIT_SHORT** wallets=7 amount=$4,959,181 score=60.6309 groups={'smart_money': 1, 'money_printer': 6}
- **BTC EXIT_SHORT** wallets=6 amount=$4,757,518 score=46.5806 groups={'money_printer': 5, 'smart_money': 1}
- **ZEC EXIT_SHORT** wallets=2 amount=$271,681 score=15.0026 groups={'money_printer': 2}
- **SOL EXIT_SHORT** wallets=2 amount=$341,093 score=12.6625 groups={'smart_money': 1, 'money_printer': 1}
- **BTC EXIT_LONG** wallets=2 amount=$533,272 score=10.0304 groups={'smart_money': 2}
- **HYPE EXIT_LONG** wallets=1 amount=$728,466 score=8.9231 groups={'money_printer': 1}
- **LIT EXIT_SHORT** wallets=1 amount=$114,427 score=7.8896 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第42轮 amount=$7,914,351 prev=74 exit_ratio=- amount_ratio=0.75x age=120.2m cooldown_left=6.0小时
- **COOLDOWN_MERGED** ETH SHORT 第36轮 amount=$1,187,641 prev=72 exit_ratio=- amount_ratio=0.21x age=270.4m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL SHORT 第20轮 amount=$280,903 prev=73 exit_ratio=- amount_ratio=0.10x age=210.4m cooldown_left=4.0小时
- **COOLDOWN_MERGED** BTC LONG 第34轮 amount=$2,127,596 prev=69 exit_ratio=- amount_ratio=0.22x age=300.4m cooldown_left=4.0小时
- **COOLDOWN_MERGED** HYPE SHORT 第22轮 amount=$1,012,014 prev=70 exit_ratio=- amount_ratio=0.93x age=300.4m cooldown_left=6.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第36轮 amount=$4,959,181 prev=72 exit_ratio=1.582 amount_ratio=0.21x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：81 条，方向正确 43，方向错误 38，平均方向收益 0.12%，最好 11.56%，最差 -19.94%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.62161 | -19.94 | -20.07 | 0.55 | -21.12 |
| 18 | LIT | SHORT | 2.63175 | 2.32745 | 11.56 | 11.43 | 11.56 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.32745 | 11.43 | 11.30 | 11.43 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.86745 | -9.15 | -9.28 | 1.11 | -9.15 |
| 45 | MON | LONG | 0.025817 | 0.023698 | -8.21 | -8.34 | 0.89 | -8.42 |
| 8 | NEAR | SHORT | 2.0234 | 1.86745 | 7.71 | 7.58 | 7.71 | -2.72 |
| 13 | GRAM | SHORT | 1.6858 | 1.55975 | 7.48 | 7.35 | 7.48 | -0.52 |
| 56 | LIT | SHORT | 2.50975 | 2.32745 | 7.26 | 7.13 | 7.26 | 0.00 |
| 37 | ZEC | LONG | 495.815 | 463.81 | -6.46 | -6.59 | 2.90 | -6.46 |
| 47 | SOL | SHORT | 82.5535 | 77.2565 | 6.42 | 6.29 | 6.49 | -0.08 |
| 44 | VVV | SHORT | 11.1805 | 10.4855 | 6.22 | 6.09 | 6.88 | 0.00 |
| 51 | ZEC | LONG | 493.435 | 463.81 | -6.00 | -6.13 | 0.83 | -6.00 |
| 40 | SOL | LONG | 82.0335 | 77.2565 | -5.82 | -5.95 | 0.71 | -5.89 |
| 5 | SOL | SHORT | 81.6175 | 77.2565 | 5.34 | 5.21 | 5.41 | -1.23 |
| 14 | kPEPE | LONG | 0.002705 | 0.002564 | -5.21 | -5.34 | 1.44 | -5.21 |
| 41 | HYPE | SHORT | 71.902 | 68.188 | 5.17 | 5.04 | 5.90 | -0.38 |
| 11 | SOL | LONG | 81.4165 | 77.2565 | -5.11 | -5.24 | 1.48 | -5.18 |
| 68 | LDO | LONG | 0.32029 | 0.30448 | -4.94 | -5.07 | 2.37 | -4.94 |
| 16 | HYPE | LONG | 71.6085 | 68.188 | -4.78 | -4.91 | 1.59 | -5.51 |
| 7 | XRP | SHORT | 1.13285 | 1.07875 | 4.78 | 4.65 | 4.78 | 0.00 |
| 24 | SOL | SHORT | 81.0475 | 77.2565 | 4.68 | 4.55 | 4.75 | -1.94 |
| 28 | HYPE | SHORT | 71.49 | 68.188 | 4.62 | 4.49 | 5.35 | -1.76 |
| 39 | XRP | SHORT | 1.12915 | 1.07875 | 4.46 | 4.33 | 4.46 | -0.20 |
| 9 | TAO | LONG | 213.63 | 204.535 | -4.26 | -4.39 | 1.58 | -4.26 |
| 59 | SOL | LONG | 80.5705 | 77.2565 | -4.11 | -4.24 | 0.03 | -4.18 |
| 4 | HYPE | SHORT | 71.0475 | 68.188 | 4.02 | 3.89 | 4.76 | -2.39 |
| 48 | BNB | SHORT | 584.295 | 561.98 | 3.82 | 3.69 | 3.94 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1736.65 | 3.71 | 3.58 | 3.96 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1736.65 | -3.62 | -3.75 | 0.48 | -3.88 |
| 38 | ETH | LONG | 1797.05 | 1736.65 | -3.36 | -3.49 | 0.75 | -3.62 |

</details>
