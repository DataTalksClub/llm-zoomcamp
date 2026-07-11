## Homework: Monitoring

In module 4 we evaluated our RAG system offline.
In module 5 we take that system online: real people ask real questions,
and we need to watch what happens while it runs.

For every question that comes in, we capture

- the tokens
- the cost
- the response time
- user feedback
- automatic relevance label from an LLM judge

We store all of it in PostgreSQL and
put it on a dashboard - Streamlit or Grafana.

In this homework we work through that pipeline the same way as in the
module.

> It's possible your answers won't match exactly. In this case, select the closest one.


For the LLM, we recommend OpenAI with `gpt-5.4-mini`, but you can use any model
and provider you like. Put your key in a
`.env` file as in the earlier modules.

## The data model

Every LLM call produces a bundle of values we want to keep together. We
record them in the `LLMCallRecord` dataclass from
[`metrics.py`](../../../05-monitoring/code/metrics.py). It carries the
model, the prompt and instructions, the answer, the token counts
(prompt, completion, total), the response time, the cost, and a
timestamp.

We save each record to the `conversations` table in PostgreSQL, and we
collect feedback (from users and from the judge) in a separate `feedback`
table.

## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and) and in the [course's learning in public guide](https://datatalks.club/docs/courses/zoomcamp-logistics/learning-in-public/).

### Example post for LinkedIn

Tag [@Alexey Grigorev](https://www.linkedin.com/in/agrigorev/) and [@DataTalksClub](https://www.linkedin.com/company/datatalks-club/) in your post - we'll like and comment to give your post more reach.

```
🚀 Module 5 of LLM Zoomcamp by @DataTalksClub complete!

Just finished Module 5 - Monitoring. Learned how to:

✅ Capture LLM metrics (tokens, cost, response time) for every call
✅ Store conversations and feedback in PostgreSQL
✅ Collect user feedback with thumbs up/down and automatic relevance from an LLM judge
✅ Build dashboards in Streamlit and Grafana to watch the system in real time

Here's my homework solution: <LINK>

Following along with this amazing free course by @Alexey Grigorev - who else is learning to build with LLMs?

You can sign up here: https://github.com/DataTalksClub/llm-zoomcamp/
```

### Example post for X

```
📊 Module 5 of LLM Zoomcamp done!

- LLM call metrics: tokens, cost, response time
- PostgreSQL for conversations and feedback
- LLM judge + user feedback
- Dashboards in Streamlit and Grafana

My solution: <LINK>

Free course by @Al_Grigor & @DataTalksClub: https://github.com/DataTalksClub/llm-zoomcamp/
```

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw5
* It's possible your answers won't match exactly. If so, select the closest one.
