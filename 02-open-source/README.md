# 2. Open-Source LLMs

In the previous module, we used OpenAI via OpenAI API. It's
a very convenient way to use an LLM, but you have to pay 
for the usage, and you don't have control over the 
model you get to use.

In this module, we'll look at using open-source LLMs instead.

## 2.1 Open-Source LLMs - Introduction



## 2.2 Using a GPU in Saturn Cloud


## 2.3 FLAN-T5


Links:

* 

## 2.4 Phi 3 Mini


`microsoft/Phi-3-mini-128k-instruct`

Links:

* 

## 2.5 HuggingFace Hub Authentication


`mistralai/Mistral-7B-v0.1`

Links:

* https://huggingface.co/docs/transformers/en/llm_tutorial
* https://huggingface.co/settings/tokens
* https://huggingface.co/mistralai/Mistral-7B-v0.1

## 2.6 Other models

* `LLM360/Amber`
* ``

Where to find them:

* Leaderboards 
* Google
* ChatGPT


## 2.7 Ollama - Running LLMs on a CPU

Video

The easiest way to run an LLM without a GPU is using [Ollama](https://github.com/ollama/ollama)

For Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh

ollama start
ollama serve phi3
```

[Prompt example](prompt.md)

Connecting to it with OpenAI API:

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
```

Docker

```bash
docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Pulling the model

```bash
docker exec -it bash
ollama pull phi3
```


## 2.8 Ollama & Phi3 + Elastic in Docker-Compose

Video

* Creating a Docker-Compose file 
* Re-running the module 1 notebook


## 2.9 UI for RAG

* Putting it in Streamlit
