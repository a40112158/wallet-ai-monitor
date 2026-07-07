# 钱包合约信号报告

Time: **2026-07-07 17:00:30 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1242，本轮 warmup 钱包：1179，变动事件：1527
- AI 输入信号：2，虚拟开仓：0，动态评分钱包：108
- 钱包胜率层：enabled=True，新记录=174，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 7，生命周期事件 8，冷却合并 5
- 信号状态：NEW=1，RE_ALERT=1，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=18，signals=42，avg_duration=180.3s，AI calls=33，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.83 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.83 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.82 | 1 | - | - | - | - |
| 0x00897e...7f2410 | smart_money | NEW | 1.76 | 1 | - | - | - | - |
| 0x00f8da...e7454b | money_printer | NEW | 1.76 | 1 | - | - | - | - |
| 0xd487e2...934982 | money_printer | NEW | 1.76 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0x50a4d3...0f8168 | smart_money | NEW | 1.66 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.65 | 2 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **ETH LONG** [RE_ALERT / 第3轮 / 持续6.5小时 / 冷却剩余7.0小时 / 金额变化0.24x] swing=83.17 AI=- conf=- AI分=None 综合=83.17 delta=$900,975 wallets=1 q=50/100 高质=0 样本=0 horizon=3-14

### 过滤/短线噪音

- MON LONG [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=57.33：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. MON OPEN_LONG / Swing 57.33 / AI评分 None / 综合 57.33 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'NEW_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$256,060，最大单钱包：$256,060
- 标记价：0.025817，均价：0.025669，权重分：5.4083，净偏向分：5.4083
- AI独立评分：None，规则评分：57.33，综合开仓评分：57.33，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=2.91136e-05，OI=1436188958.0，oracle=0.025775，15m=4.0098% ，1h=4.0098% ，volRatio=4.1042
- 中长期评分：57.33 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$256,060，6h=$256,060，24h=$256,060
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 5.0, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 9.5, 'oi_funding_health': 9.0, 'low_direction_conflict': 10.0}
- 风险标签：long_chasing_pump, price_extended_wait_pullback, volume_expansion
- Top wallets：
  - 0x39b07015ca813075bbce6f475767d5b4b9d518b0 smart_money NEW_POSITION $256,060 score=1.00 grade=NEW win72=- avg72=-

### 2. ETH OPEN_LONG / Swing 83.17 / AI评分 None / 综合 83.17 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$900,975，最大单钱包：$900,975
- 标记价：1801.95，均价：1801.31，权重分：8.0389，净偏向分：2.0097
- AI独立评分：None，规则评分：83.17，综合开仓评分：83.17，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第3轮 / 持续6.5小时 / 冷却剩余7.0小时 / 金额变化0.24x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$1,423,579，冲突比=1.58
- 市场：funding=1.25e-05，OI=804227.4125999997，oracle=1801.3，15m=1.8483% ，1h=1.8483% ，volRatio=0.4962
- 中长期评分：83.17 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$4,659,526，6h=$4,659,526，24h=$4,963,307
- 评分拆解：{'wallet_resonance': 19.17, 'wallet_quality': 5.0, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, high_long_short_conflict, long_upper_wick_risk, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xbcd420d13362532756c968f663f96ba95e240dd2 money_printer INCREASE_POSITION $900,975 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=6 amount=$5,553,515 score=38.7801 groups={'smart_money': 2, 'money_printer': 4}
- **ZEC EXIT_SHORT** wallets=2 amount=$512,598 score=13.0944 groups={'smart_money': 1, 'money_printer': 1}
- **HYPE EXIT_SHORT** wallets=2 amount=$1,008,913 score=11.8776 groups={'smart_money': 1, 'money_printer': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$433,151 score=11.8507 groups={'smart_money': 1, 'money_printer': 1}
- **BTC EXIT_LONG** wallets=2 amount=$423,912 score=10.7583 groups={'smart_money': 2}
- **LIT EXIT_SHORT** wallets=1 amount=$123,771 score=6.2139 groups={'money_printer': 1}
- **ETH EXIT_LONG** wallets=1 amount=$117,955 score=5.0717 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第11轮 amount=$3,459,258 prev=12 exit_ratio=- amount_ratio=0.64x age=419.7m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH SHORT 第7轮 amount=$1,423,579 prev=23 exit_ratio=- amount_ratio=0.29x age=210.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** SOL SHORT 第6轮 amount=$406,219 prev=24 exit_ratio=- amount_ratio=0.50x age=210.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** ZEC SHORT 第5轮 amount=$709,269 prev=19 exit_ratio=- amount_ratio=1.18x age=270.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第8轮 amount=$531,155 prev=20 exit_ratio=- amount_ratio=0.06x age=270.1m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第-轮 amount=$1,008,913 prev=28 exit_ratio=1.3167 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第5轮 amount=$512,598 prev=19 exit_ratio=0.7776 amount_ratio=1.18x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第11轮 amount=$5,553,515 prev=12 exit_ratio=0.8856 amount_ratio=0.64x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：46 条，方向正确 23，方向错误 23，平均方向收益 -0.17%，最好 9.31%，最差 -9.31%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 506.23 | 9.31 | 9.18 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 506.23 | -9.31 | -9.44 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 506.23 | -7.80 | -7.93 | 0.00 | -8.65 |
| 18 | LIT | SHORT | 2.63175 | 2.5582 | 2.79 | 2.66 | 3.01 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.5582 | 2.65 | 2.52 | 4.57 | -2.20 |
| 37 | ZEC | LONG | 495.815 | 506.23 | 2.10 | 1.97 | 2.90 | 0.00 |
| 27 | ETH | SHORT | 1767.25 | 1801.95 | -1.96 | -2.09 | 0.00 | -2.05 |
| 34 | JTO | LONG | 0.77639 | 0.76311 | -1.71 | -1.84 | 0.55 | -1.71 |
| 8 | NEAR | SHORT | 2.0234 | 2.05725 | -1.67 | -1.80 | 1.24 | -2.23 |
| 26 | BTC | SHORT | 62945.5 | 63989.5 | -1.66 | -1.79 | 0.00 | -1.72 |
| 23 | ETH | SHORT | 1773.75 | 1801.95 | -1.59 | -1.72 | 0.37 | -1.68 |
| 13 | GRAM | SHORT | 1.6858 | 1.66 | 1.53 | 1.40 | 1.76 | -0.52 |
| 24 | SOL | SHORT | 81.0475 | 82.1975 | -1.42 | -1.55 | 0.49 | -1.52 |
| 1 | BTC | SHORT | 63136.5 | 63989.5 | -1.35 | -1.48 | 0.30 | -1.41 |
| 25 | BTC | LONG | 63172.5 | 63989.5 | 1.29 | 1.16 | 1.36 | -0.36 |
| 17 | ETH | LONG | 1780.75 | 1801.95 | 1.19 | 1.06 | 1.28 | -0.76 |
| 10 | BTC | SHORT | 63245.5 | 63989.5 | -1.18 | -1.31 | 0.47 | -1.24 |
| 3 | ETH | SHORT | 1781.15 | 1801.95 | -1.17 | -1.30 | 0.78 | -1.26 |
| 12 | BTC | SHORT | 63271.5 | 63989.5 | -1.13 | -1.26 | 0.52 | -1.20 |
| 9 | TAO | LONG | 213.63 | 216.025 | 1.12 | 0.99 | 1.58 | -0.60 |
| 15 | BTC | SHORT | 63341.5 | 63989.5 | -1.02 | -1.15 | 0.63 | -1.08 |
| 11 | SOL | LONG | 81.4165 | 82.1975 | 0.96 | 0.83 | 1.06 | -0.94 |
| 2 | BTC | SHORT | 63427.5 | 63989.5 | -0.89 | -1.02 | 0.76 | -0.95 |
| 44 | VVV | SHORT | 11.1805 | 11.082 | 0.88 | 0.75 | 0.88 | 0.00 |
| 22 | BTC | LONG | 63460.5 | 63989.5 | 0.83 | 0.70 | 0.90 | -0.81 |
| 14 | kPEPE | LONG | 0.002705 | 0.002727 | 0.81 | 0.68 | 0.85 | -1.37 |
| 4 | HYPE | SHORT | 71.0475 | 71.6055 | -0.79 | -0.92 | 0.00 | -2.39 |
| 5 | SOL | SHORT | 81.6175 | 82.1975 | -0.71 | -0.84 | 1.18 | -0.81 |
| 30 | BTC | LONG | 63562.5 | 63989.5 | 0.67 | 0.54 | 0.73 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 63989.5 | -0.67 | -0.80 | 0.00 | -0.73 |

</details>
