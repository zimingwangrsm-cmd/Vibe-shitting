# Visual Explainer Plan / 插图与图解说明方案

## Principle / 原则

Keep the quantitative claims in reproducible SVG charts, and use Banana or other image tools only for sidecar explanation panels.

定量结论继续放在可复现的 SVG 图表里；Banana 一类工具只负责辅助解释的场景图或边栏图。

## Active Figure Set / 当前主图组

1. `theory_framework_map.svg`
2. `latency_diligence_curve.svg`
3. `hierarchy_window_chart.svg`
4. `first_responder_discount.svg`
5. `role_obligation_matrix.svg`
6. `role_species_windows.svg`
7. `publication_burden_u_curve.svg`
8. `red_envelope_shock.svg`

## Recommended Insertions / 建议插图位置

### Slot A: before Section 4.1

Use:

- `theory_framework_map.svg`
- `latency_diligence_curve.svg`
- `hierarchy_window_chart.svg`

Purpose:

- explain the paper’s basic game structure
- explain why “too fast” and “too slow” are both dangerous
- explain why hierarchy compresses the viable reply window

### Slot B: around Section 4.3

Use:

- `first_responder_discount.svg`

Purpose:

- show why one correct `收到老师` destroys the marginal value of later virtue
- explain diffusion before the first reply and ceremonial behavior after it

### Slot C: around Section 4.4

Use:

- `role_obligation_matrix.svg`
- `role_species_windows.svg`
- `publication_burden_u_curve.svg`

Purpose:

- turn the laboratory menagerie into institutional roles
- explain why some people are structurally unable to wait
- visualize the publication-stock U-shape

### Slot D: around Section 4.5

Use:

- `red_envelope_shock.svg`

Purpose:

- compare ordinary holiday check-ins, peer reminders, advisor red envelopes, and direct call-outs
- show that small money can restore group order faster than general principle

## Banana-Compatible Side Panels / 适合用 Banana 做的边栏图

Good targets:

- lab species poster
- call-out effect three-panel scene
- red-envelope effect explainer card
- holiday fog mood plate

Prompt pack:

- `banana-prompt-pack.md`

## Meme Handling Rule / 表情包使用规则

- If provenance is unclear, redraw.
- If a meme is heavily platform-native, keep it in social posts rather than the paper body.
- The manuscript should stay deadpan and academically disguised.
