# Projects

Use these references for the project process:

* [Project video](https://www.loom.com/share/8f99d25893de4fb8aaa95c0395c740b6)
* [Project office hours](https://www.youtube.com/watch?v=pA9S1mTqAwU)

To receive a certificate of completion for the course, you need
to deliver a project. There are two attempts for that.

[Submit your project here](cohorts/2025/project.md)


## Objective

The goal of this project is to apply the course material.
You will build an end-to-end RAG or agent application.


## Problem statement

For the project, we ask you to build an end-to-end LLM application.
It can be a RAG application, an agent application, or a combination of both.

For that, you need:

* Select a dataset or API-backed data source that you're interested in (see [Datasets](#datasets) for examples and ideas)
* Ingest the data into a knowledge base, or connect to the API that provides the data
* Implement the application flow: retrieve context from the data, optionally call tools, build the prompt, and send it to an LLM
* Evaluate the performance of your RAG or agent flow
* Create an interface for the application
* Collect user feedback and monitor your application


## Datasets you cannot use

The DataTalks.Club Zoomcamp course FAQ documents are used as the knowledge base in the course modules and homework. They cannot be used for your project. Pick a different corpus or dataset.


## Project Documentation

Your project rises or falls with its documentation.

Use these recommendations:

* Write for people who didn't take the course. Explain the problem, the data, and the flow without assuming the reader watched the videos.
* Mention the evaluation criteria in your README. This makes it easier for reviewers to find the relevant parts.
* Add screenshots where they help. For example, show the UI, the monitoring dashboard, or examples of answers from your app.
* Explain how to run the project. Include setup steps, dependencies, configuration, and any environment variables.
* Show how the project works. Add examples of inputs and outputs, common use cases, or a short walkthrough.
* Add a short app preview video if it helps. If you're using Streamlit, you can record it from the app's top-right menu ([Streamlit Guide](https://docs.streamlit.io/develop/concepts/architecture/app-chrome)). Then drag and drop the video into the online GitHub editor of your README ([Ref](https://stackoverflow.com/a/4279746)).
* Split long documentation into separate files if needed. For example, use `setup.md`, `usage.md`, or `contributing.md`.
* Keep the README up to date when the project changes.

Remember, clear and comprehensive documentation not only helps others but is also a valuable reference for yourself in the future.


## Technologies

You don't have to limit yourself to technologies covered in the course.

You can use alternatives as well:

* LLM: OpenAI, Ollama, Groq, AWS Bedrock, etc
* Knowledge base: any text, relational or vector database, including in-memory ones like we implemented in the course or SQLite
* Monitoring: Grafana, Kibana, Streamlit, dash, etc
* Interface: Streamlit, dash, Flask, FastAPI, Django, etc (could be UI or API)
* Ingestion pipeline: Kestra, dlt, Mage, Airflow, Prefect, python scripts, etc

If you use a tool that wasn't covered in the course, explain what that tool does.
Also explain how to use it.

If you're not certain about some tools, ask in Slack.

## Tips and best practices

Follow these tips while preparing the project:

* It's better to create a separate GitHub repository for your project
* Give your project a meaningful title, e.g. "DataTalksClub Zoomcamp Q&A system" or "Nutrition Facts Chat"


## Peer Reviewing

To evaluate the projects, we'll use peer reviewing.
This is a good opportunity to learn from each other.

To get points for your project, you need to evaluate 3 projects from your peers.
You get 3 extra points for each evaluation.

## Review Tips

Use these tips when reviewing a project:

* The reviewer is given a public GitHub repo link and a `commit-hash`
   * to see the code state of the repo at the provided commit hash, use the following URL:
   * `https://github.com/{username}/{repo-name}/tree/{commit-hash}`
* It's recommended to clone the repository for the review. To clone the project at the commit hash:
  ```bash
  git clone https://github.com/{username}/{repo-name}.git
  git reset --hard {commit-hash}
  ```

## Evaluation Criteria

Use these criteria to score the project:

* Problem description
    * 0 points: The problem is not described
    * 1 point: The problem is described but briefly or unclearly
    * 2 points: The problem is well-described and it's clear what problem the project solves
* Retrieval flow
    * 0 points: No knowledge base or LLM is used
    * 1 point: No knowledge base is used, and the LLM is queried directly
    * 2 points: Both a knowledge base and an LLM are used in the flow
* Retrieval evaluation
    * 0 points: No evaluation of retrieval is provided
    * 1 point: Only one retrieval approach is evaluated
    * 2 points: Multiple retrieval approaches are evaluated, and the best one is used
* LLM evaluation
    * 0 points: No evaluation of final LLM output is provided
    * 1 point: Only one approach (e.g., one prompt) is evaluated
    * 2 points: Multiple approaches are evaluated, and the best one is used
* Interface
   * 0 points: No way to interact with the application at all
   * 1 point: Command line interface, a script, or a Jupyter notebook
   * 2 points: UI (e.g., Streamlit), web application (e.g., Django), or an API (e.g., built with FastAPI)
* Ingestion pipeline
   * 0 points: No ingestion
   * 1 point: Semi-automated ingestion of the dataset into the knowledge base, e.g., with a Jupyter notebook
   * 2 points: Automated ingestion with a Python script or a special tool (e.g., Mage, dlt, Airflow, Prefect)
* Monitoring
   * 0 points: No monitoring
   * 1 point: User feedback is collected OR there's a monitoring dashboard
   * 2 points: User feedback is collected and there's a dashboard with at least 5 charts
* Containerization
    * 0 points: No containerization
    * 1 point: Dockerfile is provided for the main application OR there's a docker-compose for the dependencies only
    * 2 points: Everything is in docker-compose
* Reproducibility
    * 0 points: No instructions on how to run the code, the data is missing, or it's unclear how to access it
    * 1 point: Some instructions are provided but are incomplete, OR instructions are clear and complete, the code works, but the data is missing
    * 2 points: Instructions are clear, the dataset is accessible, it's easy to run the code, and it works. The versions for all dependencies are specified.
* Best practices
    * [ ] Hybrid search: combining both text and vector search (at least evaluating it) (1 point)
    * [ ] Document re-ranking (1 point)
    * [ ] User query rewriting (1 point)
* Bonus points (not covered in the course)
    * [ ] Deployment to the cloud (2 points)
    * [ ] Up to 3 extra bonus points if you want to award for something extra (write in feedback for what)


## Project ideas

## Datasets

Here are some datasets for your projects and potential things you can do with them

* DTC data:
   * Slack dump: book of the week channel, course channels, career questions, etc
   * DTC website with book of the week archives
   * DTC Podcast: transcripts
* Wikis
   * any subsets of Wikipedia
   * any wiki-like data source
   * notion notes
* Articles
   * Index and answer questions from one or multiple articles
* Transcripts
   * Podcast transcripts
   * YouTube video transcripts
* Books
   * Sci-fi, fiction, or non-fiction books
* Slide Decks and pictures
   * OCR and index slide decks (gpt-4o-mini can do that)
   * Describe and index pictures
* Add more here above this line - send a PR!
* Or just ask ChatGPT (see more ideas [here in this example](https://chatgpt.com/share/70b51c12-e41c-4312-831d-04f489a17f1e))

You can also generate a dataset with an LLM:

* If you have a dataset but you can't publicly release it, you can generate a similar one with an LLM
* Or you can simply think what kind of a dataset you want to have and generate it

Note that your dataset doesn't have to be in thr Q&A form. Check [etc/chunking.md](etc/chunking.md) to learn more about chunking.


## Cheating and plagiarism

Plagiarism in any form is not allowed.

Examples of plagiarism:

* Taking somebody's else notebooks and projects (in full or partly) and using it for your project
* Re-using your own projects (in full or partly) from other courses and bootcamps
* Re-using your appempt 1 project as attempt 2 if you passed attempt 1
* Re-using your project from the previous iterations of the course

Violating any of this will result in 0 points for this project.

Re-using some parts of the code from the course is allowed.
