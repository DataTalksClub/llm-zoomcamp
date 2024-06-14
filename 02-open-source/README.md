# 2. Open-Source LLMs

In the previous module, we used OpenAI via OpenAI API. It's
a very convenient way to use an LLM, but you have to pay 
for the usage, and you don't have control over the 
model you get to use.

In this module, we'll look at using open-source LLMs instead.

## 2.1 Open-Source LLMs - Introduction

<a href="https://www.youtube.com/watch?v=ATchkIRsH4g&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ATchkIRsH4g">
</a>

* Open-Source LLMs
* Replacing the LLM box in the RAG flow

## 2.2 Using a GPU in Saturn Cloud



## 2.3 FLAN-T5

Video

```bash
import os
os.environ['HF_HOME'] = '/run/cache/'
```

Model: `google/flan-t5-xl`


Links:

* https://huggingface.co/google/flan-t5-xl
* https://huggingface.co/docs/transformers/en/model_doc/flan-t5

Explanation of Parameters:

* `max_length`: Set this to a higher value if you want longer responses. For example, `max_length=300`.
* `num_beams`: Increasing this can lead to more thorough exploration of possible sequences. Typical values are between 5 and 10.
* `do_sample`: Set this to `True` to use sampling methods. This can produce more diverse responses.
* `temperature`: Lowering this value makes the model more confident and deterministic, while higher values increase diversity. Typical values range from 0.7 to 1.5.
* `top_k` and `top_p`: These parameters control nucleus sampling. `top_k` limits the sampling pool to the top `k` tokens, while `top_p` uses cumulative probability to cut off the sampling pool. Adjust these based on the desired level of randomness.


## 2.4 Phi 3 Mini

Video

Model: `microsoft/Phi-3-mini-128k-instruct`


Links:

* https://huggingface.co/microsoft/Phi-3-mini-128k-instruct

## 2.5 Mistral-7B and HuggingFace Hub Authentication


Model: `mistralai/Mistral-7B-v0.1`

[ChatGPT instructions for serving](serving-hugging-face-models.md) 


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
