# 钱包合约信号报告

Time: **2026-07-07 22:00:30 UTC**

## 运行状态

- 钱包：总数 2421，本轮扫描 2421，offset=0，next=0
- 请求：成功 2421，失败 0（失败钱包保留旧基线）
- 基线钱包：1232，本轮 warmup 钱包：1189，变动事件：1708
- AI 输入信号：1，虚拟开仓：0，动态评分钱包：126
- 钱包胜率层：enabled=True，新记录=147，本轮评估=0，窗口=24,72,168h
- AI预算：mode=over_spending，今日估算 47897/33333 points，阈值倍率=1.35，AI阈值=$67,500
- 市场确认：K线币数 5，生命周期事件 11，冷却合并 5
- 信号状态：NEW=0，RE_ALERT=1，REPEAT=0，追踪状态=6
- 中长期模式：True，窗口=2,6,24,72,168h，强候选=1，观察候选=0

### 24h运行健康

- runs=28，signals=54，avg_duration=192.5s，AI calls=40，AI estimated points=47897

### 钱包分类/胜率

- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。

| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0xb2f737...1baf9f | money_printer | NEW | 2.17 | 1 | - | - | - | - |
| 0xbb8285...59e19f | smart_money | NEW | 2.17 | 1 | - | - | - | - |
| 0x592838...54d5f9 | smart_money | NEW | 2.16 | 1 | - | - | - | - |
| 0xbf732e...575d58 | money_printer | NEW | 1.99 | 1 | - | - | - | - |
| 0x35af6c...b31428 | smart_money | NEW | 1.87 | 1 | - | - | - | - |
| 0xfe7ce0...6ab7ae | money_printer | NEW | 1.85 | 1 | - | - | - | - |
| 0x16c952...e1a282 | smart_money | NEW | 1.81 | 1 | - | - | - | - |
| 0xfe72c2...5241ce | smart_money | NEW | 1.81 | 1 | - | - | - | - |
| 0xb83de0...7d6e36 | money_printer | NEW | 1.78 | 1 | - | - | - | - |
| 0xe86b05...723664 | money_printer | NEW | 1.78 | 1 | - | - | - | - |

## AI 状态

Error code: 401 - {'error': {'message': 'Incorrect API key provided. You can find your API key at https://poe.com/api/keys.', 'type': 'authentication_error', 'code': 'invalid_api_key'}}

## 中长期合约开单候选池


### 开空强候选

- **ETH SHORT** [RE_ALERT / 第16轮 / 持续15.0小时 / 冷却剩余7.0小时 / 金额变化1.86x] swing=97.21 AI=- conf=- AI分=None 综合=97.21 delta=$17,847,595 wallets=3 q=57/100 高质=1 样本=1 horizon=3-14

## 本轮开仓/加仓信号

### 1. ETH OPEN_SHORT / Swing 97.21 / AI评分 None / 综合 97.21 / AI置信度 -

- 钱包数：3，分组：{'smart_money': 1, 'money_printer': 2}，事件：{'INCREASE_POSITION': 2, 'NEW_POSITION': 1}，中长期桶：STRONG_CANDIDATE
- 新增/加仓名义金额：$17,847,595，最大单钱包：$17,445,296
- 标记价：1771.75，均价：1783.38333333，权重分：23.7307，净偏向分：23.1389
- AI独立评分：None，规则评分：97.21，综合开仓评分：97.21，评分来源：rule_fallback
- 信号状态：RE_ALERT / 第16轮 / 持续15.0小时 / 冷却剩余7.0小时 / 金额变化1.86x
- 钱包质量：57/100 高质=1 样本=1，高质量钱包=1，低质量钱包=0，72h胜率=-，7d胜率=-
- 多空冲突：LOW，反向金额=$593,453，冲突比=0.0333
- 市场：funding=1.25e-05，OI=794714.2696000001，oracle=1769.0，15m=-0.8899% ，1h=-0.8899% ，volRatio=0.9226
- 中长期评分：97.21 / 桶=STRONG_CANDIDATE / 周期=3-14天
- 钱包净流：2h=$17,847,595，6h=$45,623,713，24h=$60,725,667
- 评分拆解：{'wallet_resonance': 23.0, 'wallet_quality': 5.72, 'multi_window_accumulation': 25.0, 'money_printer_weight': 12.0, 'price_position_health': 13.0, 'oi_funding_health': 10.0, 'low_direction_conflict': 8.49}
- 风险标签：cooldown_realert_large_add, money_printer_confirmed, multi_round_accumulation, short_lower_wick_risk, swing_strong
- Top wallets：
  - 0xa6ee1ed1ae80b8352603654b39f5e7b9bedd5078 money_printer NEW_POSITION $17,445,296 score=1.61 grade=NEW win72=- avg72=-
  - 0xc30c7ea910a71ce06ae840868b0c7e47616ba4c9 money_printer INCREASE_POSITION $225,124 score=1.00 grade=NEW win72=- avg72=-
  - 0x51b97ab1e4381e22dd6cd04d6f67393964fe3bc1 smart_money INCREASE_POSITION $177,175 score=1.00 grade=NEW win72=- avg72=-

## 减仓/平仓风险信号

- **BTC EXIT_SHORT** wallets=12 amount=$9,963,005 score=90.2825 groups={'smart_money': 2, 'money_printer': 10}
- **ETH EXIT_SHORT** wallets=9 amount=$13,123,673 score=72.1837 groups={'smart_money': 1, 'money_printer': 8}
- **HYPE EXIT_LONG** wallets=6 amount=$7,514,756 score=34.4988 groups={'smart_money': 5, 'money_printer': 1}
- **HYPE EXIT_SHORT** wallets=4 amount=$2,335,926 score=25.8103 groups={'smart_money': 1, 'money_printer': 3}
- **LIT EXIT_SHORT** wallets=3 amount=$554,177 score=22.4147 groups={'money_printer': 3}
- **BTC EXIT_LONG** wallets=4 amount=$2,038,202 score=22.3075 groups={'smart_money': 4}
- **SOL EXIT_SHORT** wallets=2 amount=$599,344 score=15.9946 groups={'money_printer': 2}

## 信号生命周期/冷却

- **COOLDOWN_MERGED** HYPE LONG 第8轮 amount=$1,344,719 prev=49 exit_ratio=- amount_ratio=0.75x age=180.0m cooldown_left=7.0小时
- **COOLDOWN_MERGED** SOL LONG 第7轮 amount=$717,255 prev=40 exit_ratio=- amount_ratio=0.68x age=360.1m cooldown_left=1.0小时
- **COOLDOWN_MERGED** BTC SHORT 第21轮 amount=$2,904,708 prev=29 exit_ratio=- amount_ratio=0.53x age=419.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** BTC LONG 第15轮 amount=$1,809,302 prev=30 exit_ratio=- amount_ratio=0.13x age=419.9m cooldown_left=7.0小时
- **COOLDOWN_MERGED** ETH LONG 第5轮 amount=$593,453 prev=38 exit_ratio=- amount_ratio=1.09x age=360.1m cooldown_left=2.0小时
- **ACTIVE_SIGNAL_DECAY** LIT SHORT 第-轮 amount=$554,177 prev=56 exit_ratio=1.4052 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** BTC LONG 第15轮 amount=$2,038,202 prev=30 exit_ratio=0.6975 amount_ratio=0.13x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** ETH SHORT 第16轮 amount=$13,123,673 prev=36 exit_ratio=2.4024 amount_ratio=1.86x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** HYPE SHORT 第-轮 amount=$2,335,926 prev=41 exit_ratio=1.332 amount_ratio=- age=-m cooldown_left=-
- **ACTIVE_SIGNAL_DECAY** HYPE LONG 第8轮 amount=$7,514,756 prev=49 exit_ratio=4.91 amount_ratio=0.75x age=-m cooldown_left=7.0小时
- **ACTIVE_SIGNAL_DECAY** BTC SHORT 第21轮 amount=$9,963,005 prev=29 exit_ratio=0.6205 amount_ratio=0.53x age=-m cooldown_left=7.0小时

## 虚拟跟单账户（总本金模式）

> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。

- 模拟本金：$10,000.00，当前权益：$9,995.40，总PnL：$-4.60 （已实现 $-4.60 / 未实现 $0.00）
- 保证金占用：$0.00 / $10,000.00 （0.0%），名义仓位：$0.00，可用保证金：$10,000.00
- 仓位规则：最多 6 个未平仓，AI仓位=开，AI平仓=开，最低综合开仓分 0.0，最大杠杆 10.0x，单笔保证金上限 8.0%，总保证金上限 35.0%；不是每个仓位 $10,000
- 交易统计：总交易 1，未平 0，已平 1，胜 0，负 1，平仓胜率 0.0%，平均平仓收益 -0.92%

## 信号方向追踪（非模拟账户）

> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。

- 追踪信号：57 条，方向正确 26，方向错误 31，平均方向收益 0.12%，最好 6.21%，最差 -6.78%

<details>
<summary>展开查看最近/波动最大的信号方向追踪明细</summary>

| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 34 | JTO | LONG | 0.77639 | 0.72374 | -6.78 | -6.91 | 0.55 | -6.78 |
| 45 | MON | LONG | 0.025817 | 0.024184 | -6.33 | -6.46 | 0.89 | -7.78 |
| 18 | LIT | SHORT | 2.63175 | 2.46835 | 6.21 | 6.08 | 6.21 | -2.05 |
| 6 | LIT | SHORT | 2.6279 | 2.46835 | 6.07 | 5.94 | 6.07 | -2.20 |
| 44 | VVV | SHORT | 11.1805 | 10.5165 | 5.94 | 5.81 | 5.94 | 0.00 |
| 21 | ZEC | LONG | 463.135 | 483.505 | 4.40 | 4.27 | 10.16 | -1.19 |
| 19 | ZEC | SHORT | 463.135 | 483.505 | -4.40 | -4.53 | 1.19 | -10.16 |
| 41 | HYPE | SHORT | 71.902 | 69.1675 | 3.80 | 3.67 | 3.80 | -0.38 |
| 31 | NEAR | LONG | 2.05555 | 1.98305 | -3.53 | -3.66 | 1.11 | -3.53 |
| 16 | HYPE | LONG | 71.6085 | 69.1675 | -3.41 | -3.54 | 1.59 | -3.41 |
| 28 | HYPE | SHORT | 71.49 | 69.1675 | 3.25 | 3.12 | 3.25 | -1.76 |
| 13 | GRAM | SHORT | 1.6858 | 1.63515 | 3.00 | 2.87 | 3.17 | -0.52 |
| 33 | ZEC | SHORT | 469.59 | 483.505 | -2.96 | -3.09 | 0.00 | -8.65 |
| 4 | HYPE | SHORT | 71.0475 | 69.1675 | 2.65 | 2.52 | 2.65 | -2.39 |
| 37 | ZEC | LONG | 495.815 | 483.505 | -2.48 | -2.61 | 2.90 | -2.48 |
| 47 | SOL | SHORT | 82.5535 | 80.6815 | 2.27 | 2.14 | 2.27 | -0.08 |
| 51 | ZEC | LONG | 493.435 | 483.505 | -2.01 | -2.14 | 0.83 | -2.01 |
| 8 | NEAR | SHORT | 2.0234 | 1.98305 | 1.99 | 1.86 | 1.99 | -2.72 |
| 7 | XRP | SHORT | 1.13285 | 1.11085 | 1.94 | 1.81 | 1.94 | 0.00 |
| 42 | ETH | SHORT | 1803.55 | 1771.75 | 1.76 | 1.63 | 1.76 | -0.39 |
| 46 | ETH | LONG | 1801.95 | 1771.75 | -1.68 | -1.81 | 0.48 | -1.68 |
| 56 | LIT | SHORT | 2.50975 | 2.46835 | 1.65 | 1.52 | 1.65 | 0.00 |
| 40 | SOL | LONG | 82.0335 | 80.6815 | -1.65 | -1.78 | 0.71 | -1.65 |
| 39 | XRP | SHORT | 1.12915 | 1.11085 | 1.62 | 1.49 | 1.62 | -0.20 |
| 14 | kPEPE | LONG | 0.002705 | 0.002664 | -1.52 | -1.65 | 1.44 | -1.52 |
| 49 | HYPE | LONG | 70.1565 | 69.1675 | -1.41 | -1.54 | 0.23 | -1.41 |
| 38 | ETH | LONG | 1797.05 | 1771.75 | -1.41 | -1.54 | 0.75 | -1.41 |
| 36 | ETH | SHORT | 1797.05 | 1771.75 | 1.41 | 1.28 | 1.41 | -0.75 |
| 5 | SOL | SHORT | 81.6175 | 80.6815 | 1.15 | 1.02 | 1.18 | -1.23 |
| 48 | BNB | SHORT | 584.295 | 577.655 | 1.14 | 1.01 | 1.14 | 0.00 |

</details>
