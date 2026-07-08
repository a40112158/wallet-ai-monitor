# 钱包合约信号报告

Time: **2026-07-08 02:30:31 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1218，本轮 warmup 钱包：1203，变动事件：1675
- AI 输入信号：2，虚拟开仓：0，动态评分钱包：132
- 钱包胜率层：enabled=True，新记录=177，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 5，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=2，追踪状态=6
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=0

### 24h运行健康

- runs=37，signals=63，avg_duration=199.3s，AI calls=46，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.15 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.15 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.09 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 2.03 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 2.03 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.00 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **HYPE LONG** [ACTIVE_REPEAT / 第12轮 / 持续16.0小时 / 冷却剩余7.0小时 / 金额变化0.23x] swing=89.22 AI=- conf=- AI分=None 综合=89.22 delta=$718,662 wallets=4 q=58/100 高质=1 样本=2 horizon=3-14
- **ZEC LONG** [ACTIVE_REPEAT / 第10轮 / 持续14.0小时 / 冷却剩余7.0小时 / 金额变化1.60x] swing=91.09 AI=- conf=- AI分=None 综合=91.09 delta=$404,294 wallets=1 q=52/100 高质=0 样本=1 horizon=3-14

## 本轮开仓/加仓信号

### 1. HYPE OPEN_LONG / Swing 89.22 / AI评分 None / 综合 89.22 / AI置信度 -

- 钱包数：4，分组：{'smart_money': 3, 'money_printer': 1}，事件：{'FLIP_POSITION': 2, 'NEW_POSITION': 1, 'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$718,662，最大单钱包：$324,284
- 标记价：67.663，均价：68.1821，权重分：23.4948，净偏向分：23.4948
- AI独立评分：None，规则评分：89.22，综合开仓评分：89.22，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第12轮 / 持续16.0小时 / 冷却剩余7.0小时 / 金额变化0.23x
- 钱包质量：58/100 高质=1 样本=2，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=21963279.33999999，oracle=67.653，15m=-3.3985% ，1h=-3.2239% ，volRatio=0.9589
- 中长期评分：89.22 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$718,662，6h=$718,662，24h=$9,074,290
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.83, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 1.39}
- 风险标签：direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money FLIP_POSITION $324,284 score=1.11 grade=B win72=- avg72=-
  - 0x7fdafde5cfb5465924316eced2d3715494c517d1 money_printer INCREASE_POSITION $157,830 score=1.39 grade=A win72=- avg72=-
  - 0x48ea62a2cc8391fbbe210e8ee89db573a8ec145f smart_money FLIP_POSITION $136,530 score=1.00 grade=NEW win72=- avg72=-

### 2. ZEC OPEN_LONG / Swing 91.09 / AI评分 None / 综合 91.09 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$404,294，最大单钱包：$404,294
- 标记价：479.345，均价：478.1649，权重分：5.7597，净偏向分：5.7597
- AI独立评分：None，规则评分：91.09，综合开仓评分：91.09，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第10轮 / 持续14.0小时 / 冷却剩余7.0小时 / 金额变化1.60x
- 钱包质量：52/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=459138.1400000001，oracle=479.33，15m=-2.0142% ，1h=-1.6328% ，volRatio=0.6683
- 中长期评分：91.09 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$404,294，6h=$404,294，24h=$4,652,285
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.25, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 3.85}
- 风险标签：money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $404,294 score=1.11 grade=B win72=- avg72=-

## 减仓/平仓风险信号

- **ETH EXIT_SHORT** wallets=8 amount=$2,421,314 score=63.776 groups={'money_printer': 8}
- **SOL EXIT_SHORT** wallets=8 amount=$2,901,201 score=57.3304 groups={'smart_money': 4, 'money_printer': 4}
- **BTC EXIT_LONG** wallets=9 amount=$5,792,335 score=57.0501 groups={'smart_money': 6, 'money_printer': 3}
- **BTC EXIT_SHORT** wallets=4 amount=$2,897,518 score=31.3388 groups={'smart_money': 1, 'money_printer': 3}
- **HYPE EXIT_LONG** wallets=3 amount=$1,221,528 score=16.6829 groups={'smart_money': 3}
- **HYPE EXIT_SHORT** wallets=2 amount=$360,741 score=13.7419 groups={'money_printer': 1, 'smart_money': 1}
- **PUMP EXIT_SHORT** wallets=1 amount=$181,475 score=7.5932 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第30轮 amount=$4,563,749 prev=58 exit_ratio=- amount_ratio=2.43x age=240.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL LONG 第13轮 amount=$612,065 prev=59 exit_ratio=- amount_ratio=0.30x age=150.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH LONG 第7轮 amount=$1,267,131 prev=63 exit_ratio=- amount_ratio=0.51x age=30.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH SHORT 第23轮 amount=$1,400,607 prev=54 exit_ratio=- amount_ratio=4.57x age=390.1m cooldown_left=4.5小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第30轮 amount=$2,897,518 prev=58 exit_ratio=0.6663 amount_ratio=2.43x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：67 条，方向正确 34，方向错误 33，平均方向收益 0.26%，最好 8.27%，最差 -7.50%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.4142 | 8.27 | 8.14 | 8.47 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.4142 | 8.13 | 8.00 | 8.34 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.90135 | -7.50 | -7.63 | 1.11 | -7.50 |
| 34 | JTO | LONG | 0.77639 | 0.719585 | -7.32 | -7.45 | 0.55 | -7.32 |
| 13 | GRAM | SHORT | 1.6858 | 1.5746 | 6.60 | 6.47 | 6.60 | -0.52 |
| 8 | NEAR | SHORT | 2.0234 | 1.90135 | 6.03 | 5.90 | 6.03 | -2.72 |
| 41 | HYPE | SHORT | 71.902 | 67.663 | 5.90 | 5.77 | 5.90 | -0.38 |
| 45 | MON | LONG | 0.025817 | 0.024343 | -5.71 | -5.84 | 0.89 | -7.78 |
| 16 | HYPE | LONG | 71.6085 | 67.663 | -5.51 | -5.64 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 67.663 | 5.35 | 5.22 | 5.35 | -1.76 |
| 4 | HYPE | SHORT | 71.0475 | 67.663 | 4.76 | 4.63 | 4.76 | -2.39 |
| 47 | SOL | SHORT | 82.5535 | 78.8295 | 4.51 | 4.38 | 4.51 | -0.08 |
| 44 | VVV | SHORT | 11.1805 | 10.7215 | 4.11 | 3.98 | 5.94 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 78.8295 | -3.91 | -4.04 | 0.71 | -3.91 |
| 14 | kPEPE | LONG | 0.002705 | 0.002602 | -3.81 | -3.94 | 1.44 | -3.81 |
| 56 | LIT | SHORT | 2.50975 | 2.4142 | 3.81 | 3.68 | 4.02 | 0.00 |
| 49 | HYPE | LONG | 70.1565 | 67.663 | -3.55 | -3.68 | 0.23 | -3.55 |
| 21 | ZEC | LONG | 463.135 | 479.345 | 3.50 | 3.37 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 479.345 | -3.50 | -3.63 | 1.19 | -10.16 |
| 5 | SOL | SHORT | 81.6175 | 78.8295 | 3.42 | 3.29 | 3.42 | -1.23 |
| 37 | ZEC | LONG | 495.815 | 479.345 | -3.32 | -3.45 | 2.90 | -3.76 |
| 7 | XRP | SHORT | 1.13285 | 1.09595 | 3.26 | 3.13 | 3.26 | 0.00 |
| 11 | SOL | LONG | 81.4165 | 78.8295 | -3.18 | -3.31 | 1.48 | -3.18 |
| 62 | UNI | LONG | 3.2692 | 3.16705 | -3.12 | -3.25 | 0.00 | -3.15 |
| 53 | HYPE | SHORT | 69.8095 | 67.663 | 3.07 | 2.94 | 3.07 | -0.73 |
| 52 | HYPE | LONG | 69.8095 | 67.663 | -3.07 | -3.20 | 0.73 | -3.07 |
| 39 | XRP | SHORT | 1.12915 | 1.09595 | 2.94 | 2.81 | 2.94 | -0.20 |
| 9 | TAO | LONG | 213.63 | 207.395 | -2.92 | -3.05 | 1.58 | -2.92 |
| 51 | ZEC | LONG | 493.435 | 479.345 | -2.86 | -2.99 | 0.83 | -3.30 |
| 42 | ETH | SHORT | 1803.55 | 1752.15 | 2.85 | 2.72 | 2.85 | -0.39 |

</details>
