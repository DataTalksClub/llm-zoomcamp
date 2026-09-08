# LLM Zoomcamp image rollout

Scope: `cohorts/2026/03-orchestration/**` and
`cohorts/2026/04-evaluation/**`.

Inventory: 40 local Markdown image references. Originals remain in place.
Technical code, commands, URLs, plots, numeric output, and live UI use
deterministic crops/upscales; bounded conceptual diagrams use the built-in
imagegen workflow after a deterministic crop. Each disposition records the
rubric decision and the invariant checked before acceptance.

## Audit entries

- `04-evaluation/01-intro.md`: `01-intro-01-agentic-rag-diagram.jpg` retained
  as `01-intro-01-agentic-rag-diagram-imagegen.png`. Built-in imagegen after
  crop `(x=75,y=30,w=450,h=295)`; bounded diagram regenerated with exact
  labels `AGENTIC RAG`, `ASSISTANT`, `SEARCH`, and `Q`. User face, Zoom
  chrome, toolbar, and watermark removed; flow meaning preserved. No exact
  numeric/code invariant.
- `04-evaluation/01-intro.md`: `01-intro-02-interact-or-generate.jpg` retained
  as `01-intro-02-interact-or-generate-imagegen.png`. Built-in imagegen after
  crop `(x=75,y=30,w=450,h=295)`; exact alternatives `Interact → logs → {Qᵢ}`
  and `Generate` from `FAQ` preserved. Zoom chrome, face, toolbar, and
  watermark removed; no extra evaluation steps added.
- `04-evaluation/01-intro.md`: `01-intro-04-generate-questions-whiteboard.jpg`
  retained as `01-intro-04-generate-questions-whiteboard-cropped.png`.
  Deterministic crop `(x=85,y=30,w=440,h=295)` and 2x Lanczos upscale used
  because the source contains exact mathematical notation and relationships.
  The `Aᵢ → Qᵢ* → [Qᵢ*, Aᵢ; aᵢ, Aᵢ]` teaching sketch remains exact; face, Zoom
  chrome, toolbar, and watermark removed.
