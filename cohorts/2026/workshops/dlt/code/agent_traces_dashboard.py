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
    # Claude Code Agent Logs API — Report

    Data loaded from `GET /logs` (Claude Code Agent Logs API) into DuckDB
    via the `agent_traces` dlt pipeline — 1,000 log records with nested
    message content normalized into a child table.
    """)
    return


@app.cell
def _(dlt):
    pipeline = dlt.attach("agent_traces")
    dataset = pipeline.dataset()
    return (dataset,)


@app.cell
def _(mo):
    mo.md("""
    ## Log types and activity
    """)
    return


@app.cell
def _(dataset):
    df_chart1 = dataset("""
        SELECT type, COUNT(*) AS records
        FROM logs
        GROUP BY 1
        ORDER BY records DESC
    """).df()
    return (df_chart1,)


@app.cell
def _(alt, df_chart1):
    _chart = alt.Chart(df_chart1).mark_bar().encode(
        x=alt.X("type:N", sort="-y"),
        y="records:Q",
        color="type:N",
        tooltip=["type:N", "records:Q"],
    ).properties(title="Logs by Type")
    _chart
    return


@app.cell
def _(dataset):
    df_chart2 = dataset("""
        SELECT
            DATE_TRUNC('minute', timestamp) AS minute,
            type,
            COUNT(*) AS records
        FROM logs
        GROUP BY 1, 2
        ORDER BY 1, 2
    """).df()
    return (df_chart2,)


@app.cell
def _(alt, df_chart2):
    _chart = alt.Chart(df_chart2).mark_line().encode(
        x="minute:T",
        y="records:Q",
        color="type:N",
        tooltip=["minute:T", "type:N", "records:Q"],
    ).properties(title="Log Activity per Minute by Type")
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## Work by git branch
    """)
    return


@app.cell
def _(dataset):
    df_chart3 = dataset("""
        SELECT git_branch, COUNT(*) AS records
        FROM logs
        GROUP BY 1
        ORDER BY records DESC
    """).df()
    return (df_chart3,)


@app.cell
def _(alt, df_chart3):
    _chart = alt.Chart(df_chart3).mark_bar().encode(
        x=alt.X("git_branch:N", sort="-y"),
        y="records:Q",
        color="git_branch:N",
        tooltip=["git_branch:N", "records:Q"],
    ).properties(title="Logs by Git Branch")
    _chart
    return


@app.cell
def _(dataset):
    df_chart4 = dataset("""
        SELECT git_branch, SUM(usage__output_tokens) AS output_tokens
        FROM logs
        WHERE usage__output_tokens IS NOT NULL
        GROUP BY 1
        ORDER BY output_tokens DESC
    """).df()
    return (df_chart4,)


@app.cell
def _(alt, df_chart4):
    _chart = alt.Chart(df_chart4).mark_bar().encode(
        x=alt.X("git_branch:N", sort="-y"),
        y="output_tokens:Q",
        color="git_branch:N",
        tooltip=["git_branch:N", "output_tokens:Q"],
    ).properties(title="Output Tokens by Git Branch")
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## Content and sessions
    """)
    return


@app.cell
def _(dataset):
    df_chart5 = dataset("""
        SELECT type, COUNT(*) AS blocks
        FROM logs__message__content
        GROUP BY 1
        ORDER BY blocks DESC
    """).df()
    return (df_chart5,)


@app.cell
def _(alt, df_chart5):
    _chart = alt.Chart(df_chart5).mark_bar().encode(
        x=alt.X("type:N", sort="-y"),
        y="blocks:Q",
        color="type:N",
        tooltip=["type:N", "blocks:Q"],
    ).properties(title="Message Content Block Types")
    _chart
    return


@app.cell
def _(dataset):
    df_chart6 = dataset("""
        SELECT cnt AS msgs_per_session, COUNT(*) AS sessions
        FROM (
            SELECT session_id, COUNT(*) AS cnt
            FROM logs
            GROUP BY 1
        )
        GROUP BY 1
        ORDER BY 1
    """).df()
    return (df_chart6,)


@app.cell
def _(alt, df_chart6):
    _chart = alt.Chart(df_chart6).mark_bar().encode(
        x=alt.X("msgs_per_session:O", title="messages per session"),
        y=alt.Y("sessions:Q", title="number of sessions"),
        tooltip=["msgs_per_session:O", "sessions:Q"],
    ).properties(title="Distribution of Messages per Session")
    _chart
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
