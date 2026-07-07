# 钱包合约信号报告

Time: **2026-07-07 22:30:33 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1232，本轮 warmup 钱包：1189，变动事件：1379
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：126
- 钱包胜率层：enabled=True，新记录=87，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 6，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=1，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=29，signals=55，avg_duration=193.0s，AI calls=41，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.12 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.12 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.10 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.94 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.89 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.86 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.83 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.83 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.77 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.77 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **BTC SHORT** [ACTIVE_REPEAT / 第22轮 / 持续16.1小时 / 冷却剩余7.0小时 / 金额变化1.50x] swing=89.87 AI=- conf=- AI分=None 综合=89.87 delta=$4,348,581 wallets=8 q=43/100 高质=2 样本=6 horizon=3-14

## 本轮开仓/加仓信号

### 1. BTC OPEN_SHORT / Swing 89.87 / AI评分 None / 综合 89.87 / AI置信度 -

- 钱包数：8，分组：{'smart_money': 1, 'money_printer': 7}，事件：{'INCREASE_POSITION': 8}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$4,348,581，最大单钱包：$1,490,184
- 标记价：63431.5，均价：63250.8875，权重分：58.3781，净偏向分：58.3781
- AI独立评分：None，规则评分：89.87，综合开仓评分：89.87，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第22轮 / 持续16.1小时 / 冷却剩余7.0小时 / 金额变化1.50x
- 钱包质量：43/100 高质=2 样本=6，高质量钱包=2，低质量钱包=3，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=37626.35194，oracle=63444.0，15m=-0.1824% ，1h=-0.3031% ，volRatio=0.6276
- 中长期评分：89.87 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$4,348,581，6h=$4,348,581，24h=$67,452,280
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 4.28, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 2.59}
- 风险标签：direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x3bcae23e8c380dab4732e9a159c0456f12d866f3 money_printer INCREASE_POSITION $1,490,184 score=1.44 grade=NEW win72=- avg72=-
  - 0x34fb5ec7d4e939161946340ea2a1f29254b893de money_printer INCREASE_POSITION $990,830 score=1.00 grade=NEW win72=- avg72=-
  - 0x7ca165f354e3260e2f8d5a7508cc9dd2fa009235 money_printer INCREASE_POSITION $599,847 score=0.61 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=10 amount=$3,702,833 score=52.7815 groups={'smart_money': 9, 'money_printer': 1}
- **BTC EXIT_SHORT** wallets=5 amount=$2,219,440 score=37.3923 groups={'money_printer': 4, 'smart_money': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$1,262,158 score=16.3157 groups={'money_printer': 2}
- **LIT EXIT_SHORT** wallets=2 amount=$296,552 score=15.7384 groups={'money_printer': 2}
- **ZEC EXIT_LONG** wallets=2 amount=$1,517,990 score=14.1306 groups={'money_printer': 2}
- **HYPE EXIT_SHORT** wallets=2 amount=$435,566 score=13.4612 groups={'smart_money': 1, 'money_printer': 1}
- **LIT EXIT_LONG** wallets=2 amount=$748,238 score=12.0463 groups={'money_printer': 1, 'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** ETH SHORT 第17轮 amount=$1,769,180 prev=36 exit_ratio=- amount_ratio=0.10x age=390.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** SOL SHORT 第13轮 amount=$693,886 prev=47 exit_ratio=- amount_ratio=1.99x age=300.0m cooldown_left=4.0小时
- **COOLDOWN_MERGED** HYPE LONG 第9轮 amount=$347,181 prev=49 exit_ratio=- amount_ratio=0.26x age=210.1m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** LIT SHORT 第-轮 amount=$296,552 prev=56 exit_ratio=0.7519 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第-轮 amount=$3,702,833 prev=35 exit_ratio=0.751 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** ZEC LONG 第-轮 amount=$1,517,990 prev=37 exit_ratio=0.591 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：58 条，方向正确 25，方向错误 33，平均方向收益 0.08%，最好 5.67%，最差 -6.37%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.72695 | -6.37 | -6.50 | 0.55 | -6.78 |
| 18 | LIT | SHORT | 2.63175 | 2.4825 | 5.67 | 5.54 | 6.21 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.4825 | 5.53 | 5.40 | 6.07 | -2.20 |
| 45 | MON | LONG | 0.025817 | 0.024449 | -5.30 | -5.43 | 0.89 | -7.78 |
| 44 | VVV | SHORT | 11.1805 | 10.6265 | 4.96 | 4.83 | 5.94 | 0.00 |
| 41 | HYPE | SHORT | 71.902 | 69.0705 | 3.94 | 3.81 | 3.94 | -0.38 |
| 13 | GRAM | SHORT | 1.6858 | 1.62015 | 3.89 | 3.76 | 3.89 | -0.52 |
| 37 | ZEC | LONG | 495.815 | 477.465 | -3.70 | -3.83 | 2.90 | -3.70 |
| 31 | NEAR | LONG | 2.05555 | 1.98085 | -3.63 | -3.76 | 1.11 | -3.63 |
| 16 | HYPE | LONG | 71.6085 | 69.0705 | -3.54 | -3.67 | 1.59 | -3.54 |
| 28 | HYPE | SHORT | 71.49 | 69.0705 | 3.38 | 3.25 | 3.38 | -1.76 |
| 51 | ZEC | LONG | 493.435 | 477.465 | -3.24 | -3.37 | 0.83 | -3.24 |
| 21 | ZEC | LONG | 463.135 | 477.465 | 3.09 | 2.96 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 477.465 | -3.09 | -3.22 | 1.19 | -10.16 |
| 4 | HYPE | SHORT | 71.0475 | 69.0705 | 2.78 | 2.65 | 2.78 | -2.39 |
| 47 | SOL | SHORT | 82.5535 | 80.7625 | 2.17 | 2.04 | 2.27 | -0.08 |
| 8 | NEAR | SHORT | 2.0234 | 1.98085 | 2.10 | 1.97 | 2.10 | -2.72 |
| 42 | ETH | SHORT | 1803.55 | 1772.15 | 1.74 | 1.61 | 1.76 | -0.39 |
| 7 | XRP | SHORT | 1.13285 | 1.11335 | 1.72 | 1.59 | 1.94 | 0.00 |
| 33 | ZEC | SHORT | 469.59 | 477.465 | -1.68 | -1.81 | 0.00 | -8.65 |
| 46 | ETH | LONG | 1801.95 | 1772.15 | -1.65 | -1.78 | 0.48 | -1.68 |
| 40 | SOL | LONG | 82.0335 | 80.7625 | -1.55 | -1.68 | 0.71 | -1.65 |
| 49 | HYPE | LONG | 70.1565 | 69.0705 | -1.55 | -1.68 | 0.23 | -1.55 |
| 14 | kPEPE | LONG | 0.002705 | 0.002667 | -1.40 | -1.53 | 1.44 | -1.52 |
| 39 | XRP | SHORT | 1.12915 | 1.11335 | 1.40 | 1.27 | 1.62 | -0.20 |
| 38 | ETH | LONG | 1797.05 | 1772.15 | -1.39 | -1.52 | 0.75 | -1.41 |
| 36 | ETH | SHORT | 1797.05 | 1772.15 | 1.39 | 1.26 | 1.41 | -0.75 |
| 56 | LIT | SHORT | 2.50975 | 2.4825 | 1.09 | 0.96 | 1.65 | 0.00 |
| 48 | BNB | SHORT | 584.295 | 578.075 | 1.06 | 0.93 | 1.14 | 0.00 |
| 53 | HYPE | SHORT | 69.8095 | 69.0705 | 1.06 | 0.93 | 1.06 | -0.73 |

</details>
