# 钱包合约信号报告

Time: **2026-07-07 17:30:32 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1245，本轮 warmup 钱包：1176，变动事件：1370
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：109
- 钱包胜率层：enabled=True，新记录=147，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 6，生命周期事件 9，冷却合并 6
- 信号状态：NEW=0，RE_ALERT=1，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=19，signals=44，avg_duration=182.1s，AI calls=34，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.74 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.74 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.71 | 1 | - | - | - | - |
| 0x00f8da...e7454b | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0xd487e2...934982 | money_printer | NEW | 1.70 | 1 | - | - | - | - |
| 0x3da0af...fefe82 | smart_money | NEW | 1.69 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.67 | 2 | - | - | - | - |
| 0x45ffe9...abff5f | smart_money | NEW | 1.66 | 2 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **SOL SHORT** [RE_ALERT / 第7轮 / 持续10.5小时 / 冷却剩余7.0小时 / 金额变化5.70x] swing=88.88 AI=- conf=- AI分=None 综合=88.88 delta=$2,315,768 wallets=5 q=33/100 高质=0 样本=3 horizon=3-14

## 本轮开仓/加仓信号

### 1. SOL OPEN_SHORT / Swing 88.88 / AI评分 None / 综合 88.88 / AI置信度 -

- 钱包数：5，分组：{'money_printer': 5}，事件：{'INCREASE_POSITION': 5}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$2,315,768，最大单钱包：$1,363,372
- 标记价：82.5535，均价：81.66606，权重分：35.2498，净偏向分：24.2718
- AI独立评分：None，规则评分：88.88，综合开仓评分：88.88，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第7轮 / 持续10.5小时 / 冷却剩余7.0小时 / 金额变化5.70x
- 钱包质量：33/100 高质=0 样本=3，高质量钱包=0，低质量钱包=2，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$961,617，冲突比=0.4152
- 市场：funding=1.25e-05，OI=5632215.06，oracle=82.565，15m=1.5983% ，1h=2.0156% ，volRatio=2.5244
- 中长期评分：88.88 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$2,315,768，6h=$3,463,656，24h=$4,332,935
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 3.34, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 2.53}
- 风险标签：cooldown_realert_large_add, direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong, volume_expansion
- Top wallets：
  - 0xb83de012dba672c76a7dbbbf3e459cb59d7d6e36 money_printer INCREASE_POSITION $1,363,372 score=1.00 grade=NEW win72=- avg72=-
  - 0x621c5551678189b9a6c94d929924c225ff1d63ab money_printer INCREASE_POSITION $485,878 score=0.54 grade=NEW win72=- avg72=-
  - 0x023a3d058020fb76cca98f01b3c48c8938a22355 money_printer INCREASE_POSITION $184,914 score=0.97 grade=B win72=- avg72=-

## 减仓/平仓风险信号

- **SOL EXIT_SHORT** wallets=4 amount=$1,296,449 score=25.1377 groups={'smart_money': 1, 'money_printer': 3}
- **BTC EXIT_SHORT** wallets=3 amount=$6,461,871 score=21.2041 groups={'money_printer': 1, 'smart_money': 2}
- **ZEC EXIT_SHORT** wallets=2 amount=$507,684 score=15.9898 groups={'money_printer': 2}
- **ZEC EXIT_LONG** wallets=1 amount=$2,516,450 score=8.6411 groups={'money_printer': 1}
- **ETH EXIT_SHORT** wallets=1 amount=$239,170 score=6.6803 groups={'money_printer': 1}
- **BTC EXIT_LONG** wallets=1 amount=$275,234 score=6.2481 groups={'smart_money': 1}
- **BLUR EXIT_SHORT** wallets=1 amount=$111,438 score=5.047 groups={'smart_money': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** BTC SHORT 第12轮 amount=$839,047 prev=26 exit_ratio=- amount_ratio=0.24x age=210.0m cooldown_left=6.5小时
- **COOLDOWN_MERGED** ETH SHORT 第8轮 amount=$518,811 prev=23 exit_ratio=- amount_ratio=0.36x age=240.1m cooldown_left=6.0小时
- **COOLDOWN_MERGED** NEAR LONG 第2轮 amount=$256,126 prev=31 exit_ratio=- amount_ratio=0.33x age=120.0m cooldown_left=5.0小时
- **COOLDOWN_MERGED** ZEC SHORT 第6轮 amount=$787,206 prev=19 exit_ratio=- amount_ratio=1.11x age=300.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL LONG 第3轮 amount=$961,617 prev=40 exit_ratio=- amount_ratio=1.17x age=90.1m cooldown_left=5.5小时
- **COOLDOWN_MERGED** ZEC LONG 第4轮 amount=$607,320 prev=21 exit_ratio=- amount_ratio=0.24x age=300.1m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC LONG 第4轮 amount=$2,516,450 prev=21 exit_ratio=4.7187 amount_ratio=0.24x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第6轮 amount=$507,684 prev=19 exit_ratio=0.7701 amount_ratio=1.11x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** SOL SHORT 第7轮 amount=$1,296,449 prev=24 exit_ratio=1.1294 amount_ratio=5.70x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：47 条，方向正确 25，方向错误 22，平均方向收益 -0.25%，最好 8.67%，最差 -8.67%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 503.29 | 8.67 | 8.54 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 503.29 | -8.67 | -8.80 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 503.29 | -7.18 | -7.31 | 0.00 | -8.65 |
| 34 | JTO | LONG | 0.77639 | 0.7506 | -3.32 | -3.45 | 0.55 | -3.32 |
| 27 | ETH | SHORT | 1767.25 | 1806.45 | -2.22 | -2.35 | 0.00 | -2.22 |
| 8 | NEAR | SHORT | 2.0234 | 2.0682 | -2.21 | -2.34 | 1.24 | -2.23 |
| 26 | BTC | SHORT | 62945.5 | 64143.5 | -1.90 | -2.03 | 0.00 | -1.90 |
| 24 | SOL | SHORT | 81.0475 | 82.5535 | -1.86 | -1.99 | 0.49 | -1.86 |
| 18 | LIT | SHORT | 2.63175 | 2.58305 | 1.85 | 1.72 | 3.01 | -2.05 |
| 23 | ETH | SHORT | 1773.75 | 1806.45 | -1.84 | -1.97 | 0.37 | -1.84 |
| 6 | LIT | SHORT | 2.6279 | 2.58305 | 1.71 | 1.58 | 4.57 | -2.20 |
| 1 | BTC | SHORT | 63136.5 | 64143.5 | -1.59 | -1.72 | 0.30 | -1.59 |
| 13 | GRAM | SHORT | 1.6858 | 1.6591 | 1.58 | 1.45 | 1.76 | -0.52 |
| 25 | BTC | LONG | 63172.5 | 64143.5 | 1.54 | 1.41 | 1.54 | -0.36 |
| 37 | ZEC | LONG | 495.815 | 503.29 | 1.51 | 1.38 | 2.90 | 0.00 |
| 17 | ETH | LONG | 1780.75 | 1806.45 | 1.44 | 1.31 | 1.44 | -0.76 |
| 3 | ETH | SHORT | 1781.15 | 1806.45 | -1.42 | -1.55 | 0.78 | -1.42 |
| 10 | BTC | SHORT | 63245.5 | 64143.5 | -1.42 | -1.55 | 0.47 | -1.42 |
| 11 | SOL | LONG | 81.4165 | 82.5535 | 1.40 | 1.27 | 1.40 | -0.94 |
| 12 | BTC | SHORT | 63271.5 | 64143.5 | -1.38 | -1.51 | 0.52 | -1.38 |
| 15 | BTC | SHORT | 63341.5 | 64143.5 | -1.27 | -1.40 | 0.63 | -1.27 |
| 5 | SOL | SHORT | 81.6175 | 82.5535 | -1.15 | -1.28 | 1.18 | -1.15 |
| 2 | BTC | SHORT | 63427.5 | 64143.5 | -1.13 | -1.26 | 0.76 | -1.13 |
| 14 | kPEPE | LONG | 0.002705 | 0.002735 | 1.11 | 0.98 | 1.11 | -1.37 |
| 22 | BTC | LONG | 63460.5 | 64143.5 | 1.08 | 0.95 | 1.08 | -0.81 |
| 9 | TAO | LONG | 213.63 | 215.66 | 0.95 | 0.82 | 1.58 | -0.60 |
| 30 | BTC | LONG | 63562.5 | 64143.5 | 0.91 | 0.78 | 0.91 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 64143.5 | -0.91 | -1.04 | 0.00 | -0.91 |
| 4 | HYPE | SHORT | 71.0475 | 71.6915 | -0.91 | -1.04 | 0.00 | -2.39 |
| 45 | MON | LONG | 0.025817 | 0.026046 | 0.89 | 0.76 | 0.89 | 0.00 |

</details>
