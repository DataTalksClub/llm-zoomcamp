# End-to-End Project Example

<a href="https://www.youtube.com/watch?v=E9O0Tg68PPg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/E9O0Tg68PPg">
</a>

In this module, we walk through building a complete RAG project
from scratch - a fitness assistant that helps users with exercise
questions. We'll follow the same project criteria used for the
course project.

The project is [alexeygrigorev/fitness-assistant](https://github.com/alexeygrigorev/fitness-assistant)
on GitHub. Check the final result - it's been polished beyond what
we show in the videos.


## What we'll build

A RAG application that:

- Uses a dataset of exercises with muscle groups, equipment, and
  instructions
- Answers questions about exercises, replacements, and proper form
- Has a search component, an LLM component, and evaluation
- Includes an API interface (Flask)
- Has monitoring with PostgreSQL and Grafana
- Is containerized with Docker


## Generating the dataset

Since we don't have a real fitness FAQ database, we generate one
with an LLM. The idea is to create a dataset with records like:

```json
{
  "id": "push-up-001",
  "exercise": "Push-up",
  "muscle_group": "Chest",
  "equipment": "None (bodyweight)",
  "difficulty": "Beginner",
  "instructions": "Start in a plank position with hands slightly wider than shoulders...",
  "tips": "Keep your core tight and avoid sagging hips..."
}
```

We use GPT to generate hundreds of these records across different
muscle groups and exercise types.


## Setting up the project

Create a new project with uv:

```bash
mkdir fitness-assistant
cd fitness-assistant
uv init
uv add openai minsearch requests python-dotenv jupyter
```

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

This is the same setup we used in module 01.


[<< Back to module](../)
|
[Next: Evaluating Retrieval >>](02-evaluating-retrieval)
