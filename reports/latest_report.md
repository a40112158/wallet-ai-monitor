# 钱包合约信号报告

Time: **2026-07-08 08:00:38 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1216，本轮 warmup 钱包：1205，变动事件：1479
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：143
- 钱包胜率层：enabled=True，新记录=126，本轮评估=0，窗口=24,72,168h
- AI预算：mode=under_spending_expand，今日估算 0/33333 points，阈值倍率=0.55，AI阈值=$27,500
- 市场确认：K线币数 6，生命周期事件 4，冷却合并 3
- 信号状态：NEW=0，RE_ALERT=1，REPEAT=0，追踪状态=4
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=45，signals=63，avg_duration=211.6s，AI calls=50，AI estimated points=47505

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0x592838...54d5f9 | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.20 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 2.17 | 1 | - | - | - | - |
| 0x0b1ace...f27741 | smart_money | NEW | 2.14 | 1 | - | - | - | - |
| 0xa33a4a...081ff8 | money_printer | NEW | 2.14 | 1 | - | - | - | - |
| 0xf17de4...2adab2 | money_printer | NEW | 2.10 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 2.07 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 2.00 | 1 | - | - | - | - |
| 0x0873ca...1701df | smart_money | NEW | 1.96 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **ETH LONG** [RE_ALERT / 第10轮 / 持续21.5小时 / 冷却剩余7.0小时 / 金额变化25.14x] swing=87.89 AI=- conf=- AI分=None 综合=87.89 delta=$8,917,815 wallets=2 q=59/100 高质=1 样本=1 horizon=3-14

## 本轮开仓/加仓信号

### 1. ETH OPEN_LONG / Swing 87.89 / AI评分 None / 综合 87.89 / AI置信度 -

- 钱包数：2，分组：{'money_printer': 2}，事件：{'NEW_POSITION': 1, 'INCREASE_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$8,917,815，最大单钱包：$8,779,750
- 标记价：1755.95，均价：1751.46，权重分：17.2719，净偏向分：9.63
- AI独立评分：None，规则评分：87.89，综合开仓评分：87.89，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第10轮 / 持续21.5小时 / 冷却剩余7.0小时 / 金额变化25.14x
- 钱包质量：59/100 高质=1 样本=1，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$5,260,883，冲突比=0.5899
- 市场：funding=1.25e-05，OI=803099.4280000002，oracle=1756.1，15m=-0.0911% ，1h=-0.0911% ，volRatio=1.894
- 中长期评分：87.89 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$8,917,815，6h=$25,038,394，24h=$32,481,614
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.89, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x15a4f009bb324a3fb9e36137136b201e3fe0dfdb money_printer NEW_POSITION $8,779,750 score=1.00 grade=NEW win72=- avg72=-
  - 0xca4903c207a0df58bf37d4bc8bbc5210726f53c8 money_printer INCREASE_POSITION $138,065 score=1.55 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_LONG** wallets=5 amount=$4,866,732 score=34.8465 groups={'smart_money': 2, 'money_printer': 3}
- **BTC EXIT_SHORT** wallets=4 amount=$1,059,341 score=26.1516 groups={'smart_money': 2, 'money_printer': 2}
- **ETH EXIT_SHORT** wallets=2 amount=$1,801,903 score=18.2365 groups={'money_printer': 2}
- **ZEC EXIT_LONG** wallets=1 amount=$108,642 score=5.1882 groups={'smart_money': 1}
- **WLD EXIT_LONG** wallets=1 amount=$143,870 score=5.158 groups={'smart_money': 1}
- **JTO EXIT_LONG** wallets=1 amount=$108,418 score=5.0351 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第39轮 amount=$5,965,175 prev=74 exit_ratio=- amount_ratio=0.48x age=29.8m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH SHORT 第33轮 amount=$5,260,883 prev=72 exit_ratio=- amount_ratio=1.34x age=180.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** HYPE SHORT 第19轮 amount=$656,949 prev=70 exit_ratio=- amount_ratio=1.44x age=210.0m cooldown_left=3.5小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第33轮 amount=$1,801,903 prev=72 exit_ratio=0.5748 amount_ratio=1.34x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：75 条，方向正确 39，方向错误 36，平均方向收益 0.17%，最好 9.89%，最差 -18.13%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.63561 | -18.13 | -18.26 | 0.55 | -18.13 |
| 18 | LIT | SHORT | 2.63175 | 2.37155 | 9.89 | 9.76 | 9.89 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.37155 | 9.75 | 9.62 | 9.75 | -2.20 |
| 31 | NEAR | LONG | 2.05555 | 1.9036 | -7.39 | -7.52 | 1.11 | -7.50 |
| 45 | MON | LONG | 0.025817 | 0.024161 | -6.41 | -6.54 | 0.89 | -7.78 |
| 13 | GRAM | SHORT | 1.6858 | 1.5811 | 6.21 | 6.08 | 6.60 | -0.52 |
| 8 | NEAR | SHORT | 2.0234 | 1.9036 | 5.92 | 5.79 | 6.03 | -2.72 |
| 56 | LIT | SHORT | 2.50975 | 2.37155 | 5.51 | 5.38 | 5.51 | 0.00 |
| 47 | SOL | SHORT | 82.5535 | 78.2595 | 5.20 | 5.07 | 5.37 | -0.08 |
| 44 | VVV | SHORT | 11.1805 | 10.609 | 5.11 | 4.98 | 5.94 | 0.00 |
| 41 | HYPE | SHORT | 71.902 | 68.2535 | 5.07 | 4.94 | 5.90 | -0.38 |
| 16 | HYPE | LONG | 71.6085 | 68.2535 | -4.69 | -4.82 | 1.59 | -5.51 |
| 40 | SOL | LONG | 82.0335 | 78.2595 | -4.60 | -4.73 | 0.71 | -4.77 |
| 28 | HYPE | SHORT | 71.49 | 68.2535 | 4.53 | 4.40 | 5.35 | -1.76 |
| 5 | SOL | SHORT | 81.6175 | 78.2595 | 4.11 | 3.98 | 4.28 | -1.23 |
| 37 | ZEC | LONG | 495.815 | 475.98 | -4.00 | -4.13 | 2.90 | -4.00 |
| 4 | HYPE | SHORT | 71.0475 | 68.2535 | 3.93 | 3.80 | 4.76 | -2.39 |
| 11 | SOL | LONG | 81.4165 | 78.2595 | -3.88 | -4.01 | 1.48 | -4.05 |
| 51 | ZEC | LONG | 493.435 | 475.98 | -3.54 | -3.67 | 0.83 | -3.54 |
| 7 | XRP | SHORT | 1.13285 | 1.09295 | 3.52 | 3.39 | 3.96 | 0.00 |
| 24 | SOL | SHORT | 81.0475 | 78.2595 | 3.44 | 3.31 | 3.61 | -1.94 |
| 39 | XRP | SHORT | 1.12915 | 1.09295 | 3.21 | 3.08 | 3.65 | -0.20 |
| 14 | kPEPE | LONG | 0.002705 | 0.002623 | -3.03 | -3.16 | 1.44 | -4.07 |
| 48 | BNB | SHORT | 584.295 | 567.425 | 2.89 | 2.76 | 3.14 | 0.00 |
| 59 | SOL | LONG | 80.5705 | 78.2595 | -2.87 | -3.00 | 0.03 | -3.04 |
| 21 | ZEC | LONG | 463.135 | 475.98 | 2.77 | 2.64 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 475.98 | -2.77 | -2.90 | 1.19 | -10.16 |
| 49 | HYPE | LONG | 70.1565 | 68.2535 | -2.71 | -2.84 | 0.23 | -3.55 |
| 9 | TAO | LONG | 213.63 | 207.86 | -2.70 | -2.83 | 1.58 | -2.92 |
| 42 | ETH | SHORT | 1803.55 | 1755.95 | 2.64 | 2.51 | 2.99 | -0.39 |

</details>
