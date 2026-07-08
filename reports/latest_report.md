# 钱包合约信号报告

Time: **2026-07-08 07:30:49 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1214，本轮 warmup 钱包：1207，变动事件：1559
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：143
- 钱包胜率层：enabled=True，新记录=228，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 4，生命周期事件 3，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=1，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=44，signals=62，avg_duration=211.2s，AI calls=49，AI estimated points=47505

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.19 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.11 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.11 | 1 | - | - | - | - |
| 0xf17de4...2adab2 | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.09 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.02 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 1.98 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **BTC SHORT** [ACTIVE_REPEAT / 第38轮 / 持续25.1小时 / 冷却剩余7.0小时 / 金额变化10.80x] swing=89.82 AI=- conf=- AI分=None 综合=89.82 delta=$12,516,660 wallets=28 q=55/100 高质=11 样本=22 horizon=3-14

## 本轮开仓/加仓信号

### 1. BTC OPEN_SHORT / Swing 89.82 / AI评分 None / 综合 89.82 / AI置信度 -

- 钱包数：28，分组：{'smart_money': 12, 'money_printer': 16}，事件：{'FLIP_POSITION': 8, 'INCREASE_POSITION': 20}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$12,516,660，最大单钱包：$2,031,927
- 标记价：62824.5，均价：62600.25，权重分：194.224，净偏向分：183.1016
- AI独立评分：None，规则评分：89.82，综合开仓评分：89.82，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第38轮 / 持续25.1小时 / 冷却剩余7.0小时 / 金额变化10.80x
- 钱包质量：55/100 高质=11 样本=22，高质量钱包=11，低质量钱包=7，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$955,703，冲突比=0.0764
- 市场：funding=1.25e-05，OI=38059.23376，oracle=62833.0，15m=-0.0032% ，1h=0.1976% ，volRatio=1.2212
- 中长期评分：89.82 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$12,516,660，6h=$12,516,660，24h=$72,420,976
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.54, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 1.29}
- 风险标签：direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x95995f302ad58138d791ce49f9f3b1274e80c60a money_printer INCREASE_POSITION $2,031,927 score=1.00 grade=NEW win72=- avg72=-
  - 0xadc9cf23f55c6221a05a8150e5768d7c3289562f money_printer INCREASE_POSITION $1,515,502 score=1.69 grade=NEW win72=- avg72=-
  - 0x621c5551678189b9a6c94d929924c225ff1d63ab money_printer INCREASE_POSITION $1,015,961 score=1.75 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=5 amount=$2,462,775 score=37.7003 groups={'smart_money': 1, 'money_printer': 4}
- **BTC EXIT_SHORT** wallets=3 amount=$625,522 score=20.1709 groups={'smart_money': 1, 'money_printer': 2}
- **ETH EXIT_LONG** wallets=2 amount=$1,229,838 score=12.5925 groups={'smart_money': 1, 'money_printer': 1}
- **SOL EXIT_SHORT** wallets=1 amount=$609,991 score=9.24 groups={'money_printer': 1}
- **ETH EXIT_SHORT** wallets=1 amount=$353,735 score=8.6947 groups={'money_printer': 1}
- **SOL EXIT_LONG** wallets=1 amount=$559,353 score=5.9259 groups={'smart_money': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$170,346 score=5.2313 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第32轮 amount=$3,931,560 prev=72 exit_ratio=- amount_ratio=6.92x age=150.2m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第18轮 amount=$457,333 prev=70 exit_ratio=- amount_ratio=0.77x age=180.2m cooldown_left=4.0小时
- **COOLDOWN_MERGED** BTC LONG 第31轮 amount=$955,703 prev=69 exit_ratio=- amount_ratio=1.94x age=180.2m cooldown_left=6.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：74 条，方向正确 41，方向错误 33，平均方向收益 0.32%，最好 9.79%，最差 -13.14%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.674355 | -13.14 | -13.27 | 0.55 | -13.14 |
| 18 | LIT | SHORT | 2.63175 | 2.37405 | 9.79 | 9.66 | 9.79 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.37405 | 9.66 | 9.53 | 9.66 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.90995 | -7.08 | -7.21 | 1.11 | -7.50 |
| 13 | GRAM | SHORT | 1.6858 | 1.57795 | 6.40 | 6.27 | 6.60 | -0.52 |
| 45 | MON | LONG | 0.025817 | 0.024344 | -5.71 | -5.84 | 0.89 | -7.78 |
| 8 | NEAR | SHORT | 2.0234 | 1.90995 | 5.61 | 5.48 | 6.03 | -2.72 |
| 56 | LIT | SHORT | 2.50975 | 2.37405 | 5.41 | 5.28 | 5.41 | 0.00 |
| 47 | SOL | SHORT | 82.5535 | 78.1265 | 5.36 | 5.23 | 5.37 | -0.08 |
| 41 | HYPE | SHORT | 71.902 | 68.1385 | 5.23 | 5.10 | 5.90 | -0.38 |
| 44 | VVV | SHORT | 11.1805 | 10.602 | 5.17 | 5.04 | 5.94 | 0.00 |
| 16 | HYPE | LONG | 71.6085 | 68.1385 | -4.85 | -4.98 | 1.59 | -5.51 |
| 40 | SOL | LONG | 82.0335 | 78.1265 | -4.76 | -4.89 | 0.71 | -4.77 |
| 28 | HYPE | SHORT | 71.49 | 68.1385 | 4.69 | 4.56 | 5.35 | -1.76 |
| 5 | SOL | SHORT | 81.6175 | 78.1265 | 4.28 | 4.15 | 4.28 | -1.23 |
| 4 | HYPE | SHORT | 71.0475 | 68.1385 | 4.09 | 3.96 | 4.76 | -2.39 |
| 11 | SOL | LONG | 81.4165 | 78.1265 | -4.04 | -4.17 | 1.48 | -4.05 |
| 37 | ZEC | LONG | 495.815 | 477.295 | -3.74 | -3.87 | 2.90 | -3.94 |
| 24 | SOL | SHORT | 81.0475 | 78.1265 | 3.60 | 3.47 | 3.61 | -1.94 |
| 7 | XRP | SHORT | 1.13285 | 1.09385 | 3.44 | 3.31 | 3.96 | 0.00 |
| 51 | ZEC | LONG | 493.435 | 477.295 | -3.27 | -3.40 | 0.83 | -3.48 |
| 39 | XRP | SHORT | 1.12915 | 1.09385 | 3.13 | 3.00 | 3.65 | -0.20 |
| 21 | ZEC | LONG | 463.135 | 477.295 | 3.06 | 2.93 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 477.295 | -3.06 | -3.19 | 1.19 | -10.16 |
| 59 | SOL | LONG | 80.5705 | 78.1265 | -3.03 | -3.16 | 0.03 | -3.04 |
| 14 | kPEPE | LONG | 0.002705 | 0.002623 | -3.03 | -3.16 | 1.44 | -4.07 |
| 48 | BNB | SHORT | 584.295 | 567.175 | 2.93 | 2.80 | 3.14 | 0.00 |
| 49 | HYPE | LONG | 70.1565 | 68.1385 | -2.88 | -3.01 | 0.23 | -3.55 |
| 42 | ETH | SHORT | 1803.55 | 1754.15 | 2.74 | 2.61 | 2.99 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1754.15 | -2.65 | -2.78 | 0.48 | -2.90 |

</details>
