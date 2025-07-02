# Projects 

* Video: https://www.loom.com/share/8f99d25893de4fb8aaa95c0395c740b6
* Office hours: https://www.youtube.com/watch?v=pA9S1mTqAwU

In order to receive a certificate of completion for the course, you need
to deliver a project. There are two attempts for that.

[Submit your project here](cohorts/2025/project.md)


## Objective

The goal of this project is to apply everything we have learned
in this course to build an end-to-end RAG application.


## Problem statement

For the project, we ask you to build an end-to-end RAG project. 

For that, you need:

* Select a dataset that you're interested in (see [Datasets](#datasets) for examples and ideas)
* Ingest the data into a knowledge base
* Implement the retrieval flow: query the knowledge base, build the prompt, send the promt to an LLM
* Evaluate the performance of your RAG flow
* Create an interface for the application
* Collect user feedback and monitor your application


## Project Documentation

Your project rises or falls with its documentation. Hence, here are some general recommendations:

* **Write for a Broader Audience 📝**: Assume the reader has no prior knowledge of the course materials. This way, your documentation will be accessible not only to evaluators but also to anyone interested in your project.
* **Include Evaluation Criteria 🎯**: Make it easier for evaluators to assess your work by clearly mentioning each criterion in your README. Include relevant screenshots to visually support your points.
* **Think of Future Opportunities 🚀**: Imagine that potential hiring managers will look at your projects. Make it straightforward for them to understand what the project is about and what you contributed. Highlight key features and your role in the project.
* **Be Detailed and Comprehensive 📋**: Include as much detail as possible in the README file. Explain the setup, the functionality, and the workflow of your project. Tools like ChatGPT or other LLMs can assist you in expanding and refining your documentation.
* **Provide Clear Setup Instructions ⚙️**: Include step-by-step instructions on how to set up and run your project locally. Make sure to cover dependencies, configurations, and any other requirements needed to get your project up and running.
* **Use Visuals and Examples 🖼️**: Wherever possible, include diagrams, screenshots, or GIFs to illustrate key points. Use examples to show how to use your project, demonstrate common use cases, and provide sample inputs and expected outputs.
  * **App Preview Video 🎥**: Consider adding a short preview video of your app in action to the README. For example, if you're using Streamlit, you can easily record a screencast from the app's top-right menu ([Streamlit Guide](https://docs.streamlit.io/develop/concepts/architecture/app-chrome)). Once you saved the video file locally, you can just drag & drop it into the online GitHub editor of your README to add it ([Ref](https://stackoverflow.com/a/4279746)).
* **Organize with Sub-Files 🗂️**: If your documentation becomes lengthy, consider splitting it into sub-files and linking them in your README. This keeps the main README clean and neat while providing additional detailed information in separate files (e.g., `setup.md`, `usage.md`, `contributing.md`).
* **Keep It Updated 🔄**: As your project evolves, make sure your documentation reflects any changes or updates. Outdated documentation can confuse readers and diminish the credibility of your project.

Remember, clear and comprehensive documentation not only helps others but is also a valuable reference for yourself in the future.


## Technologies

You don't have to limit yourself to technologies covered in the course. You can use alternatives as well:

* LLM: OpenAI, Ollama, Groq, AWS Bedrock, etc
* Knowledge base: any text, relational or vector database, including in-memory ones like we implemented in the course or SQLite  
* Monitoring: Grafana, Kibana, Streamlit, dash, etc
* Interface: Streamlit, dash, Flask, FastAPI, Django, etc (could be UI or API)
* Ingestion pipeline: Mage, dlt, Airflow, Prefect, python script, etc

If you use a tool that wasn't covered in the course, be sure to give a very detailed explanation
of what that tool does and how to use it. 

If you're not certain about some tools, ask in Slack.

## Tips and best practices

* It's better to create a separate GitHub repository for your project
* Give your project a meaningful title, e.g. "DataTalksClub Zoomcamp Q&A system" or "Nutrition Facts Chat"


## Peer reviewing

> [!IMPORTANT]  
> To evaluate the projects, we'll use peer reviewing. This is a great opportunity for you to learn from each other.
> * To get points for your project, you need to evaluate 3 projects of your peers
> * You get 3 extra points for each evaluation

### Review Tips

* The reviewer is given a public GitHut repo link and a `commit-hash`
   * to see the code state of the repo at the provided commit hash, use the following URL:
   * `https://github.com/{username}/{repo-name}/tree/{commit-hash}`
* It's recommended to clone the repository for the review. To clone the project at the commit hash:
  ```bash
  git clone https://github.com/{username}/{repo-name}.git
  git reset --hard {commit-hash}
  ```

## Evaluation Criteria

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

### Datasets

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

Plagiarism in any form is not allowed. Examples of plagiarism:

* Taking somebody's else notebooks and projects (in full or partly) and using it for your project
* Re-using your own projects (in full or partly) from other courses and bootcamps
* Re-using your appempt 1 project as attempt 2 if you passed attempt 1
* Re-using your project from the previous iterations of the course

Violating any of this will result in 0 points for this project.

Re-using some parts of the code from the course is allowed.
