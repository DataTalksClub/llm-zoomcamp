# LLM Zoomcamp 2024 Competition

In the competition, you need to use LLMs to solve high school mathematics problems. 
Your task is to develop models that can accurately solve these problems and submit your predictions.

For more details, visit the [competition page](https://www.kaggle.com/competitions/llm-zoomcamp-2024-competition/overview).


## Getting started

Getting started code: [starter_notebook.ipynb](starter_notebook.ipynb)

You will need to install langchain for this code:

```bash
pip install -qU langchain-openai langchain
```

Thanks [Blaq](https://www.linkedin.com/in/chinonsoodiaka/) for contibuting the notebook!

## Evaluation

We use accuracy as the evaluation metric. Sometimes multiple
answers are correct. In this case, a solution is correct if
it matches at least one of the possible answers. 

You can find the code for evaluation in [scorer.py](scorer.py) - it's taken [from kaggle](https://www.kaggle.com/code/dremovd/accuracy-multiple-correct?scriptVersionId=158029538)
and this is exactly the code we use in the competition.
