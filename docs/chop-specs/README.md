# Chop specs

The per-module cut lists ("specs") used to slice each workshop recording into
per-lesson clips, plus the generic chopper `chop.sh`. Full process:
[../video-lesson-chopping.md](../video-lesson-chopping.md).

## Spec format

One line per lesson clip:

```
clipname|start1-end1[,start2-end2,...]
```

- Times are in **seconds** (fractional allowed, e.g. `1860.7`, used where a
  clean cut fell mid-caption-cue).
- Multiple comma-separated ranges are **concatenated** — this drops the gap
  between them (used to cut Q&A, dead air, or fumbles out of the middle).
- Lines starting with `#` are comments.

## Usage

```bash
bash chop.sh <source-720p.mkv> <out-dir> <module>.spec <filename-prefix>
```

Each clip is re-encoded (`libx264 -crf 23 -preset faster`) with YouTube
loudness normalization (`loudnorm=I=-14:TP=-1.5:LRA=11`). Sources are the
best-quality 720p downloads (see the process doc).

## Files

| Spec | Module |
|------|--------|
| `module1-rag.spec` | Module 1 Part 1 — RAG (l01–l10) |
| `module1-agents.spec` | Module 1 Part 2 — Agents (l11–l16) |
| `module2-vector-search.spec` | Module 2 — Vector Search |
| `module4-evaluation.spec` | Module 4 — Evaluation (l01–l06, l11–l15) |
| `module5-monitoring.spec` | Module 5 — Monitoring (l10/l11/l13 deferred to homework — no clip) |

Boundaries land on clean sentence ends; they were hand-tuned during review, so
these reflect the final cuts.
