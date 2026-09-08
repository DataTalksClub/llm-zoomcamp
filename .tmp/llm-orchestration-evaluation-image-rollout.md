# LLM Zoomcamp image rollout

Scope: `cohorts/2026/03-orchestration/**` and
`cohorts/2026/04-evaluation/**`.

Inventory: 43 local Markdown image references. Originals remain in place.
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
- `04-evaluation/13-llm-as-judge.md`: `13-llm-as-judge-05-score-counts.jpg` retained as `13-llm-as-judge-05-score-counts-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/12-rag-answers.md`: `12-rag-answers-05-total-cost.jpg` retained as `12-rag-answers-05-total-cost-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/12-rag-answers.md`: `12-rag-answers-04-answer-record.jpg` retained as `12-rag-answers-04-answer-record-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/12-rag-answers.md`: `12-rag-answers-03-rag-one-question.jpg` retained as `12-rag-answers-03-rag-one-question-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/06-search-tuning.md`: `06-search-tuning-04-grid-sorted-by-mrr.jpg` retained as `06-search-tuning-04-grid-sorted-by-mrr-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/06-search-tuning.md`: `06-search-tuning-02-boost-sweep-results.jpg` retained as `06-search-tuning-02-boost-sweep-results-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/05-search-metrics.md`: `05-search-metrics-04-mrr-rank-annotations.jpg` retained as `05-search-metrics-04-mrr-rank-annotations-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/05-search-metrics.md`: `05-search-metrics-02-hit-rate-count.jpg` retained as `05-search-metrics-02-hit-rate-count-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, metric formulas, ranks, dataframe values, generated answers, costs, and score counts are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/04-search-evaluation.md`: `04-search-evaluation-06-relevance-total-sample.jpg` retained as `04-search-evaluation-06-relevance-total-sample-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact search code, document IDs, relevance lists, matrix positions, and numeric output are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/04-search-evaluation.md`: `04-search-evaluation-04-compute-relevance-first.jpg` retained as `04-search-evaluation-04-compute-relevance-first-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact search code, document IDs, relevance lists, matrix positions, and numeric output are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/04-search-evaluation.md`: `04-search-evaluation-03-relevance-matrix-whiteboard.jpg` retained as `04-search-evaluation-03-relevance-matrix-whiteboard-cropped.png`. Deterministic crop (x=85,y=30,w=440,h=295) and 2x Lanczos upscale used because exact search code, document IDs, relevance lists, matrix positions, and numeric output are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/04-search-evaluation.md`: `04-search-evaluation-02-minsearch-test-search.jpg` retained as `04-search-evaluation-02-minsearch-test-search-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact search code, document IDs, relevance lists, matrix positions, and numeric output are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/03-ground-truth-batch.md`: `03-ground-truth-batch-05-total-cost-dataframe.jpg` retained as `03-ground-truth-batch-05-total-cost-dataframe-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, notebook output, URLs, document IDs, questions, and numeric values are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
- `04-evaluation/03-ground-truth-batch.md`: `03-ground-truth-batch-04-parallel-progress-bar.jpg` retained as `03-ground-truth-batch-04-parallel-progress-bar-cropped.png`. Deterministic crop (x=50,y=60,w=540,h=260) and 2x Lanczos upscale used because exact code, notebook output, URLs, document IDs, questions, and numeric values are instructional source data. Face, Zoom/browser chrome, cursor, and unrelated overlays removed; original preserved.
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

## Final audit

- Source references inspected: 43.
- Retained: 43. Removed: 0; every referenced image had a concrete teaching
  point under the illustration rubric.
- Built-in imagegen: 3 bounded diagrams (`01-intro-01`, `01-intro-02`, and
  `03-ground-truth-batch-03`). Deterministic crops/upscales: 40 exact UI,
  code, formula, table, plot, answer, and numeric-output captures.
- All 43 current Markdown references resolve; all 43 original JPEGs remain;
  no current lesson reference points to the old JPEGs.
- Limitation: deterministic upscaling improves framing and display size but
  cannot restore information absent from the 640×360 sources. Exact technical
  screenshots therefore retain their source text density and any source-edge
  truncation; no imagegen approximation was used for those assets.

## Focused repair batch 2: six independent-review corrections (2026-09-08)

These six active references were regenerated with the built-in imagegen tool
from a semantic reference plus a bounded crop. The generated outputs were
inspected at native resolution and at the 608px lesson display width before
selection. The old published PNGs were not used as final assets. The first
asset also has its original workshop JPG; the other five are conceptual
diagrams that were added without local JPG sources, so their prior PNG and a
bounded crop are recorded as semantic references rather than misrepresented as
original screenshots.

| Active reference | Source/reference inputs | Imagegen output | Verified invariant |
|---|---|---|---|
| `04-evaluation/images/01-intro-01-agentic-rag-diagram-imagegen.png` | Original JPG `01-intro-01-agentic-rag-diagram.jpg` (SHA-256 `9927037ef08c2621260a7b57f14caa5363ce343a625b12db8a9bfff44b05b658`); bounded crop `.tmp/llm-orchestration-evaluation-crops/01-intro-01-agentic-rag-diagram-source-crop.png` (SHA-256 `3752d51598017b8299d0f5148198872e255ac2316ffbdb1e53c156567f260bc3`), `(x=75,y=30,w=450,h=295)` | `exec-c2a849d1-a49e-4762-ab7f-1a4bc2ebe992`; final SHA-256 `0037093d3e4a384ef14ffbe9049ed4e0e4fdd4dd9f111a29b0b49b04a3608016` | Question → assistant → search/FAQ knowledge base → retrieved context → generated answer; original answer remains separate for evaluation; no dangling arrow. |
| `04-evaluation/images/11-evaluation-intro-01-rag-agent-evaluation-imagegen.png` | Prior semantic PNG at `HEAD` (SHA-256 `19f0e0f2dfa392122bdaec254de7b1d0ed065f80ca83e74d3cba56f0ed923b4c`); bounded crop `.tmp/llm-orchestration-evaluation-crops/batch2/11-evaluation-intro-01-rag-agent-evaluation-reference-crop.png` (SHA-256 `5843a22dd39ce2bf73c92654b78d6d7dd611e124126cee227a7713b7b4df6fb8`), `(x=36,y=20,w=1600,h=900)`; no local original JPG was available | Final correction `exec-be15d747-17d7-4e06-9a90-5fe4a512b8f9`; final SHA-256 `4d8bfda9ed1cc0ccd90944355dde5eda498027b18998ea673b8b20f52e71ad15` | RAG and agent lanes are complete; original answer is a separate judge input; generated answer and tool-call trajectory are separate inputs, with no answer → trajectory chain. The first candidate `exec-b8e58b0a-f01e-4722-87f9-452b6f042939` was rejected for chaining those two artifacts. |
| `04-evaluation/images/14-agent-evaluation-01-agent-evaluation-record-imagegen.png` | Prior semantic PNG at `HEAD` (SHA-256 `b397288625c82807912483b112a1ef96d1577878f1b25650ed6150afa41f5ae6`); bounded crop `.tmp/llm-orchestration-evaluation-crops/batch2/14-agent-evaluation-01-agent-evaluation-record-reference-crop.png` (SHA-256 `54ed2d732974e6aa655ce5e3f172e0cf20296477adc8e5be552a7b49b056da58`), `(x=36,y=20,w=1600,h=900)`; no local original JPG was available | `exec-37671904-8764-4cfc-a4a4-36a00922d99e`; final SHA-256 `1446a5c0529863e053eb032801510126333bddb28ff3a321e18d0f4a751711d4` | Question alone enters the agent; original answer bypasses the agent as reference data; the record contains question, original answer, generated answer, and tool-call trajectory. |
| `07-project-example/images/02-evaluating-retrieval-01-hit-rate-mrr-imagegen.png` | Prior semantic PNG at `HEAD` (SHA-256 `54122bac67dc3e282822b381254b2ec16e91cd3dce2cf76b6c3549927bf2a6ac`); bounded crop `.tmp/llm-orchestration-evaluation-crops/batch2/02-evaluating-retrieval-01-hit-rate-mrr-reference-crop.png` (SHA-256 `f426198a42eea43233657723bd1482f0b88affd21fdb7a3dab1907df512aad1e`), `(x=36,y=35,w=1600,h=870)`; no local original JPG was available | `exec-08941298-2622-41bc-934d-fd83af38af1b`; final SHA-256 `56cb305bfb1330498cc3fa51ea554a9c70a25132a501c167c210d203bf5bec74` | Relevant document is ground truth applied after ranked retrieval to produce relevance labels, Hit Rate, and MRR; it is not a search input. |
| `07-project-example/images/03-evaluating-rag-01-llm-judge-imagegen.png` | Prior semantic PNG at `HEAD` (SHA-256 `1a60472ba16ca292b421ac97e5c20a36c2ae4ea4a1a7ab2f91499bcec817b80a`); bounded crop `.tmp/llm-orchestration-evaluation-crops/batch2/03-evaluating-rag-01-llm-judge-reference-crop.png` (SHA-256 `bbe42a3e0a4655a0163c6817bcd24fb4fce72972f58982dd9c562171f83a44eb`), `(x=36,y=35,w=1600,h=870)`; no local original JPG was available | `exec-40c29563-9803-41c5-ab70-9fe7f0872e11`; final SHA-256 `39290050db9fe56d10f2c6df94f8563e2455554605780526203b6a0a9572886d` | The judge receives the question and generated answer only; output is `NON_RELEVANT`, `PARTLY_RELEVANT`, or `RELEVANT`; no unsupported original-answer branch. |
| `07-project-example/images/07-chunking-01-long-document-chunks-imagegen.png` | Prior semantic PNG at `HEAD` (SHA-256 `613e9264bd08d66aa427b4f553722091fc891f7903a968d9c4441ed0ee2330ec`); bounded crop `.tmp/llm-orchestration-evaluation-crops/batch2/07-chunking-01-long-document-chunks-reference-crop.png` (SHA-256 `7a93072c79f01f48f3b79fe3aa5b29ea2aa13aca03446851887c2c4c37ee2ef6`), `(x=36,y=35,w=1600,h=870)`; no local original JPG was available | `exec-2d920a25-7fe4-43b4-be91-370897c4bdd9`; final SHA-256 `98623aa0a542419f39aeea0a4bada24869640d5d278413ee8c12258ac5f4e68a` | Separate text, image/LLM-description-or-CLIP, and slide-deck/document-slide lanes; images are not flattened into generic text chunking. |

The five conceptual assets without local JPG sources require source-video
recovery if a future audit needs a frame-level comparison. This batch does not
claim such unavailable JPG provenance.

## Focused repair batch 3: LLM-judge answer comparison (2026-09-09)

The published illustration was regenerated with the built-in imagegen tool,
not upscaled or sharpened. The previous semantic PNG was used as a reference
because this conceptual asset has no original workshop JPG in the repository.
The bounded crop was made from that PNG and is reconstructible from the
recorded crop box.

| Active reference | Source/reference inputs | Imagegen output | Verified invariant |
|---|---|---|---|
| `07-project-example/images/03-evaluating-rag-01-llm-judge-imagegen.png` | Previous semantic PNG at `HEAD` (SHA-256 `39290050db9fe56d10f2c6df94f8563e2455554605780526203b6a0a9572886d`); bounded crop `.tmp/asset-repair-crops/03-evaluating-rag-01-llm-judge-reference-crop.png` (SHA-256 `23258b34d567f783cd1f80fb4db7f92cdb05a5be3e6ef4afa25ddc13e3299618`), `(x=36,y=35,w=1600,h=870)`; original JPG unavailable | Built-in imagegen run `exec-a900407c-13e7-401a-83f0-ce5be3debdb3`; final SHA-256 `03c430a76a72a33d0e4b155d09feff3b2c4f64aff5260beccb353055f53a267`; C2PA metadata present | The diagram now shows separate `REFERENCE ANSWER` and `GENERATED ANSWER` inputs converging on `COMPARE ANSWERS`, then `LLM JUDGE`, then the exact relevance outcomes `NON_RELEVANT`, `PARTLY_RELEVANT`, and `RELEVANT`. Native `1701x925` and 608px `608x331` renders were inspected. This supersedes the earlier entry that showed only the generated-answer lane. |
