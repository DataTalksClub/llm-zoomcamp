## Homework: Evaluation

In homework 2 we built keyword, vector, and hybrid search over the course
lessons, and ended with an open question: which one is best? The way to answer
that is to measure, and that's what we do here.

In this homework we generate a ground truth dataset and use it to evaluate
search, the same way we did in the module. There we only evaluated keyword
search. Here we also evaluate vector and hybrid search, so we can finally
compare them on numbers instead of intuition.

Like in homework 1 and 2, our knowledge base is the course lessons themselves.
Each module has a `lessons/` folder of numbered markdown pages, and we pull
them from GitHub. We use commit `8c1834d`, so everyone works with the exact
same 72 pages.

> It's possible your answers won't match exactly. If so, select the closest one.

## Setup

This homework continues from homework 2. We reuse the same chunks and the same
search functions, so it's easiest to keep working in the same project.

We need a few more libraries for generating questions with an LLM:

```bash
uv add openai pydantic python-dotenv pandas
```

For the LLM, we recommend OpenAI with `gpt-5.4-mini`, but you can use any model
and provider you like - just adapt the client accordingly. Put your key in a
`.env` file as in the earlier modules.

Load the data exactly as in homework 2:

```python
from gitsource import GithubRepositoryDataReader

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)
documents = [file.parse() for file in reader.read()]
```

This gives 72 pages.

## Generating ground truth

To evaluate search, we need a dataset of questions where we know which document
is the correct answer. This is the ground truth.

We generate it the same way as in the module. For each lesson page, we ask an
LLM to write 5 questions that are answered by that page. Each question is then
labeled with the page it came from.

We use the same structured-output approach as in the module - the same
`Questions` model and the `llm_structured` helper from `evaluation_utils.py`.

Download `evaluation_utils.py` and the `rag_helper.py` it depends on:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget ${PREFIX}/01-agentic-rag/code/rag_helper.py
wget ${PREFIX}/04-evaluation/code/evaluation_utils.py
```

The module's instructions generate questions from a FAQ record, so we adapt
them for a lesson page:

```python
data_gen_instructions = """
You emulate a student who is taking our LLM course.
You are given one lesson page from the course.
Formulate 5 questions this student might ask that are answered by this page.

Rules:
- The page should contain the answer to each question.
- Make the questions complete and not too short.
- Use as few words as possible from the page; don't copy its phrasing.
- The questions should resemble how people actually ask things online:
  not too formal, not too short, not too long.
- Ask about the content of the lesson, not about its formatting or filename.
""".strip()
```

We ask for different wording from the page on purpose. Real users don't phrase
their questions the way the lesson does, and copying the text would make the
evaluation too easy.

For each page, build a JSON user prompt from its `filename` and `content`, then
call `llm_structured` with the `Questions` model. Turn each returned question
into a record labeled with the page's `filename`. The call also returns the
token usage, the same as in the lessons.

## Q1. Generating questions

Generating questions for all 72 pages costs money and takes time, so let's
start small and generate questions for just the first 3 pages:

- `01-agentic-rag/lessons/01-intro.md`
- `01-agentic-rag/lessons/02-environment.md`
- `01-agentic-rag/lessons/03-rag.md`

Each call returns the token usage, which most LLM APIs report on the response
object (e.g. `response.usage.input_tokens` / `prompt_tokens`).

What's the average number of input tokens across these 3 calls?

* 140
* 1400
* 14000
* 140000

> These numbers vary between runs, even with the same model, so pick the closest
> option. A different provider or model may land further apart, but the input
> tokens stay in the same order of magnitude - the prompt we send is the same.

## The full ground truth

You don't need to generate the data for the rest of the homework. We already
did it for all 72 pages, using the same approach as in the lessons, and saved
the 360 questions to a file.

Download it:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget ${PREFIX}/cohorts/2026/04-evaluation/ground-truth.csv
```

Load it with pandas into a list of records called `ground_truth`. Each record
has a `question` and the `filename` of the page that should answer it.

## Searching the chunks

We search over the same chunks as in homework 2.

Create them with `chunk_documents`:

```python
from gitsource import chunk_documents

chunks = chunk_documents(documents, size=2000, step=1000)
```

This gives 295 chunks.

Now rebuild the search from homework 2 over these chunks. Build a text index
(`Index`) and a vector index (`VectorSearch`), both keyed on `filename`. Wrap
each one in a function, `text_search` and `vector_search`, that takes a query
and the number of results to return (5 by default).

For hybrid search, reuse the `rrf` function from homework 2:

```python
def rrf(result_lists, k=60, num_results=5):
    scores = {}
    docs = {}

    for results in result_lists:
        for rank, doc in enumerate(results):
            key = (doc["filename"], doc["start"])
            scores[key] = scores.get(key, 0) + 1 / (k + rank)
            docs[key] = doc

    ranked = sorted(scores, key=scores.get, reverse=True)
    return [docs[key] for key in ranked[:num_results]]
```

Then define `hybrid_search` on top of it:

```python
def hybrid_search(query, k=60):
    text_results = text_search(query, num_results=10)
    vector_results = vector_search(query, num_results=10)
    return rrf([text_results, vector_results], k=k)
```

## Q2. First result with text search

Take the first question from the ground truth:

```python
q = ground_truth[0]["question"]
```

After running `text_search` for it, what's the `filename` of the first result?

* `01-agentic-rag/lessons/01-intro.md`
* `01-agentic-rag/lessons/03-rag.md`
* `01-agentic-rag/lessons/13-function-calling.md`
* `01-agentic-rag/lessons/10-rag-next-steps.md`

## Q3. First result with vector search

After running `vector_search` for the same question, what's the `filename` of
the first result?

* `01-agentic-rag/lessons/01-intro.md`
* `01-agentic-rag/lessons/03-rag.md`
* `04-evaluation/lessons/11-evaluation-intro.md`
* `04-evaluation/lessons/12-rag-answers.md`

This question was generated from `01-agentic-rag/lessons/01-intro.md`. Notice
that one method finds the right page at the top and the other doesn't. That's
exactly why we measure across the whole dataset instead of trusting one query.

## Evaluation metrics

We evaluate search exactly as in the module, reusing the same functions from the
lecture. We change only the label. Our ground truth uses `filename`, so a result
counts as a hit when a returned chunk's `filename` matches the question's
`filename`, not a document `id`.

As a reminder, these functions do the following:

- `compute_relevance` runs search for a question and returns a list of 0s and 1s
- `hit_rate` is the fraction of questions where the correct page appears in the results
- `mrr` (Mean Reciprocal Rank) also rewards finding the page near the top
- `evaluate` runs a search function over the whole ground truth and returns both metrics

## Q4. Evaluating text search

Evaluate `text_search` on the ground truth data.

What's the Hit Rate?

* 0.55
* 0.66
* 0.76
* 0.88

## Q5. Evaluating vector search

Now evaluate `vector_search` - the part we left for the homework, since the
module only evaluated keyword search.

What's the MRR?

* 0.35
* 0.45
* 0.55
* 0.65

## Q6. Tuning hybrid search

The `k` constant in RRF controls how much the top ranks matter. A smaller `k`
sharpens the gap between positions, so being at the top of a list counts for
more. The RRF paper uses 60 as a default, but the best value depends on the data
- so let's measure it.

Evaluate `hybrid_search` over the full ground truth dataset for `k` values 1,
50, 100, and 200. Compare the MRR values for these runs.

Which `k` gives the best MRR?

* 1
* 50
* 100
* 200

> Several values of `k` may give the same MRR. If there's a tie, pick the
> smallest `k`.

## Using this framework

You now have an `evaluate` function that takes any search function and returns
Hit Rate and MRR.

Use it to measure any change you make to search:

- tune the field boosts in keyword search
- try a different embedding model for vector search
- change `k` in the RRF formula for hybrid search
- change the number of results you return

Change a setting, re-run `evaluate`, and see whether the metric moves. The
ground truth stays fixed, so the comparison is fair. That's how you replace
guessing with measuring.

## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and) and in the [course's learning in public guide](https://datatalks.club/docs/courses/zoomcamp-logistics/learning-in-public/).

### Example post for LinkedIn

Tag [@Alexey Grigorev](https://www.linkedin.com/in/agrigorev/) and [@DataTalksClub](https://www.linkedin.com/company/datatalks-club/) in your post - we'll like and comment to give your post more reach.

```
🚀 Module 4 of LLM Zoomcamp by @DataTalksClub complete!

Just finished Module 4 - Evaluation. Learned how to:

✅ Generate ground truth questions with an LLM and structured output
✅ Measure retrieval quality with Hit Rate and MRR
✅ Evaluate keyword, vector, and hybrid search on the same dataset
✅ Replace gut-feeling with numbers when comparing search methods

Here's my homework solution: <LINK>

Following along with this amazing free course by @Alexey Grigorev - who else is learning to build with LLMs?

You can sign up here: https://github.com/DataTalksClub/llm-zoomcamp/
```

### Example post for X

```
📏 Module 4 of LLM Zoomcamp done!

- Ground truth generation with structured output
- Hit Rate and MRR
- Evaluating keyword vs vector vs hybrid search
- Measuring instead of guessing

My solution: <LINK>

Free course by @Al_Grigor & @DataTalksClub: https://github.com/DataTalksClub/llm-zoomcamp/
```

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw4
* It's possible your answers won't match exactly. If so, select the closest one.
