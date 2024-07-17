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

<a href="https://www.youtube.com/watch?v=E0cAqBWfJYY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/E0cAqBWfJYY">
</a>

* Registering in Saturn Cloud
* Configuring secrets and git
* Creating an instance with a GPU

```bash
pip install -U transformers accelerate bitsandbytes sentencepiece
```

Links:

* https://saturncloud.io/
* https://github.com/DataTalksClub/llm-zoomcamp-saturncloud

Google Colab as an alternative:

* [Video](https://www.loom.com/share/591f39e4e231486bbfc3fbd316ec03c5)
* [Notebook](https://colab.research.google.com/drive/1XmxUZutZXoAEdQZU45EXWPseBX9s2NRd)

## 2.3 FLAN-T5

<a href="https://www.youtube.com/watch?v=a86iTyxnFE4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/a86iTyxnFE4">
</a>

* Model: `google/flan-t5-xl`
* Notebook: [huggingface-flan-t5.ipynb](huggingface-flan-t5.ipynb)

```bash
import os
os.environ['HF_HOME'] = '/run/cache/'
```

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

<a href="https://www.youtube.com/watch?v=8KH6AS2PqWk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/8KH6AS2PqWk">
</a>

* Model: `microsoft/Phi-3-mini-128k-instruct`
* Notebook: [huggingface-phi3.ipynb](huggingface-phi3.ipynb)


Links:

* https://huggingface.co/microsoft/Phi-3-mini-128k-instruct

## 2.5 Mistral-7B and HuggingFace Hub Authentication

<a href="https://www.youtube.com/watch?v=TdVEOzSoUCs&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/TdVEOzSoUCs">
</a>

* Model: `mistralai/Mistral-7B-v0.1`
* Notebook: [huggingface-mistral-7b.ipynb](huggingface-mistral-7b.ipynb)

[ChatGPT instructions for serving](serving-hugging-face-models.md) 


Links:

* https://huggingface.co/docs/transformers/en/llm_tutorial
* https://huggingface.co/settings/tokens
* https://huggingface.co/mistralai/Mistral-7B-v0.1


## 2.6 Other models

<a href="https://www.youtube.com/watch?v=GzPV_HTmCkc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/GzPV_HTmCkc">
</a>

* [`LLM360/Amber`](https://huggingface.co/LLM360/Amber)
* [Gemma-7B](https://huggingface.co/blog/gemma)
* [SaulLM-7B](https://huggingface.co/papers/2403.03883) 
* [Granite-7B](https://huggingface.co/ibm-granite/granite-7b-base)
* [MPT-7B](https://huggingface.co/mosaicml/mpt-7b)
* [OpenLLaMA-7B](https://huggingface.co/openlm-research/open_llama_7b)

Where to find them:

* Leaderboards 
* Google
* ChatGPT

Links:

* https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
* https://huggingface.co/spaces/optimum/llm-perf-leaderboard


## 2.7 Ollama - Running LLMs on a CPU

<a href="https://www.youtube.com/watch?v=PVpBGs_iSjY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/PVpBGs_iSjY">
</a>

* The easiest way to run an LLM without a GPU is using [Ollama](https://github.com/ollama/ollama)
* Notebook [ollama.ipynb](ollama.ipynb)

For Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh

ollama start
ollama pull phi3
ollama run phi3
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
docker exec -it ollama bash
ollama pull phi3
```


## 2.8 Ollama & Phi3 + Elastic in Docker-Compose

<a href="https://www.youtube.com/watch?v=4juoo_jk96U&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/4juoo_jk96U">
</a>

* Creating a Docker-Compose file 
* Re-running the module 1 notebook

* Notebook: [rag-intro.ipynb](rag-intro.ipynb)

## 2.9 UI for RAG

<a href="https://www.youtube.com/watch?v=R6L8PZ-7bGo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/R6L8PZ-7bGo">
</a>

* Putting it in Streamlit
* [Code](qa_faq.py)

If you want to learn more about streamlit, you can
use [this material](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md)
from [our repository with projects of the week](https://github.com/DataTalksClub/project-of-the-week/tree/main).

## Homework

See [here](../cohorts/2024/02-open-source/homework.md)

# Notes

* [Workaround by Pham Nguyen Hung to use ElasticSearch container with Saturn Cloud & Google Colab instead of minsearch](https://hung.bearblog.dev/llm-zoomcamp-zrok/)
* [Notes by slavaheroes](https://github.com/slavaheroes/llm-zoomcamp/blob/homeworks/02-open-source/notes.md)
* [Notes by Pham Nguyen Hung](https://hung.bearblog.dev/llm-zoomcamp-2-os/)
* [Notes by Marat on Open-Sourced and Closed-Sourced Models and ways to run them](https://machine-mind-ml.medium.com/open-sourced-vs-closed-sourced-llms-2392c7db6e10)
* [Notes by dimzachar](https://github.com/dimzachar/llm_zoomcamp/blob/master/notes/02-open-source/README.md)
* [Notes by Waleed](https://waleedayoub.com/post/llmzoomcamp_week2-open-source_notes/)
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
