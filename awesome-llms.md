# Awesome LLMs

In this file, we will collect all interesting links

## OpenAI API Alternatives

OpenAI and GPT are not the only hosted LLMs that we can use. There are
many other services, and most of them expose an OpenAI-compatible API,
so you usually only need to change the `base_url`, API key, and model name.

> Free tiers change often. This list was last reviewed on **2026-06-30** —
> double-check current limits before relying on them.

### Free to use (ongoing free tier, no payment required)

* [Google Gemini](https://ai.google.dev/) (free rate-limited tier on Flash / Flash-Lite models, no card; this is the same as Google AI Studio)
* [Groq](https://console.groq.com/) (free rate-limited dev tier, no card)
* [Mistral AI](https://console.mistral.ai/) (free rate-limited "Experiment" tier, no card)
* [OpenRouter](https://openrouter.ai/) (single OpenAI-compatible API routing to many providers; free access to ~26 `:free` models, ~50 req/day, no card)
* [Z.AI (GLM)](https://z.ai/model-api) (genuinely free rate-limited GLM Flash models)
* [Cerebras](https://cloud.cerebras.ai/) (free ~1M tokens/day, resets daily, no card)
* [SambaNova Cloud](https://cloud.sambanova.ai/) (free rate-limited tier, no card, plus a one-time $5 credit)
* [GitHub Models](https://github.com/marketplace/models) (free rate-limited prototyping tier for any GitHub user via a `models:read` token)
* [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/get-started/) (free 10,000 Neurons/day across hosted open-source models)
* [Cohere](https://dashboard.cohere.com/) (free trial key, ~1,000 calls/month, non-commercial use only)
* [OVH AI Endpoints](https://endpoints.ai.cloud.ovh.net/) (rate-limited free API access)
* [HuggingFace Inference](https://huggingface.co/docs/inference-providers/pricing) (minimal: ~$0.10/month routed-inference credit, then pay-as-you-go)
* [wit.ai](https://wit.ai/) (Meta's NLP service, free)

### Free signup credits, then paid

* [Anthropic API](https://console.anthropic.com/) (~$5 one-time signup credit after phone verification)
* [AI21 Labs](https://studio.ai21.com/) ($10 trial credits, valid 7 days, no card)
* [xAI Grok](https://console.x.ai/) (~$25 promo signup credit, expires 30 days; OpenAI-compatible API)
* [DeepSeek](https://platform.deepseek.com/) (one-time credit for new accounts, then low-cost pay-per-token)
* [AWS Bedrock](https://aws.amazon.com/bedrock/) (new AWS accounts get up to $200 credits / 6 months; needs an AWS account and per-model access approval)
* [NVIDIA NIM](https://build.nvidia.com/) (no-card developer access to 100+ hosted models, limited credits)
* [Scaleway Generative APIs](https://www.scaleway.com/en/generative-apis/) (1,000,000 free tokens one-time for new EU customers)
* [Hyperbolic](https://app.hyperbolic.ai/) ($1 promo credit after phone verification)
* [Nebius Token Factory](https://tokenfactory.nebius.com/) ($1 trial credit, valid 30 days)
* [Fireworks AI](https://app.fireworks.ai/signup) ($1 starter credit)

### Paid only (no free tier)

* [Together AI](https://www.together.ai/pricing) (no free tier; ~$5 minimum credit purchase)
* [Replicate](https://replicate.com/pricing) (pay-per-use; only some "Try for Free" models)


## Local LLMs on CPUs

These services help run LLMs locally, also without GPUs

- [ollama](https://github.com/ollama/ollama)
- [LM Studio](https://lmstudio.ai/)
- [vLLM](https://github.com/vllm-project/vllm) (high-throughput serving, GPU; exposes an OpenAI-compatible endpoint)
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
  - [TextLens API](https://ckmtools.dev/textlens) - REST API for readability scoring, sentiment analysis, and keyword extraction
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



