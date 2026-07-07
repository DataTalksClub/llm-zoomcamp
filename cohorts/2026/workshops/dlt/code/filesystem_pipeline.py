"""dlt filesystem pipeline: load raw AI-agent session logs into DuckDB.

Sources: Claude Code (`~/.claude`), a Claude variant (`~/.zlaude`), Codex
(`~/.codex`), and a Codex variant (`~/.zodex`). Every source stores sessions as
JSONL transcripts with heterogeneous per-line records, so we keep each line
verbatim in a `data` column and pull a few lightweight fields up for
convenience. All four sources land in one unified table, `log_records`,
discriminated by an `agent` column. Model later with DuckDB's JSON functions.
"""

import json
from pathlib import Path
from typing import Iterator, Optional

import dlt
from dlt.sources import TDataItems
from dlt.sources.filesystem import FileItemDict, filesystem

HOME = str(Path.home())

# agent name -> (bucket_url, file_glob). Claude-style layouts keep sessions
# under projects/; Codex-style layouts keep them under sessions/YYYY/MM/DD/.
SOURCES = {
    "claude": (f"file://{HOME}/.claude", "projects/**/*.jsonl"),
    "zlaude": (f"file://{HOME}/.zlaude", "projects/**/*.jsonl"),
    "codex": (f"file://{HOME}/.codex", "sessions/**/*.jsonl"),
    "zodex": (f"file://{HOME}/.zodex", "sessions/**/*.jsonl"),
}

TABLE_NAME = "log_records"


def _session_id_from_name(file_name: str) -> str:
    """The session id lives in the filename for every source.

    Claude/zlaude: '<uuid>.jsonl'. Codex/zodex: 'rollout-<ts>-<uuid>.jsonl',
    where the uuid is the trailing five dash-joined groups.
    """
    stem = file_name[:-6] if file_name.endswith(".jsonl") else file_name
    if stem.startswith("rollout-"):
        parts = stem.split("-")
        if len(parts) >= 5:
            return "-".join(parts[-5:])
    return stem


def raw_reader(agent: str):
    """Build a transformer that turns each JSONL line into a raw record row."""

    @dlt.transformer(name=f"read_{agent}")
    def _read(items: Iterator[FileItemDict]) -> Iterator[TDataItems]:
        for file_obj in items:
            file_name = file_obj["file_name"]
            rel_path = file_obj.get("relative_path", file_name)
            session_id = _session_id_from_name(file_name)
            rows = []
            with file_obj.open() as f:  # binary; decode per line, tolerate bad utf-8
                for line_no, raw in enumerate(f):
                    if isinstance(raw, bytes):
                        raw = raw.decode("utf-8", errors="replace")
                    line = raw.strip()
                    if not line:
                        continue
                    rec_type: Optional[str] = None
                    ts: Optional[str] = None
                    try:
                        rec = json.loads(line)
                        if isinstance(rec, dict):
                            rec_type = rec.get("type")
                            t = rec.get("timestamp")
                            ts = t if isinstance(t, str) else (str(t) if t is not None else None)
                    except json.JSONDecodeError:
                        pass
                    rows.append(
                        {
                            "agent": agent,
                            "session_id": session_id,
                            "source_file": rel_path,
                            "line_no": line_no,
                            "type": rec_type,
                            "timestamp": ts,
                            "data": line,
                        }
                    )
            if rows:
                yield rows

    return _read


def build_resources(sample: bool = False):
    resources = []
    for agent, (bucket_url, file_glob) in SOURCES.items():
        files = filesystem(
            bucket_url=bucket_url,
            file_glob=file_glob,
            files_per_page=1 if sample else 100,
        )
        if sample:
            files = files.add_limit(1)  # one file per source for a quick verify
        resources.append(files | raw_reader(agent))
    return resources


def load(sample: bool = False) -> None:
    pipeline = dlt.pipeline(
        pipeline_name="agent_logs",
        destination="duckdb",
        dataset_name="agent_logs",
        dev_mode=sample,  # throwaway dataset for sample runs; keep data for full load
    )
    info = pipeline.run(
        build_resources(sample=sample),
        table_name=TABLE_NAME,
        write_disposition="replace",
    )
    print(info)
    print(pipeline.last_trace.last_normalize_info)


if __name__ == "__main__":
    import sys

    load(sample="--sample" in sys.argv)
