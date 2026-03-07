# Read, Seen, Ignored: A Signaling-Game Analysis of Reply Latency in Advisor Group Chats

**Internal Editorial Note / 内部编辑说明**  
This bilingual file is the internal synthesis draft. The canonical submission manuscripts are `read-seen-ignored_submission_en.md` and `read-seen-ignored_submission_zh.md`.  
本双语文件是内部整合工作稿。正式投稿主稿以 `read-seen-ignored_submission_en.md` 和 `read-seen-ignored_submission_zh.md` 为准。

**已读、不回、稍后回复：导师群聊响应延迟的信号博弈分析**

**Author / 作者**  
Cangsheng / 沧生  
VIBE SHITTING Lab for Reputational Studies

**Keywords / 关键词**  
advisor group chats; signaling; chronemics; communication visibility; volunteer's dilemma; expectation states; graduate student life  
导师群聊；信号理论；时序线索；沟通可见性；志愿者困境；期望状态；研究生生活

## Abstract

This paper examines reply latency in advisor group chats as a hybrid signaling game, chronemic cue, and multi-person volunteer's dilemma. We argue that graduate students do not optimize for immediate response, but for a narrow band of delay that simultaneously conveys diligence, preserves reliability, limits assignment hazard, and remains legible to a heterogeneous audience. Drawing on signaling theory, reputation models, computer-mediated communication, communication visibility, expectation states, and volunteer's-dilemma logic, we analyze 4,236 message-response dyads across 28 reconstructed research groups. The findings show an inverse-U relation between latency and perceived diligence: replies that are too fast imply suspicious idleness, while replies that are too slow imply neglect or collapse. Group size shifts the waiting game rightward until task ownership becomes salient, at which point diffusion of responsibility rapidly collapses. First visible replies alter the payoff structure for everyone else, producing a first-responder discount. Role heterogeneity matters: first-author juniors and procurement stewards face earlier optimal windows than generic bystanders, while peer-only lurkers can delay more safely when advisor visibility is absent. Holiday periods shift tolerance later, but never enough to protect the already marked. Light emoji use partially repairs moderate delay for low-urgency messages but fails under high hierarchy or urgent summons. We conclude that advisor-group-chat latency is not mere etiquette but a small technology of reputational labor under public asymmetry.

## 中文摘要

本文将导师群聊中的回复时延理解为一种混合性的“信号博弈 + 时序线索 + 多人志愿者困境”。本文认为，研究生优化的并不是“越快越好”的响应速度，而是一段狭窄的延迟区间，用来同时传达勤奋、维持可靠、控制任务追加风险，并让异质性的观察者都能读懂自己的“忙碌合法性”。本文结合信号理论、声誉模型、计算机媒介沟通、沟通可见性、期望状态理论与志愿者困境逻辑，对 28 个重建研究群中的 4,236 个“消息-回复”对进行分析。结果表明，回复延迟与感知勤奋度之间存在明显的倒 U 型关系：过快回复意味着可疑的空闲，过慢回复则意味着疏忽、崩溃或软性失联。群聊人数越多，最初的等待博弈越容易右移，但一旦任务归属变得清晰，责任扩散会迅速崩塌。第一个可见回复会改变其他所有人的收益结构，形成“首回复折扣”。角色异质性同样重要：一作学弟和负责采购报销的学长，比普通围观者面临更早的最优窗口；而在导师不可见的纯同辈场景中，“浑水的鱼”则拥有更大的拖延安全带。假期会整体放宽时延容忍度，但永远不足以保护那些已经被点名的人。低强度表情只能在低紧急度消息中部分修复中度延迟，在强层级或高紧急度情境下几乎无效。本文据此认为，导师群聊中的回复时延并非简单礼仪，而是在公开不对称关系中进行声誉劳动的一项微型技术。

## 1. Introduction

Academic group chats are frequently described as logistical tools. In practice, they operate as compact theaters of hierarchy, diligence, and moral visibility. A single message from an advisor does not merely request information; it opens a scene in which all observers may infer who is attentive, who is overloaded, who is avoiding work, and who is dangerously available for further assignment. Under such conditions, reply timing becomes consequential.

Common advice within student communities recommends responsiveness. Yet extreme responsiveness carries its own penalty. A reply that arrives within seconds may successfully signal reliability, but it may also imply a troubling surplus of attention. In many laboratories, the student who is always online is rewarded not merely with trust, but with additional labor. Conversely, excessive delay can be interpreted as negligence, indifference, or collapse. Students therefore face a narrow strategic problem: how to answer quickly enough to remain legible as responsible, but slowly enough to avoid advertising unclaimed capacity.

This paper proposes that reply latency in advisor group chats should be analyzed not as a trivial matter of etiquette, but as a signaling problem embedded in a multi-actor coordination game. The student does not simply transmit information. The student performs an equilibrium between obedience, competence, self-protection, and survivable ambiguity. The group chat is not only a communication channel; it is a public arena in which timestamps become evidence.

The contribution of this paper is fourfold. First, it deepens the theoretical base for studying reply delay by combining signaling theory with chronemics in computer-mediated communication. Second, it models advisor group chats as visible multi-person settings in which group size and reply order shape incentives. Third, it introduces heterogeneous role structures, including first-author juniors, procurement stewards, postdoc proxies, and peer-only bystanders, to show that reply latency is not judged symmetrically. Fourth, it retains the comic realism of graduate life by treating laboratory politics as analytically meaningful rather than merely anecdotal.

## 2. Literature Review and Theoretical Framework

### 2.1 Signaling Under Repeated Asymmetry

Signaling theory explains how observable actions communicate hidden states under incomplete information. In classic form, a costly or difficult-to-fake signal allows observers to infer qualities they cannot directly inspect (Spence, 1973). In repeated settings, small observable choices can accumulate into durable reputations, because today’s act is interpreted in light of tomorrow’s interaction and yesterday’s memory (Kreps & Wilson, 1982).

Advisor group chats present exactly this structure. Supervisors cannot directly observe whether a student is productively coding, physically in transit, quietly panicking, or staring at the message while composing a more respectable version of “收到老师”. What they can observe is whether the student replies, how fast, and in what tone. Latency therefore functions as a low-cost but continuously available signal of diligence, deference, availability, and emotional intactness. Unlike job-market signaling, however, this signal is not deployed once. It is repeated dozens or hundreds of times before the same audience.

The implication is that reply delay cannot be reduced to communication speed. It is better understood as reputational calibration under chronic asymmetry. Students do not simply signal competence. They signal a carefully mixed bundle: “I am responsible, I am not ignoring you, and I am hopefully not so free that you should give me three more tasks.”

### 2.2 Chronemics and Social Information in Computer-Mediated Communication

Research on computer-mediated communication shows that when face-to-face cues are reduced, users rely more heavily on text, timing, and contextual traces to infer social meaning (Walther, 1992; Walther, 1996). Chronemics, or the communication of meaning through time, is therefore central rather than peripheral in online interaction. Response delay is not merely the absence of content; it is itself content in temporal form.

Walther and Tidwell (1995) argue that relational cues survive in lean media by migrating into alternative channels such as timing and message management. Tidwell and Walther (2002) similarly show that people build impressions gradually through small mediated disclosures, even when interaction is text-heavy and asynchronous. More directly, Kalman et al. (2013) demonstrate that online chronemics convey social information, while Ziano and Wang (2021) show that response delays in email shape how senders are perceived. These lines of work imply that a timestamp in a chat window is already a socioemotional cue.

For academic group chats, the consequence is sharp. A six-minute delay can be read as “currently working but attentive,” a forty-minute delay as “occupied or strategically hiding,” and a three-second delay as “alarmingly available.” The same text, sent at a different time, becomes a different self.

### 2.3 Communication Visibility and the Public Audience Problem

Advisor group chats are not dyadic spaces. They are partially public environments in which supervisors, postdocs, senior students, and junior students all see not only messages, but the order and timing of response. Leonardi’s (2014) account of communication visibility is helpful here: digital systems make previously hidden interaction traces more observable, allowing third parties to infer who knows what, who is connected to whom, and who acts first.

This matters because the student in a group chat does not reply to a single superior. The student replies before a composite audience. A peer-originated question becomes quasi-supervisory when the advisor is visibly present. A direct request from the advisor becomes a public exam when ten other people watch in silence. The timestamp becomes a public micro-performance whose meaning is amplified by audience composition.

This also explains why the same student may reply differently in a private chat, a small working group, and a lab-wide announcement channel. Visibility changes the interpretive stakes. In visible settings, delay is not only judged by the sender, but co-read by everyone else as evidence of character, reliability, and room for future extraction.

### 2.4 Status Heterogeneity and Expectation States

Expectation states theory suggests that status structures shape who is expected to speak, defer, take initiative, or bear responsibility in group settings (Berger, Cohen, & Zelditch, 1972). In laboratories, such expectations do not map only onto formal titles. They attach to practical roles: the senior student who runs instruments, the postdoc proxy who relays advisor intent, the first-author junior whose draft is under discussion, the lab manager who controls schedules, and the unfortunate soul who handles procurement and reimbursement.

The consequence is asymmetry in latency interpretation. The same fifteen-minute delay means something different when produced by a postdoc, a first-year student, or the person already known to “own” the task. Once ownership is salient, hiding in group size becomes difficult. The first-author junior who delays on paper comments is read differently from an uninvolved bystander delaying on a lab-wide reminder. Status and role ownership therefore reshape the response curve, not merely its moral rhetoric.

In comic terms, the laboratory contains constitutional offices. The procurement senior occupies a strange position of low authorship prestige but high invoice sovereignty. The first-author junior occupies the inverse office: high obligation, low veto power. These are jokes, but not only jokes.

### 2.5 Volunteer's Dilemma and Reply Order in Multi-Person Chat

If one person’s visible reply can satisfy the audience’s immediate demand, then advisor group chats resemble a volunteer’s dilemma. In such settings, everyone benefits if someone responds, but each actor may prefer that another person incur the cost first (Diekmann, 1985; Diekmann, 1993). Classic work on diffusion of responsibility makes a similar point: as the number of potential responders grows, each individual can more easily wait and see whether someone else moves first (Darley & Latané, 1968).

This logic is highly legible in graduate group chats. When an advisor asks, “Who can update the figure by tonight?”, silence does not mean the group failed to understand. It may mean each member is rationally calculating whether another body will volunteer first. Group size can therefore widen the initial waiting window. Yet the effect is not unlimited. When task ownership is obvious, diffusion collapses. If the message concerns the reimbursement form, everyone knows the procurement senior cannot hide forever. If the message concerns a manuscript revision, the first-author junior becomes the default volunteer whether or not they chose the office.

Reply order also matters because the first visible response changes the game for everyone else. Once someone has replied credibly, later responses no longer earn the same diligence premium. We call this the **first-responder discount**: after a sufficiently legible first answer appears, the marginal reputational benefit of joining late declines, while the risk of attracting extra labor may remain.

### 2.6 A Vernacular Extension: Lab Politics, MBTI Talk, and Holiday Fog

Current Chinese platform discourse often translates group behavior into comic folk types rather than formal organizational theory. On Weibo and Xiaohongshu, MBTI functions less as validated psychology than as a social shorthand for interpreting coworkers, friends, and team scenes. We therefore treat MBTI-style labels not as scientific variables, but as vernacular descriptors that help render strategic heterogeneity visible. The “J-like duty keeper,” the “P-like muddy-water fish,” and the “I-read-it-but-opened-another-tab” type are folk sociologies, not instruments.

This vernacular matters because it captures how participants themselves narrate laboratory politics. In one recurrent scene, the senior responsible for procurement controls invoices, reagent orders, and reimbursement rituals, and therefore cannot disappear at the same speed as an uninvolved peer. In another, the first-author junior carries public manuscript responsibility while enjoying almost no real veto. A third figure is the muddy-water fish, whose method is to wait for a more status-legible organism to type “收到老师” first.

Holiday periods add a further layer of comic realism. Post-holiday discourse regularly describes people as cognitively slower, emotionally softer, and less ready to resume institutional performance. In laboratory settings, this produces what we call **holiday fog**: the felt wish to say, “Advisor, I am somehow dumber than the vacation itself; do you still want to meet?” The paper does not treat this as a clinical measure. It treats it as a socially intelligible condition that shifts acceptable delay slightly to the right without suspending hierarchy.

## 3. Research Design

### 3.1 Corpus Construction

The study analyzes 4,236 message-response dyads reconstructed from 28 advisor-linked research groups across the period January 2024 to December 2025. Group size ranges from 4 to 17 visible members. The corpus includes 173 student-side actors distributed across seniority levels and task ownership roles. The unit of analysis is a visible incoming message and the first visible student response that follows it.

The dataset is intentionally synthetic, but it is built to preserve the emotional realism of the interaction environment. We treat the corpus not as a literal archive of every laboratory, but as a stylized model of norm perception. This is appropriate because the paper asks not what students objectively do in all cases, but what latency patterns become intelligible as diligence, negligence, strategic patience, or hazardous availability.

### 3.2 Group Structure and Core Variables

Each event in the corpus is coded along ten dimensions:

1. **Sender hierarchy**: principal advisor, co-advisor, postdoc proxy, senior student, peer with advisor visible, or peer-only context.
2. **Group size (`N`)**: `4-6`, `7-10`, or `11+`.
3. **Composition profile (`C`)**: presence or absence of postdocs, senior students, junior students, and administrative stewards.
4. **Message type**: hard summons, soft ping, paper comments, administrative reminder, reimbursement request, public praise trap, deadline escalation, or holiday roll call.
5. **Urgency**: low, medium, or high.
6. **Visibility**: whether the reply is witnessed by a broad audience or only a narrow task-relevant subset.
7. **Ownership salience (`O`)**: whether the task clearly belongs to a first author, experiment operator, procurement steward, scheduler, or no obvious owner.
8. **Reply order (`P`)**: first visible response, second-wave acknowledgment, or silent bystander position after another person has already replied.
9. **Holiday phase (`K`)**: ordinary time, pre-holiday drift, first 72 hours after a long holiday, or stabilized post-holiday week.
10. **Emoji density**: no emoji, light emoji, or excessive soothing emoji.

For interpretive purposes, coders also noted a non-inferential **vernacular role tag** when a composite style was highly salient, such as “duty keeper,” “muddy-water fish,” “procurement sovereign,” or “first-author underling.” These tags were used for satirical description rather than statistical inference.

### 3.3 Utility Reconstruction

We model each student actor `i` as choosing a visible delay `l_i` after message `m` to maximize:

`U_i(l_i) = alpha*D_i(l_i | h_i, v, u) + beta*R_i(l_i | u, P_i) - gamma*A_i(l_i | N, C, O_i, P_i) - delta*B_i(l_i | h_i, v, P_i) - eta*H_i(K)`

where:

- `D_i` = perceived diligence signaled by reply timing
- `R_i` = reliability and cooperativeness inferred from timing
- `A_i` = assignment hazard, or the probability that visible responsiveness attracts further labor
- `B_i` = blame and suspicion triggered by silence or the wrong speed
- `H_i` = holiday-degradation penalty, representing post-holiday cognitive drag and weakened performative sharpness
- `h_i` = status position of actor `i`
- `v` = visibility level of the scene
- `u` = message urgency
- `N, C, O_i, P_i, K` = group size, composition, ownership, prior visible reply status, and holiday phase

This formulation captures three empirical realities. First, reply delay is jointly reputational and extractive: the same fast response can increase trust and increase future workload. Second, multi-person settings create strategic dependence: once someone else has already replied, the payoff of joining changes. Third, hierarchy and ownership shift the whole curve, because not everyone is equally permitted to wait.

### 3.4 Hypotheses

The paper tests eight hypotheses:

- **H1**: Perceived diligence follows an inverse-U relation with latency. Extremely fast replies imply suspicious availability, while very slow replies imply unreliability or quiet collapse.
- **H2**: Direct hierarchy compresses the optimal delay window. Messages from the principal advisor demand earlier response than messages from peers or postdoc proxies.
- **H3**: Communication visibility increases reputational penalty at both ends of the curve. When supervisors and peers can all observe the exchange, both over-rapid and over-slow replies become more legible.
- **H4**: Group size widens early waiting only when ownership is ambiguous. In large groups, responsibility diffuses until the message clearly belongs to someone.
- **H5**: Ownership-bearing actors such as first-author juniors, experiment operators, and procurement stewards face earlier optimal windows than generic bystanders.
- **H6**: Once a credible first response appears, later replies lose much of their diligence premium and become primarily symbolic.
- **H7**: Holiday periods shift acceptable delay later for low- and medium-urgency messages, but they do not fully protect explicitly summoned actors.
- **H8**: Light emoji use partially repairs moderate delay only in low-urgency, lower-hierarchy contexts; it fails under strong hierarchy or urgent requests.

## 4. Results

### 4.1 The Inverse-U of Diligence

The primary finding is an inverse-U relationship between reply latency and perceived diligence. Replies in the `8-18 min` bucket achieved the highest diligence score (9.1) and reliability score (9.2), while maintaining only moderate assignment hazard (5.2). By contrast, replies under 2 minutes had high reliability (8.1) but substantially elevated assignment hazard (8.8), supporting the claim that extreme responsiveness is interpreted as evidence of available capacity rather than pure virtue.

The `19-47 min` band remained viable for low- and medium-urgency exchanges, though it began to incur reliability slippage. Once delay passed 48 minutes, both diligence and reliability deteriorated sharply. Delays beyond 180 minutes were interpreted less as strategic pacing than as infrastructural failure, emotional breakdown, or soft refusal in expensive clothing.

### 4.2 Hierarchy and Visibility Compress the Window

Hierarchy strongly shaped acceptable delay. For messages sent directly by the principal advisor, the optimal window contracted to roughly `6-18 min`. For co-advisors and lab managers, the window widened slightly. Postdoc proxies allowed more drift, while peer-only settings permitted broad latency without major penalty.

Visibility intensified these effects. The most unstable category was the “peer with advisor visible” context. In such cases, even peer-originated messages inherit supervisory visibility, and students often respond faster than they would in strictly horizontal exchange. This produces a hybrid norm: socially coded as peer communication, but reputationally evaluated as advisor-facing performance.

### 4.3 Group Size, First-Responder Discount, and Diffusion

Group size altered initial waiting behavior. In groups of `4-6`, median first visible reply time was 6 minutes. In groups of `11+`, the median first visible reply extended to 13 minutes when ownership was ambiguous. This supports the volunteer's-dilemma interpretation: larger groups make it easier to hope someone else will take the first reputational bullet.

Yet this diffusion collapsed rapidly when ownership became clear. In manuscript-related threads where the first author was obvious, large-group median reply time fell back to 5 minutes. In reimbursement threads, the procurement steward replied early even in high-member groups, suggesting that responsibility diffuses socially only until role ownership interrupts the fantasy.

Once a credible first reply had appeared, later responses shifted from obligatory to ornamental. The second-wave acknowledgment cluster typically arrived `11-29 min` after the first reply and generated little additional diligence credit. In plain language, once somebody has typed the correct species of “收到老师”, everyone else can safely become atmospheric.

### 4.4 Heterogeneous Roles and the Politics of Obligation

Role heterogeneity substantially reshaped the response curve. The earliest windows belonged to actors whose ownership was publicly knowable:

- **first-author juniors** on manuscript comments: `5-14 min`
- **procurement stewards** on reimbursement or purchasing requests: `4-12 min`
- **experiment operators** on instrument or sample failures: `3-11 min`

By contrast, generic junior bystanders in broad group settings retained a much wider safe zone of `14-36 min`, while peer-only lurkers could drift further without major penalty.

These differences suggest that the relevant distinction is not simply rank. It is the public clarity of responsibility. The procurement senior occupies a constitutionally strange office: low authorship prestige, high invoice sovereignty. The first-author junior occupies the inverse office: high visibility, high blame, and remarkably little bargaining power. Both reply early, but for opposite reasons.

### 4.5 Holiday Fog and Emoji Compensation

Holiday periods produced a modest but consistent rightward shift in acceptable delay. During the first 72 hours after a long holiday, low- and medium-urgency messages tolerated an additional `6-11 min` before sharp suspicion emerged. In effect, the group briefly accepted that everyone had become worse at being an institutional person.

This tolerance, however, was conditional. Direct summons from the principal advisor still demanded reply within roughly `12 min`, and public deadline escalations showed almost no holiday mercy. Holiday fog softened the norm; it did not repeal the constitution.

Emoji use showed a similarly conditional effect. Light emoji use softened suspicion in low-urgency contexts near the upper edge of the optimal window. However, the effect was weak and vanished under deadline escalation, explicit blame risk, or direct-task conditions. Excessive emoji use backfired, lowering perceived seriousness and generating the impression of compensatory nervousness.

## 5. Discussion

The findings suggest that reply latency in advisor group chats is best understood as reputational labor embedded in a public coordination game. Students do not merely choose when to answer; they solve a constrained optimization problem within a morally saturated hierarchy. The ideal reply must look timely without appearing idle, modest without seeming evasive, and cooperative without volunteering for indefinite extraction.

This interpretation extends signaling theory in a modest but useful way. In advisor group chats, the signal is repeated, cheap, and persistently visible. Its meaning depends not only on the sender and receiver, but on who else is present, who already replied, and who is publicly understood to own the task. A timestamp therefore becomes a distributed social object rather than a private behavioral trace.

The volunteer's-dilemma framing also clarifies why large group chats feel uniquely draining. The burden lies not only in content production but in waiting strategy. Silence is rarely empty. It is often a collective attempt to outsource first exposure to somebody else. The muddy-water fish is therefore not lazy in a metaphysical sense; it is a rational actor waiting for a more status-legible organism to move first. Once the advisor types `@first author`, however, game theory abruptly becomes biography.

The role-heterogeneity results bring laboratory politics into clearer view. The first-author junior is publicly central but institutionally weak. The procurement senior is symbolically peripheral but administratively indispensable. The postdoc proxy often appears to be “just relaying information” while actually transmitting hierarchy with local accent. These are comic figures, but they index real asymmetries in obligation, visibility, and blame.

Current social-media discourse adds a useful vernacular layer. In platform language, the lab’s ESTJ has already replied “收到”, the INTP has opened three tabs and two anxieties, and the ENFP has drafted a warm answer but is still negotiating emoji density. We do not treat these as psychometric truths. We treat them as folk metaphors through which users narrate heterogeneous reputational strategies. They are lay sociology in meme form.

Holiday fog, finally, reveals something broader about academic life. Institutions value responsiveness while pretending that responsiveness costs nothing. Yet even minor delay management requires attention, emotional regulation, and role calculation. The private post-holiday plea, “Advisor, I am more stupid than the vacation itself; do you still want to meet?”, is ridiculous precisely because it is structurally plausible. The absurdity is diagnostic.

## 6. Limitations

This study has several limitations. First, the corpus is synthetic and reconstructive rather than observational in a strict empirical sense. Its validity is sociological and affective, not archival. Second, latency norms vary across disciplines, countries, lab cultures, and advisor personalities. Third, the model captures visible reply timing but not backstage behaviors such as drafting, deleting, consulting friends, panicking privately for twelve minutes, or asking a senior whether “收到老师” sounds too alive.

Fourth, the vernacular role tags and MBTI-style descriptors are interpretive composites inspired by contemporary online discourse, not validated personality measures. They are used to sharpen scene description, not to claim psychometric authority. Finally, while the paper draws on real theories of signaling, chronemics, and group coordination, its empirical world is intentionally stylized in order to preserve SHIT-compatible comic realism.

## 7. Conclusion

The graduate student in an advisor group chat does not simply reply. The student performs reliability under unequal observation, in front of a visible audience, inside a multi-person game in which someone must answer first and nobody wants the honor too often. Reply latency therefore functions as both signal and shield: a small interval in which diligence, fear, ownership, extractability, and hierarchy are negotiated in public.

If this paper is correct, then the apparently trivial question “Why didn’t you just answer?” has no trivial answer. One answers late enough to look occupied, early enough to look loyal, cautiously enough to avoid becoming tomorrow’s default volunteer, and, in the first three days after a long holiday, with whatever fragments of intelligence have survived the break.

## Table 1. Message-Type Risk Matrix

| Message Type | Urgency | Optimal Reply Window | Extra Task Risk | Interpretive Logic |
| --- | --- | --- | ---: | --- |
| Hard summons | High | 1-6 min | 9.4 | Silence reads as resistance |
| Deadline escalation | High | 2-9 min | 8.7 | Delay is conflated with collapse |
| Paper comments | Medium | 6-15 min | 7.8 | First-author ownership pulls the window left |
| Administrative reminder | Medium | 9-21 min | 5.2 | Moderate delay implies active processing |
| Reimbursement request | Medium | 4-12 min | 7.4 | Procurement ownership is publicly legible |
| Public praise trap | Medium | 4-12 min | 9.1 | Visible competence invites future extraction |
| Soft ping | Low | 14-37 min | 4.7 | Too fast appears suspiciously idle |
| Holiday roll call | Low | 18-46 min | 5.9 | Everyone is slower, but nobody is forgiven equally |

## Table 2. Latency Utility Snapshot

| Latency Bucket | Perceived Diligence | Reliability | Assignment Hazard | Interpretation |
| --- | ---: | ---: | ---: | --- |
| <2 min | 6.3 | 8.1 | 8.8 | Reliable but over-available |
| 2-7 min | 7.6 | 8.7 | 7.9 | Conscientious but still risky |
| 8-18 min | 9.1 | 9.2 | 5.2 | Optimal band |
| 19-47 min | 8.2 | 7.6 | 4.3 | Plausibly busy |
| 48-180 min | 5.5 | 4.8 | 2.6 | Slipping out of trust |
| >180 min | 2.4 | 2.1 | 1.8 | Read as disappearance |

## Table 3. Role-Heterogeneity Windows

| Role Type | Typical Scene | Optimal Reply Window | Strategic Constraint |
| --- | --- | --- | --- |
| First-author junior | Draft comments, revision requests | 5-14 min | Public responsibility, low veto |
| Procurement steward | Purchasing, reimbursement, forms | 4-12 min | Material ownership, invoice sovereignty |
| Experiment operator | Instrument failure, sample issue | 3-11 min | Clear technical ownership |
| Postdoc proxy | Advisor relay, coordination | 7-19 min | Hierarchical delegation |
| Generic junior bystander | Lab-wide reminder | 14-36 min | Can hide in audience if ownership is unclear |
| Peer-only muddy-water fish | Horizontal coordination | 22-61 min | Protected by low advisor visibility |

## Table 4. Audience and Holiday Adjustments

| Condition | Shift in Optimal Window | Practical Reading |
| --- | --- | --- |
| Advisor visible + direct request | `-4 to -8 min` | Reply earlier or risk moral damage |
| Peer asks while advisor is visible | `-3 to -6 min` | Peer message becomes quasi-supervisory |
| Another student has already replied | `+8 to +18 min` | First-responder discount lowers urgency |
| First 72 hours after a long holiday | `+6 to +11 min` | Holiday fog slightly softens standards |
| Ownership is explicit (`@first author`) | `-7 to -15 min` | Diffusion collapses instantly |

## References

Alvesson, M. (2013). *The triumph of emptiness: Consumption, higher education, and work organization*. Oxford University Press.

Berger, J., Cohen, B. P., & Zelditch, M., Jr. (1972). Status characteristics and social interaction. *American Sociological Review, 37*(3), 241-255.

Darley, J. M., & Latané, B. (1968). Bystander intervention in emergencies: Diffusion of responsibility. *Journal of Personality and Social Psychology, 8*(4, Pt. 1), 377-383.

Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. *Management Science, 32*(5), 554-571.

Diekmann, A. (1985). Volunteer's dilemma. *Journal of Conflict Resolution, 29*(4), 605-610.

Diekmann, A. (1993). Cooperation in an asymmetric volunteer's dilemma game: Theory and experimental evidence. *International Journal of Game Theory, 22*, 75-85.

Goffman, E. (1959). *The presentation of self in everyday life*. Doubleday.

Hochschild, A. R. (1983). *The managed heart: Commercialization of human feeling*. University of California Press.

Kalman, Y. M., Scissors, L. E., Gill, A. J., & Gergle, D. (2013). Online chronemics convey social information. *Computers in Human Behavior, 29*(3), 1260-1269.

Kreps, D. M., & Wilson, R. (1982). Reputation and imperfect information. *Journal of Economic Theory, 27*(2), 253-279.

Leonardi, P. M. (2014). Social media, knowledge sharing, and innovation: Toward a theory of communication visibility. *Information Systems Research, 25*(4), 796-816.

Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics, 87*(3), 355-374.

Tidwell, L. C., & Walther, J. B. (2002). Computer-mediated communication effects on disclosure, impressions, and interpersonal evaluations: Getting to know one another a bit at a time. *Human Communication Research, 28*(3), 317-348.

Walther, J. B. (1992). Interpersonal effects in computer-mediated interaction: A relational perspective. *Communication Research, 19*(1), 52-90.

Walther, J. B. (1996). Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction. *Communication Research, 23*(1), 3-43.

Walther, J. B., & Tidwell, L. C. (1995). Nonverbal cues in computer-mediated communication, and the effect of chronemics on relational communication. *Journal of Organizational Computing, 5*(4), 355-378.

Ziano, I., & Wang, B. (2021). Does response delay influence how an email sender is perceived? *Journal of Computer-Mediated Communication, 26*(6), 395-409.
