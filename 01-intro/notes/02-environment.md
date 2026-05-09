# Environment

For this workshop, all you need is Python with Jupyter.

I use GitHub Codespaces to run it, but you can use whatever
environment you like.


## Prerequisites

- Python (3.11 or later)
- An [OpenAI account](https://openai.com/) (or an OpenAI-compatible
  provider like Groq, Gemini, or Ollama)
- Basic familiarity with Python and the command line


## Setting up Github Codespaces

GitHub Codespaces is the recommended environment for this workshop.

But you can use any other environment with Jupyter Notebook.
If you want to do it on your laptop, that's perfectly fine.

- Open this repository in GitHub Codespaces, or copy the
  `01-intro` folder into your own repository
- Add the OpenAI key:
    - Go to Settings -> Secrets and Variables (under Security) -> Codespaces
    - Click "New repository secret"
    - Name: `OPENAI_API_KEY`, Secret: your key
    - Click "Add secret"
- Create a codespace
    - Click "Code"
    - Select the "Codespaces" tab
    - "Create codespace on main"

In case you use it on your laptop, set the API key before you start
Jupyter:

```bash
export OPENAI_API_KEY='YOUR_KEY'
```


## Creating the project

We'll start from scratch - no cloning needed. You'll create the
project yourself, step by step.

First, install uv (a fast Python package manager):

```bash
pip install uv
```

Create an empty folder for the project and initialize it:

```bash
mkdir llm-zoomcamp-code
cd llm-zoomcamp-code
uv init
```

This creates a `pyproject.toml` and a basic project structure.

Now add the dependencies we'll need:

```bash
uv add requests minsearch openai jupyter
```

This installs:

- `requests` - to fetch the FAQ dataset from the internet
- `minsearch` - a simple in-memory search engine for indexing and
  searching text
- `openai` - the OpenAI API client for calling the LLM
- `jupyter` - the notebook environment where we'll write and run code

Start Jupyter:

```bash
uv run jupyter notebook
```

Create a new notebook. Throughout the workshop, you'll copy code from the section notes into notebook cells. Check that the OpenAI client works:

```python
from openai import OpenAI
openai_client = OpenAI()
```

For Groq or other OpenAI-compatible providers:

```python
from openai import OpenAI
import os

openai_client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url='https://api.groq.com/openai/v1'
)
```

If you see an error, make sure you set the key correctly.

