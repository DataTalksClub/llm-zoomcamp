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
| `04-metrics-05-printed-call-record.jpg` | 11/12 (2,2,1,2,2,2) | keep / deterministic crop | Shows the updated assistant construction alongside a real printed call record containing response-time, token, and cost fields. Crop `580x259+29+61`; removes the webcam tile, browser/recording chrome, and watermark while preserving exact output; the source's lower edge remains truncated. |
| `04-metrics-06-streamlit-metrics-display.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows response time, prompt/completion tokens, and cost under a completed answer in the running app. Crop `420x325+100+35`; removes browser chrome, webcam tile, and watermark. |
| `05-database-02-timezone-aware-timestamp.jpg` | 8/12 (1,2,1,0,2,2) | remove / redundant | The frame is a GitHub-rendered copy of the exact schema printed immediately below it; it adds no runtime state or evidence. The primary-question test fails despite the caption being specific, and the source also contains a selection/cursor artifact. Original JPEG preserved. |
| `05-database-03-db-init-run.jpg` | 11/12 (2,2,2,1,2,2) | keep / deterministic crop | Shows `db_init.py` and the successful `Database initialized` result, adding runtime evidence to the source code. Crop `503x360+29+0`; removes the webcam tile and Zoom watermark while preserving exact code/output. |
| `05-database-06-psql-check-conversations.jpg` | 12/12 (2,2,2,2,2,2) | keep / deterministic crop | Shows the saved conversation row in PostgreSQL, including the question, response time, and cost values that the surrounding code writes. Crop `503x360+29+0`; removes the webcam tile and Zoom watermark while preserving exact terminal output. |
| `06-querying-03-conversations-from-psql.jpg` | 12/12 (2,2,2,2,2,2) | keep / deterministic crop | Shows the query script reading persisted conversations back from PostgreSQL, including the returned row and the transition from write to read. Crop `503x360+29+0`; removes the webcam tile and Zoom watermark while preserving exact code/output. |
| `07-streamlit-dashboard-04-charts-response-time.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the response-time-over-time plot and a recent conversation in the running dashboard, making the time-series result visible. Crop `420x325+100+35`; removes browser chrome, webcam tile, and Zoom watermark; the native chart tooltip/cursor state is retained as exact UI evidence. |
| `07-streamlit-dashboard-06-dashboard-overview.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the four summary metrics—conversations, average response time, total cost, and average tokens—on the running dashboard. Crop `420x325+100+35`; removes browser chrome, webcam tile, and Zoom watermark. |
| `08-user-feedback-06-app-feedback-buttons.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the user-facing +1 and -1 controls below an answered question, complementing the code with the actual interaction surface. Crop `420x325+100+35`; removes browser chrome, webcam tile, and Zoom watermark; the source's text selection remains documented as a native UI artifact. |
| `08-user-feedback-07-thanks-after-click.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the state transition after a positive rating: the controls remain and the app displays `Thanks!`. Crop `420x325+100+35`; removes browser chrome, webcam tile, and Zoom watermark while preserving the exact UI state. |
| `09-built-in-judge-04-judge-run-output.jpg` | 12/12 (2,2,2,2,2,2) | keep / deterministic crop | Shows the judge code and its real `relevance` verdict plus explanation in the terminal, which is the key runtime evidence for this lesson. Crop `503x360+29+0`; removes the webcam tile and Zoom watermark while preserving exact code/output. |
| `12-grafana-02-add-datasource-list.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the Grafana data-source picker and the PostgreSQL option learners must select. Crop `580x259+29+61`; removes browser chrome, webcam tile, and Zoom watermark while preserving the exact UI labels. |
| `12-grafana-03-postgres-datasource-config.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the configured PostgreSQL host, database, user, and SSL mode that connect Grafana to the course database. Crop `580x259+29+61`; removes browser chrome, webcam tile, and Zoom watermark while preserving exact fields and labels. |
| `12-grafana-06-token-usage-query.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the token-usage time-series result and the exact Grafana SQL query using time buckets and `AVG(total_tokens)`. Crop `580x259+29+61`; removes browser chrome, webcam tile, and Zoom watermark while preserving exact query and chart. |
| `12-grafana-08-finished-dashboard-panels.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the completed Grafana layout with cost and relevance panels, making the assembled monitoring result concrete. Crop `580x259+29+61`; removes browser chrome, webcam tile, and Zoom watermark while preserving exact panel values and relationships. |
| `14-next-steps-01-grafana-dashboard-recap.jpg` | 5/12 (1,2,1,0,1,0) | remove / redundant and mismatched | The visible state is a `Save dashboard` dialog over a partial dashboard, not the dashboard recap named by the caption. It duplicates the finished dashboard evidence in lesson 12 and adds no new learner-facing fact. Original JPEG preserved. |
| `14-next-steps-02-app-relevance-verdict.jpg` | 11/12 (2,2,2,2,1,2) | keep / deterministic crop | Shows the completed assistant answer together with the judge's `PARTLY_RELEVANT` verdict and explanation, making the second quality signal concrete. Crop `420x325+100+35`; removes browser chrome, webcam tile, and Zoom watermark; native text selection is retained as exact UI state. |
