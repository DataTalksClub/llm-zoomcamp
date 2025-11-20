# chat_starter_qdrant — README

Quick steps to get this folder running: set up Python/UV, prepare Qdrant (Docker), extract documents into Qdrant, run the chat backend (UV), run the Phoenix frontend, interact with the chat (ask course questions), then run evaluation to push reference and compute QA quality / hallucination metrics for RAG.

Prerequisites
- Docker (for Qdrant)
- uv
- Python 3.12+
- Git (optional)

1) Project setup (virtual environment + deps)
- Create and activate a venv:
    - bash (macOS / Linux)
        ```bash
        uv sync
        source .venv/bin/activate
        ```
    - Windows (PowerShell)
        ```powershell
        uv sync
        python -m venv .venv
        .\.venv\Scripts\Activate.ps1
        ```

2) Environment variables
- Copy or create a `.env` file with at least:
    ```
    OPENAI_API_KEY=sk-...
    # any other engine or DB variables used by the code
    ```
- Load env vars (some projects load .env automatically; otherwise export them in your shell).

3) Start Qdrant (Docker)
- Quick Docker run:
    ```bash
    docker run -p 6333:6333 -p 6334:6334 --name qdrant -d qdrant/qdrant
    ```
- Verify Qdrant is healthy:
    ```bash
    curl http://localhost:6333/collections || echo "Qdrant not responding"
    ```

4) Document extraction / ingestion into Qdrant
- Run the ingestion/extraction script provided in this folder (replace with actual script name/args):
    ```bash
    # example — replace with the repo's script
    python documents_extraction.py 
    ```
- Confirm documents were ingested:
    ```bash
    # list collections
    curl http://localhost:6333/collections
    ```


5) Run Phoenix frontend (if present)
- Run below:
    ```bash
    phoenix serve
    ```
- Phoenix default: http://localhost:6006

6) Interact with the streamlit chat
- Run below:
    ```
    streamlit run chat.py
    ```
- Ask course-related questions (examples):
    - "What is the scope of the ml Zoomcamp course?"
    - "How long is the course?"
    - "Do I need to submit homework each week?"
- Observe responses and check that answers reference ingested documents.
- Streamlit default: http://localhost:8501

7) Evaluation (push reference, QA quality, hallucination in RAG)
- Run evaluation scripts included in the repo:
    ```bash
    # example evaluation runner — replace with actual path/flags
    python evaluation.py
    ```
- Observe the results in Phoenix UI
