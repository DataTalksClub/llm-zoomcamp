# Projects 

Video: https://www.loom.com/share/8f99d25893de4fb8aaa95c0395c740b6

[Submit your project here](cohorts/2024/project.md)

## Objective

The goal of this project is to apply everything we have learned
in this course to build an end-to-end RAG application.

In order to receive a certificate of completion for the course, you need
to deliver a project. There are two attempts for that.


## Problem statement

For the project, we ask you to build an end-to-end RAG project. 

For that, you need:

* Select a dataset that you're interested in (see [Datasets](#datasets))
* Ingest the data into a knowledge base
* Implement the RAG flow: query the knowledge base, build the prompt, send the promt to an LLM
* Evaluate the performance of your RAG flow
* Create the interface for the application
* Collect user feedback and monitor your application

## Technologies

You don't have to limit yourself to technologies covered in the course. You can use alternatives as well:

* LLM: OpenAI, Groq, AWS Bedrock, etc
* Knowledge base: any text, relational or vector database, including in-memory ones like we implemented in the course or SQLite  
* Monitoring: Grafana, Kibana, Streamlit, dash, etc
* Interface: Streamlit, dash, Flask, FastAPI, Django, etc (could be UI or API)
* Ingestion orchestration: Mage, dlt, Airflow, Prefect, python script, etc

If you use a tool that wasn't covered in the course, be sure to give a very detailed explanation
of what that tool does and how to use it. 

If you're not certain about some tools, ask in Slack.

## Peer reviewing

> [!IMPORTANT]  
> To evaluate the projects, we'll use peer reviewing. This is a great opportunity for you to learn from each other.
> * To get points for your project, you need to evaluate 3 projects of your peers
> * You get 3 extra points for each evaluation

## Evaluation Criteria

* Problem description
    * 0 points: The problem is not described
    * 1 point: The problem is described but shortly or not clearly 
    * 2 points: The problem is well described and it's clear what the problem the project solves
* RAG flow
    * 0 points: No knowledge base and LLM
    * 2 points: No knowledge base is used, query the LLM directly
    * 4 points: Both a klowledge base and an LLM are used in the RAG flow 
* Interface
   * 0 points: No way to interact with the application at all
   * 2 points: Command line interface, a script, or a jupyter notebook
   * 4 points: UI (e.g. in streamlit), web application (e.g. Django) or an API (built e.g. with FastAPI) 
* Retrieval evaluation
    * 0 points: No evaluation for retrieval
    * 2 points: Only one approach for retrieval is evaluated
    * 4 poinst: Multiple approaces are evaluated and the best one is used  
* RAG evaluation
    * 0 points: No evaluation for RAG
    * 2 points: Only one approach (e.g. only one prompt) for RAG is evaluated
    * 4 poinst: Multiple approaces are evaluated and the best one is used  
* Reproducibility
    * 0 points: No instructions on how to run the code at all, the data is missing or it's not clear how to access it
    * 2 points: Some instructions are there, but they are not complete OR instructions are clear and complete, the code works, but the data is missing
    * 4 points: Instructions are clear, it's easy to run the code, and it works. The versions for all the dependencies are specified.
* Containerization
    * 0 points: No containerization
    * 2 points: Dockerfile is provided for the main application OR there's a docker-compose for the dependencies only
    * 4 points: Everyting is in docker-compose
* Ingestion orchestration
   * 0 points: No ingestion
   * 2 points: Semi-automated ingestion of the dataset to the knowledge base, e.g. with a Jupyter notebook
   * 4 points: Automated ingestion with a python script or a special tool (Mage, dlt, Airflow, prefect, etc) 
* Best practices
    * [ ] Hybrid search: combining both text and vector search (at least evaluating it) (2 points)
    * [ ] Document reranking (2 points)
    * [ ] User query rewriting (2 points)
    * [ ] More TBA 
* Bonus points (not covered in the course)
    * [ ] Deployment to the cloud (2 points)
    * [ ] More TBA

> [!NOTE]
> It's highly recommended to create a new repository for your project (not inside an existing repo)
> with a meaningful title, such as "DataTalks.Club FAQ Q&A System" or "Talk with a YouTube video".
> Include as many details as possible in the README file. ChatGPT or other LLMs can assist you with this.
> Doing so will make it easier to showcase your project for potential job opportunities. But
> if you leave the README file empty or with minimal details, there may be point deductions as
> per the [Evaluation Criteria](#evaluation-criteria).

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
