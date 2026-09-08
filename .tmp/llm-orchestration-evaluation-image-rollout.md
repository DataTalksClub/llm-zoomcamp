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
- `04-evaluation/01-intro.md`: `01-intro-05-rag-evaluation-diagram.jpg` retained
  as `01-intro-05-rag-evaluation-diagram-cropped.png`. Deterministic crop
  `(x=85,y=30,w=440,h=295)` and 2x Lanczos upscale used because exact math and
  labelled connections are instructional source data. `RAG`, `SEARCH`, `KB`,
  `ASSISTANT`, `PROMPT`, `LLM`, `Q`, and `A` relationships remain intact;
  recording chrome and face are removed.
- `04-evaluation/03-ground-truth-batch.md`: `03-ground-truth-batch-03-parallel-split-whiteboard.jpg` retained as `03-ground-truth-batch-03-parallel-split-whiteboard-imagegen.png`. Built-in imagegen after crop
  `(x=75,y=30,w=450,h=295)`; five exact partitions `1`–`5` and one downward
  arrow per partition preserve the parallel-processing teaching point. Zoom
  chrome, face, toolbar, cursor, and watermark removed; no invented total or
  extra label added.
- `03-orchestration/01-intro.md`: `01-intro-02-chatgpt-writing-flow-yaml.jpg`
  retained as `01-intro-02-chatgpt-writing-flow-yaml-cropped.png`. Deterministic
  crop `(x=10,y=55,w=510,h=264)` and 2x Lanczos upscale used because the
  Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame,
  browser controls, and unrelated overlays removed; original preserved.
<!-- next audit entries go above this marker -->
- `03-orchestration/04-ai-copilot.md`: `04-ai-copilot-03-generated-taxi-flow.jpg` retained as `04-ai-copilot-03-generated-taxi-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/04-ai-copilot.md`: `04-ai-copilot-01-copilot-landing-examples.jpg` retained as `04-ai-copilot-01-copilot-landing-examples-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/03-setup.md`: `03-setup-04-tavily-api-keys.jpg` retained as `03-setup-04-tavily-api-keys-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/03-setup.md`: `03-setup-02-gemini-api-key.jpg` retained as `03-setup-02-gemini-api-key-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/02-context-engineering.md`: `02-context-engineering-03-training-cutoff-answer.jpg` retained as `02-context-engineering-03-training-cutoff-answer-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/02-context-engineering.md`: `02-context-engineering-02-generated-kestra-flow.jpg` retained as `02-context-engineering-02-generated-kestra-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/01-intro.md`: `01-intro-03-generated-flow-without-context.jpg` retained as `01-intro-03-generated-flow-without-context-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
