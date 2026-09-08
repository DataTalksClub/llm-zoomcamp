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
| `01-intro-02-ragbase-pipeline-code.jpg` | 11/12 (2,2,2,1,2,2) | keep / deterministic crop | Shows the reusable search, prompt-building, and LLM call stages. Crop `503x360+29+0`; removes side border, webcam tile, and Zoom watermark while preserving exact code. |
| `02-assistant-04-makefile-run-target.jpg` | 11/12 (2,2,2,1,2,2) | keep / deterministic crop | Shows the `make run` target and the assistant's terminal response, proving the command-line entry point works. Crop `503x360+29+0`; exact command and output are retained, with the source's long terminal lines still edge-truncated. |
| `03-chat-app-03-answer-in-browser.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the user-facing chat flow and a completed answer in the browser, which the code and prose cannot demonstrate as directly. Crop `420x325+100+35`; removes browser chrome, webcam tile, and Zoom watermark. |
