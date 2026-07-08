# 钱包合约信号报告

Time: **2026-07-08 06:00:39 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1216，本轮 warmup 钱包：1205，变动事件：1341
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：143
- 钱包胜率层：enabled=True，新记录=120，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 5，生命周期事件 5，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=1，追踪状态=5
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=44，signals=70，avg_duration=200.6s，AI calls=50，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.07 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.07 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.06 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.06 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.99 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 1.95 | 1 | - | - | - | - |
| 0x4ef1c5...a528e3 | smart_money | NEW | 1.95 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **SOL SHORT** [ACTIVE_REPEAT / 第16轮 / 持续23.0小时 / 冷却剩余7.0小时 / 金额变化0.98x] swing=90.26 AI=- conf=- AI分=None 综合=90.26 delta=$2,862,367 wallets=1 q=50/100 高质=0 样本=0 horizon=3-14

## 本轮开仓/加仓信号

### 1. SOL OPEN_SHORT / Swing 90.26 / AI评分 None / 综合 90.26 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$2,862,367，最大单钱包：$2,862,367
- 标记价：78.3505，均价：78.3859，权重分：8.7166，净偏向分：7.112
- AI独立评分：None，规则评分：90.26，综合开仓评分：90.26，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第16轮 / 持续23.0小时 / 冷却剩余7.0小时 / 金额变化0.98x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$702,564，冲突比=0.2454
- 市场：funding=-1.02954e-05，OI=5259540.819999999，oracle=78.395，15m=-1.0012% ，1h=-1.0012% ，volRatio=1.3225
- 中长期评分：90.26 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,862,367，6h=$2,862,367，24h=$7,195,302
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.0, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 3.26}
- 风险标签：money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x77375a8c9d13bf79afb2a87f1b0ac1dfd5f5bf66 money_printer NEW_POSITION $2,862,367 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=9 amount=$6,148,813 score=73.283 groups={'smart_money': 1, 'money_printer': 8}
- **SOL EXIT_SHORT** wallets=4 amount=$1,517,145 score=32.0803 groups={'smart_money': 1, 'money_printer': 3}
- **ETH EXIT_SHORT** wallets=3 amount=$987,164 score=24.6535 groups={'money_printer': 3}
- **XRP EXIT_SHORT** wallets=1 amount=$212,209 score=8.6589 groups={'money_printer': 1}
- **BTC EXIT_LONG** wallets=1 amount=$6,559,656 score=6.8169 groups={'smart_money': 1}
- **ETH EXIT_LONG** wallets=1 amount=$216,197 score=6.2711 groups={'smart_money': 1}
- **HYPE EXIT_SHORT** wallets=1 amount=$102,479 score=5.8768 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC LONG 第29轮 amount=$4,232,181 prev=69 exit_ratio=- amount_ratio=2.68x age=90.0m cooldown_left=5.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第15轮 amount=$573,365 prev=70 exit_ratio=- amount_ratio=0.95x age=90.0m cooldown_left=5.5小时
- **COOLDOWN_MERGED** BTC SHORT 第35轮 amount=$1,277,456 prev=60 exit_ratio=- amount_ratio=1.06x age=330.2m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL LONG 第15轮 amount=$702,564 prev=59 exit_ratio=- amount_ratio=0.59x age=360.1m cooldown_left=3.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第35轮 amount=$6,148,813 prev=60 exit_ratio=0.6979 amount_ratio=1.06x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：73 条，方向正确 40，方向错误 33，平均方向收益 0.34%，最好 7.78%，最差 -7.80%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.71585 | -7.80 | -7.93 | 0.55 | -7.80 |
| 18 | LIT | SHORT | 2.63175 | 2.42705 | 7.78 | 7.65 | 8.64 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.42705 | 7.64 | 7.51 | 8.51 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.918 | -6.69 | -6.82 | 1.11 | -7.50 |
| 8 | NEAR | SHORT | 2.0234 | 1.918 | 5.21 | 5.08 | 6.03 | -2.72 |
| 13 | GRAM | SHORT | 1.6858 | 1.5994 | 5.13 | 5.00 | 6.60 | -0.52 |
| 45 | MON | LONG | 0.025817 | 0.024499 | -5.11 | -5.24 | 0.89 | -7.78 |
| 47 | SOL | SHORT | 82.5535 | 78.3505 | 5.09 | 4.96 | 5.09 | -0.08 |
| 41 | HYPE | SHORT | 71.902 | 68.3195 | 4.98 | 4.85 | 5.90 | -0.38 |
| 44 | VVV | SHORT | 11.1805 | 10.6575 | 4.68 | 4.55 | 5.94 | 0.00 |
| 16 | HYPE | LONG | 71.6085 | 68.3195 | -4.59 | -4.72 | 1.59 | -5.51 |
| 40 | SOL | LONG | 82.0335 | 78.3505 | -4.49 | -4.62 | 0.71 | -4.49 |
| 28 | HYPE | SHORT | 71.49 | 68.3195 | 4.43 | 4.30 | 5.35 | -1.76 |
| 5 | SOL | SHORT | 81.6175 | 78.3505 | 4.00 | 3.87 | 4.00 | -1.23 |
| 21 | ZEC | LONG | 463.135 | 481.595 | 3.99 | 3.86 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 481.595 | -3.99 | -4.12 | 1.19 | -10.16 |
| 4 | HYPE | SHORT | 71.0475 | 68.3195 | 3.84 | 3.71 | 4.76 | -2.39 |
| 7 | XRP | SHORT | 1.13285 | 1.09005 | 3.78 | 3.65 | 3.78 | 0.00 |
| 11 | SOL | LONG | 81.4165 | 78.3505 | -3.77 | -3.90 | 1.48 | -3.77 |
| 14 | kPEPE | LONG | 0.002705 | 0.002609 | -3.55 | -3.68 | 1.44 | -3.88 |
| 39 | XRP | SHORT | 1.12915 | 1.09005 | 3.46 | 3.33 | 3.46 | -0.20 |
| 24 | SOL | SHORT | 81.0475 | 78.3505 | 3.33 | 3.20 | 3.33 | -1.94 |
| 56 | LIT | SHORT | 2.50975 | 2.42705 | 3.30 | 3.17 | 4.20 | 0.00 |
| 37 | ZEC | LONG | 495.815 | 481.595 | -2.87 | -3.00 | 2.90 | -3.76 |
| 48 | BNB | SHORT | 584.295 | 567.85 | 2.81 | 2.68 | 2.81 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1753.25 | 2.79 | 2.66 | 2.89 | -0.39 |
| 59 | SOL | LONG | 80.5705 | 78.3505 | -2.76 | -2.89 | 0.03 | -2.76 |
| 46 | ETH | LONG | 1801.95 | 1753.25 | -2.70 | -2.83 | 0.48 | -2.81 |
| 49 | HYPE | LONG | 70.1565 | 68.3195 | -2.62 | -2.75 | 0.23 | -3.55 |
| 33 | ZEC | SHORT | 469.59 | 481.595 | -2.56 | -2.69 | 0.00 | -8.65 |

</details>
