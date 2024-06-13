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

Prompt example:

```
Question: I just discovered the couse. can i still enrol

Context:

Course - Can I still join the course after the start date?
Yes, even if you don't register, you're still eligible to submit the homeworks.
Be aware, however, that there will be deadlines for turning in the final projects. So don't leave everything for the last minute.

Environment - Is Python 3.9 still the recommended version to use in 2024?
Yes, for simplicity (of troubleshooting against the recorded videos) and stability. [source]
But Python 3.10 and 3.11 should work fine.

How can we contribute to the course?
Star the repo! Share it with friends if you find it useful ❣️
Create a PR if you see you can improve the text or the structure of the repository.

Are we still using the NYC Trip data for January 2021? Or are we using the 2022 data?
We will use the same data, as the project will essentially remain the same as last year’s. The data is available here

Docker-Compose - docker-compose still not available after changing .bashrc
This is happen to me after following 1.4.1 video where we are installing docker compose in our Google Cloud VM. In my case, the docker-compose file downloaded from github named docker-compose-linux-x86_64 while it is more convenient to use docker-compose command instead. So just change the docker-compose-linux-x86_64 into docker-compose.

Answer:
```

Connecting to it with OpenAI API:

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
```

## 2.8 Ollama & Phi3 + Elastic in Docker-Compose




## 2.9 Serving LLMs 


