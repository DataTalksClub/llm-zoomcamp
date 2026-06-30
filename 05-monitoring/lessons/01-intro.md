# Monitoring

Video: [Watch this lesson](https://www.youtube.com/watch?v=lbEj3Waxs1U&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous module we evaluated our system offline, before anyone
used it. We measured search quality with Hit Rate and MRR, and answer
quality with cosine similarity and an LLM judge.

But once we deploy, real people start asking real questions. The offline
numbers stop telling the whole story. We don't know how long answers
take, what they cost, or whether anyone finds them useful. We need to
watch the system while it runs.

That's monitoring: online evaluation. We collect metrics from the
running system and put them on a dashboard. Then we can see how it
performs with real traffic.

For every question that comes in, there's a lot we can capture:

- The instructions, prompt, and model behind the answer
- Input and output tokens, and how much the call cost
- Response time: how long the person waited
- User feedback: a thumbs up or thumbs down on the answer
- Relevance: does the answer address the question?

Collecting and viewing all of this takes three new pieces:

- a user interface where people ask questions
- a database to store conversations and feedback
- a dashboard to visualize the metrics

We build all three on top of the RAG pipeline from the earlier modules.
We don't rebuild the RAG part. We wrap it in a Streamlit app and save
every interaction to PostgreSQL. Then we put a dashboard in front of the
data. At the end we add Grafana for a more powerful view.

We focus on RAG here. Monitoring an agent works almost the same way, so
we leave it as homework. The [agents module](../../01-agentic-rag/)
already has the pieces you need to apply these same ideas there.

## Prerequisites

This module builds on the project from module 1. On top of those
libraries, we use psycopg (the PostgreSQL driver) and Streamlit here.

If you're starting from scratch, clone the course repo and install the
dependencies for this module:

```bash
git clone https://github.com/DataTalksClub/llm-zoomcamp.git llm-zoomcamp-2026-code
cd llm-zoomcamp-2026-code
uv init
uv add requests minsearch openai jupyter python-dotenv "psycopg[binary]" streamlit
```

You also need a `.env` file with your API key. See the
[module 1 environment setup](../../01-agentic-rag/lessons/02-environment.md)
for details.

[← Back to module](../) | [Assistant →](02-assistant-setup.md)
