# Course repository layout

Shared lesson content lives in the top-level module directories. Each module keeps its
`module.yaml`, ordered Unit Markdown, and module overview material. A module directory must not
contain a copy of a cohort's Homework.

Each `cohorts/<identifier>/` directory owns the delivery-specific composition and assessment
content:

- `cohort.yaml` selects the legacy or module-based presentation and orders the flow;
- `homework.yaml` defines the Homework form and Questions;
- the adjacent `homework.md` contains the Homework instructions;
- other files are cohort-only supporting material and are not shared Units unless explicitly
  referenced by the source contract.

The same top-level module may be referenced by more than one Cohort. The platform projects the
shared Unit source into each Cohort without duplicating the Markdown in this repository.
