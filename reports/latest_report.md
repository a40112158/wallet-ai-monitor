# 钱包合约信号报告

Time: **2026-07-08 00:00:32 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1225，本轮 warmup 钱包：1196，变动事件：1408
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：131
- 钱包胜率层：enabled=True，新记录=183，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 10，冷却合并 6
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=1，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=32，signals=56，avg_duration=195.6s，AI calls=42，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.19 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.19 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.18 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 2.00 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.93 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.88 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.82 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.82 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.79 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 1.78 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **SOL LONG** [ACTIVE_REPEAT / 第8轮 / 持续14.8小时 / 冷却剩余7.0小时 / 金额变化1.50x] swing=88.0 AI=- conf=- AI分=None 综合=88.0 delta=$1,078,314 wallets=4 q=50/100 高质=1 样本=4 horizon=3-14

## 本轮开仓/加仓信号

### 1. SOL OPEN_LONG / Swing 88.0 / AI评分 None / 综合 88.0 / AI置信度 -

- 钱包数：4，分组：{'smart_money': 2, 'money_printer': 2}，事件：{'INCREASE_POSITION': 3, 'FLIP_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$1,078,314，最大单钱包：$429,289
- 标记价：80.5705，均价：80.636525，权重分：25.3861，净偏向分：6.3465
- AI独立评分：None，规则评分：88.0，综合开仓评分：88.0，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第8轮 / 持续14.8小时 / 冷却剩余7.0小时 / 金额变化1.50x
- 钱包质量：50/100 高质=1 样本=4，高质量钱包=1，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$1,122,703，冲突比=1.0412
- 市场：funding=-1.9934e-06，OI=5495269.500000001，oracle=80.62，15m=-0.5928% ，1h=-0.5928% ，volRatio=0.9423
- 中长期评分：88.0 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$1,078,314，6h=$1,078,314，24h=$3,659,460
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.0, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 0.0}
- 风险标签：direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x72cb918356c4f6d3f1b2e532928110ba6995f139 money_printer INCREASE_POSITION $429,289 score=0.65 grade=NEW win72=- avg72=-
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $307,522 score=1.02 grade=B win72=- avg72=-
  - 0x39475d17bcd20adc540e647dae6781b153fbf3b1 money_printer FLIP_POSITION $171,539 score=1.12 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=12 amount=$5,465,077 score=81.7203 groups={'smart_money': 2, 'money_printer': 10}
- **SOL EXIT_SHORT** wallets=4 amount=$1,659,668 score=28.5435 groups={'money_printer': 3, 'smart_money': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$25,005,533 score=15.6638 groups={'money_printer': 2}
- **HYPE EXIT_SHORT** wallets=2 amount=$1,043,530 score=13.8493 groups={'smart_money': 1, 'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=2 amount=$386,298 score=12.4402 groups={'smart_money': 1, 'money_printer': 1}
- **HYPE EXIT_LONG** wallets=2 amount=$976,517 score=12.1129 groups={'smart_money': 2}
- **ETH EXIT_LONG** wallets=2 amount=$554,442 score=11.1382 groups={'smart_money': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第20轮 amount=$14,634,009 prev=50 exit_ratio=- amount_ratio=4.11x age=300.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第18轮 amount=$3,899,584 prev=55 exit_ratio=- amount_ratio=14.83x age=149.9m cooldown_left=6.0小时
- **COOLDOWN_MERGED** HYPE LONG 第10轮 amount=$762,314 prev=49 exit_ratio=- amount_ratio=2.20x age=300.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** HYPE SHORT 第10轮 amount=$1,020,794 prev=53 exit_ratio=- amount_ratio=1.80x age=270.0m cooldown_left=2.5小时
- **COOLDOWN_MERGED** SOL SHORT 第14轮 amount=$1,122,703 prev=47 exit_ratio=- amount_ratio=1.62x age=390.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC SHORT 第25轮 amount=$999,077 prev=58 exit_ratio=- amount_ratio=0.28x age=90.0m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第25轮 amount=$5,465,077 prev=58 exit_ratio=1.2567 amount_ratio=0.28x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第20轮 amount=$25,005,533 prev=50 exit_ratio=1.5997 amount_ratio=4.11x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第10轮 amount=$976,517 prev=49 exit_ratio=0.638 amount_ratio=2.20x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第14轮 amount=$1,659,668 prev=47 exit_ratio=0.7167 amount_ratio=1.62x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：59 条，方向正确 27，方向错误 32，平均方向收益 0.18%，最好 6.45%，最差 -5.33%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.46205 | 6.45 | 6.32 | 6.45 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.46205 | 6.31 | 6.18 | 6.31 | -2.20 |
| 44 | VVV | SHORT | 11.1805 | 10.545 | 5.68 | 5.55 | 5.94 | 0.00 |
| 45 | MON | LONG | 0.025817 | 0.024441 | -5.33 | -5.46 | 0.89 | -7.78 |
| 34 | JTO | LONG | 0.77639 | 0.738875 | -4.83 | -4.96 | 0.55 | -6.78 |
| 21 | ZEC | LONG | 463.135 | 483.955 | 4.50 | 4.37 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 483.955 | -4.50 | -4.63 | 1.19 | -10.16 |
| 41 | HYPE | SHORT | 71.902 | 69.1595 | 3.81 | 3.68 | 3.94 | -0.38 |
| 13 | GRAM | SHORT | 1.6858 | 1.622 | 3.78 | 3.65 | 3.89 | -0.52 |
| 31 | NEAR | LONG | 2.05555 | 1.97785 | -3.78 | -3.91 | 1.11 | -3.78 |
| 16 | HYPE | LONG | 71.6085 | 69.1595 | -3.42 | -3.55 | 1.59 | -3.54 |
| 28 | HYPE | SHORT | 71.49 | 69.1595 | 3.26 | 3.13 | 3.38 | -1.76 |
| 33 | ZEC | SHORT | 469.59 | 483.955 | -3.06 | -3.19 | 0.00 | -8.65 |
| 4 | HYPE | SHORT | 71.0475 | 69.1595 | 2.66 | 2.53 | 2.78 | -2.39 |
| 47 | SOL | SHORT | 82.5535 | 80.5705 | 2.40 | 2.27 | 2.40 | -0.08 |
| 37 | ZEC | LONG | 495.815 | 483.955 | -2.39 | -2.52 | 2.90 | -3.70 |
| 8 | NEAR | SHORT | 2.0234 | 1.97785 | 2.25 | 2.12 | 2.25 | -2.72 |
| 51 | ZEC | LONG | 493.435 | 483.955 | -1.92 | -2.05 | 0.83 | -3.24 |
| 56 | LIT | SHORT | 2.50975 | 2.46205 | 1.90 | 1.77 | 1.90 | 0.00 |
| 7 | XRP | SHORT | 1.13285 | 1.11185 | 1.85 | 1.72 | 1.94 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 80.5705 | -1.78 | -1.91 | 0.71 | -1.78 |
| 42 | ETH | SHORT | 1803.55 | 1772.05 | 1.75 | 1.62 | 1.76 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1772.05 | -1.66 | -1.79 | 0.48 | -1.68 |
| 39 | XRP | SHORT | 1.12915 | 1.11185 | 1.53 | 1.40 | 1.62 | -0.20 |
| 14 | kPEPE | LONG | 0.002705 | 0.002665 | -1.48 | -1.61 | 1.44 | -1.52 |
| 49 | HYPE | LONG | 70.1565 | 69.1595 | -1.42 | -1.55 | 0.23 | -1.55 |
| 38 | ETH | LONG | 1797.05 | 1772.05 | -1.39 | -1.52 | 0.75 | -1.41 |
| 36 | ETH | SHORT | 1797.05 | 1772.05 | 1.39 | 1.26 | 1.41 | -0.75 |
| 48 | BNB | SHORT | 584.295 | 576.665 | 1.31 | 1.18 | 1.31 | 0.00 |
| 5 | SOL | SHORT | 81.6175 | 80.5705 | 1.28 | 1.15 | 1.28 | -1.23 |

</details>
