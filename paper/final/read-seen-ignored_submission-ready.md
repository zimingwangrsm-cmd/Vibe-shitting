# Read, Seen, Ignored: A Signaling-Game Analysis of Reply Latency in Advisor Group Chats

**已读、不回、稍后回复：导师群聊响应延迟的信号博弈分析**

**Author / 作者**  
Cangsheng / 沧生  
VIBE SHITTING Lab for Reputational Studies

**Keywords / 关键词**  
advisor group chats; signaling; reputational labor; graduate student life; latency; digital etiquette  
导师群聊；信号博弈；声誉劳动；研究生生活；回复延迟；数字礼仪

## Abstract

This paper examines reply latency in advisor group chats as a form of reputational signaling. We argue that graduate students do not optimize for immediate response, but for a narrow band of delay that simultaneously conveys diligence, preserves reliability, and reduces the probability of attracting additional tasks. Using a mixed-method design that combines message annotation, latency bucketing, hierarchy coding, and payoff reconstruction, we analyze 4,236 message-response dyads across 28 reconstructed research groups. The findings show an inverse-U relation between latency and perceived diligence: replies that are too fast imply suspicious idleness, while replies that are too slow imply neglect. The most stable zone for routine messages lies between 8 and 18 minutes, but hierarchy and message visibility compress or widen this window. Direct advisor messages move the window earlier, while peer-only contexts permit longer strategic drift. Light emoji use partially offsets moderate delay for low-urgency messages but fails in high-urgency or high-visibility contexts. We conclude that response latency in academic group chats operates less as a communication habit than as a technology of self-presentation under chronic asymmetry.

## 中文摘要

本文将导师群聊中的回复时延视为一种声誉信号行为。我们认为，研究生优化的并不是“越快越好”的响应速度，而是一段狭窄的延迟区间，它需要同时传达勤奋、维持可靠性，并尽可能降低吸引额外任务的概率。本文采用混合研究设计，对 28 个重建研究群中的 4,236 个“消息-回复”对进行分析，方法包括消息标注、时延分桶、层级编码与收益重建。结果表明，回复延迟与感知勤奋度之间呈倒 U 型关系：过快回复意味着可疑的空闲，过慢回复则意味着疏忽。对于常规消息而言，最稳定的回复窗口位于 8 至 18 分钟之间，但层级关系与消息可见性会压缩或扩张这一窗口。导师本人发出的消息会将最优窗口整体前移，而纯同辈情境则允许更长的策略性漂移。低强度表情在低紧急度消息中可以部分修复中度延迟，但在高紧急度或高可见度情境中无效。本文由此认为，学术群聊中的响应延迟，与其说是一种沟通习惯，不如说是一种在长期不对称关系中进行自我呈现的技术。

## 1. Introduction

Academic group chats are frequently treated as logistical channels. In practice, they operate as compact theaters of hierarchy, diligence, and moral visibility. A single message from an advisor does not merely request information; it opens a scene in which all observers may infer who is attentive, who is overloaded, who is avoiding work, and who is dangerously available for further assignment. Under such conditions, reply timing becomes consequential.

Common advice within student communities recommends responsiveness. Yet extreme responsiveness carries its own penalty. A reply that arrives within seconds may successfully signal reliability, but it may also imply a troubling surplus of attention. In many laboratories, “always online” is rewarded not with admiration alone but with additional labor. Conversely, excessive delay can be interpreted as negligence, indifference, or collapse. Students therefore face a narrow strategic problem: how to answer quickly enough to remain legible as responsible, but slowly enough to avoid advertising unclaimed capacity.

This paper proposes that reply latency in advisor group chats should be analyzed as a signaling problem rather than a purely communicative one. The student does not simply transmit information. The student performs an equilibrium between obedience, competence, and survivable ambiguity. The central contribution of this paper is to formalize that equilibrium, show its sensitivity to hierarchy and visibility, and argue that latency itself constitutes a small but recurring unit of reputational labor.

## 2. Conceptual Background

Our argument draws on three lines of thought. First, signaling theory suggests that agents use observable actions to communicate hidden states under asymmetrical information. In academic chat environments, the hidden states include busyness, discipline, competence, panic, and emotional stability. Latency becomes a low-cost but continuously available signal.

Second, impression management scholarship reminds us that social action is staged before audiences. Group chats amplify this process by preserving text, timestamps, and visibility. The student is not replying to a single superior but to a composite audience: advisor, postdoc, peers, and future memory. The timestamp therefore becomes a public micro-performance.

Third, theories of emotional and reputational labor clarify why this process is experienced as exhausting even when materially trivial. The act of deciding whether to reply now, in ten minutes, or “after polishing the wording” is not simply clerical. It is a repeated calibration of self-presentation under asymmetric dependence. The apparent triviality of the decision is precisely what gives it disciplinary force: it must be performed constantly, invisibly, and without complaint.

## 3. Research Design

### 3.1 Corpus Construction

The study analyzes 4,236 message-response dyads reconstructed from 28 advisor-linked research groups across the period January 2024 to December 2025. The corpus is composed of simulated logs and retrospective reconstructions of common interaction patterns reported by graduate students. The unit of analysis is a visible incoming message and the first visible student response.

While the dataset is intentionally synthetic, it is constructed to preserve the emotional realism of the interaction environment. We treat the resulting corpus not as a record of literal behavior but as a model of perceived norm structure. This is appropriate because the paper asks not what students objectively do in all cases, but what latency patterns become intelligible as diligence, negligence, or hazardous availability.

### 3.2 Coding Scheme

Each dyad was coded along five dimensions:

1. **Sender hierarchy**: principal advisor, co-advisor, postdoc proxy, lab manager, peer with advisor visible, or peer-only private context.
2. **Message type**: hard summons, soft ping, paper comments, administrative reminder, public praise trap, deadline escalation, or weekend latent request.
3. **Urgency**: low, medium, or high.
4. **Visibility**: whether only the dyadic relation was salient or whether a wider audience was present.
5. **Emoji density**: no emoji, light emoji, or excessive soothing emoji.

Response latency was grouped into six buckets: `<2 min`, `2-7 min`, `8-18 min`, `19-47 min`, `48-180 min`, and `>180 min`.

### 3.3 Utility Reconstruction

We modeled student utility as:

`U(l) = alpha*D(l) + beta*R(l) - gamma*T(l) - delta*M(l)`

where `D(l)` is perceived diligence, `R(l)` is reliability, `T(l)` is task accretion risk, and `M(l)` is moral suspicion induced by the “wrong” speed. This formulation reflects the practical trade-off reported across the corpus: the best reply is not the fastest one, but the one that optimizes visibility without triggering new extraction.

### 3.4 Hypotheses

The paper tests four hypotheses:

- **H1**: perceived diligence follows an inverse-U pattern over latency.
- **H2**: direct hierarchy compresses the optimal delay window.
- **H3**: public visibility heightens penalties for both over-rapid and over-slow replies.
- **H4**: light emoji usage partially repairs moderate delay only for low-urgency messages.

## 4. Results

### 4.1 The Inverse-U of Diligence

The primary finding is an inverse-U relationship between reply latency and perceived diligence. Replies in the `8-18 min` bucket achieved the highest diligence score (9.1) and reliability score (9.2), while maintaining only moderate task accretion risk (5.2). By contrast, replies under 2 minutes had high reliability (8.1) but substantially elevated task accretion risk (8.8), supporting the claim that extreme responsiveness is interpreted as evidence of available capacity.

The `19-47 min` band remained viable for low- and medium-urgency exchanges, though it began to incur reliability slippage. Once delay passed 48 minutes, both diligence and reliability deteriorated sharply. Delays beyond 180 minutes were interpreted less as strategic pacing than as infrastructural failure, emotional breakdown, or quiet refusal.

### 4.2 Hierarchy Compresses the Window

Hierarchy strongly shaped acceptable delay. For messages sent directly by the principal advisor, the optimal window contracted to roughly `6-18 min`. For co-advisors and lab managers, the window widened slightly. Postdoc proxies allowed more drift, while peer-only settings permitted broad latency without major penalty.

The most unstable category was the “peer with advisor visible” context. In such cases, even peer-originated messages inherit supervisory visibility, and students often respond faster than they would in strictly horizontal exchange. This produces a peculiar hybrid norm: socially coded as peer communication, but reputationally evaluated as advisor-facing performance.

### 4.3 Message Type and Task Accretion Risk

Message type influenced not only urgency but downstream labor consequences. Two categories were especially dangerous:

- **hard summons**: because delay is interpreted as resistance
- **public praise trap**: because successful response performance invites additional responsibility

The “public praise trap” deserves emphasis. Messages such as “X did a great job on the last revision” appear positive, but they often convert visible competence into future extractability. Students who responded too quickly to such messages signaled both gratitude and dangerous readiness, increasing the probability of subsequent assignment.

### 4.4 Emoji Compensation

Light emoji use slightly softened suspicion in low-urgency contexts, especially when delay sat near the upper end of the optimal window. However, the effect was weak and vanished under deadline escalation or direct-task conditions. Excessive emoji use backfired, lowering perceived seriousness and occasionally generating the impression of compensatory nervousness.

## 5. Discussion

The findings suggest that reply latency in advisor group chats is best understood as reputational labor. Students do not merely choose when to answer; they continuously solve a constrained optimization problem within a morally saturated hierarchy. The ideal reply must look timely without appearing idle, modest without seeming evasive, and warm without seeming unserious.

This helps explain why group chat participation often feels draining even when message volume is low. The burden lies not only in content production but in timestamp management. Each notification triggers a minor interpretive drama: if I reply now, what hidden state am I revealing? If I reply later, what failure am I confessing? Strategic delay emerges as a survival technology for those who must remain visible, obedient, and finite at once.

The paper also contributes to a broader critique of academic life. Contemporary research culture increasingly valorizes availability while denying that availability is work. Group chat latency exposes the contradiction. Institutions celebrate “responsiveness” as professionalism, yet the same signal can be used to identify and exploit whoever appears most reachable. Students therefore cultivate a narrow zone of plausible busyness: not absent, not free, but continuously almost occupied.

## 6. Limitations

This study has several limitations. First, the corpus is synthetic and reconstructive rather than observational in a strict empirical sense. Its validity is sociological and affective, not archival. Second, latency norms vary across disciplines, countries, and advisor personalities. Third, the model captures visible reply timing but not invisible backstage behaviors such as drafting, deleting, consulting friends, or panicking privately for twelve minutes before typing “收到老师”.

These limitations do not nullify the analysis. Instead, they suggest that the structure identified here is best read as a stylized model of academic chat anxiety rather than a universal law of all digital supervision.

## 7. Conclusion

The graduate student in an advisor group chat does not simply reply. The student performs reliability under unequal observation. Reply latency therefore functions as a reputational instrument: a small interval in which diligence, fear, self-preservation, and extractability are negotiated in public.

If this paper is correct, then the apparently trivial question “Why didn’t you just answer?” has no trivial answer. One answers late enough to look occupied, early enough to look loyal, and carefully enough to avoid becoming tomorrow’s default volunteer.

## Table 1. Message-Type Risk Matrix

| Message Type | Urgency | Optimal Reply Window | Extra Task Risk | Interpretive Logic |
| --- | --- | --- | ---: | --- |
| Hard summons | High | 1-6 min | 9.4 | Silence reads as resistance |
| Deadline escalation | High | 2-9 min | 8.7 | Delay is conflated with collapse |
| Paper comments | Medium | 13-28 min | 6.1 | Fast reply reveals draft availability |
| Administrative reminder | Medium | 9-21 min | 5.2 | Moderate delay implies active processing |
| Public praise trap | Medium | 4-12 min | 9.1 | Visible competence invites future extraction |
| Soft ping | Low | 14-37 min | 4.7 | Too fast appears suspiciously idle |
| Weekend latent request | Low | 31-83 min | 6.8 | Delayed care beats instant surrender |

## Table 2. Latency Utility Snapshot

| Latency Bucket | Perceived Diligence | Reliability | Task Accretion Risk | Interpretation |
| --- | ---: | ---: | ---: | --- |
| <2 min | 6.3 | 8.1 | 8.8 | Reliable but over-available |
| 2-7 min | 7.4 | 8.5 | 7.9 | Conscientious but still risky |
| 8-18 min | 9.1 | 9.2 | 5.2 | Optimal band |
| 19-47 min | 8.4 | 7.8 | 4.3 | Plausibly busy |
| 48-180 min | 5.7 | 4.9 | 2.6 | Slipping out of trust |
| >180 min | 2.4 | 2.1 | 1.8 | Read as disappearance |

## References

Alvesson, M. (2013). *The triumph of emptiness: Consumption, higher education, and work organization*. Oxford University Press.

Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. *Management Science, 32*(5), 554-571.

Flush, A., & Queue, M. (2025). Idle yet reachable: Micro-delays in graduate messaging economies. *Journal of Invisible Labor, 11*(2), 1-19.

Goffman, E. (1959). *The presentation of self in everyday life*. Doubleday.

Hochschild, A. R. (1983). *The managed heart: Commercialization of human feeling*. University of California Press.

Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics, 87*(3), 355-374.

Stool, R. #2. (2024). Needs more depth: Strategic vagueness in evaluative prose. *Annals of Elastic Critique, 7*(4), 404-417.

Walther, J. B. (1996). Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction. *Communication Research, 23*(1), 3-43.
