# 钱包合约信号报告

Time: **2026-07-07 21:30:36 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1236，本轮 warmup 钱包：1185，变动事件：1602
- AI 输入信号：2，虚拟开仓：0，动态评分钱包：126
- 钱包胜率层：enabled=True，新记录=225，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 9，冷却合并 4
- 信号状态：NEW=0，RE_ALERT=1，REPEAT=1，追踪状态=6
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=0

### 24h运行健康

- runs=27，signals=52，avg_duration=192.7s，AI calls=39，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.01 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.01 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 2.00 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.00 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.85 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.82 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.79 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.79 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.76 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.76 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **BTC LONG** [RE_ALERT / 第14轮 / 持续9.0小时 / 冷却剩余7.0小时 / 金额变化30.04x] swing=88.05 AI=- conf=- AI分=None 综合=88.05 delta=$13,760,405 wallets=14 q=60/100 高质=7 样本=13 horizon=3-14

### 开空强候选

- **LIT SHORT** [ACTIVE_REPEAT / 第3轮 / 持续14.5小时 / 冷却剩余7.0小时 / 金额变化0.34x] swing=97.0 AI=- conf=- AI分=None 综合=97.0 delta=$394,387 wallets=1 q=50/100 高质=0 样本=0 horizon=3-14

## 本轮开仓/加仓信号

### 1. BTC OPEN_LONG / Swing 88.05 / AI评分 None / 综合 88.05 / AI置信度 -

- 钱包数：14，分组：{'smart_money': 9, 'money_printer': 5}，事件：{'FLIP_POSITION': 8, 'INCREASE_POSITION': 6}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$13,760,405，最大单钱包：$8,405,370
- 标记价：63470.5，均价：63551.2，权重分：92.2844，净偏向分：64.5389
- AI独立评分：None，规则评分：88.05，综合开仓评分：88.05，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第14轮 / 持续9.0小时 / 冷却剩余7.0小时 / 金额变化30.04x
- 钱包质量：60/100 高质=7 样本=13，高质量钱包=7，低质量钱包=2，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$5,516,125，冲突比=0.4009
- 市场：funding=1.25e-05，OI=38130.33234，oracle=63481.0，15m=-0.7641% ，1h=-1.0749% ，volRatio=1.8027
- 中长期评分：88.05 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$13,760,405，6h=$27,495,132，24h=$39,707,999
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 6.05, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xcf3f419d08a5bdc2c6e5fbd9ad70904c5420f95f smart_money INCREASE_POSITION $8,405,370 score=0.92 grade=NEW win72=- avg72=-
  - 0x023a3d058020fb76cca98f01b3c48c8938a22355 money_printer INCREASE_POSITION $1,114,922 score=1.28 grade=A win72=- avg72=-
  - 0xf9109ada2f73c62e9889b45453065f0d99260a2d smart_money INCREASE_POSITION $884,124 score=1.27 grade=NEW win72=- avg72=-

### 2. LIT OPEN_SHORT / Swing 97.0 / AI评分 None / 综合 97.0 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$394,387，最大单钱包：$394,387
- 标记价：2.50975，均价：2.508945，权重分：7.5545，净偏向分：7.5545
- AI独立评分：None，规则评分：97.0，综合开仓评分：97.0，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第3轮 / 持续14.5小时 / 冷却剩余7.0小时 / 金额变化0.34x
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=54334688.0，oracle=2.5099，15m=-2.5147% ，1h=-3.3886% ，volRatio=0.9335
- 中长期评分：97.0 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$394,387，6h=$394,387，24h=$1,742,064
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.0, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 12.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 10.0}
- 风险标签：money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xf17de447fdfa1778db06111e3cbdc878332adab2 money_printer NEW_POSITION $394,387 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=19 amount=$23,470,504 score=140.7411 groups={'smart_money': 3, 'money_printer': 16}
- **HYPE EXIT_LONG** wallets=6 amount=$5,194,016 score=33.769 groups={'smart_money': 6}
- **SOL EXIT_SHORT** wallets=4 amount=$1,304,248 score=28.8971 groups={'money_printer': 4}
- **HYPE EXIT_SHORT** wallets=4 amount=$3,091,275 score=27.3081 groups={'smart_money': 1, 'money_printer': 3}
- **ETH EXIT_LONG** wallets=3 amount=$2,291,907 score=16.5613 groups={'smart_money': 3}
- **ZEC EXIT_SHORT** wallets=2 amount=$475,097 score=12.624 groups={'smart_money': 1, 'money_printer': 1}
- **BTC EXIT_LONG** wallets=2 amount=$253,882 score=10.9231 groups={'smart_money': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第15轮 amount=$9,617,140 prev=36 exit_ratio=- amount_ratio=13.98x age=330.1m cooldown_left=5.5小时
- **COOLDOWN_MERGED** HYPE LONG 第7轮 amount=$1,793,194 prev=49 exit_ratio=- amount_ratio=2.31x age=150.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL LONG 第6轮 amount=$1,054,194 prev=40 exit_ratio=- amount_ratio=2.97x age=330.1m cooldown_left=1.5小时
- **COOLDOWN_MERGED** BTC SHORT 第20轮 amount=$5,516,125 prev=29 exit_ratio=- amount_ratio=1.94x age=390.0m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第-轮 amount=$3,091,275 prev=41 exit_ratio=1.7627 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第7轮 amount=$5,194,016 prev=49 exit_ratio=3.3937 amount_ratio=2.31x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第-轮 amount=$1,304,248 prev=47 exit_ratio=0.5632 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** ETH LONG 第-轮 amount=$2,291,907 prev=38 exit_ratio=0.6098 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第20轮 amount=$23,470,504 prev=29 exit_ratio=1.4617 amount_ratio=1.94x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：56 条，方向正确 24，方向错误 32，平均方向收益 -0.04%，最好 5.11%，最差 -7.78%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 45 | MON | LONG | 0.025817 | 0.023808 | -7.78 | -7.91 | 0.89 | -7.78 |
| 34 | JTO | LONG | 0.77639 | 0.72652 | -6.42 | -6.55 | 0.55 | -6.42 |
| 44 | VVV | SHORT | 11.1805 | 10.6095 | 5.11 | 4.98 | 5.11 | 0.00 |
| 18 | LIT | SHORT | 2.63175 | 2.50975 | 4.64 | 4.51 | 4.64 | -2.05 |
| 21 | ZEC | LONG | 463.135 | 484.17 | 4.54 | 4.41 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 484.17 | -4.54 | -4.67 | 1.19 | -10.16 |
| 6 | LIT | SHORT | 2.6279 | 2.50975 | 4.50 | 4.37 | 4.57 | -2.20 |
| 41 | HYPE | SHORT | 71.902 | 69.3405 | 3.56 | 3.43 | 3.56 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 69.3405 | -3.17 | -3.30 | 1.59 | -3.17 |
| 33 | ZEC | SHORT | 469.59 | 484.17 | -3.10 | -3.23 | 0.00 | -8.65 |
| 28 | HYPE | SHORT | 71.49 | 69.3405 | 3.01 | 2.88 | 3.01 | -1.76 |
| 31 | NEAR | LONG | 2.05555 | 1.99435 | -2.98 | -3.11 | 1.11 | -2.98 |
| 13 | GRAM | SHORT | 1.6858 | 1.6405 | 2.69 | 2.56 | 3.17 | -0.52 |
| 4 | HYPE | SHORT | 71.0475 | 69.3405 | 2.40 | 2.27 | 2.40 | -2.39 |
| 37 | ZEC | LONG | 495.815 | 484.17 | -2.35 | -2.48 | 2.90 | -2.35 |
| 47 | SOL | SHORT | 82.5535 | 80.7945 | 2.13 | 2.00 | 2.13 | -0.08 |
| 51 | ZEC | LONG | 493.435 | 484.17 | -1.88 | -2.01 | 0.83 | -1.88 |
| 40 | SOL | LONG | 82.0335 | 80.7945 | -1.51 | -1.64 | 0.71 | -1.51 |
| 42 | ETH | SHORT | 1803.55 | 1776.55 | 1.50 | 1.37 | 1.50 | -0.39 |
| 7 | XRP | SHORT | 1.13285 | 1.11595 | 1.49 | 1.36 | 1.58 | 0.00 |
| 14 | kPEPE | LONG | 0.002705 | 0.002665 | -1.48 | -1.61 | 1.44 | -1.48 |
| 8 | NEAR | SHORT | 2.0234 | 1.99435 | 1.44 | 1.31 | 1.44 | -2.72 |
| 46 | ETH | LONG | 1801.95 | 1776.55 | -1.41 | -1.54 | 0.48 | -1.41 |
| 39 | XRP | SHORT | 1.12915 | 1.11595 | 1.17 | 1.04 | 1.19 | -0.20 |
| 49 | HYPE | LONG | 70.1565 | 69.3405 | -1.16 | -1.29 | 0.23 | -1.16 |
| 38 | ETH | LONG | 1797.05 | 1776.55 | -1.14 | -1.27 | 0.75 | -1.14 |
| 36 | ETH | SHORT | 1797.05 | 1776.55 | 1.14 | 1.01 | 1.14 | -0.75 |
| 5 | SOL | SHORT | 81.6175 | 80.7945 | 1.01 | 0.88 | 1.18 | -1.23 |
| 48 | BNB | SHORT | 584.295 | 578.91 | 0.92 | 0.79 | 0.92 | 0.00 |
| 43 | BTC | LONG | 64028.5 | 63470.5 | -0.87 | -1.00 | 0.20 | -0.87 |

</details>
