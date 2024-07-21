# Awesome LLMs

In this file, we will collect all interesting links

## OpenAI API Alternatives

OpenAI and GPT are not the only hosted LLMs that we can use. 
There are other services that we can use


* [mistral.ai](https://mistral.ai) (5€ free credit on sign up)
* [Groq](https://console.groq.com) (can inference from open source LLMs with rate limits)
* [TogetherAI](https://api.together.ai) (can inference from variety of open source LLMs, 25$ free credit on sign up)
* [Google Gemini](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python) (2 months unlimited access)
* [OpenRouterAI](https://openrouter.ai/) (some small open-source models, such as Gemma 7B, are free)
* [HuggingFace API](https://huggingface.co/docs/api-inference/index) (over 150,000 open-source models, rate-limited and free)
* [Cohere](https://cohere.com/) (provides a developer trail key which allows upto 100 reqs/min for generating, summarizing, and classifying text. Read more [here](https://cohere.com/blog/free-developer-tier-announcement))
* [wit](https://wit.ai/) (Facebook AI Afiliate - free)
* [Anthropic API](https://www.anthropic.com/pricing#anthropic-api) (starting from $0.25 / MTok for input and $1.25 / MTok for the output for the most affordable model)
* [AI21Labs API](https://www.ai21.com/pricing#foundation-models) (Free trial including $10 credits for 3 months)
* [Replicate](https://replicate.com/) (faster inference, can host any ML model. charges 0.10$ per 1M input tokens for llama/Mistral model)


## Local LLMs on CPUs

These services help run LLMs locally, also without GPUs

- [ollama](https://github.com/ollama/ollama)
- [Jan.AI](https://jan.ai/)
- [h2oGPT](https://github.com/h2oai/h2ogpt)


## Applications
- **Text Generation**
  - [OpenAI GPT-3 Playground](https://platform.openai.com/playground)
  - [AI Dungeon](https://play.aidungeon.io/)
- **Chatbots**
  - [Rasa](https://rasa.com/)
  - [Microsoft Bot Framework](https://dev.botframework.com/)
- **Sentiment Analysis**
  - [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
  - [TextBlob](https://textblob.readthedocs.io/en/dev/)
- **Summarization**
  - [Sumy](https://github.com/miso-belica/sumy)
  - [Hugging Face Transformers Summarization](https://huggingface.co/transformers/task_summary.html)
- **Translation**
  - [MarianMT by Hugging Face](https://huggingface.co/transformers/model_doc/marian.html)

## Fine-Tuning
- **Guides and Tutorials**
  - [Fine-Tuning GPT-3](https://platform.openai.com/docs/guides/fine-tuning)
  - [Hugging Face Fine-Tuning Tutorial](https://huggingface.co/transformers/training.html)
- **Tools and Frameworks**
  - [Hugging Face Trainer](https://huggingface.co/transformers/main_classes/trainer.html)
  - [Fastai](https://docs.fast.ai/text.learner.html)
- **Colab Notebooks**
  - [Fine-Tuning BERT on Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification.ipynb)
  - [Fine-Tuning GPT-2 on Colab](https://colab.research.google.com/github/fastai/course-v3/blob/master/nbs/dl2/12a_ulmfit.ipynb)

## Prompt Engineering
- **Techniques and Best Practices**
  - [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/completions/best-practices)
  - [Prompt Design for GPT-3](https://beta.openai.com/docs/guides/prompt-design)
- **Tools**
  - [Prompt Designer](https://promptdesigner.com/)
  - [Prompt Engineering Toolkit](https://github.com/prompt-engineering/awesome-prompt-engineering)
- **Examples and Case Studies**
  - [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
  - [GPT-3 Prompt Engineering Examples](https://github.com/shreyashankar/gpt-3-sandbox)

## Deployment
- **Hosting Services**
  - [Hugging Face Inference API](https://huggingface.co/inference-api)
  - [AWS SageMaker](https://aws.amazon.com/sagemaker/)
- **Serverless Deployments**
  - [Serverless GPT-3 with AWS Lambda](https://towardsdatascience.com/building-serverless-gpt-3-powered-apis-with-aws-lambda-f2d4b8a91058)
  - [Deploying on Vercel](https://vercel.com/guides/deploying-next-and-vercel-api-with-openai-gpt-3)
- **Containerization**
  - [Dockerizing a GPT Model](https://medium.com/swlh/dockerize-your-gpt-3-chatbot-28dd48c19c91)
  - [Kubernetes for ML Deployments](https://towardsdatascience.com/kubernetes-for-machine-learning-6c7f5c5466a2)

## Monitoring and Logging
- **Best Practices**
  - [Logging and Monitoring AI Models](https://www.dominodatalab.com/resources/whitepapers/logging-and-monitoring-for-machine-learning)
  - [Monitor Your NLP Models](https://towardsdatascience.com/monitor-your-nlp-models-40c2fb141a51)

## Ethics and Bias
- **Frameworks and Guidelines**
  - [AI Ethics Guidelines Global Inventory](https://algorithmwatch.org/en/project/ai-ethics-guidelines-global-inventory/)
  - [Google AI Principles](https://ai.google/principles/)
- **Tools**
  - [Fairness Indicators](https://www.tensorflow.org/tfx/guide/fairness_indicators)
  - [IBM AI Fairness 360](https://aif360.mybluemix.net/)
- **Research Papers**
  - [Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification](http://gendershades.org/overview.html)
  - [AI Fairness and Bias](https://arxiv.org/abs/1908.09635)



