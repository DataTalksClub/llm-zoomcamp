# LLM Zoomcamp image rollout

Scope: `cohorts/2026/01-agentic-rag/**` and
`cohorts/2026/02-vector-search/**`.

The inventory covers every local Markdown image reference in the two lesson
trees. Originals remain in place. Technical code, commands, URLs, plots,
numeric output, and live UI use deterministic crops/upscales; bounded
conceptual diagrams use the built-in imagegen workflow after a deterministic
crop. Each disposition below records the rubric decision and the invariant
checked before acceptance.

## Audit entries

- `03-rag-01-assistant-question-sketch.jpg` — **remove**, score 3/12.
  The source is a GitHub lesson-page screenshot rather than the captioned
  student/assistant sketch. It duplicates the surrounding prose and code,
  leaves the teaching point unreadable at lesson size, and fails the caption
  and accessibility hard gate. The original file remains unreferenced.

- `06-building-prompt-01-rag-flow-diagram.jpg` — **remove**, score 4/12.
  The source is a code/notebook frame, not the captioned hand-drawn flow
  diagram. Its code is repeated in the lesson and the important right side
  is partly obscured by capture chrome, so changing only the caption would not
  restore a distinct teaching point. The original file remains unreferenced.

- `03-rag-08-rag-architecture-sketch.jpg` — **crop/replace**, score 10/12.
  The source teaches the RAG relationship, but includes whiteboard UI,
  webcam, and Zoom chrome. Deterministic crop `(448x320+84+16)` was used as
  the imagegen reference; the accepted imagegen replacement preserves `RAG`,
  `Q`, `A`, `ASSISTANT`, both question/answer arrow directions, and the
  assistant-to-database arrow. No faces, controls, cursors, or extra labels
  remain.

- `09-data-ingestion-06-annotated-architecture-sketch.jpg` — **crop/replace**,
  score 11/12. The source has a strong architecture teaching point but is a
  webcam/whiteboard capture. Deterministic crop `(448x320+84+16)` was used as
  the imagegen reference. The first generation was rejected because it added
  an unrequested `Q + A` label; a targeted second pass removed it. The final
  asset preserves `FAQ.json -> INGESTOR -> KB`, the shared KB arrows, the user
  `Q`/assistant `A` flow, `PROMPT -> LLM`, and the return arrow, with no faces,
  capture chrome, cursors, watermarks, or extra components.

- `11-agents-intro-04-agentic-flow-diagram.jpg` — **crop/replace**, score
  10/12. The source shows the useful retry state transition, but it includes
  browser/Zoom chrome and a selection highlight. A deterministic crop
  `(500x285+30+35)` was used as the imagegen reference. The accepted diagram
  preserves the four exact nodes and their top-to-bottom arrows, removes the
  highlight and all capture artifacts, and was checked for the corrected
  `Ollama` spelling and final answer state.

- `01-intro-03-rag-pipeline-whiteboard.jpg` — **crop/replace**, score 11/12.
  The source directly teaches the retrieval/prompt/LLM relationship but is a
  whiteboard capture with webcam, toolbar, and Zoom chrome. Deterministic crop
  `(448x320+84+16)` was used as the imagegen reference. The accepted asset
  preserves `Q`, `A`, `ASSISTANT`, `FAQ`, `PROMPT`, `LLM`, both retrieval
  directions, and the answer return path; no capture artifacts remain.

- `02-embeddings-01-vector-space-whiteboard.jpg` — **crop/replace**, score
  10/12. The source teaches semantic proximity but is a whiteboard capture
  with webcam, toolbar, and Zoom chrome. Deterministic crop `(448x320+84+16)`
  was used as the imagegen reference. The accepted image preserves the exact
  labels `enroll`, `join`, and `Docker`, with the first two close together and
  Docker clearly distant; no extra labels or capture artifacts remain.

- `07-sqlitesearch-vector-01-ann-vs-nn-whiteboard.jpg` — **crop/replace**,
  score 10/12. The source teaches ANN candidate narrowing but is a
  whiteboard capture with webcam, toolbar, and Zoom chrome. Deterministic crop
  `(448x320+84+16)` was used as the imagegen reference. The accepted asset
  preserves the FAQ point cloud, local candidate region, query point, and
  exact `FAQ`/`ANN` labels; no numeric claims or capture artifacts remain.

- `07-sqlitesearch-vector-02-ingestion-deployment-split.jpg` —
  **crop/replace**, score 11/12. The source clearly teaches the shared
  persistent-index relationship but is a whiteboard capture with webcam,
  toolbar, and Zoom chrome. Deterministic crop `(448x320+84+16)` was used as
  the imagegen reference. The final diagram preserves separate `INGESTION`
  and `DEPLOYMENT` paths, one shared `FAQ INDEX`, `FAQ DOCS`, `ASSISTANT`, and
  the question/answer direction; no capture artifacts remain.

- `10-next-steps-03-similarity-whiteboard.jpg` — **crop/replace**, score 8/12.
  The source contains the exact similarity notation and ranking sketch, so
  imagegen was not used: generated text could corrupt the formula. A
  deterministic crop `(448x320+84+16)` removed the webcam, toolbar, and Zoom
  frame, then Lanczos upscaling produced a crisp sibling while preserving the
  handwritten equation and ranked-page relationship.

- `07-llm-05-chatgpt-message-history.jpg` — **remove**, score 3/12. The
  source is a generic personal ChatGPT conversation, not a clear view of the
  system/developer/user role structure described by the caption. It is
  transient and potentially private, duplicates the surrounding prose, and
  fails the rubric's personal-content hard gate. The original file remains
  unreferenced.
