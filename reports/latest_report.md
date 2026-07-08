# 钱包合约信号报告

Time: **2026-07-08 05:00:36 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1216，本轮 warmup 钱包：1205，变动事件：1298
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：140
- 钱包胜率层：enabled=True，新记录=102，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 7，生命周期事件 5，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=0，REPEAT=1，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=42，signals=69，avg_duration=200.0s，AI calls=49，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.10 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.03 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.03 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.02 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.00 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.97 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.94 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **ETH SHORT** [ACTIVE_REPEAT / 第28轮 / 持续22.0小时 / 冷却剩余7.0小时 / 金额变化0.18x] swing=94.8 AI=- conf=- AI分=None 综合=94.8 delta=$3,134,816 wallets=4 q=72/100 高质=2 样本=2 horizon=3-14

## 本轮开仓/加仓信号

### 1. ETH OPEN_SHORT / Swing 94.8 / AI评分 None / 综合 94.8 / AI置信度 -

- 钱包数：4，分组：{'money_printer': 4}，事件：{'INCREASE_POSITION': 4}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$3,134,816，最大单钱包：$1,804,870
- 标记价：1756.85，均价：1750.5725，权重分：34.0222，净偏向分：34.0222
- AI独立评分：None，规则评分：94.8，综合开仓评分：94.8，评分来源：rule_fallback
- 信号状态：ACTIVE_REPEAT / 第28轮 / 持续22.0小时 / 冷却剩余7.0小时 / 金额变化0.18x
- 钱包质量：72/100 高质=2 样本=2，高质量钱包=2，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=799369.4181999998，oracle=1756.9，15m=0.074% ，1h=0.074% ，volRatio=0.406
- 中长期评分：94.8 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$3,134,816，6h=$3,134,816，24h=$63,860,483
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 7.2, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 4.61}
- 风险标签：direction_conflict, money_printer_confirmed, multi_round_accumulation, short_lower_wick_risk, swing_strong
- Top wallets：
  - 0x77375a8c9d13bf79afb2a87f1b0ac1dfd5f5bf66 money_printer INCREASE_POSITION $1,804,870 score=1.00 grade=NEW win72=- avg72=-
  - 0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00 money_printer INCREASE_POSITION $614,419 score=1.79 grade=S win72=- avg72=-
  - 0x645b2eeaa0a46df3c4211bebda1b2c7703e287b8 money_printer INCREASE_POSITION $547,677 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=4 amount=$2,166,974 score=35.3695 groups={'money_printer': 4}
- **BTC EXIT_LONG** wallets=4 amount=$1,876,974 score=26.0671 groups={'smart_money': 3, 'money_printer': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$1,440,673 score=18.5588 groups={'money_printer': 2}
- **SOL EXIT_SHORT** wallets=1 amount=$150,660 score=7.5344 groups={'money_printer': 1}
- **XRP EXIT_SHORT** wallets=1 amount=$165,526 score=6.015 groups={'smart_money': 1}
- **NEAR EXIT_LONG** wallets=1 amount=$288,832 score=5.4606 groups={'smart_money': 1}
- **ZEC EXIT_LONG** wallets=1 amount=$217,199 score=5.3369 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第33轮 amount=$2,061,774 prev=58 exit_ratio=- amount_ratio=0.30x age=390.1m cooldown_left=4.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第13轮 amount=$577,919 prev=70 exit_ratio=- amount_ratio=0.90x age=30.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** BTC LONG 第27轮 amount=$769,872 prev=69 exit_ratio=- amount_ratio=0.05x age=30.0m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** ZEC LONG 第-轮 amount=$217,199 prev=67 exit_ratio=0.5372 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** NEAR LONG 第-轮 amount=$288,832 prev=65 exit_ratio=0.8169 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：72 条，方向正确 40，方向错误 32，平均方向收益 0.30%，最好 7.44%，最差 -7.18%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.43605 | 7.44 | 7.31 | 8.64 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.43605 | 7.30 | 7.17 | 8.51 | -2.20 |
| 34 | JTO | LONG | 0.77639 | 0.72062 | -7.18 | -7.31 | 0.55 | -7.60 |
| 31 | NEAR | LONG | 2.05555 | 1.92555 | -6.32 | -6.45 | 1.11 | -7.50 |
| 45 | MON | LONG | 0.025817 | 0.024383 | -5.55 | -5.68 | 0.89 | -7.78 |
| 13 | GRAM | SHORT | 1.6858 | 1.59385 | 5.45 | 5.32 | 6.60 | -0.52 |
| 41 | HYPE | SHORT | 71.902 | 68.2435 | 5.09 | 4.96 | 5.90 | -0.38 |
| 8 | NEAR | SHORT | 2.0234 | 1.92555 | 4.84 | 4.71 | 6.03 | -2.72 |
| 47 | SOL | SHORT | 82.5535 | 78.6355 | 4.75 | 4.62 | 4.75 | -0.08 |
| 16 | HYPE | LONG | 71.6085 | 68.2435 | -4.70 | -4.83 | 1.59 | -5.51 |
| 28 | HYPE | SHORT | 71.49 | 68.2435 | 4.54 | 4.41 | 5.35 | -1.76 |
| 21 | ZEC | LONG | 463.135 | 482.665 | 4.22 | 4.09 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 482.665 | -4.22 | -4.35 | 1.19 | -10.16 |
| 44 | VVV | SHORT | 11.1805 | 10.71 | 4.21 | 4.08 | 5.94 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 78.6355 | -4.14 | -4.27 | 0.71 | -4.14 |
| 4 | HYPE | SHORT | 71.0475 | 68.2435 | 3.95 | 3.82 | 4.76 | -2.39 |
| 5 | SOL | SHORT | 81.6175 | 78.6355 | 3.65 | 3.52 | 3.65 | -1.23 |
| 11 | SOL | LONG | 81.4165 | 78.6355 | -3.42 | -3.55 | 1.48 | -3.42 |
| 7 | XRP | SHORT | 1.13285 | 1.09435 | 3.40 | 3.27 | 3.40 | 0.00 |
| 14 | kPEPE | LONG | 0.002705 | 0.00262 | -3.14 | -3.27 | 1.44 | -3.88 |
| 39 | XRP | SHORT | 1.12915 | 1.09435 | 3.08 | 2.95 | 3.08 | -0.20 |
| 24 | SOL | SHORT | 81.0475 | 78.6355 | 2.98 | 2.85 | 2.98 | -1.94 |
| 56 | LIT | SHORT | 2.50975 | 2.43605 | 2.94 | 2.81 | 4.20 | 0.00 |
| 33 | ZEC | SHORT | 469.59 | 482.665 | -2.78 | -2.91 | 0.00 | -8.65 |
| 49 | HYPE | LONG | 70.1565 | 68.2435 | -2.73 | -2.86 | 0.23 | -3.55 |
| 37 | ZEC | LONG | 495.815 | 482.665 | -2.65 | -2.78 | 2.90 | -3.76 |
| 42 | ETH | SHORT | 1803.55 | 1756.85 | 2.59 | 2.46 | 2.89 | -0.39 |
| 48 | BNB | SHORT | 584.295 | 569.62 | 2.51 | 2.38 | 2.72 | 0.00 |
| 46 | ETH | LONG | 1801.95 | 1756.85 | -2.50 | -2.63 | 0.48 | -2.81 |
| 59 | SOL | LONG | 80.5705 | 78.6355 | -2.40 | -2.53 | 0.03 | -2.40 |

</details>
