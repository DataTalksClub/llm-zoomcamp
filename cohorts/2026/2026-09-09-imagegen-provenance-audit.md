# Imagegen provenance audit

Date: 2026-09-09

Scope: the 37 `*-imagegen.png` files referenced by current Markdown lessons in
`cohorts/2026/01-agentic-rag` through `cohorts/2026/07-project-example`.
The unreferenced sibling
`04-evaluation/images/01-intro-02-interact-or-generate-imagegen.png` was not
modified.

## Method

- The original workshop JPG remains the source of truth for every repaired
  screenshot-derived diagram below.
- Each retained source crop was made at native pixels with `convert -crop` and
  `+repage` only. No crop was resized, upscaled, sharpened, or Lanczos-filtered.
- Each repaired output was generated with the built-in imagegen edit workflow
  using the original JPG and its bounded native crop. The previous published
  PNG was not used as the final source.
- Every active reference was inspected at native resolution and as a
  review-only simulated 608px-wide render. The simulated renders are not
  published assets.
- C2PA presence was checked with a string-level metadata check. Standalone
  cryptographic verification was not run because `c2patool` is unavailable.

## Durable source JPG → native crop → imagegen output chains

The following seven active outputs were regenerated in this repair. Source JPGs
and native crops are retained beside the published outputs.

| Published output | Original JPG / SHA-256 | Native crop / box / SHA-256 | Imagegen run | Output / native size / SHA-256 |
| --- | --- | --- | --- | --- |
| `01-agentic-rag/images/03-rag-08-rag-architecture-sketch-imagegen.png` | `03-rag-08-rag-architecture-sketch.jpg` / `047a596e66266afb1e8a43016613521b1f5b67e49a7f1466d1200a6acce5ac17` | `03-rag-08-rag-architecture-sketch-source-crop.png` / `448x320+84+16` / `24b7529fe82d0b30959420a736ddc1a6b05c85f11e45a804b3962286ecba6d8e` | `exec-979c8cd1-55b3-46a3-818b-d4552ac463ce` | `1484x1060` / `af6e300269aa399410236ac1430b92682e0491fddac393a7699affcc8dfa5d9f` |
| `01-agentic-rag/images/09-data-ingestion-06-annotated-architecture-sketch-imagegen.png` | `09-data-ingestion-06-annotated-architecture-sketch.jpg` / `3643d9f18a4833474d99fd2e856444f5e84be3d42949c593bd5218154bbd2c28` | `09-data-ingestion-06-annotated-architecture-sketch-source-crop.png` / `448x320+84+16` / `7239fb813f44d63d9bb3025f5b44057223b277ee769f1daaf02cb93ad54188a6` | `exec-ead23052-aec9-4eb9-a1b5-6d8f2eaf1343` | `1484x1060` / `fa0bbf42e291aa5e7c9da2a948dd2578ba3e6dfff0b34ba7561584155a63fe0b` |
| `02-vector-search/images/01-intro-03-rag-pipeline-whiteboard-imagegen.png` | `01-intro-03-rag-pipeline-whiteboard.jpg` / `6a2fd2516749f3f9256133a6600ba309cf5eedb4117481cdec0595aac38cccfa` | `01-intro-03-rag-pipeline-whiteboard-source-crop.png` / `448x320+84+16` / `6eaf6610bdd42691c6bce27e813d47836960e80afed0038afc9db53eb7bec186` | `exec-990d8897-1de0-4027-b764-dca7ad116248` | `1484x1060` / `e45b23c1bd686fea9771b5fab7cb8cbf301a2ff9081c62b08ae6f04bcd49eece` |
| `02-vector-search/images/02-embeddings-01-vector-space-whiteboard-imagegen.png` | `02-embeddings-01-vector-space-whiteboard.jpg` / `2b38832c5367f9f368ad662733d28381288a2a9be6f4eb21693065f61cf2fdae` | `02-embeddings-01-vector-space-whiteboard-source-crop.png` / `448x320+84+16` / `38a3342684fabee23e7189771685c2f2be4d0c301d53cde961741d0cb0df2043` | `exec-8b23a4d4-af14-43e7-aee1-38055b568145` | `1484x1060` / `92d493aa15b8cbc037896a29d3ee140b3fedc4fe7dc14563aac48bccb369cb32` |
| `02-vector-search/images/07-sqlitesearch-vector-01-ann-vs-nn-whiteboard-imagegen.png` | `07-sqlitesearch-vector-01-ann-vs-nn-whiteboard.jpg` / `8403f56a3542effbb13663736c152f637fe999124bc8cf04dad0c578fc0a3f81` | `07-sqlitesearch-vector-01-ann-vs-nn-whiteboard-source-crop.png` / `448x320+84+16` / `158242335fb8d1ae91e416ffa57e3accc8a36bf0c81ab7cf5011ed8ac94e526f` | `exec-f3fdfdde-5e04-4e19-a0a1-bbe29c02968e` | `1484x1060` / `6831af5aa47f7f08c72b8e24296fb1c320dd9c3b0be9c7cc921ec60396ab4801` |
| `02-vector-search/images/07-sqlitesearch-vector-02-ingestion-deployment-split-imagegen.png` | `07-sqlitesearch-vector-02-ingestion-deployment-split.jpg` / `544f7f3247150fdfdd8bc91cfdd9b21d6d035dbb9bbe6a3aebf8f1d1aa961308` | `07-sqlitesearch-vector-02-ingestion-deployment-split-source-crop.png` / `448x320+84+16` / `99112d1f30716a0c141f3c7144d8fe710c7d9db5f1c3d382d2173f052d497128` | `exec-62cf9524-76b9-476a-9514-4de97d58a629` | `1484x1060` / `5a0a3f5f9b3dd7447afb30e09324fbfc9db965e91e09d820f953e321446c0bbf` |
| `04-evaluation/images/03-ground-truth-batch-03-parallel-split-whiteboard-imagegen.png` | `03-ground-truth-batch-03-parallel-split-whiteboard.jpg` / `6dc2d593df4387b9cc48517d500696e2a14534e9c6153eb59db6d7005c1fcb93` | `03-ground-truth-batch-03-parallel-split-whiteboard-source-crop.png` / `450x295+75+30` / `50cbe699b34dd9dbd737ab086416a9af8e30f2494a3e471e89ac8ed080128cd0` | `exec-dce49013-2b29-44ff-85d0-bc7df151b8bd` | `1983x793` / `9a48cc736a49ab075c1132985f48c0ffa6e27e2842fef071755d9233384081c9` |

The repaired diagrams preserve the source labels, code-like text, numbers,
arrow directions, and structures. Camera/face, browser/editor/Zoom chrome,
cursor, play, toolbar, and selection overlays were removed.

## Existing current imagegen regenerations left unchanged

These seven active outputs already have current imagegen regeneration evidence
in the tracked rollout notes and C2PA-bearing published files. They were not
regenerated again.

| Published output | Existing run/evidence |
| --- | --- |
| `01-agentic-rag/images/11-agents-intro-04-agentic-flow-diagram-imagegen.png` | `exec-abf6b1f8-fa80-4b25-974e-e64782e61016`; tracked note `01-agentic-rag/images/2026-09-09-imagegen-repair-provenance.md` |
| `04-evaluation/images/01-intro-01-agentic-rag-diagram-imagegen.png` | `exec-c2a849d1-a49e-4762-ab7f-1a4bc2ebe992`; `.tmp/llm-orchestration-evaluation-image-rollout.md` |
| `04-evaluation/images/11-evaluation-intro-01-rag-agent-evaluation-imagegen.png` | `exec-be15d747-17d7-4e06-9a90-5fe4a512b8f9`; `.tmp/llm-orchestration-evaluation-image-rollout.md` |
| `04-evaluation/images/14-agent-evaluation-01-agent-evaluation-record-imagegen.png` | `exec-37671904-8764-4cfc-a4a4-36a00922d99e`; `.tmp/llm-orchestration-evaluation-image-rollout.md` |
| `07-project-example/images/02-evaluating-retrieval-01-hit-rate-mrr-imagegen.png` | `exec-08941298-2622-41bc-934d-fd83af38af1b`; `.tmp/llm-orchestration-evaluation-image-rollout.md` |
| `07-project-example/images/03-evaluating-rag-01-llm-judge-imagegen.png` | `exec-a900407c-13e7-401a-83f0-ce5be3debdb3`; `.tmp/llm-orchestration-evaluation-image-rollout.md` |
| `07-project-example/images/07-chunking-01-long-document-chunks-imagegen.png` | `exec-2d920a25-7fe4-43b4-be91-370897c4bdd9`; `.tmp/llm-orchestration-evaluation-image-rollout.md` |

The five conceptual entries in this table that have no local original JPG are
explicitly recorded as semantic-reference regenerations in the rollout note;
they are not relabeled as screenshot-derived chains.

## Standalone prompt-native imagegen references left unchanged

These 23 active lesson illustrations are clean, C2PA-bearing imagegen assets
created as conceptual diagrams rather than redraws of workshop screenshots.
No corresponding original non-crisp JPG exists in the repository's retained
evidence, so no synthetic JPG or misleading crop was added. The images remain
unchanged and are not claimed as durable JPG → crop → output chains.

### Agentic RAG

- `01-agentic-rag/images/01-intro-01-rag-project-overview-imagegen.png`
- `01-agentic-rag/images/08-rag-helper-01-reusable-rag-helper-imagegen.png`
- `01-agentic-rag/images/10-rag-next-steps-01-rag-roadmap-imagegen.png`
- `01-agentic-rag/images/12-rag-revision-01-typo-retry-imagegen.png`
- `01-agentic-rag/images/16-other-frameworks-01-shared-agent-loop-imagegen.png`

### Vector search

- `02-vector-search/images/10-next-steps-01-similarity-search-imagegen.png`

### Orchestration

- `03-orchestration/images/01-intro-01-ai-orchestration-path-imagegen.png`
- `03-orchestration/images/02-context-engineering-01-context-quality-flow-imagegen.png`
- `03-orchestration/images/03-setup-01-secure-kestra-setup-imagegen.png`
- `03-orchestration/images/08-best-practices-01-pattern-selection-imagegen.png`

### Evaluation

- `04-evaluation/images/15-next-steps-01-evaluation-feedback-loop-imagegen.png`

### Monitoring

- `05-monitoring/images/10-feedback-dashboard-01-monitoring-panels-imagegen.png`
- `05-monitoring/images/11-synthetic-data-01-live-data-loop-imagegen.png`
- `05-monitoring/images/13-docker-compose-01-service-topology-imagegen.png`

### Best practices

- `06-best-practices/images/01-intro-01-rag-technique-map-imagegen.png`
- `06-best-practices/images/02-hybrid-search-01-keyword-vector-fusion-imagegen.png`
- `06-best-practices/images/03-reranking-01-rrf-rerank-imagegen.png`
- `06-best-practices/images/04-langchain-01-retriever-wrapper-imagegen.png`
- `06-best-practices/images/05-next-steps-01-retrieval-roadmap-imagegen.png`

### Project example

- `07-project-example/images/01-intro-01-fitness-rag-project-imagegen.png`
- `07-project-example/images/04-interface-01-api-ingestion-flow-imagegen.png`
- `07-project-example/images/05-monitoring-01-compose-observability-imagegen.png`
- `07-project-example/images/06-summary-01-project-delivery-path-imagegen.png`

## Audit result

- 37/37 active Markdown imagegen references resolve.
- 30/30 non-accepted active references were audited: seven received durable
  source-JPG → native-crop → imagegen repairs; 23 are prompt-native diagrams
  with no source JPG available to reconstruct honestly.
- 7/7 newly generated outputs contain C2PA metadata and were checked at native
  resolution and simulated 608px width.
- Existing originals were preserved; no lesson Markdown, code, labels, numbers,
  or reference structure was changed.
