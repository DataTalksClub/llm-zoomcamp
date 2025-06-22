## Homework: Evaluation and Monitoring

In this homework, we'll evaluate the quality of our RAG system.

> It's possible that your answers won't match exactly. If it's the case, select the closest one.

## Getting the data

Let's start by getting the dataset. We will use the data we generated in the module.

In particular, we'll evaluate the quality of our RAG system
with [gpt-4o-mini](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/04-monitoring/data/results-gpt4o-mini.csv)


Read it:

```python
url = f'{github_url}?raw=1'
df = pd.read_csv(url)
```

We will use only the first 300 documents:


```python
df = df.iloc[:300]
```

## Q1. Getting the embeddings model

Now, get the embeddings model `multi-qa-mpnet-base-dot-v1` from
[the Sentence Transformer library](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html#model-overview)

> Note: this is not the same model as in HW3

```bash
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer(model_name)
```

Create the embeddings for the first LLM answer:

```python
answer_llm = df.iloc[0].answer_llm
```

What's the first value of the resulting vector?

* -0.42
* -0.22
* -0.02
* 0.21

**Answer**: -0.42

We just need to run the code: 
```python
answer_llm = df.iloc[0].answer_llm
print("Answer: ",answer_llm)
embedd_answer = model.encode(answer_llm)
print("Embedding: ",embedd_answer[0])
```
The output is:
```text
Answer:  You can sign up for the course by visiting the course page at [http://mlzoomcamp.com/](http://mlzoomcamp.com/).
Embeddings:  -0.42244655
```

## Q2. Computing the dot product


Now for each answer pair, let's create embeddings and compute dot product between them

We will put the results (scores) into the `evaluations` list

What's the 75% percentile of the score?

* 21.67
* 31.67
* 41.67
* 51.67

**Answer**: 31.67

We generate the dot product between the LLM answer and the original one:
```python
from tqdm.auto import tqdm

evaluations=[]
for doc in tqdm(documents):
    answer_llm_emb = model.encode(doc['answer_llm'])
    answer_orig_emb = model.encode(doc['answer_orig'])
    dot_product= answer_llm_emb.dot(answer_orig_emb)
    evaluations.append(dot_product)

print("Count of evaluations:", len(evaluations))
print(evaluations)
```

And the we calculate the percentile 75%:
```python
import numpy as np

p75 = np.percentile(evaluations, 75)
print("Percentile 75%: ", p75)
```

Output:
```text
Percentile 75%:  31.67430877685547
```

## Q3. Computing the cosine

From Q2, we can see that the results are not within the [0, 1] range. It's because the vectors coming from this model are not normalized.

So we need to normalize them.

To do it, we 

* Compute the norm of a vector
* Divide each element by this norm

So, for vector `v`, it'll be `v / ||v||`

In numpy, this is how you do it:

```python
norm = np.sqrt((v * v).sum())
v_norm = v / norm
```

    Let's put it into a function and then compute dot product 
    between normalized vectors. This will give us cosine similarity

    What's the 75% cosine in the scores?

* 0.63
* 0.73
* 0.83
* 0.93

**Anmswer**: 0.83

This time we define a function to calculte the normalized vector and we apply it to both embeddings:
```python
def normalize_vector(v):
    norm = np.sqrt((v * v).sum())
    if norm != 0:
        v_norm = v / norm
    else:
        v_norm= 0
    return v_norm

evaluations=[]
for doc in tqdm(documents):
    answer_llm_emb = normalize_vector(model.encode(doc['answer_llm']))
    answer_orig_emb = normalize_vector(model.encode(doc['answer_orig']))
    cosine_sim= answer_llm_emb.dot(answer_orig_emb)
    evaluations.append(cosine_sim)

print("Count of evaluations:", len(evaluations))
print(evaluations)    
```

And then we can calculate the 75th percentile:
```python
import numpy as np

p75 = np.percentile(evaluations, 75)
print("Percentile 75%: ", p75)
```
```text
Percentile 75%:  0.8362348973751068
```

## Q4. Rouge

Now we will explore an alternative metric - the ROUGE score.  

This is a set of metrics that compares two answers based on the overlap of n-grams, word sequences, and word pairs.

It can give a more nuanced view of text similarity than just cosine similarity alone.

We don't need to implement it ourselves, there's a python package for it:

```bash
pip install rouge
```

(The latest version at the moment of writing is `1.0.1`)

Let's compute the ROUGE score between the answers at the index 10 of our dataframe (`doc_id=5170565b`)

```
from rouge import Rouge
rouge_scorer = Rouge()

scores = rouge_scorer.get_scores(r['answer_llm'], r['answer_orig'])[0]
```

There are three scores: `rouge-1`, `rouge-2` and `rouge-l`, and precision, recall and F1 score for each.

* `rouge-1` - the overlap of unigrams,
* `rouge-2` - bigrams,
* `rouge-l` - the longest common subsequence

What's the F score for `rouge-1`?

- 0.35
- 0.45
- 0.55
- 0.65

**Answer**: 0.45

Simply:
```python
from rouge import Rouge
rouge_scorer = Rouge()

scores = rouge_scorer.get_scores(documents[10]['answer_orig'], documents[10]['answer_llm'])[0]
print("Rouge Score: \n", scores)
```
```text
Rouge Score: 
 {'rouge-1': {'r': 0.45454545454545453, 'p': 0.45454545454545453, 'f': 0.45454544954545456}, 'rouge-2': {'r': 0.21621621621621623, 'p': 0.21621621621621623, 'f': 0.21621621121621637}, 'rouge-l': {'r': 0.42424242424242425, 'p': 0.42424242424242425, 'f': 0.42424241924242434}}
```

## Q5. Average rouge score

Let's compute the average between `rouge-1`, `rouge-2` and `rouge-l` for the same record from Q4

- 0.35
- 0.45
- 0.55
- 0.65

**Answer**: 0.35

We have the scores, so we only need to calkculate the mean:
```python
np.mean([scores['rouge-1']['f'],scores['rouge-2']['f'], scores['rouge-l']['f']])
```

or

```python
rouge_1 = scores['rouge-1']['f']
rouge_2 = scores['rouge-2']['f']
rouge_l = scores['rouge-l']['f']
rouge_avg = (rouge_1 + rouge_2 + rouge_l) / 3
print("Avg score: ",rouge_avg)
```

and the output is:
```text
Avg score:  0.36500136000136507
```

## Q6. Average rouge score for all the data points

Now let's compute the score for all the records

```python
rouge_1 = scores['rouge-1']['f']
rouge_2 = scores['rouge-2']['f']
rouge_l = scores['rouge-l']['f']
rouge_avg = (rouge_1 + rouge_2 + rouge_l) / 3
```

And create a dataframe from them

What's the agerage `rouge_2` across all the records?

- 0.10
- 0.20
- 0.30
- 0.40

**Answer**: 0.30

We generate the rouge scores and save the average for every data point:

```python
def avg_rouge_score(scores):
    rouge_1 = scores['rouge-1']['f']
    rouge_2 = scores['rouge-2']['f']
    rouge_l = scores['rouge-l']['f']
    
    rouge_avg = (rouge_1 + rouge_2 + rouge_l) / 3    

    return rouge_avg

evaluations=[]
for doc in tqdm(documents):
    scores = rouge_scorer.get_scores(doc['answer_llm'], doc['answer_orig'])[0]
    avg_score= avg_rouge_score(scores)
    evaluations.append(avg_score)

print("Count of evaluations:", len(evaluations))
print(evaluations)    
```

Then create a dataframe and get the mean value:
```python
df_rouge= pd.DataFrame(evaluations, columns=['avg_rouge_score'])
df_rouge.mean()
```

```text
avg_rouge_score    0.313205
dtype: float64
```
