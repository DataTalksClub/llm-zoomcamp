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
