# Research Proposal

## Title / 标题

**Read, Seen, Ignored: A Signaling-Game Analysis of Reply Latency in Advisor Group Chats**  
**已读、不回、稍后回复：导师群聊响应延迟的信号博弈分析**

## Project Summary / 项目摘要

This project studies an ordinary but high-stakes academic phenomenon: the timing of replies in advisor group chats.  
本项目研究一个日常但高压的学术现象：导师群聊中的回复时机。

The core claim is that graduate students do not optimize for immediate response. Instead, they search for a narrow delay band that balances three incompatible goals:

1. appearing diligent  
2. remaining reliable  
3. minimizing the probability of attracting new work

核心主张是：研究生优化的并不是“秒回”，而是一段狭窄的延迟区间，用来同时平衡“显得勤奋”“保持可靠”“尽量少接新活”这三个互相冲突的目标。

## Why This Fits SHIT / 为什么这题适合 SHIT

- It begins from a recognizably painful real-life situation.  
  它来自一个很多人都立刻能懂的真实痛点。
- It can be formalized with ridiculous seriousness.  
  它非常适合被一本正经地形式化。
- It produces charts, matrices, and variables that look publishable.  
  它天然能长出“像论文”的图表和变量。
- It is funny because it is half true.  
  它的笑点来自“太像真的了”。

## Research Questions / 研究问题

1. Does perceived diligence increase monotonically with reply speed, or does it follow an inverse-U pattern?  
   感知勤奋度是否随着回复速度单调上升，还是呈倒 U 型？
2. How do hierarchy and message visibility reshape the acceptable delay window?  
   层级关系和群聊可见性如何重塑可接受的延迟窗口？
3. Can low-density emoji usage repair suspicion caused by delayed response?  
   低密度表情是否能修复延迟回复带来的怀疑？

## Hypotheses / 研究假设

### H1

Perceived diligence follows an inverse-U relation with latency. Extremely fast replies imply suspicious availability, while very late replies imply unreliability.  
感知勤奋度与延迟呈倒 U 型关系：过快显得“太闲”，过慢显得“不靠谱”。

### H2

Direct hierarchy compresses the optimal delay window. Messages from the principal advisor demand earlier response than messages from postdocs or peers.  
直接层级关系会压缩最优回复窗口：导师本人的消息比博士后或同门的消息要求更早。

### H3

Public visibility increases reputational penalty. When advisors and peers can all see the exchange, reply timing becomes more heavily interpreted as a signal of work ethic.  
公开可见性会提高声誉惩罚：当导师和同门都能看到对话时，回复时机会更强地被解读为工作态度信号。

### H4

Light emoji use can partially offset moderate delay for low-urgency messages, but fails under high-urgency or direct-task conditions.  
轻度表情使用可以部分抵消低紧急度消息中的中等延迟，但在高紧急度或直接任务情境下无效。

## Proposed Data Design / 数据设计

### Corpus / 语料

- 4,236 message-response dyads
- 28 simulated or reconstructed research groups
- 173 student-side respondents
- observation window: January 2024 to December 2025

### Unit of Analysis / 分析单位

One advisor-group-chat message and the first visible student response that follows it.  
一条群消息及其之后第一个对外可见的学生回复。

### Core Variables / 核心变量

- latency bucket
- sender hierarchy
- message urgency
- public visibility
- emoji density
- perceived diligence score
- task accretion risk
- reputational survivability index

## Method / 方法

### 1. Message Annotation

Each interaction is coded by message type:

- hard summons
- soft ping
- paper comments
- administrative reminder
- public praise trap
- deadline escalation

### 2. Delay Bucketing

Response time is grouped into:

- `<2 min`
- `2-7 min`
- `8-18 min`
- `19-47 min`
- `48-180 min`
- `>180 min`

### 3. Payoff Reconstruction

We model utility as:

`U(l) = alpha*D(l) + beta*R(l) - gamma*T(l) - delta*M(l)`

where:

- `D` = perceived diligence
- `R` = reliability
- `T` = task accretion risk
- `M` = moral suspicion for replying at the wrong speed

## Expected Results / 预期结果

- The most stable zone will sit between roughly 8 and 23 minutes for routine messages.  
  对常规消息而言，最稳定的窗口预计会落在 8 到 23 分钟之间。
- Messages from the principal advisor will shift the window earlier.  
  导师本人发出的消息会把窗口整体前移。
- Publicly visible “praise” messages will create the highest trap risk.  
  公开可见的“表扬型消息”会形成最高的陷阱风险。
- Fast replies will be rewarded in reliability but punished in task accretion.  
  快速回复会提升可靠性，但也会提高任务追加风险。

## Figure Plan / 图表计划

1. Inverse-U curve of latency and perceived diligence  
2. Hierarchy-based acceptable delay table  
3. Message-type risk matrix  
4. Payoff matrix for visibility and latency

## Deliverables / 交付物

- full manuscript
- figure source tables
- submission metadata
- shareable recap posts

## Safety / 安全边界

This paper is satirical but avoids:

- real political content
- dangerous instructions
- real-person targeting

本稿件保持讽刺性，但不触碰现实政治、危险指导或真实人物攻击。
