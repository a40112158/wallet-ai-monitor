# 钱包合约信号报告

Time: **2026-07-07 16:30:29 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1241，本轮 warmup 钱包：1180，变动事件：1600
- AI 输入信号：3，虚拟开仓：0，动态评分钱包：90
- 钱包胜率层：enabled=True，新记录=186，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 7，生命周期事件 10，冷却合并 4
- 信号状态：NEW=1，RE_ALERT=2，REPEAT=0，追踪状态=7
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=2，观察候选=1

### 24h运行健康

- runs=17，signals=39，avg_duration=177.2s，AI calls=32，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xbf732e...575d58 | money_printer | NEW | 2.20 | 1 | - | - | - | - |
| 0xb2f737...1baf9f | money_printer | NEW | 1.73 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 1.73 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.73 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 1.72 | 1 | - | - | - | - |
| 0x48ec00...a79faf | smart_money | NEW | 1.68 | 1 | - | - | - | - |
| 0x3da0af...fefe82 | smart_money | NEW | 1.66 | 1 | - | - | - | - |
| 0x50a4d3...0f8168 | smart_money | NEW | 1.66 | 1 | - | - | - | - |
| 0x335f45...d9b60e | money_printer | NEW | 1.65 | 2 | - | - | - | - |
| 0x45ffe9...abff5f | smart_money | NEW | 1.64 | 2 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池

### 开多强候选

- **BTC LONG** [RE_ALERT / 第7轮 / 持续4.0小时 / 冷却剩余7.0小时 / 金额变化1.79x] swing=87.06 AI=- conf=- AI分=None 综合=87.06 delta=$8,804,330 wallets=3 q=51/100 高质=0 样本=1 horizon=3-14

### 开空强候选

- **ETH SHORT** [RE_ALERT / 第6轮 / 持续9.5小时 / 冷却剩余7.0小时 / 金额变化0.91x] swing=91.92 AI=- conf=- AI分=None 综合=91.92 delta=$4,950,893 wallets=8 q=24/100 高质=0 样本=7 horizon=3-14

### 观察候选

- **VVV SHORT** [NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-] swing=67.31 bucket=WATCHLIST_CANDIDATE AI分=None 综合=67.31 delta=$333,277 q=45/100 高质=0 样本=1 risk=money_printer_confirmed,swing_watch,volume_expansion

## 本轮开仓/加仓信号

### 1. ETH OPEN_SHORT / Swing 91.92 / AI评分 None / 综合 91.92 / AI置信度 -

- 钱包数：8，分组：{'money_printer': 8}，事件：{'INCREASE_POSITION': 8}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$4,950,893，最大单钱包：$1,087,645
- 标记价：1803.55，均价：1741.0125，权重分：56.3564，净偏向分：35.1016
- AI独立评分：None，规则评分：91.92，综合开仓评分：91.92，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第6轮 / 持续9.5小时 / 冷却剩余7.0小时 / 金额变化0.91x
- 钱包质量：24/100 高质=0 样本=7，高质量钱包=0，低质量钱包=4，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$2,489,642，冲突比=0.5029
- 市场：funding=1.25e-05，OI=802447.9567999999，oracle=1803.1，15m=1.6027% ，1h=1.0099% ，volRatio=0.6299
- 中长期评分：91.92 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$10,413,582，6h=$18,233,346，24h=$20,052,847
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 2.42, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 6.5}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0xb8eb97eaed8367079894d2f1bed69bd220ec1dd5 money_printer INCREASE_POSITION $1,087,645 score=0.52 grade=NEW win72=- avg72=-
  - 0x7fdafde5cfb5465924316eced2d3715494c517d1 money_printer INCREASE_POSITION $1,062,512 score=0.78 grade=C win72=- avg72=-
  - 0x023a3d058020fb76cca98f01b3c48c8938a22355 money_printer INCREASE_POSITION $1,014,304 score=0.85 grade=C win72=- avg72=-

### 2. BTC OPEN_LONG / Swing 87.06 / AI评分 None / 综合 87.06 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 2, 'money_printer': 1}，事件：{'INCREASE_POSITION': 3}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$8,804,330，最大单钱包：$8,208,249
- 标记价：64028.5，均价：63245.8，权重分：20.3491，净偏向分：10.9131
- AI独立评分：None，规则评分：87.06，综合开仓评分：87.06，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第7轮 / 持续4.0小时 / 冷却剩余7.0小时 / 金额变化1.79x
- 钱包质量：51/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：MEDIUM，反向金额=$5,443,471，冲突比=0.6183
- 市场：funding=1.25e-05，OI=38285.717，oracle=64024.0，15m=1.3579% ，1h=0.7672% ，volRatio=0.4161
- 中长期评分：87.06 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$19,896,484，6h=$25,947,594，24h=$25,947,594
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.06, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 9.0, 'low_direction_conflict': 0.0}
- 风险标签：cooldown_realert_large_add, direction_conflict, money_printer_confirmed, multi_round_accumulation, swing_strong
- Top wallets：
  - 0x469e9a7f624b04c24f0e64edf8d8a277e6bf58a5 money_printer INCREASE_POSITION $8,208,249 score=1.00 grade=NEW win72=- avg72=-
  - 0x8f63c88fccae90c1f9eb8b447f830bce7b71dd74 smart_money INCREASE_POSITION $396,056 score=1.08 grade=NEW win72=- avg72=-
  - 0x00897e2d7168165b81558c3cd9257efb007f2410 smart_money INCREASE_POSITION $200,025 score=1.00 grade=NEW win72=- avg72=-

### 3. VVV OPEN_SHORT / Swing 67.31 / AI评分 None / 综合 67.31 / AI置信度 -

- 钱包数：1，分组：{'money_printer': 1}，事件：{'INCREASE_POSITION': 1}，中长期桶：WATCHLIST_CANDIDATE
- 新增/加仓名义金额：$333,277，最大单钱包：$333,277
- 标记价：11.1805，均价：11.0378，权重分：7.0279，净偏向分：7.0279
- AI独立评分：None，规则评分：67.31，综合开仓评分：67.31，评分来源：rule_fallback
- 信号状态：NEW_SIGNAL / 第1轮 / 持续刚刚 / 冷却剩余7.0小时 / 金额变化-
- 钱包质量：45/100 高质=0 样本=1，高质量钱包=0，低质量钱包=0，72h胜率=-，7d胜率=-
- 市场：funding=1.25e-05，OI=1835471.76，oracle=11.175，15m=2.0449% ，1h=1.2373% ，volRatio=3.8492
- 中长期评分：67.31 / 桶=WATCHLIST_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$333,277，6h=$333,277，24h=$333,277
- 评分拆解：{'wallet_resonance': 3.83, 'wallet_quality': 4.48, 'multi_window_accumulation': 20.0, 'money_printer_weight': 6.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 10.0}
- 风险标签：money_printer_confirmed, swing_watch, volume_expansion
- Top wallets：
  - 0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00 money_printer INCREASE_POSITION $333,277 score=0.77 grade=C win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=8 amount=$9,863,649 score=58.0531 groups={'money_printer': 7, 'smart_money': 1}
- **BTC EXIT_LONG** wallets=5 amount=$1,113,879 score=29.9672 groups={'smart_money': 5}
- **ETH EXIT_SHORT** wallets=3 amount=$5,135,819 score=19.56 groups={'money_printer': 2, 'smart_money': 1}
- **ZEC EXIT_SHORT** wallets=2 amount=$906,569 score=14.2264 groups={'smart_money': 1, 'money_printer': 1}
- **ZEC EXIT_LONG** wallets=2 amount=$930,533 score=13.0626 groups={'money_printer': 1, 'smart_money': 1}
- **ETH EXIT_LONG** wallets=2 amount=$352,535 score=12.3394 groups={'smart_money': 1, 'money_printer': 1}
- **HYPE EXIT_LONG** wallets=1 amount=$180,700 score=6.7041 groups={'money_printer': 1}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** SOL SHORT 第5轮 amount=$810,782 prev=24 exit_ratio=- amount_ratio=1.78x age=180.1m cooldown_left=6.5小时
- **COOLDOWN_MERGED** BTC SHORT 第10轮 amount=$5,443,471 prev=12 exit_ratio=- amount_ratio=9.25x age=389.7m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ZEC SHORT 第4轮 amount=$599,551 prev=19 exit_ratio=- amount_ratio=0.58x age=240.1m cooldown_left=7.0小时
- **COOLDOWN_MERGED** XRP SHORT 第3轮 amount=$427,194 prev=39 exit_ratio=- amount_ratio=0.74x age=30.0m cooldown_left=6.5小时
- **ACTIVE_SIGNAL_DECAY** ETH LONG 第-轮 amount=$352,535 prev=17 exit_ratio=1.1605 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** ZEC LONG 第-轮 amount=$930,533 prev=21 exit_ratio=1.7449 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第6轮 amount=$5,135,819 prev=23 exit_ratio=2.743 amount_ratio=0.91x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第7轮 amount=$1,113,879 prev=20 exit_ratio=0.9868 amount_ratio=1.79x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ZEC SHORT 第4轮 amount=$906,569 prev=19 exit_ratio=1.3752 amount_ratio=0.58x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第10轮 amount=$9,863,649 prev=12 exit_ratio=1.573 amount_ratio=9.25x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：44 条，方向正确 21，方向错误 23，平均方向收益 -0.24%，最好 10.16%，最差 -10.16%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 21 | ZEC | LONG | 463.135 | 510.2 | 10.16 | 10.03 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 510.2 | -10.16 | -10.29 | 1.19 | -10.16 |
| 33 | ZEC | SHORT | 469.59 | 510.2 | -8.65 | -8.78 | 0.00 | -8.65 |
| 37 | ZEC | LONG | 495.815 | 510.2 | 2.90 | 2.77 | 2.90 | 0.00 |
| 27 | ETH | SHORT | 1767.25 | 1803.55 | -2.05 | -2.18 | 0.00 | -2.05 |
| 8 | NEAR | SHORT | 2.0234 | 2.06195 | -1.91 | -2.04 | 1.24 | -2.23 |
| 18 | LIT | SHORT | 2.63175 | 2.5843 | 1.80 | 1.67 | 3.01 | -2.05 |
| 13 | GRAM | SHORT | 1.6858 | 1.65605 | 1.76 | 1.63 | 1.76 | -0.52 |
| 26 | BTC | SHORT | 62945.5 | 64028.5 | -1.72 | -1.85 | 0.00 | -1.72 |
| 23 | ETH | SHORT | 1773.75 | 1803.55 | -1.68 | -1.81 | 0.37 | -1.68 |
| 6 | LIT | SHORT | 2.6279 | 2.5843 | 1.66 | 1.53 | 4.57 | -2.20 |
| 4 | HYPE | SHORT | 71.0475 | 72.1745 | -1.59 | -1.72 | 0.00 | -2.39 |
| 24 | SOL | SHORT | 81.0475 | 82.278 | -1.52 | -1.65 | 0.49 | -1.52 |
| 1 | BTC | SHORT | 63136.5 | 64028.5 | -1.41 | -1.54 | 0.30 | -1.41 |
| 25 | BTC | LONG | 63172.5 | 64028.5 | 1.36 | 1.23 | 1.36 | -0.36 |
| 17 | ETH | LONG | 1780.75 | 1803.55 | 1.28 | 1.15 | 1.28 | -0.76 |
| 3 | ETH | SHORT | 1781.15 | 1803.55 | -1.26 | -1.39 | 0.78 | -1.26 |
| 10 | BTC | SHORT | 63245.5 | 64028.5 | -1.24 | -1.37 | 0.47 | -1.24 |
| 12 | BTC | SHORT | 63271.5 | 64028.5 | -1.20 | -1.33 | 0.52 | -1.20 |
| 15 | BTC | SHORT | 63341.5 | 64028.5 | -1.08 | -1.21 | 0.63 | -1.08 |
| 11 | SOL | LONG | 81.4165 | 82.278 | 1.06 | 0.93 | 1.06 | -0.94 |
| 9 | TAO | LONG | 213.63 | 215.885 | 1.06 | 0.93 | 1.58 | -0.60 |
| 28 | HYPE | SHORT | 71.49 | 72.1745 | -0.96 | -1.09 | 0.00 | -1.76 |
| 2 | BTC | SHORT | 63427.5 | 64028.5 | -0.95 | -1.08 | 0.76 | -0.95 |
| 22 | BTC | LONG | 63460.5 | 64028.5 | 0.90 | 0.77 | 0.90 | -0.81 |
| 14 | kPEPE | LONG | 0.002705 | 0.002728 | 0.85 | 0.72 | 0.85 | -1.37 |
| 5 | SOL | SHORT | 81.6175 | 82.278 | -0.81 | -0.94 | 1.18 | -0.81 |
| 16 | HYPE | LONG | 71.6085 | 72.1745 | 0.79 | 0.66 | 1.59 | -0.59 |
| 30 | BTC | LONG | 63562.5 | 64028.5 | 0.73 | 0.60 | 0.73 | 0.00 |
| 29 | BTC | SHORT | 63562.5 | 64028.5 | -0.73 | -0.86 | 0.00 | -0.73 |

</details>
