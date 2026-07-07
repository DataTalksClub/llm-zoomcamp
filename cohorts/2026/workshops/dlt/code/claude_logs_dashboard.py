import marimo

__generated_with = "0.23.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import dlt

    return alt, dlt, mo


@app.cell
def _(mo):
    mo.md("""
    # AI Agent Logs — Overview

    Raw session logs from Claude Code (`claude`, `zlaude`) and Codex (`codex`, `zodex`),
    loaded into DuckDB as one `log_records` table (one row per JSONL line).
    """)
    return


@app.cell
def _(dlt):
    # Catalog name (agent_logs_store) differs from the dataset schema
    # (agent_logs) to avoid DuckDB's ambiguous catalog/schema resolution.
    pipeline = dlt.pipeline(
        pipeline_name="agent_logs",
        destination=dlt.destinations.duckdb("agent_logs_store.duckdb"),
        dataset_name="agent_logs",
    )
    dataset = pipeline.dataset()
    return (dataset,)


@app.cell
def _(mo):
    mo.md("""
    ## Records per day by type

    Daily volume for the 8 most common record types, **log-scaled** so the
    conversational types (`assistant`, `user`) stay visible next to codex's
    high-volume `event_msg` / `response_item` telemetry.
    """)
    return


@app.cell
def _(dataset):
    df_daily_type = dataset("""
        WITH top_types AS (
            SELECT type
            FROM log_records
            WHERE type IS NOT NULL
            GROUP BY 1
            ORDER BY COUNT(*) DESC
            LIMIT 8
        )
        SELECT
            DATE_TRUNC('day', timestamp)::date AS day,
            type,
            COUNT(*) AS records
        FROM log_records
        WHERE timestamp IS NOT NULL
          AND type IN (SELECT type FROM top_types)
        GROUP BY 1, 2
        ORDER BY 1, 2
    """).df()
    return (df_daily_type,)


@app.cell
def _(alt, df_daily_type):
    _chart = alt.Chart(df_daily_type).mark_line(point=True).encode(
        x="day:T",
        y=alt.Y("records:Q", scale=alt.Scale(type="log"), title="records (log scale)"),
        color="type:N",
        tooltip=["day:T", "type:N", "records:Q"],
    ).properties(title="Records per Day by Type", width="container")
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## Activity over time
    """)
    return


@app.cell
def _(dataset):
    df_chart1 = dataset("""
        SELECT
            DATE_TRUNC('day', timestamp) AS day,
            agent,
            COUNT(*) AS records
        FROM log_records
        WHERE timestamp IS NOT NULL
        GROUP BY 1, 2
        ORDER BY 1, 2
    """).df()
    return (df_chart1,)


@app.cell
def _(alt, df_chart1):
    _chart = alt.Chart(df_chart1).mark_line(point=True).encode(
        x="day:T",
        y="records:Q",
        color="agent:N",
        tooltip=["day:T", "agent:N", "records:Q"],
    ).properties(title="Daily Log Activity by Agent")
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## Volume and sessions by agent
    """)
    return


@app.cell
def _(dataset):
    df_chart2 = dataset("""
        SELECT
            agent,
            COUNT(*) AS records
        FROM log_records
        GROUP BY 1
        ORDER BY records DESC
    """).df()
    return (df_chart2,)


@app.cell
def _(alt, df_chart2):
    _chart = alt.Chart(df_chart2).mark_bar().encode(
        x=alt.X("agent:N", sort="-y"),
        y="records:Q",
        color="agent:N",
        tooltip=["agent:N", "records:Q"],
    ).properties(title="Total Log Records by Agent")
    _chart
    return


@app.cell
def _(dataset):
    df_chart3 = dataset("""
        SELECT
            agent,
            COUNT(DISTINCT session_id) AS sessions
        FROM log_records
        GROUP BY 1
        ORDER BY sessions DESC
    """).df()
    return (df_chart3,)


@app.cell
def _(alt, df_chart3):
    _chart = alt.Chart(df_chart3).mark_bar().encode(
        x=alt.X("agent:N", sort="-y"),
        y="sessions:Q",
        color="agent:N",
        tooltip=["agent:N", "sessions:Q"],
    ).properties(title="Distinct Sessions by Agent")
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## Record-type composition
    """)
    return


@app.cell
def _(dataset):
    df_chart4 = dataset("""
        WITH ranked AS (
            SELECT
                agent,
                type,
                COUNT(*) AS records,
                ROW_NUMBER() OVER (PARTITION BY agent ORDER BY COUNT(*) DESC) AS rn
            FROM log_records
            WHERE type IS NOT NULL
            GROUP BY 1, 2
        )
        SELECT
            agent,
            CASE WHEN rn <= 8 THEN type ELSE 'other' END AS type,
            SUM(records) AS records
        FROM ranked
        GROUP BY 1, 2
        ORDER BY agent, records DESC
    """).df()
    return (df_chart4,)


@app.cell
def _(alt, df_chart4):
    _chart = alt.Chart(df_chart4).mark_bar().encode(
        x="agent:N",
        y="records:Q",
        color="type:N",
        tooltip=["agent:N", "type:N", "records:Q"],
    ).properties(title="Record-Type Composition by Agent")
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## Session depth
    """)
    return


@app.cell
def _(dataset):
    df_chart5 = dataset("""
        SELECT
            agent,
            COUNT(*) * 1.0 / COUNT(DISTINCT session_id) AS avg_records_per_session
        FROM log_records
        GROUP BY 1
        ORDER BY avg_records_per_session DESC
    """).df()
    return (df_chart5,)


@app.cell
def _(alt, df_chart5):
    _chart = alt.Chart(df_chart5).mark_bar().encode(
        x=alt.X("agent:N", sort="-y"),
        y=alt.Y("avg_records_per_session:Q", title="avg records / session"),
        color="agent:N",
        tooltip=["agent:N", "avg_records_per_session:Q"],
    ).properties(title="Average Records per Session by Agent")
    _chart
    return


if __name__ == "__main__":
    app.run()
