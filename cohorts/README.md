# Cohorts

The current curriculum — every module, unit, image and code sample — lives at
the **repository root**, not here. `cohorts/<year>/` holds only what is
specific to one delivery of the course: dates, homework, and (for a past
cohort) a frozen copy of the curriculum as it was taught that year.

**2026 is the current cohort. Fix curriculum at the repository root, not
inside `cohorts/2026/`.** This is recorded once, machine-readably, at the
root: `course.yaml:current_cohort` names it, and `course.yaml:cohorts` lists
every cohort and where its content actually lives.

## Layout

```
<repo root>/
├── course.yaml                   # course identity, incl. the description and cohorts index
├── 01-agentic-rag/               # the directory name IS the module slug
│   ├── module.yaml                 # module identity and unit list
│   ├── README.md                   # GitHub-facing module index, not published
│   ├── 01-intro.md                 # units: NN-kebab.md, the stem IS the unit slug
│   ├── 02-environment.md
│   └── code/                       # notebooks and scripts the units link
├── ...
└── cohorts/
    ├── README.md                  # this file
    ├── 2026/                      # the directory name IS the cohort identifier
    │   ├── cohort.yaml            # dates, curriculum: current, homework list
    │   ├── README.md              # the human-readable schedule
    │   ├── workshops/             # non-module cohort material is allowed
    │   └── homework/
    │       ├── 01-agentic-rag/
    │       │   ├── homework.md    # homework instructions, fixed name
    │       │   └── homework.yaml  # homework identity, due date, form, questions
    │       └── ...
    ├── 2025/                      # earlier cohort: frozen, full copy
    └── 2024/
```

Two rules carry most of the weight:

- **Names are identity.** The module slug and the unit slug are the directory
  and file names. Nothing in YAML restates them, and renaming one moves a
  published URL.
- **A module directory is self-contained.** Its units, images and code live
  inside it, units are siblings of `module.yaml`, and a relative link never
  climbs past the module directory except into a sibling module or the
  repository root. Anything further away is written as an absolute GitHub URL.

## Current cohort vs. frozen cohort

A cohort's `cohort.yaml` says which kind it is:

- **`curriculum: current`** — the cohort teaches whatever is currently at the
  repository root. `cohorts/<year>/` carries only dates and homework
  (`cohorts/<year>/homework/<module>/`); there is no module or lesson content
  here to duplicate or drift from the root.
- **`curriculum: github_archive`** — the cohort's curriculum was materially
  different from what root teaches now, so it was frozen: a full,
  standalone copy of every module it taught. It is kept for GitHub readers
  only and is never re-imported as current module or lesson content.
  `cohorts/2024/` and `cohorts/2025/` are this repository's archives,
  retrofitted with a minimal `cohort.yaml` after the fact — their interior
  (module directories, differing numbering/naming from 2026, README files)
  is untouched pre-migration content, not reshaped to match the current
  convention. `course.yaml:cohorts` marks both `legacy: true` for exactly
  that reason.

## Editing

- Fix curriculum content (lessons, images, code) at the **repository root**.
  That is where pull requests for the current cohort are accepted.
- Fix dates or homework for the current cohort under `cohorts/2026/`.
- Earlier, frozen cohorts are archives: the drift is the record of what was
  actually taught. Backport only factual or breaking errors, and do it
  per-cohort explicitly.
- A published slug is frozen. Renaming one is a platform decision, not a
  repository pull request.

## The conventions themselves

This repository does not restate them. `DataTalksClub/zoomcamp-ops` is the
authority: `STRUCTURE.md` for the repository layout and
`docs/shared-curriculum-v2.md` for the shared-root schema this repository
follows, plus the curriculum contract documented beside it for the YAML
schemas and the unit page rules. The `scripts/check-zoomcamp/` conformance
checker in that repository reports what a change breaks before it is pushed.

The website's ingestion parser is the final authority and fails loudly on
push; the checker exists so that almost never happens.
