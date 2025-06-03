# Module 1: Introduction
 
Overview of the module: In this module, we will learn what LLM and RAG are and
implement a simple RAG pipeline to answer questions about 
the FAQ Documents from our Zoomcamp courses

Practical steps covered:

* Index Zoomcamp FAQ documents
    * DE Zoomcamp: https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit
    * ML Zoomcamp: https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit
    * MLOps Zoomcamp: https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit
* Create a Q&A system for answering questions about these documents 

Table of contents

## Lecture 1.1: Introduction to large language models (LLMs) and retrieval-augmented generation (RAG)

> Links:
> [Lecture recording](https://www.youtube.com/watch?v=Q75JgLEXMsM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

Welcome to LLM Zoomcamp, where we start a practical journey into the world of Large Language Models (LLMs) and their real-world applications.

### Course Focus

> [!NOTE]
> This course is designed not as a theoretical deep-dive into the mathematics behind neural networks, but as a hands-on exploration of how we can leverage these powerful tools to solve genuine problems that we face in our community.

We will focus on building practical systems that can answer questions intelligently by combining the power of modern language models (LLMs) with information retrieval techniques like retrieval-augmented generation (RAG).

### What Problem Will We Solve During This Course?

LLM Zoomcamp is DataTalks.Club's fifth course, building upon our tradition of practical, project-based learning. As our community has grown across multiple specialized courses, we've accumulated extensive knowledge bases in the form of FAQ documents.

These documents represent thousands of hours of collective knowledge: questions asked by previous students and carefully crafted answers by instructors and teaching assistants. They're invaluable resources that could save new students significant time and reduce repetitive questions in our community channels.

Here are the FAQs of our first three courses:

- [Data Engineering Zoomcamp FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit): A comprehensive 321-page document filled with student questions and detailed answers
- [ML Zoomcamp FAQ](https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit): An equally extensive FAQ covering machine learning concepts and practical issues
- [MLOps Zoomcamp FAQ](https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit): Specialized Q&A focused on MLOps practices and tools

But the question is: how does a student finds an answer to their question if FAQ is such long? It's very similar to trying to find a needle in a haystack.

For example, a new student joins our Data Engineering Zoomcamp and wants to know "How do I set up my development environment on Windows?", so they want to find an aswer to their question.

To do that, they could:
1. Manually search through 321 pages of FAQ
2. Use basic text search (Ctrl+F) with limited effectiveness
3. Give up and ask the question again in our Slack channel (creating duplication)

As a result, they could miss out on the detailed, high-quality answer that already exists in the FAQ and create a duplication. This scenario plays out daily across technical communities worldwide. The knowledge exists, but discovery is the bottleneck.

### Solution Idea

What if we could create an intelligent assistant that:

- Understands the intent behind a student's question
- Quickly searches through our entire knowledge base
- Finds the most relevant information
- Provides a comprehensive, contextual answer in natural language

This is exactly what we'll build in this course. But first, we need to understand the technologies that make this possible.

### Understanding Large Language Models: The Foundation

To build our intelligent Q&A system, we first need to understand the foundational technology: large language models.

#### What Are Language Models?

Language models aren't new, you interact with them daily without realizing it. Every time you type on your smartphone and see predictive text suggestions, you're using a language model.

> **Example**: When you type "How are" in WhatsApp, your phone suggests "you" as the next word because it has learned from patterns that "How are you?" is a common phrase.

These simple models work through basic statistical methods:
- They analyze the frequency of word combinations
- They predict the most likely next word based on previous words
- They use techniques like Naive Bayes classification
- They have relatively few parameters (thousands to millions)

While effective for their purpose, these models are quite limited. They can't understand context deeply, handle complex reasoning, or maintain coherent conversations.

#### The "Large" in Large Language Models

The breakthrough came with models that are "large" in multiple dimensions:

**Scale of Parameters**: Instead of thousands of parameters, LLMs have billions or even trillions. To put this in perspective:
- Simple phone autocomplete: ~100,000 parameters
- GPT-3: 175 billion parameters
- GPT-4: Estimated 1+ trillion parameters

**Training Data Volume**: LLMs are trained on massive datasets containing:
- Books, articles, and academic papers
- Web pages and forums
- Code repositories
- Reference materials and encyclopedias
- Conversations and Q&A pairs

**Computational Architecture**: Modern LLMs use transformer architectures that can:
- Process long sequences of text
- Understand relationships between distant words
- Maintain context across lengthy conversations
- Perform reasoning-like operations

#### The Emergence of Intelligence-Like Behavior

Here's what makes LLMs remarkable: despite fundamentally being "next word predictors," their scale and training enable them to exhibit behaviors that feel genuinely intelligent.

When you interact with ChatGPT, Claude, or similar models, you experience:
- **Contextual understanding**: They grasp what you're asking, even with ambiguous phrasing
- **Knowledge synthesis**: They combine information from different domains
- **Reasoning patterns**: They can work through multi-step problems
- **Adaptive communication**: They adjust their response style to match your needs

> [!NOTE]
> In this course, we treat LLMs as "black boxes." We won't dive into transformer architectures, attention mechanisms, or training procedures. Instead, we focus on how to effectively use these powerful tools to solve real problems.

#### How LLMs Process Your Requests

Understanding the basic input-output flow helps us use LLMs more effectively:

```
Your Input (Prompt) → [LLM Processing] → Generated Response
```

**The Prompt**: This is your input text. LLMs interpret everything as a completion task. Even when you ask a question, the model is essentially completing the pattern of "Question: [your question] Answer: [response]"

**Example Interaction**:
```
Input: "Explain how photosynthesis works"

Internal Processing: The LLM recognizes this as a request for explanation and begins generating a response that would logically complete this prompt.

Output: "Photosynthesis is the process by which plants convert sunlight, carbon dioxide, and water into glucose and oxygen..."
```

### The Limitation: When LLMs Don't Know Enough

Now that we understand what LLMs can do, let's explore their fundamental limitation - and why we need additional techniques to solve our FAQ problem.

#### The Knowledge Cutoff Problem

Despite their impressive capabilities, LLMs have a critical constraint: **their knowledge is frozen at training time**. Consider these scenarios:

**Scenario 1 - Perfect LLM Performance**:
```
Question: "How do I cook salmon?"
LLM Response: Provides detailed cooking instructions, temperature guidelines, timing recommendations, etc.
```
This works perfectly because cooking salmon is well-documented in the LLM's training data.

**Scenario 2 - LLM Knowledge Gap**:
```
Question: "Is it too late to join the Data Engineering Zoomcamp?"
LLM Response: "I'd be happy to help, but I need more information. Which Data Engineering program are you referring to, and what is the current date?"
```

The LLM has no context about:
- Which specific course you mean
- Current enrollment periods
- Course-specific policies
- Real-time availability

**Scenario 3 - Domain-Specific Questions**:
```
Question: "How do I set up my development environment for this course?"
LLM Response: Provides generic development setup advice that may not match the specific requirements, tools, or versions needed for our particular curriculum.
```

#### Why This Matters for Our FAQ System

If we simply connected students to ChatGPT, they would get generic answers that might not address:
- Course-specific requirements
- Specific tools and versions we use
- Our particular setup procedures
- Community-specific conventions
- Current course policies and deadlines

We need a way to give the LLM access to our specific knowledge base so it can provide accurate, relevant answers.

### Introducing RAG: The Solution to LLM Limitations

This is where **RAG (Retrieval Augmented Generation)** comes in - the core technique we'll learn throughout this course.

#### What is RAG?

**RAG = Retrieval (Search) + Augmented (Enhanced) + Generation (LLM)**

The core insight is brilliant in its simplicity: instead of expecting the LLM to know everything, we give it access to relevant information just-in-time.

#### The RAG Approach

**Traditional LLM Approach**:
- Ask LLM a domain-specific question
- LLM responds with generic or incomplete information
- User gets frustrated with irrelevant answers

**RAG Approach**:
- Ask LLM a domain-specific question
- System searches relevant knowledge base
- Provides LLM with specific, current information
- LLM generates an informed, contextual response

This transforms LLMs from knowledgeable generalists into domain-specific experts.

### How RAG Works: A Complete Walkthrough

Let's trace through exactly how RAG solves our FAQ problem:

#### The Complete RAG Flow

```
Student Question → Knowledge Base Search → Document Retrieval → Context Enhancement → LLM Generation → Comprehensive Answer
```

#### Step-by-Step Process

**1. User Initiates Query**
```
Student asks: "How do I enroll in the Data Engineering Zoomcamp?"
```

**2. Query Processing and Search**
The system takes this question and searches our FAQ knowledge base. This isn't just simple text matching - it looks for semantically relevant content that might answer the question, even if the exact words don't match.

**3. Document Retrieval**
The search returns multiple relevant documents:
- **Document 1**: "Registration process and deadlines"
- **Document 2**: "Prerequisites and requirements"
- **Document 3**: "Course schedule and format"
- **Document 4**: "Payment and enrollment FAQ"
- **Document 5**: "Technical setup requirements"

**4. Context Assembly**
The system creates an enhanced prompt:
```
Question: How do I enroll in the Data Engineering Zoomcamp?

Context:
[Document 1 content]: Registration opens on January 15th each cohort. Students can register through the course website by filling out the enrollment form...

[Document 2 content]: Prerequisites include basic programming knowledge in Python and familiarity with command line...

[Document 3 content]: The course runs for 8 weeks with live sessions every Monday and Wednesday...

[Additional relevant context from Documents 4 and 5]

Answer:
```

**5. LLM Generation**
The LLM now has both the original question and rich context from our specific knowledge base. It generates a comprehensive answer that addresses:
- Specific enrollment steps
- Current deadlines and dates
- Prerequisites and expectations
- What to expect from the course format
- Any technical requirements

**6. Response Delivery**
The student receives a detailed, accurate answer that's specifically tailored to our Data Engineering Zoomcamp, not generic advice about online courses.

#### The Power of Context

Notice how the same LLM that previously couldn't answer course-specific questions now provides expert-level responses. The difference is context - we've given the LLM the specific information it needs to be helpful.

### The Modular Power of RAG: Flexibility and Evolution

One of RAG's greatest strengths is its modular architecture. This flexibility allows us to experiment, improve, and adapt our system as needs change.

#### Interchangeable Search Components

**Our Learning Journey in This Module**:

**Week 1**: We'll start with a simple, custom search engine to understand the fundamentals
- Build a basic keyword-based search
- Learn how document indexing works
- Understand relevance scoring

**Week 2**: We'll upgrade to Elasticsearch
- Professional-grade search capabilities
- Advanced query processing
- Better performance and scalability

**Future Modules**: We'll explore vector search
- Semantic similarity instead of just keyword matching
- Handle synonyms and conceptual queries
- More sophisticated relevance understanding

**The Key Point**: We can swap these search technologies without changing the overall architecture. Each has trade-offs:
- Simple search: Easy to understand, limited capability
- Elasticsearch: Professional features, more complex setup
- Vector search: Most sophisticated, requires additional infrastructure

#### Interchangeable LLM Components

**Module 1 Approach**: We'll use OpenAI's models (GPT-3.5/GPT-4)
- High quality responses
- Easy API integration
- Paid service

**Alternative Options**: The same RAG framework works with:
- **Open-source models** (Llama, Mistral, etc.): Free but require more setup
- **Local models** (via Ollama): Complete privacy and control
- **Other commercial APIs** (Claude, Gemini, etc.): Different strengths and pricing

**The Flexibility Advantage**: You can experiment with different combinations:
- Elasticsearch + GPT-4 for maximum capability
- Simple search + local LLM for complete privacy
- Vector search + Claude for cost optimization

### What You'll Build in This Course

#### Your Learning Journey

By the end of this course, you'll have built a complete, production-ready RAG system that includes:

**Technical Components**:
- A robust search and retrieval system
- LLM integration with proper prompt engineering
- A user-friendly web interface
- Error handling and system monitoring

**Practical Skills**:
- How to evaluate and improve RAG system performance
- Techniques for handling different types of queries
- Methods for updating and maintaining knowledge bases
- Best practices for deploying RAG applications

**Real-World Application**:
- A working Q&A system for any knowledge base you choose
- The ability to adapt the system to new domains
- Understanding of when and how to use RAG effectively

#### Beyond This Course

The skills you develop here extend far beyond FAQ systems:
- **Customer Support**: Automated response systems that understand product documentation
- **Internal Knowledge Management**: Help employees find information across company documents
- **Research Assistance**: Systems that can synthesize information from academic papers
- **Code Documentation**: Tools that help developers understand large codebases

### Key Takeaways

As we conclude this introduction, let's crystallize the essential concepts:

1. **LLMs are Powerful but Limited**: Large Language Models can generate human-like text but are constrained by their training data cutoff and lack domain-specific knowledge.

2. **RAG Bridges the Knowledge Gap**: By combining search with generation, RAG provides LLMs with just-in-time access to relevant, specific information.

3. **Modular Architecture Enables Innovation**: RAG's component-based design allows continuous improvement and experimentation with different search and LLM technologies.

4. **Real-World Problem Solving**: This course emphasizes practical application - you'll solve genuine problems that exist in educational and business contexts.

5. **The Future is Augmented Intelligence**: RAG represents a broader trend toward systems that combine AI reasoning with accurate information retrieval.

Remember, we're not just learning to use tools - we're learning to solve real problems that affect real people. Every FAQ system, customer support bot, and knowledge assistant you build has the potential to save someone time, reduce frustration, and provide better access to information.

Let's begin this journey together, starting with setting up our development environment and building our first RAG system.

## 1.2 Preparing the Environment

<a href="https://www.youtube.com/watch?v=ozCpmkbJNJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ozCpmkbJNJE">
</a>

* Installing libraries
* Alternative: installing anaconda or miniconda

```bash
pip install tqdm notebook==7.1.2 openai elasticsearch==8.13.0 pandas scikit-learn ipywidgets
```

## 1.3 Retrieval

<a href="https://www.youtube.com/watch?v=olvem333Bqo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/olvem333Bqo">
</a>

Note: as of now, you can install minsearch with pip:

```bash
pip install minsearch
```

* We will use the search engine we build in the [build-your-own-search-engine workshop](https://github.com/alexeygrigorev/build-your-own-search-engine): [minsearch](https://github.com/alexeygrigorev/minsearch)
* Indexing the documents
* Peforming the search


## 1.4 Generation with OpenAI

<a href="https://www.youtube.com/watch?v=qz316T3U49Q&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/qz316T3U49Q">
</a>

* Invoking OpenAI API
* Building the prompt
* Getting the answer


If you don't want to use a service, you can run an LLM locally
refer to [module 2](../02-open-source/) for more details.

In particular, check "2.7 Ollama - Running LLMs on a CPU" - 
it can work with OpenAI API, so to make the example from 1.4 
work locally, you only need to change a few lines of code.


## 1.4.2 OpenAI API Alternatives

<a href="https://www.youtube.com/watch?v=HObjFso2UJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/HObjFso2UJE">
</a>

[Open AI Alternatives](../awesome-llms.md#openai-api-alternatives)


## 1.5 Cleaned RAG flow

<a href="https://www.youtube.com/watch?v=vkTiVwwch6A&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/vkTiVwwch6A">
</a>

* Cleaning the code we wrote so far
* Making it modular

## 1.6 Searching with ElasticSearch

<a href="https://www.youtube.com/watch?v=1lgbR5wMvsI&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/1lgbR5wMvsI">
</a>

* Run ElasticSearch with Docker
* Index the documents
* Replace MinSearch with ElasticSearch

Running ElasticSearch:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -m 4GB \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

If the previous command doesn't work (i.e. you see "error pulling image configuration"), try to run ElasticSearch directly from Docker Hub:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    elasticsearch:8.4.3
```

Index settings:

```python
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} 
        }
    }
}
```

Query:

```python
{
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "data-engineering-zoomcamp"
                }
            }
        }
    }
}
```

We use `"type": "best_fields"`. You can read more about 
different types of `multi_match` search in [elastic-search.md](elastic-search.md).

# 1.7 Homework
More information [here](../cohorts/2025/01-intro/homework.md).


# Extra materials

* If you're curious to know how the code for parsing the FAQ works, check [this video](https://www.loom.com/share/ff54d898188b402d880dbea2a7cb8064)

# Open-Source LLMs (optional)

It's also possible to run LLMs locally. For that, we 
can use Ollama. Check these videos from LLM Zoomcamp 2024
if you're interested in learning more about it:

* [Ollama - Running LLMs on a CPU](https://www.youtube.com/watch?v=PVpBGs_iSjY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
* [Ollama & Phi3 + Elastic in Docker-Compose](https://www.youtube.com/watch?v=4juoo_jk96U&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
* [UI for RAG](https://www.youtube.com/watch?v=R6L8PZ-7bGo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

To see the command lines used in the videos,
see [2024 cohort folder](../cohorts/2024/02-open-source#27-ollama---running-llms-on-a-cpu)

# Notes

* [Notes by slavaheroes](https://github.com/slavaheroes/llm-zoomcamp/blob/homeworks/01-intro/notes.md)
* [Notes by Pham Nguyen Hung](https://hung.bearblog.dev/llm-zoomcamp-1-rag/)
* [Notes by dimzachar](https://github.com/dimzachar/llm_zoomcamp/blob/master/notes/01-intro/README.md)
* [Notes by Olawale Ogundeji](https://github.com/presiZHai/LLM-Zoomcamp/blob/main/01-intro/notes.md)
* [Notes by Uchechukwu](https://medium.com/@njokuuchechi/an-intro-to-large-language-models-llms-0c51c09abe10)
* [Notes by Kamal](https://github.com/mk-hassan/llm-zoomcamp/blob/main/Module-1%3A%20Introduction%20to%20LLMs%20and%20RAG/README.md)
* [Notes by Marat](https://machine-mind-ml.medium.com/discovering-semantic-search-and-rag-with-large-language-models-be7d9ba5bef4)
* [Notes by Waleed](https://waleedayoub.com/post/llmzoomcamp_week1-intro_notes/)
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
