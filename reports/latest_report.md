# 钱包合约信号报告

Time: **2026-07-08 00:30:27 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1225，本轮 warmup 钱包：1196，变动事件：1588
- AI 输入信号：2，虚拟开仓：0，动态评分钱包：131
- 钱包胜率层：enabled=True，新记录=147，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 7，生命周期事件 7，冷却合并 5
- 信号状态：NEW=1，RE_ALERT=1，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=33，signals=57，avg_duration=196.6s，AI calls=43，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.09 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.08 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 2.02 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.95 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.81 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.79 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.75 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.75 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 1.74 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **BTC SHORT** [RE_ALERT / 第26轮 / 持续18.1小时 / 冷却剩余7.0小时 / 金额变化8.82x] swing=90.82 AI=- conf=- AI分=None 综合=90.82 delta=$8,811,063 wallets=18 q=47/100 高质=3 样本=16 horizon=3-14

### 过滤/短线噪音

- BNB LONG [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=52.33：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. BTC OPEN_SHORT / Swing 90.82 / AI评分 None / 综合 90.82 / AI置信度 -

- 钱包数：18，分组：{'smart_money': 8, 'money_printer': 10}，事件：{'FLIP_POSITION': 7, 'INCREASE_POSITION': 11}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$8,811,063，最大单钱包：$2,054,842
- 标记价：63613.5，均价：63328.98333333，权重分：119.4907，净偏向分：107.4026
- AI独立评分：None，规则评分：90.82，综合开仓评分：90.82，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第26轮 / 持续18.1小时 / 冷却剩余7.0小时 / 金额变化8.82x
- 钱包质量：47/100 高质=3 样本=16，高质量钱包=3，低质量钱包=5，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$1,188,477，冲突比=0.1349
- 市场：funding=1.25e-05，OI=37860.4033，oracle=63615.0，15m=0.1102% ，1h=-0.19% ，volRatio=0.5794
- 中长期评分：90.82 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$13,159,645，6h=$13,159,645，24h=$76,263,344
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.67, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 3.15}
- 风险标签：cooldown_realert_large_add, direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x09bc1cf4d9f0b59e1425a8fde4d4b1f7d3c9410d money_printer INCREASE_POSITION $2,054,842 score=1.26 grade=NEW win72=- avg72=-
  - 0x0fd468a73084daa6ea77a9261e40fdec3e67e0c7 money_printer INCREASE_POSITION $1,320,964 score=1.07 grade=NEW win72=- avg72=-
  - 0x7ca165f354e3260e2f8d5a7508cc9dd2fa009235 money_printer INCREASE_POSITION $1,125,540 score=0.93 grade=NEW win72=- avg72=-

### 2. BNB OPEN_LONG / Swing 52.33 / AI评分 None / 综合 52.33 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'FLIP_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$352,144，最大单钱包：$352,144
- 标记价：577.5，均价：576.122，权重分：5.7771，净偏向分：5.7771
- AI独立评分：None，规则评分：52.33，综合开仓评分：52.33，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：54/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=-8.6067e-06，OI=44352.808，oracle=577.85，15m=-0.3315% ，1h=-0.5907% ，volRatio=14.7071
- 中长期评分：52.33 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$352,144，6h=$352,144，24h=$352,144
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 5.38, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 0.11}
- 风险标签：direction_conflict, long_upper_wick_risk, volume_expansion
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money FLIP_POSITION $352,144 score=1.17 grade=B win72=- avg72=-

## 减仓/平仓风险信号

- **SOL EXIT_SHORT** wallets=4 amount=$1,673,330 score=28.3671 groups={'smart_money': 2, 'money_printer': 2}
- **BTC EXIT_SHORT** wallets=3 amount=$3,708,031 score=21.866 groups={'money_printer': 3}
- **HYPE EXIT_LONG** wallets=3 amount=$578,999 score=21.4533 groups={'money_printer': 3}
- **XRP EXIT_SHORT** wallets=3 amount=$459,791 score=18.7331 groups={'smart_money': 2, 'money_printer': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$3,825,841 score=18.6844 groups={'money_printer': 2}
- **BTC EXIT_LONG** wallets=2 amount=$299,161 score=12.6409 groups={'money_printer': 1, 'smart_money': 1}
- **HYPE EXIT_SHORT** wallets=1 amount=$708,101 score=8.8105 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ZEC LONG 第9轮 amount=$253,157 prev=51 exit_ratio=- amount_ratio=0.25x age=330.0m cooldown_left=1.5小时
- **COOLDOWN_MERGED** ETH SHORT 第21轮 amount=$6,420,936 prev=50 exit_ratio=- amount_ratio=0.44x age=330.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** SOL SHORT 第15轮 amount=$2,906,832 prev=47 exit_ratio=- amount_ratio=2.59x age=419.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第19轮 amount=$1,188,477 prev=55 exit_ratio=- amount_ratio=0.30x age=179.8m cooldown_left=5.5小时
- **COOLDOWN_MERGED** SOL LONG 第9轮 amount=$335,852 prev=59 exit_ratio=- amount_ratio=0.31x age=29.9m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第26轮 amount=$3,708,031 prev=58 exit_ratio=0.8527 amount_ratio=8.82x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第15轮 amount=$1,673,330 prev=47 exit_ratio=0.7226 amount_ratio=2.59x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：61 条，方向正确 27，方向错误 34，平均方向收益 0.03%，最好 5.45%，最差 -5.23%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.48845 | 5.45 | 5.32 | 6.45 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.48845 | 5.31 | 5.18 | 6.31 | -2.20 |
| 45 | MON | LONG | 0.025817 | 0.024468 | -5.23 | -5.36 | 0.89 | -7.78 |
| 34 | JTO | LONG | 0.77639 | 0.73641 | -5.15 | -5.28 | 0.55 | -6.78 |
| 21 | ZEC | LONG | 463.135 | 484.715 | 4.66 | 4.53 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 484.715 | -4.66 | -4.79 | 1.19 | -10.16 |
| 13 | GRAM | SHORT | 1.6858 | 1.61905 | 3.96 | 3.83 | 3.96 | -0.52 |
| 31 | NEAR | LONG | 2.05555 | 1.9849 | -3.44 | -3.57 | 1.11 | -3.78 |
| 33 | ZEC | SHORT | 469.59 | 484.715 | -3.22 | -3.35 | 0.00 | -8.65 |
| 41 | HYPE | SHORT | 71.902 | 69.6455 | 3.14 | 3.01 | 3.94 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 69.6455 | -2.74 | -2.87 | 1.59 | -3.54 |
| 28 | HYPE | SHORT | 71.49 | 69.6455 | 2.58 | 2.45 | 3.38 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 80.5985 | 2.37 | 2.24 | 2.40 | -0.08 |
| 44 | VVV | SHORT | 11.1805 | 10.9295 | 2.24 | 2.11 | 5.94 | 0.00 |
| 37 | ZEC | LONG | 495.815 | 484.715 | -2.24 | -2.37 | 2.90 | -3.70 |
| 4 | HYPE | SHORT | 71.0475 | 69.6455 | 1.97 | 1.84 | 2.78 | -2.39 |
| 8 | NEAR | SHORT | 2.0234 | 1.9849 | 1.90 | 1.77 | 2.25 | -2.72 |
| 51 | ZEC | LONG | 493.435 | 484.715 | -1.77 | -1.90 | 0.83 | -3.24 |
| 40 | SOL | LONG | 82.0335 | 80.5985 | -1.75 | -1.88 | 0.71 | -1.78 |
| 7 | XRP | SHORT | 1.13285 | 1.11335 | 1.72 | 1.59 | 1.94 | 0.00 |
| 39 | XRP | SHORT | 1.12915 | 1.11335 | 1.40 | 1.27 | 1.62 | -0.20 |
| 42 | ETH | SHORT | 1803.55 | 1780.35 | 1.29 | 1.16 | 1.76 | -0.39 |
| 5 | SOL | SHORT | 81.6175 | 80.5985 | 1.25 | 1.12 | 1.28 | -1.23 |
| 46 | ETH | LONG | 1801.95 | 1780.35 | -1.20 | -1.33 | 0.48 | -1.68 |
| 48 | BNB | SHORT | 584.295 | 577.5 | 1.16 | 1.03 | 1.31 | 0.00 |
| 14 | kPEPE | LONG | 0.002705 | 0.002675 | -1.11 | -1.24 | 1.44 | -1.52 |
| 26 | BTC | SHORT | 62945.5 | 63613.5 | -1.06 | -1.19 | 0.00 | -1.93 |
| 11 | SOL | LONG | 81.4165 | 80.5985 | -1.00 | -1.13 | 1.48 | -1.04 |
| 38 | ETH | LONG | 1797.05 | 1780.35 | -0.93 | -1.06 | 0.75 | -1.41 |
| 36 | ETH | SHORT | 1797.05 | 1780.35 | 0.93 | 0.80 | 1.41 | -0.75 |

</details>
