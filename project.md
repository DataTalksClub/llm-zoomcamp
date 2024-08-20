# Projects 

Video: https://www.loom.com/share/8f99d25893de4fb8aaa95c0395c740b6

[Submit your project here](cohorts/2024/project.md)

## Objective

The goal of this project is to apply everything we have learned
in this course to build an end-to-end machine learning project.

In order to receive a certificate of completion for the course, you need
to deliver a project. There are two attempts for that.


## Problem statement

For the project, we will ask you to build an end-to-end RAG project. 

For that, you will need:

* Select a dataset that you're interested in (see [Datasets](#datasets))
* Index the data with a database
* Implement the RAG flow: query the database, build the prompt, send the promt to an LLM 
* 

## Technologies 

You don't have to limit yourself to technologies covered in the course. You can use alternatives as well:


If you use a tool that wasn't covered in the course, be sure to explain what that tool does.

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
* Database
* LLM
* Basic RAG flow
* Serving / Interface
    * 0 points: No interface for RAG
    * 2 points: Command line interface, a script or a notebook
    * 4 points: UI (such as streamlit) or 
* Evaluation
    * 0 points: No evaluation
    * 2 points: Only one approach is used and evaluated
    * 4 poinst: multiple approaces are evaluated and the best one is used  
* Monitoring
* Reproducibility
    * 0 points: No instructions on how to run the code at all, the data is missing
    * 2 points: Some instructions are there, but they are not complete OR instructions are clear and complete, the code works, but the data is missing
    * 4 points: Instructions are clear, it's easy to run the code, and it works. The versions for all the dependencies are specified.
* Containerization
    * 
* Best practices
* Bonus points (not covered in the course)
    * [ ] Deployment to the cloud (2 points)

* Cloud
    * 0 points: Cloud is not used, things run only locally
    * 2 points: The project is developed on the cloud OR uses localstack (or similar tool) OR the project is deployed to Kubernetes or similar container management platforms
    * 4 points: The project is developed on the cloud and IaC tools are used for provisioning the infrastructure
* Experiment tracking and model registry
    * 0 points: No experiment tracking or model registry
    * 2 points: Experiments are tracked or models are registered in the registry
    * 4 points: Both experiment tracking and model registry are used
* Workflow orchestration
    * 0 points: No workflow orchestration
    * 2 points: Basic workflow orchestration
    * 4 points: Fully deployed workflow 
* Model deployment
    * 0 points: Model is not deployed
    * 2 points: Model is deployed but only locally
    * 4 points: The model deployment code is containerized and could be deployed to cloud or special tools for model deployment are used
* Model monitoring
    * 0 points: No model monitoring
    * 2 points: Basic model monitoring that calculates and reports metrics
    * 4 points: Comprehensive model monitoring that sends alerts or runs a conditional workflow (e.g. retraining, generating debugging dashboard, switching to a different model) if the defined metrics threshold is violated
* Reproducibility
    * 0 points: No instructions on how to run the code at all, the data is missing
    * 2 points: Some instructions are there, but they are not complete OR instructions are clear and complete, the code works, but the data is missing
    * 4 points: Instructions are clear, it's easy to run the code, and it works. The versions for all the dependencies are specified.
* Best practices
    * [ ] There are unit tests (1 point)
    * [ ] There is an integration test (1 point)
    * [ ] Linter and/or code formatter are used (1 point)
    * [ ] There's a Makefile (1 point)
    * [ ] There are pre-commit hooks (1 point)
    * [ ] There's a CI/CD pipeline (2 points)

> [!NOTE]
> It's highly recommended to create a new repository for your project (not inside an existing repo) with a meaningful title, such as
> "Car Price Prediction" or "Music Genre Classification" and include as many details as possible in the README file. ChatGPT can assist you with this. Doing so will not only make it easier to showcase your project for potential job opportunities but also have it featured on the [Projects Gallery App](#projects-gallery).
> If you leave the README file empty or with minimal details, there may be point deductions as per the [Evaluation Criteria](#evaluation-criteria).


## Project ideas


### Datasets

Here are some datasets for your projects and potential things you can do with them

* DTC Slack dump: book of the week channel, course channels, career questions, etc
* DTC website with book of the week archives
* DTC Podcast: transcripts
* Any book(s), video(s), audio(s)
* add more here

Note that your dataset doesn't have to be in thr Q&A form. Check [etc/chunking.md](etc/chunking.md) to learn more about chunking.

