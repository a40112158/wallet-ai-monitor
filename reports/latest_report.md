# 钱包合约信号报告

Time: **2026-07-07 18:30:34 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1246，本轮 warmup 钱包：1175，变动事件：1378
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：112
- 钱包胜率层：enabled=True，新记录=132，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 5，生命周期事件 7，冷却合并 4
- 信号状态：NEW=1，RE_ALERT=0，REPEAT=0，追踪状态=5
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=0，观察候选=0

### 24h运行健康

- runs=21，signals=45，avg_duration=185.2s，AI calls=35，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.81 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.81 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.80 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.68 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.65 | 2 | - | - | - | - |
| 0x45ffe9...abff5f | smart_money | NEW | 1.64 | 2 | - | - | - | - |
| 0xb756c8...f80cdb | smart_money | NEW | 1.63 | 1 | - | - | - | - |
| 0x3da0af...fefe82 | smart_money | NEW | 1.63 | 1 | - | - | - | - |
| 0x50a4d3...0f8168 | smart_money | NEW | 1.63 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 过滤/短线噪音

- BNB SHORT [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=60.81：中长期条件不足，默认不作为主开单候选。

## 本轮开仓/加仓信号

### 1. BNB OPEN_SHORT / Swing 60.81 / AI评分 None / 综合 60.81 / AI置信度 -

- 钱包数：1，分组：{'smart_money': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：WEAK_OR_SHORT_TERM
- 新增/加仓名义金额：$344,229，最大单钱包：$344,229
- 标记价：584.295，均价：584.878，权重分：5.114，净偏向分：5.114
- AI独立评分：None，规则评分：60.81，综合开仓评分：60.81，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：40/100 高质=0 样本=1，高质量钱包=0，低质量钱包=1，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=45433.516，oracle=584.2，15m=0.1681% ，1h=0.5872% ，volRatio=1.2103
- 中长期评分：60.81 / 桶=WEAK_OR_SHORT_TERM / 周期=3-14天
- 钱包净流：2h=$344,229，6h=$344,229，24h=$344,229
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 3.98, 'multi_window_accumulation': 20.0, 'money_printer_weight': 0.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 10.0}
- Top wallets：
  - 0x5323b92268b4e140ac2133c677e991cd9ad1b23c smart_money INCREASE_POSITION $344,229 score=0.69 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=6 amount=$8,512,780 score=36.9883 groups={'money_printer': 5, 'smart_money': 1}
- **ETH EXIT_SHORT** wallets=2 amount=$866,289 score=13.4262 groups={'money_printer': 2}
- **SOL EXIT_SHORT** wallets=2 amount=$470,770 score=11.3242 groups={'smart_money': 1, 'money_printer': 1}
- **ZEC EXIT_SHORT** wallets=1 amount=$477,446 score=9.0542 groups={'money_printer': 1}
- **BTC EXIT_LONG** wallets=1 amount=$101,022 score=7.8962 groups={'money_printer': 1}
- **SOL EXIT_LONG** wallets=1 amount=$1,059,619 score=6.0251 groups={'smart_money': 1}
- **ETH EXIT_LONG** wallets=1 amount=$154,320 score=6.0237 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第14轮 amount=$3,705,236 prev=26 exit_ratio=- amount_ratio=3.52x age=270.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL SHORT 第9轮 amount=$733,723 prev=24 exit_ratio=- amount_ratio=0.33x age=300.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** ETH SHORT 第10轮 amount=$885,159 prev=23 exit_ratio=- amount_ratio=0.43x age=300.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** BTC LONG 第9轮 amount=$372,803 prev=20 exit_ratio=- amount_ratio=0.70x age=360.2m cooldown_left=5.0小时
- **ACTIVE_SIGNAL_DECAY** SOL LONG 第-轮 amount=$1,059,619 prev=40 exit_ratio=1.2917 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第-轮 amount=$477,446 prev=19 exit_ratio=0.7242 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第14轮 amount=$8,512,780 prev=26 exit_ratio=0.5548 amount_ratio=3.52x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：48 条，方向正确 25，方向错误 23，平均方向收益 -0.17%，最好 7.88%，最差 -7.88%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 499.65 | 7.88 | 7.75 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 499.65 | -7.88 | -8.01 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 499.65 | -6.40 | -6.53 | 0.00 | -8.65 |
| 34 | JTO | LONG | 0.77639 | 0.752815 | -3.04 | -3.17 | 0.55 | -3.32 |
| 18 | LIT | SHORT | 2.63175 | 2.56265 | 2.63 | 2.50 | 3.01 | -2.05 |
| 44 | VVV | SHORT | 11.1805 | 10.896 | 2.54 | 2.41 | 2.54 | 0.00 |
| 6 | LIT | SHORT | 2.6279 | 2.56265 | 2.48 | 2.35 | 4.57 | -2.20 |
| 27 | ETH | SHORT | 1767.25 | 1801.55 | -1.94 | -2.07 | 0.00 | -2.45 |
| 8 | NEAR | SHORT | 2.0234 | 2.05845 | -1.73 | -1.86 | 1.24 | -2.72 |
| 26 | BTC | SHORT | 62945.5 | 63998.5 | -1.67 | -1.80 | 0.00 | -1.93 |
| 23 | ETH | SHORT | 1773.75 | 1801.55 | -1.57 | -1.70 | 0.37 | -2.07 |
| 1 | BTC | SHORT | 63136.5 | 63998.5 | -1.37 | -1.50 | 0.30 | -1.62 |
| 13 | GRAM | SHORT | 1.6858 | 1.6637 | 1.31 | 1.18 | 1.76 | -0.52 |
| 25 | BTC | LONG | 63172.5 | 63998.5 | 1.31 | 1.18 | 1.56 | -0.36 |
| 24 | SOL | SHORT | 81.0475 | 82.0625 | -1.25 | -1.38 | 0.49 | -1.94 |
| 10 | BTC | SHORT | 63245.5 | 63998.5 | -1.19 | -1.32 | 0.47 | -1.45 |
| 17 | ETH | LONG | 1780.75 | 1801.55 | 1.17 | 1.04 | 1.67 | -0.76 |
| 12 | BTC | SHORT | 63271.5 | 63998.5 | -1.15 | -1.28 | 0.52 | -1.40 |
| 3 | ETH | SHORT | 1781.15 | 1801.55 | -1.15 | -1.28 | 0.78 | -1.65 |
| 15 | BTC | SHORT | 63341.5 | 63998.5 | -1.04 | -1.17 | 0.63 | -1.29 |
| 2 | BTC | SHORT | 63427.5 | 63998.5 | -0.90 | -1.03 | 0.76 | -1.15 |
| 22 | BTC | LONG | 63460.5 | 63998.5 | 0.85 | 0.72 | 1.10 | -0.81 |
| 11 | SOL | LONG | 81.4165 | 82.0625 | 0.79 | 0.66 | 1.48 | -0.94 |
| 9 | TAO | LONG | 213.63 | 215.325 | 0.79 | 0.66 | 1.58 | -0.60 |
| 37 | ZEC | LONG | 495.815 | 499.65 | 0.77 | 0.64 | 2.90 | 0.00 |
| 30 | BTC | LONG | 63562.5 | 63998.5 | 0.69 | 0.56 | 0.94 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 63998.5 | -0.69 | -0.82 | 0.00 | -0.94 |
| 41 | HYPE | SHORT | 71.902 | 71.4555 | 0.62 | 0.49 | 0.62 | -0.38 |
| 47 | SOL | SHORT | 82.5535 | 82.0625 | 0.59 | 0.46 | 0.59 | -0.08 |
| 7 | XRP | SHORT | 1.13285 | 1.12615 | 0.59 | 0.46 | 1.58 | 0.00 |

</details>
