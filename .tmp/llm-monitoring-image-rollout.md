# LLM Zoomcamp monitoring image rollout

Scope: `cohorts/2026/05-monitoring/**`.

The inventory contains 20 local Markdown image references. Every source was
inspected with the lesson context and the illustration rubric. The imagegen
skill was available, but none of these sources is a bounded explanatory
diagram: all are exact code, terminal output, Streamlit states, plots, or
Grafana UI. Imagegen was therefore intentionally not used; generated text or
numbers would risk changing the lesson's evidence. The retained sources use
deterministic crops and Lanczos upscaling, with originals preserved. Crop
coordinates are in source pixels as `WIDTHxHEIGHT+X+Y`.

The crop preparation files and contact sheets are disposable and remain under
`.tmp/llm-monitoring-image-rollout-crops/` until the final cleanup.

## Per-source decisions

Each retained source has a focused commit containing its sibling asset,
Markdown reference, and this report entry. The one removed reference has a
focused removal commit; its original source file remains preserved.

| Source | Rubric score | Decision | Teaching point / reason |
| --- | ---: | --- | --- |
