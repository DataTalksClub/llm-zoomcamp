# Synthetic Data Generation

When you first set up Grafana, there's no data to visualize. You could
use the app manually for a while, but that's slow. Instead, we generate
synthetic data to populate the dashboards.

We create two types of data:

- Historical data: conversations spread over the last 6 hours
- Live data: new conversations inserted every second


## Historical data

We generate conversations with random questions, answers, and metrics,
spaced out over the last 6 hours:

```python
import time
import random
import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from db import save_conversation, save_feedback

tz = ZoneInfo("Europe/Berlin")

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

def generate_historical(start_time, end_time):
    current_time = start_time
    count = 0

    while current_time < end_time:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        relevance = random.choice(RELEVANCE)

        answer_data = {
            "answer": answer,
            "response_time": random.uniform(0.5, 5.0),
            "relevance": relevance,
            "relevance_explanation": f"Answer is {relevance.lower()}.",
            "model_used": "gpt-5.4-mini",
            "prompt_tokens": random.randint(50, 200),
            "completion_tokens": random.randint(50, 300),
            "total_tokens": random.randint(100, 500),
            "openai_cost": random.uniform(0.0001, 0.01),
        }

        save_conversation(conversation_id, question, answer_data, course, current_time)

        if random.random() < 0.7:
            feedback = 1 if random.random() < 0.8 else -1
            save_feedback(conversation_id, feedback, current_time)

        current_time += timedelta(minutes=random.randint(1, 15))
        count += 1

    print(f"Generated {count} historical conversations")


def generate_live():
    print("Starting live data generation (Ctrl+C to stop)...")
    try:
        while True:
            current_time = datetime.now(tz)
            conversation_id = str(uuid.uuid4())
            question = random.choice(SAMPLE_QUESTIONS)
            answer = random.choice(SAMPLE_ANSWERS)
            course = random.choice(COURSES)
            relevance = random.choice(RELEVANCE)

            answer_data = {
                "answer": answer,
                "response_time": random.uniform(0.5, 5.0),
                "relevance": relevance,
                "relevance_explanation": f"Answer is {relevance.lower()}.",
                "model_used": "gpt-5.4-mini",
                "prompt_tokens": random.randint(50, 200),
                "completion_tokens": random.randint(50, 300),
                "total_tokens": random.randint(100, 500),
                "openai_cost": random.uniform(0.0001, 0.01),
            }

            save_conversation(conversation_id, question, answer_data, course, current_time)

            if random.random() < 0.7:
                feedback = 1 if random.random() < 0.8 else -1
                save_feedback(conversation_id, feedback, current_time)

            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped.")


if __name__ == "__main__":
    end_time = datetime.now(tz)
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
data every second. Switch to Grafana and you'll see the dashboard come
alive with charts updating in real time.


## Timezone handling

Notice the `tz = ZoneInfo("Europe/Berlin")` in the script. This
ensures timestamps are stored with proper timezone information. Grafana
respects these timezones when displaying data.

If your users are in a different timezone, adjust this accordingly. The
important thing is to use `TIMESTAMP WITH TIME ZONE` in PostgreSQL and
always store timezone-aware datetimes.


[<< Previous: Grafana Dashboards](05-grafana.md)
|
[Next: Next Steps >>](07-next-steps.md)
