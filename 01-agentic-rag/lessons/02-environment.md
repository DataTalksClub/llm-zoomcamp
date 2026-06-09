# Environment

Video: [Watch this lesson](https://www.youtube.com/watch?v=3U4gBrmkZyM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

For this module, all you need is Python with Jupyter.

## Prerequisites

You need the following:

- Python (3.14 or later)
- An [OpenAI account](https://openai.com/) (or an OpenAI-compatible
  provider like Groq, Gemini, or Ollama)
- Basic familiarity with Python and the command line

## Creating the project

We'll start from scratch - no cloning needed. You'll create the
project yourself, step by step.

First, install uv. It's a Python package manager, and I switched all my
projects to it because it's fast and convenient. Once I started using
it, I never wanted to go back.

On Mac or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

(You can also use `pip install uv` if you prefer.)

Create an empty folder for the project and initialize it:

```bash
mkdir llm-zoomcamp-2026-code
cd llm-zoomcamp-2026-code
uv init
```

This creates a `pyproject.toml` and a basic project structure.

Now add the dependencies we'll need:

```bash
uv add requests minsearch openai jupyter python-dotenv
```

This installs:

- `requests` - to fetch the FAQ dataset from the internet
- `minsearch` - a simple in-memory search engine for indexing and
  searching text
- `openai` - the OpenAI API client for calling the LLM
- `jupyter` - the notebook environment where we'll write and run code
- `python-dotenv` - to load API keys from a `.env` file

## Setting up API keys

We need an API key to talk to the LLM. If you're using OpenAI, you'll
need to deposit some money first. The minimum is $5 (as of June 2026).
This lesson costs well under 10 cents to run, so that $5 goes a long
way.

I also recommend creating a separate OpenAI project for the course.
Then you can open the usage page and see exactly how much you spent
here, apart from your other work.

The safest way to store the key is in a `.env` file that never gets
committed to git.

Create a `.env` file in your project folder and put your API key in
it:

```bash
OPENAI_API_KEY=sk-YOUR_KEY_HERE
```

Now add `.env` to `.gitignore` to make sure you never accidentally
commit your key:

```bash
.env
```

Never commit `.env` to git. Treat the API key like a password. If it
leaks, someone else can run up charges on your account.

## Starting Jupyter

Start Jupyter:

```bash
uv run jupyter notebook
```

Create a new notebook. Throughout the course, you'll copy code from
the section notes into notebook cells.

Check that the OpenAI client works:

```python
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
openai_client = OpenAI()
```

If you see an error, make sure the key in your `.env` file is
correct.

For Groq or other OpenAI-compatible providers, add the key to
`.env`:

```bash
GROQ_API_KEY=your_key_here
```

And configure the client:

```python
from openai import OpenAI
import os

openai_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
```

## (Optional) Auto-loading .env with dirdotenv

If you don't want to call `load_dotenv()` in every notebook, use
[dirdotenv](https://github.com/alexeygrigorev/dirdotenv).

It loads `.env` files automatically when you `cd` into a directory:

```bash
uv tool install dirdotenv
echo 'eval "$(dirdotenv hook bash)"' >> ~/.bashrc
```

Restart your terminal, and now whenever you enter the project
directory, the variables from `.env` are loaded automatically. No
`load_dotenv()` needed.

[← Introduction](01-intro.md) | [What is RAG →](03-rag.md)
