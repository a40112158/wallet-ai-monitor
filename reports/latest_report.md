# 钱包合约信号报告

Time: **2026-07-08 01:00:31 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1221，本轮 warmup 钱包：1200，变动事件：1342
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：131
- 钱包胜率层：enabled=True，新记录=93，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 5，冷却合并 4
- 信号状态：NEW=1，RE_ALERT=0，REPEAT=0，追踪状态=5
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=34，signals=59，avg_duration=197.5s，AI calls=44，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.10 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.10 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.09 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 2.08 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.99 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.84 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.82 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.78 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.78 | 1 | - | - | - | - |
| 0x4537e1...798732 | smart_money | NEW | 1.72 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 过滤/短线噪音

- UNI LONG [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=60.83：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. UNI OPEN_LONG / Swing 60.83 / AI评分 None / 综合 60.83 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'NEW_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$502,888，最大单钱包：$502,888
- 标记价：3.2692，均价：3.25548，权重分：5.7015，净偏向分：5.7015
- AI独立评分：None，规则评分：60.83，综合开仓评分：60.83，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：50/100 高质=0 样本=0，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=2.68022e-05，OI=3928587.4，oracle=3.2655，15m=2.2969% ，1h=2.2969% ，volRatio=5.9412
- 中长期评分：60.83 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$502,888，6h=$502,888，24h=$502,888
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 5.0, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 10.0}
- 风险标签：volume_expansion
- Top wallets：
  - 0x6f7f358df5a6a4b02178bdbfaae5ed4dc14b28ae smart_money NEW_POSITION $502,888 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=7 amount=$2,609,071 score=43.1887 groups={'smart_money': 3, 'money_printer': 4}
- **SOL EXIT_SHORT** wallets=5 amount=$1,136,572 score=30.5622 groups={'smart_money': 3, 'money_printer': 2}
- **BTC EXIT_LONG** wallets=2 amount=$592,851 score=13.0867 groups={'smart_money': 1, 'money_printer': 1}
- **SOL EXIT_LONG** wallets=1 amount=$285,767 score=8.4804 groups={'money_printer': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$153,961 score=7.003 groups={'money_printer': 1}
- **HYPE EXIT_SHORT** wallets=1 amount=$318,897 score=5.662 groups={'money_printer': 1}
- **PAXG EXIT_SHORT** wallets=1 amount=$287,615 score=5.4588 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** SOL LONG 第10轮 amount=$816,061 prev=59 exit_ratio=- amount_ratio=2.43x age=60.0m cooldown_left=6.0小时
- **COOLDOWN_MERGED** BTC SHORT 第27轮 amount=$1,414,386 prev=58 exit_ratio=- amount_ratio=0.16x age=150.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH SHORT 第22轮 amount=$306,752 prev=50 exit_ratio=- amount_ratio=0.05x age=360.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** BTC LONG 第20轮 amount=$2,543,820 prev=55 exit_ratio=- amount_ratio=2.14x age=209.9m cooldown_left=5.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第27轮 amount=$2,609,071 prev=58 exit_ratio=0.6 amount_ratio=0.16x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：62 条，方向正确 28，方向错误 34，平均方向收益 0.11%，最好 5.54%，最差 -5.26%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 18 | LIT | SHORT | 2.63175 | 2.4859 | 5.54 | 5.41 | 6.45 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.4859 | 5.40 | 5.27 | 6.31 | -2.20 |
| 21 | ZEC | LONG | 463.135 | 487.505 | 5.26 | 5.13 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 487.505 | -5.26 | -5.39 | 1.19 | -10.16 |
| 13 | GRAM | SHORT | 1.6858 | 1.61155 | 4.40 | 4.27 | 4.40 | -0.52 |
| 45 | MON | LONG | 0.025817 | 0.024733 | -4.20 | -4.33 | 0.89 | -7.78 |
| 33 | ZEC | SHORT | 469.59 | 487.505 | -3.82 | -3.95 | 0.00 | -8.65 |
| 34 | JTO | LONG | 0.77639 | 0.74877 | -3.56 | -3.69 | 0.55 | -6.78 |
| 41 | HYPE | SHORT | 71.902 | 69.4345 | 3.43 | 3.30 | 3.94 | -0.38 |
| 31 | NEAR | LONG | 2.05555 | 1.99085 | -3.15 | -3.28 | 1.11 | -3.78 |
| 16 | HYPE | LONG | 71.6085 | 69.4345 | -3.04 | -3.17 | 1.59 | -3.54 |
| 44 | VVV | SHORT | 11.1805 | 10.8455 | 3.00 | 2.87 | 5.94 | 0.00 |
| 28 | HYPE | SHORT | 71.49 | 69.4345 | 2.88 | 2.75 | 3.38 | -1.76 |
| 47 | SOL | SHORT | 82.5535 | 80.3485 | 2.67 | 2.54 | 2.67 | -0.08 |
| 4 | HYPE | SHORT | 71.0475 | 69.4345 | 2.27 | 2.14 | 2.78 | -2.39 |
| 40 | SOL | LONG | 82.0335 | 80.3485 | -2.05 | -2.18 | 0.71 | -2.05 |
| 7 | XRP | SHORT | 1.13285 | 1.11335 | 1.72 | 1.59 | 1.94 | 0.00 |
| 37 | ZEC | LONG | 495.815 | 487.505 | -1.68 | -1.81 | 2.90 | -3.70 |
| 8 | NEAR | SHORT | 2.0234 | 1.99085 | 1.61 | 1.48 | 2.25 | -2.72 |
| 5 | SOL | SHORT | 81.6175 | 80.3485 | 1.55 | 1.42 | 1.55 | -1.23 |
| 39 | XRP | SHORT | 1.12915 | 1.11335 | 1.40 | 1.27 | 1.62 | -0.20 |
| 11 | SOL | LONG | 81.4165 | 80.3485 | -1.31 | -1.44 | 1.48 | -1.31 |
| 42 | ETH | SHORT | 1803.55 | 1780.25 | 1.29 | 1.16 | 1.76 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1780.25 | -1.20 | -1.33 | 0.48 | -1.68 |
| 51 | ZEC | LONG | 493.435 | 487.505 | -1.20 | -1.33 | 0.83 | -3.24 |
| 14 | kPEPE | LONG | 0.002705 | 0.002674 | -1.15 | -1.28 | 1.44 | -1.52 |
| 26 | BTC | SHORT | 62945.5 | 63595.5 | -1.03 | -1.16 | 0.00 | -1.93 |
| 49 | HYPE | LONG | 70.1565 | 69.4345 | -1.03 | -1.16 | 0.23 | -1.55 |
| 48 | BNB | SHORT | 584.295 | 578.42 | 1.01 | 0.88 | 1.31 | 0.00 |
| 56 | LIT | SHORT | 2.50975 | 2.4859 | 0.95 | 0.82 | 1.90 | 0.00 |

</details>
