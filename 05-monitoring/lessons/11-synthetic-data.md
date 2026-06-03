# Synthetic Data Generation

When you first set up Grafana, there's no data to visualize. You could
use the app manually for a while, but that's slow. Instead, we generate
synthetic data to populate the dashboards.

We create two types of data:

- Historical data: conversations spread over the last 6 hours
- Live data: new conversations inserted every second

## Sample data

Create `generate_data.py`.

Imports and sample data:

```python
import time
import random
from datetime import datetime, timedelta
from db_init import get_db_connection, DB_TIMEZONE
from db_save import save_conversation
from db_feedback import save_feedback
from metrics import LLMCallRecord
```

```python
SAMPLE_QUESTIONS = [
    "How do I install Docker?",
    "Can I still join the course?",
    "What are the prerequisites?",
    "How do I submit homework?",
    "When are the office hours?",
]

SAMPLE_ANSWERS = [
    "You can install Docker by downloading Docker Desktop from the official website.",
    "Yes, you can join at any time. The materials remain available.",
    "You need basic Python knowledge and familiarity with the command line.",
    "Submit your homework through the course portal before the deadline.",
    "Office hours are held weekly. Check the calendar for details.",
]

COURSES = [
    "data-engineering-zoomcamp",
    "machine-learning-zoomcamp",
    "mlops-zoomcamp",
]

RELEVANCE = ["RELEVANT", "PARTLY_RELEVANT", "NON_RELEVANT"]
```

## Generating conversations

A helper to create a fake `LLMCallRecord`:

```python
def fake_record(question, answer):
    return LLMCallRecord(
        model="gpt-5.4-mini",
        prompt=question,
        instructions="",
        answer=answer,
        prompt_tokens=random.randint(50, 200),
        completion_tokens=random.randint(50, 300),
        total_tokens=random.randint(100, 500),
        response_time=random.uniform(0.5, 5.0),
        cost=random.uniform(0.0001, 0.01),
    )
```

## Historical data

Generate conversations spread across a time range:

```python
def generate_historical(start_time, end_time):
    current_time = start_time
    count = 0

    while current_time < end_time:
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        record = fake_record(question, answer)

        conversation_id = save_conversation(record, question, course)

        if random.random() < 0.7:
            relevance = random.choice(RELEVANCE)
            save_feedback(
                conversation_id, "judge",
                relevance=relevance,
                explanation=f"Answer is {relevance.lower()}.",
            )

        if random.random() < 0.5:
            score = 1 if random.random() < 0.8 else -1
            save_feedback(conversation_id, "user", score=score)

        current_time += timedelta(minutes=random.randint(1, 15))
        count += 1

    print(f"Generated {count} historical conversations")
```

## Live data

Keep inserting new conversations every second:

```python
def generate_live():
    print("Starting live data generation (Ctrl+C to stop)...")
    try:
        while True:
            question = random.choice(SAMPLE_QUESTIONS)
            answer = random.choice(SAMPLE_ANSWERS)
            course = random.choice(COURSES)
            record = fake_record(question, answer)

            conversation_id = save_conversation(record, question, course)

            if random.random() < 0.7:
                relevance = random.choice(RELEVANCE)
                save_feedback(
                    conversation_id, "judge",
                    relevance=relevance,
                    explanation=f"Answer is {relevance.lower()}.",
                )

            if random.random() < 0.5:
                score = 1 if random.random() < 0.8 else -1
                save_feedback(conversation_id, "user", score=score)

            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped.")
```

## Running it

```python
if __name__ == "__main__":
    end_time = datetime.now(DB_TIMEZONE)
    start_time = end_time - timedelta(hours=6)

    print(f"Generating data from {start_time} to {end_time}")
    generate_historical(start_time, end_time)

    generate_live()
```

Run it:

```bash
uv run python generate_data.py
```

The script first backfills 6 hours of data, then keeps generating live
data every second. We'll use this data in Grafana in the next lesson to
see the dashboard come alive with charts updating in real time.

[← Feedback Dashboard](10-feedback-dashboard.md) | [Grafana →](12-grafana.md)
