# Module 1: Introduction
## 1.1 Introduction to LLM and RAG

### LLM
#### What is LLM
- Large Language Model
- Large, has billions of parameters, trained on tons of data.

#### What is Language Model
- Used to predict the next token/word based on words user input.

#### Basic Flow

``` "Prompt" -> LLM -> Answer ```

### RAG
#### What is RAG
- Retrieval Augmented Generation
- Retrieval = Search
- Generation = LLM
- Give context to LLM to generate answer based on the search.

## 1.2 Preparing the Environment
### Running code on Github Codespace
- At public repo, click `code` and then `codespace` tab

### Installing packages
``` pip install tqdm notebook==7.1.2 openai elasticsearch scikit-learn pandas ```

### Get openai API keys
[Platform.openai.com](platform.openai.com)

### Set key on workspace
```python export OPENAI_API_KEY="key" ```

### Sample code running OpenAi Chatcompletion
[Intro to openai](./Note/Intro%20to%20Openai.ipynb)

## 1.3 Retrieval and Search
[RAG notebook](./RAG.ipynb)
- We will use the search engine we build in the [build-your-own-search-engine workshop](https://github.com/alexeygrigorev/build-your-own-search-engine): [minsearch](https://github.com/alexeygrigorev/minsearch)
- Or install minsearch using pip
```bash pip install minsearch ```
- Indexing the documents
- Peforming the search

## 1.4 - Generating Answers with gpt-4o
- Invoking OpenAI API
- Building the prompt
- Getting the answer

## 1.5 Cleaned RAG flow
- Cleaning the code we wrote so far
- Making it modular

## 1.6
if running the code on Git Bash on Windows, add winpty in front.
```bash 
docker run -it \
   --rm \
   --name elasticsearch \
   -p 9200:9200 \
   -p 9300:9300 \
   -e "discovery.type=single-node" \
   -e "xpack.security.enabled=false" \
   elasticsearch:9.0.1
```