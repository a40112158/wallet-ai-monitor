# 钱包合约信号报告

Time: **2026-07-07 19:30:30 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1243，本轮 warmup 钱包：1178，变动事件：1743
- AI 输入信号：2，虚拟开仓：0，动态评分钱包：112
- 钱包胜率层：enabled=True，新记录=252，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 11，冷却合并 5
- 信号状态：NEW=0，RE_ALERT=2，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=0

### 24h运行健康

- runs=23，signals=49，avg_duration=189.0s，AI calls=37，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.16 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.00 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.00 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.98 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.82 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.79 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.72 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.72 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **HYPE LONG** [RE_ALERT / 第4轮 / 持续9.0小时 / 冷却剩余7.0小时 / 金额变化2.39x] swing=89.41 AI=- conf=- AI分=None 综合=89.41 delta=$3,659,653 wallets=8 q=45/100 高质=0 样本=2 horizon=3-14

### 开空强候选

- **HYPE SHORT** [RE_ALERT / 第6轮 / 持续12.5小时 / 冷却剩余7.0小时 / 金额变化2.75x] swing=88.65 AI=- conf=- AI分=None 综合=88.65 delta=$2,253,329 wallets=3 q=48/100 高质=0 样本=3 horizon=3-14

## 本轮开仓/加仓信号

### 1. HYPE OPEN_LONG / Swing 89.41 / AI评分 None / 综合 89.41 / AI置信度 -

- 钱包数：8，分组：{'smart_money': 5, 'money_printer': 3}，事件：{'NEW_POSITION': 1, 'INCREASE_POSITION': 7}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$3,659,653，最大单钱包：$1,256,571
- 标记价：69.8095，均价：70.405925，权重分：49.157，净偏向分：26.4567
- AI独立评分：None，规则评分：89.41，综合开仓评分：89.41，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第4轮 / 持续9.0小时 / 冷却剩余7.0小时 / 金额变化2.39x
- 钱包质量：45/100 高质=0 样本=2，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$2,253,329，冲突比=0.6157
- 市场：funding=1.25e-05，OI=22479935.419999987，oracle=69.825，15m=-2.9595% ，1h=-2.6682% ，volRatio=1.5481
- 中长期评分：89.41 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$5,190,160，6h=$5,190,160，24h=$8,355,628
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.52, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 2.89}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x1116b5fcc070945062e8879841c29807db373d0d smart_money NEW_POSITION $1,256,571 score=1.00 grade=NEW win72=- avg72=-
  - 0xad227f63d34e7251c1d0ab65e64eeea07aee4e44 money_printer INCREASE_POSITION $698,095 score=0.54 grade=NEW win72=- avg72=-
  - 0xfba7c3e68638fda0a13994ddb6733cbd016ec826 smart_money INCREASE_POSITION $371,961 score=1.00 grade=NEW win72=- avg72=-

### 2. HYPE OPEN_SHORT / Swing 88.65 / AI评分 None / 综合 88.65 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 1, 'money_printer': 2}，事件：{'INCREASE_POSITION': 3}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$2,253,329，最大单钱包：$1,304,400
- 标记价：69.8095，均价：68.89363333，权重分：20.7432，净偏向分：5.1858
- AI独立评分：None，规则评分：88.65，综合开仓评分：88.65，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第6轮 / 持续12.5小时 / 冷却剩余7.0小时 / 金额变化2.75x
- 钱包质量：48/100 高质=0 样本=3，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：HIGH，反向金额=$3,659,653，冲突比=1.6241
- 市场：funding=1.25e-05，OI=22479935.419999987，oracle=69.825，15m=-2.9595% ，1h=-2.6682% ，volRatio=1.5481
- 中长期评分：88.65 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,253,329，6h=$4,773,315，24h=$6,863,098
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.78, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 12.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 1.87}
- 风险标签：cooldown_realert_large_add, direction_conflict, high_long_short_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $1,304,400 score=0.99 grade=NEW win72=- avg72=-
  - 0x3bcae23e8c380dab4732e9a159c0456f12d866f3 money_printer INCREASE_POSITION $796,329 score=0.96 grade=NEW win72=- avg72=-
  - 0xf822fa0fd364c573fcdb7009fcf47601bc8be01a money_printer INCREASE_POSITION $152,600 score=0.86 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **ETH EXIT_SHORT** wallets=6 amount=$2,472,394 score=44.784 groups={'money_printer': 6}
- **BTC EXIT_SHORT** wallets=5 amount=$8,022,801 score=32.7762 groups={'money_printer': 2, 'smart_money': 3}
- **BTC EXIT_LONG** wallets=5 amount=$3,041,140 score=30.2779 groups={'smart_money': 4, 'money_printer': 1}
- **HYPE EXIT_LONG** wallets=4 amount=$2,501,499 score=27.3073 groups={'money_printer': 2, 'smart_money': 2}
- **SOL EXIT_SHORT** wallets=2 amount=$580,360 score=14.1487 groups={'money_printer': 2}
- **NEAR EXIT_LONG** wallets=2 amount=$433,639 score=11.7478 groups={'money_printer': 1, 'smart_money': 1}
- **ZEC EXIT_LONG** wallets=2 amount=$639,952 score=10.0782 groups={'smart_money': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第16轮 amount=$9,670,096 prev=26 exit_ratio=- amount_ratio=3.46x age=330.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH SHORT 第12轮 amount=$3,742,079 prev=23 exit_ratio=- amount_ratio=0.24x age=360.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL SHORT 第11轮 amount=$1,011,747 prev=24 exit_ratio=- amount_ratio=1.58x age=360.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ZEC LONG 第7轮 amount=$736,830 prev=37 exit_ratio=- amount_ratio=0.64x age=210.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH LONG 第4轮 amount=$543,336 prev=38 exit_ratio=- amount_ratio=0.60x age=210.1m cooldown_left=4.5小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第12轮 amount=$2,472,394 prev=23 exit_ratio=1.3205 amount_ratio=0.24x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第4轮 amount=$2,501,499 prev=49 exit_ratio=1.6344 amount_ratio=2.39x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第11轮 amount=$580,360 prev=24 exit_ratio=0.5056 amount_ratio=1.58x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第-轮 amount=$3,041,140 prev=22 exit_ratio=1.2445 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** NEAR LONG 第-轮 amount=$433,639 prev=31 exit_ratio=0.5567 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第16轮 amount=$8,022,801 prev=26 exit_ratio=0.5228 amount_ratio=3.46x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：53 条，方向正确 20，方向错误 33，平均方向收益 -0.01%，最好 6.06%，最差 -6.06%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 491.22 | 6.06 | 5.93 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 491.22 | -6.06 | -6.19 | 1.19 | -10.16 |
| 34 | JTO | LONG | 0.77639 | 0.73353 | -5.52 | -5.65 | 0.55 | -5.52 |
| 33 | ZEC | SHORT | 469.59 | 491.22 | -4.61 | -4.74 | 0.00 | -8.65 |
| 18 | LIT | SHORT | 2.63175 | 2.51395 | 4.48 | 4.35 | 4.48 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.51395 | 4.34 | 4.21 | 4.57 | -2.20 |
| 44 | VVV | SHORT | 11.1805 | 10.834 | 3.10 | 2.97 | 3.44 | 0.00 |
| 41 | HYPE | SHORT | 71.902 | 69.8095 | 2.91 | 2.78 | 2.91 | -0.38 |
| 13 | GRAM | SHORT | 1.6858 | 1.6396 | 2.74 | 2.61 | 3.17 | -0.52 |
| 45 | MON | LONG | 0.025817 | 0.025153 | -2.57 | -2.70 | 0.89 | -2.57 |
| 16 | HYPE | LONG | 71.6085 | 69.8095 | -2.51 | -2.64 | 1.59 | -2.51 |
| 28 | HYPE | SHORT | 71.49 | 69.8095 | 2.35 | 2.22 | 2.35 | -1.76 |
| 31 | NEAR | LONG | 2.05555 | 2.0127 | -2.08 | -2.21 | 1.11 | -2.12 |
| 4 | HYPE | SHORT | 71.0475 | 69.8095 | 1.74 | 1.61 | 1.74 | -2.39 |
| 47 | SOL | SHORT | 82.5535 | 81.1425 | 1.71 | 1.58 | 1.82 | -0.08 |
| 7 | XRP | SHORT | 1.13285 | 1.11835 | 1.28 | 1.15 | 1.58 | 0.00 |
| 26 | BTC | SHORT | 62945.5 | 63656.5 | -1.13 | -1.26 | 0.00 | -1.93 |
| 40 | SOL | LONG | 82.0335 | 81.1425 | -1.09 | -1.22 | 0.71 | -1.20 |
| 42 | ETH | SHORT | 1803.55 | 1784.75 | 1.04 | 0.91 | 1.14 | -0.39 |
| 27 | ETH | SHORT | 1767.25 | 1784.75 | -0.99 | -1.12 | 0.00 | -2.45 |
| 39 | XRP | SHORT | 1.12915 | 1.11835 | 0.96 | 0.83 | 1.19 | -0.20 |
| 46 | ETH | LONG | 1801.95 | 1784.75 | -0.95 | -1.08 | 0.48 | -1.05 |
| 37 | ZEC | LONG | 495.815 | 491.22 | -0.93 | -1.06 | 2.90 | -0.93 |
| 1 | BTC | SHORT | 63136.5 | 63656.5 | -0.82 | -0.95 | 0.30 | -1.62 |
| 25 | BTC | LONG | 63172.5 | 63656.5 | 0.77 | 0.64 | 1.56 | -0.36 |
| 38 | ETH | LONG | 1797.05 | 1784.75 | -0.68 | -0.81 | 0.75 | -0.78 |
| 36 | ETH | SHORT | 1797.05 | 1784.75 | 0.68 | 0.55 | 0.78 | -0.75 |
| 10 | BTC | SHORT | 63245.5 | 63656.5 | -0.65 | -0.78 | 0.47 | -1.45 |
| 23 | ETH | SHORT | 1773.75 | 1784.75 | -0.62 | -0.75 | 0.37 | -2.07 |
| 12 | BTC | SHORT | 63271.5 | 63656.5 | -0.61 | -0.74 | 0.52 | -1.40 |

</details>
