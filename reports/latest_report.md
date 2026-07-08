# 钱包合约信号报告

Time: **2026-07-08 09:01:13 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1214，本轮 warmup 钱包：1207，变动事件：1884
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：146
- 钱包胜率层：enabled=True，新记录=264，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 7，冷却合并 6
- 信号状态：NEW=1，RE_ALERT=0，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=1

### 24h运行健康

- runs=47，signals=67，avg_duration=211.8s，AI calls=52，AI estimated points=47505

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.19 | 1 | - | - | - | - |
| 0xf17de4...2adab2 | money_printer | NEW | 2.19 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 2.08 | 1 | - | - | - | - |
| 0x4ef1c5...a528e3 | smart_money | NEW | 2.08 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 观察候选

- **PUMP LONG** [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=72.75 bucket=WATCHLIST_CANDIDATE AI分=None 综合=72.75 delta=$478,780 q=61/100 高质=1 样本=1 risk=money_printer_confirmed,swing_watch,volume_expansion

## 本轮开仓/加仓信号

### 1. PUMP OPEN_LONG / Swing 72.75 / AI评分 None / 综合 72.75 / AI置信度 -

- 钱包数：2，分组：{'smart_money': 1, 'money_printer': 1}，事件：{'INCREASE_POSITION': 2}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$478,780，最大单钱包：$359,651
- 标记价：0.001471，均价：0.0015085，权重分：13.6528，净偏向分：13.6528
- AI独立评分：None，规则评分：72.75，综合开仓评分：72.75，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：61/100 高质=1 样本=1，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=-3.27494e-05，OI=28152960218.0，oracle=0.001473，15m=-4.0962% ，1h=-4.0962% ，volRatio=23.393
- 中长期评分：72.75 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$478,780，6h=$478,780，24h=$478,780
- 评分拆解：{'wallet_resonance': 7.67, 'wallet_quality': 6.09, 'multi_window_accumulation': 20.0, 'money_printer_weight': 6.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 10.0}
- 风险标签：money_printer_confirmed, swing_watch, volume_expansion
- Top wallets：
  - 0x2a72b57dea119cc0bac14df798f9e9b8b148267c smart_money INCREASE_POSITION $359,651 score=1.00 grade=NEW win72=- avg72=-
  - 0xd4c1f7e8d876c4749228d515473d36f919583d1d money_printer INCREASE_POSITION $119,129 score=1.73 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=8 amount=$7,634,236 score=48.4689 groups={'smart_money': 4, 'money_printer': 4}
- **BTC EXIT_SHORT** wallets=5 amount=$739,194 score=36.6843 groups={'smart_money': 2, 'money_printer': 3}
- **ETH EXIT_SHORT** wallets=4 amount=$780,710 score=27.3763 groups={'smart_money': 2, 'money_printer': 2}
- **PUMP EXIT_SHORT** wallets=2 amount=$320,594 score=16.2756 groups={'money_printer': 2}
- **HYPE EXIT_LONG** wallets=1 amount=$424,996 score=8.5527 groups={'money_printer': 1}
- **LIT EXIT_SHORT** wallets=1 amount=$201,972 score=8.2678 groups={'money_printer': 1}
- **SOL EXIT_LONG** wallets=1 amount=$208,771 score=7.8174 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第41轮 amount=$10,602,253 prev=74 exit_ratio=- amount_ratio=3.07x age=90.4m cooldown_left=6.5小时
- **COOLDOWN_MERGED** HYPE SHORT 第21轮 amount=$1,084,042 prev=70 exit_ratio=- amount_ratio=0.44x age=270.6m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH SHORT 第35轮 amount=$5,769,233 prev=72 exit_ratio=- amount_ratio=1.38x age=240.6m cooldown_left=6.5小时
- **COOLDOWN_MERGED** SOL SHORT 第19轮 amount=$2,874,150 prev=73 exit_ratio=- amount_ratio=6.80x age=180.6m cooldown_left=4.5小时
- **COOLDOWN_MERGED** BTC LONG 第33轮 amount=$9,855,654 prev=69 exit_ratio=- amount_ratio=0.69x age=270.6m cooldown_left=4.5小时
- **COOLDOWN_MERGED** SOL LONG 第18轮 amount=$4,241,117 prev=77 exit_ratio=- amount_ratio=1.63x age=30.6m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第-轮 amount=$424,996 prev=66 exit_ratio=0.5914 amount_ratio=- age=-m cooldown_left=-

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：79 条，方向正确 41，方向错误 38，平均方向收益 0.11%，最好 10.70%，最差 -21.12%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.61244 | -21.12 | -21.25 | 0.55 | -21.12 |
| 18 | LIT | SHORT | 2.63175 | 2.3501 | 10.70 | 10.57 | 10.70 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.3501 | 10.57 | 10.44 | 10.57 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.87795 | -8.64 | -8.77 | 1.11 | -8.64 |
| 45 | MON | LONG | 0.025817 | 0.023642 | -8.42 | -8.55 | 0.89 | -8.42 |
| 13 | GRAM | SHORT | 1.6858 | 1.56185 | 7.35 | 7.22 | 7.35 | -0.52 |
| 8 | NEAR | SHORT | 2.0234 | 1.87795 | 7.19 | 7.06 | 7.19 | -2.72 |
| 44 | VVV | SHORT | 11.1805 | 10.4115 | 6.88 | 6.75 | 6.88 | 0.00 |
| 47 | SOL | SHORT | 82.5535 | 77.2735 | 6.40 | 6.27 | 6.49 | -0.08 |
| 56 | LIT | SHORT | 2.50975 | 2.3501 | 6.36 | 6.23 | 6.36 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 77.2735 | -5.80 | -5.93 | 0.71 | -5.89 |
| 41 | HYPE | SHORT | 71.902 | 68.008 | 5.42 | 5.29 | 5.90 | -0.38 |
| 5 | SOL | SHORT | 81.6175 | 77.2735 | 5.32 | 5.19 | 5.41 | -1.23 |
| 11 | SOL | LONG | 81.4165 | 77.2735 | -5.09 | -5.22 | 1.48 | -5.18 |
| 16 | HYPE | LONG | 71.6085 | 68.008 | -5.03 | -5.16 | 1.59 | -5.51 |
| 37 | ZEC | LONG | 495.815 | 470.99 | -5.01 | -5.14 | 2.90 | -5.24 |
| 14 | kPEPE | LONG | 0.002705 | 0.00257 | -4.99 | -5.12 | 1.44 | -4.99 |
| 28 | HYPE | SHORT | 71.49 | 68.008 | 4.87 | 4.74 | 5.35 | -1.76 |
| 7 | XRP | SHORT | 1.13285 | 1.07895 | 4.76 | 4.63 | 4.76 | 0.00 |
| 24 | SOL | SHORT | 81.0475 | 77.2735 | 4.66 | 4.53 | 4.75 | -1.94 |
| 68 | LDO | LONG | 0.32029 | 0.30545 | -4.63 | -4.76 | 2.37 | -4.63 |
| 51 | ZEC | LONG | 493.435 | 470.99 | -4.55 | -4.68 | 0.83 | -4.78 |
| 39 | XRP | SHORT | 1.12915 | 1.07895 | 4.45 | 4.32 | 4.45 | -0.20 |
| 4 | HYPE | SHORT | 71.0475 | 68.008 | 4.28 | 4.15 | 4.76 | -2.39 |
| 9 | TAO | LONG | 213.63 | 204.785 | -4.14 | -4.27 | 1.58 | -4.14 |
| 59 | SOL | LONG | 80.5705 | 77.2735 | -4.09 | -4.22 | 0.03 | -4.18 |
| 48 | BNB | SHORT | 584.295 | 561.29 | 3.94 | 3.81 | 3.94 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1735.95 | 3.75 | 3.62 | 3.96 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1735.95 | -3.66 | -3.79 | 0.48 | -3.88 |
| 38 | ETH | LONG | 1797.05 | 1735.95 | -3.40 | -3.53 | 0.75 | -3.62 |

</details>
