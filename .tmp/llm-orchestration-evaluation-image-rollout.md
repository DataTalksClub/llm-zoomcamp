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
- `04-evaluation/02-ground-truth.md`: `02-ground-truth-06-parsed-questions-output.jpg` retained as `02-ground-truth-06-parsed-questions-output-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, notebook output, URLs, document IDs, questions, and numeric values are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/02-ground-truth.md`: `02-ground-truth-03-document-id-print.jpg` retained as `02-ground-truth-03-document-id-print-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, notebook output, URLs, document IDs, questions, and numeric values are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/02-ground-truth.md`: `02-ground-truth-02-filter-llm-zoomcamp-docs.jpg` retained as `02-ground-truth-02-filter-llm-zoomcamp-docs-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, notebook output, URLs, document IDs, questions, and numeric values are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/01-intro.md`: `01-intro-03-faq-qA-pairs.jpg` retained as `01-intro-03-faq-qA-pairs-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, notebook output, URLs, document IDs, questions, and numeric values are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `03-orchestration/07-multi-agent.md`: `07-multi-agent-03-execution-durations.jpg` retained as `07-multi-agent-03-execution-durations-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/07-multi-agent.md`: `07-multi-agent-02-research-output-logs.jpg` retained as `07-multi-agent-02-research-output-logs-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/07-multi-agent.md`: `07-multi-agent-01-multi-agent-flow.jpg` retained as `07-multi-agent-01-multi-agent-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/06-agents.md`: `06-agents-03-web-research-agent.jpg` retained as `06-agents-03-web-research-agent-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/06-agents.md`: `06-agents-02-agent-execution-tokens.jpg` retained as `06-agents-02-agent-execution-tokens-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/06-agents.md`: `06-agents-01-simple-agent-flow.jpg` retained as `06-agents-01-simple-agent-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/05-rag.md`: `05-rag-05-websearch-rag-answer.jpg` retained as `05-rag-05-websearch-rag-answer-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/05-rag.md`: `05-rag-04-websearch-retriever-flow.jpg` retained as `05-rag-04-websearch-retriever-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/05-rag.md`: `05-rag-03-rag-grounded-answer.jpg` retained as `05-rag-03-rag-grounded-answer-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/05-rag.md`: `05-rag-02-rag-flow-topology.jpg` retained as `05-rag-02-rag-flow-topology-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/05-rag.md`: `05-rag-01-without-rag-hallucinated-answer.jpg` retained as `05-rag-01-without-rag-hallucinated-answer-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra UI, flow YAML, execution output, or timeline is exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/04-ai-copilot.md`: `04-ai-copilot-04-accept-copilot-diff.jpg` retained as `04-ai-copilot-04-accept-copilot-diff-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/04-ai-copilot.md`: `04-ai-copilot-03-generated-taxi-flow.jpg` retained as `04-ai-copilot-03-generated-taxi-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/04-ai-copilot.md`: `04-ai-copilot-01-copilot-landing-examples.jpg` retained as `04-ai-copilot-01-copilot-landing-examples-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/03-setup.md`: `03-setup-04-tavily-api-keys.jpg` retained as `03-setup-04-tavily-api-keys-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/03-setup.md`: `03-setup-02-gemini-api-key.jpg` retained as `03-setup-02-gemini-api-key-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/02-context-engineering.md`: `02-context-engineering-03-training-cutoff-answer.jpg` retained as `02-context-engineering-03-training-cutoff-answer-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/02-context-engineering.md`: `02-context-engineering-02-generated-kestra-flow.jpg` retained as `02-context-engineering-02-generated-kestra-flow-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
- `03-orchestration/01-intro.md`: `01-intro-03-generated-flow-without-context.jpg` retained as `01-intro-03-generated-flow-without-context-cropped.png`. Deterministic crop (x=10,y=55,w=510,h=264) and 2x Lanczos upscale used because the Kestra/ChatGPT UI and YAML are exact technical content. Face, recording frame, browser controls, and unrelated overlays removed; original preserved.
