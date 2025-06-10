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