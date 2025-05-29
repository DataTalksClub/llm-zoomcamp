# Key Takeaways from the LLM Zoomcamp 2025 Pre-Course Live Q&A

[![Watch the Launch Stream](https://img.youtube.com/vi/8lgiOLMMKcY/maxresdefault.jpg)](https://youtu.be/8lgiOLMMKcY)

> **[Watch the LLM Zoomcamp 2025 Pre-Course Live Q&A](https://youtu.be/8lgiOLMMKcY)**

## 1. Do you think LLMs are a lasting technology or are they just a passing trend like the metaverse or NFTs?

**Answer:** While there’s certainly hype around LLMs, they’ve already become deeply integrated into daily workflows—used for coding, personal productivity, and prototype development. Even after the hype subsides, the underlying tools and techniques (like RAG pipelines and vector search) will remain valuable. Future models and interfaces may evolve, but the core capabilities of LLMs are here to stay.

## 2. What prerequisites would set me up for success in the course and help me get the best out of it?

**Answer:** You should be comfortable with:

* General programming (ideally in Python)
* Command-line tools
* Connecting services (e.g., spinning up ElasticSearch or similar)
  No deep machine-learning or advanced software-engineering background is required, but familiarity with basic scripting and package installation will make the coursework smoother.

## 3. Is it beneficial if I do the course again this year even though I completed it last year?

**Answer:** Yes. The curriculum has been updated with fewer but deeper modules, new evaluation/monitoring tooling (Phoenix instead of Grafana), and likely a new vector-search backend. You’ll also get to experiment with the latest LLMs and compete in a fresh challenge exercise.

## 4. Will the course help me implement RAG from a live database?

**Answer:** Most likely yes. Whether your data is in a transactional database or a knowledge-base store, the course teaches you how to connect to your data source, chunk and index content, and build a RAG application. The exact workflow may vary by database type, but the principles carry over.

## 5. Are we going to do any agentic AI development in this course?

**Answer:** Not as part of the core modules. There **will** likely be an optional parallel workshop on agentic workflows in June, but agent development is not formally included in this year’s curriculum.

## 6. Will this course include MLOps (LM Ops) content?

**Answer:** To a degree. The monitoring module covers key LM Ops practices (metrics, cost tracking, query logging), but full deployment and continuous-training pipelines are reserved for the separate Open Source LLM Zoom Camp.

## 7. What will be the infrastructure cost, and can I run everything locally without cloud resources?

**Answer:**

* **Local:** 100 % feasible—you can use tools like Llama.cpp or Gro to run models on your own machine.
* **Cloud APIs:** Costs are modest. For OpenAI, \~1 million tokens in/out costs around \$10 total. Gro offers a free tier for basic experimentation.

## 8. Will this course cover MCP (Model Context Protocol)?

**Answer:** No, MCP (and other emerging protocols) are not in this year’s syllabus. As with agentic AI, these topics may surface in a future specialized offering once industry practices stabilize.

## 9. Do we discuss evaluating LLM-based applications, generating metrics, and setting up guardrails?

**Answer:**

* **Evaluation metrics:** Yes. You’ll learn classical IR metrics (e.g., MRR, recall) for search and how to use LLMs themselves as “judges” for end-to-end RAG evaluation.
* **Guardrails:** No formal guardrail framework is included, though monitoring best practices will help you detect and respond to undesired behavior.

## 10. Will we cover chunking techniques in the course?

**Answer:** Yes and no. You’ll see how data is pre-chunked in the example repo and learn best practices for chunk size and strategy—but actual implementation and experimentation with chunking are left as part of your hands-on project work.

## 11. Is the RAG pipeline included in the course?

**Answer:** Absolutely. RAG is the central focus: indexing, retrieval, prompt construction, and response handling are all core modules, and you’ll build full pipelines from scratch.

## 12. Can different programming languages like JavaScript be used for this course?

**Answer:** The taught examples use Python, but you’re welcome to implement your project in another language (e.g., JavaScript). You’ll just need to provide clear installation and usage instructions (npm commands, environment setup) so peers can run and review your work.

## 13. Can we expect a complex project, and learn from examples?

**Answer:** Project complexity is up to you. The course provides exemplar student projects (food-search RAG, recipe recommenders, etc.) to illustrate scope and quality. You then pick your own data and extend the RAG concepts to a domain of your choice.

## 14. As someone new, how do I navigate the GitHub repo structure?

**Answer:**

1. Open the repo’s README and follow the module links in order.
2. Click each module’s folder to access videos and homework.
3. Use the “Project Attempts” section to browse past student projects and peer-review guidelines.

## 15. What is the estimated weekly time investment for the course?

**Answer:** Roughly **10 hours per week**:

* Module videos + readings: \~4 hours
* Homework/project work: \~6 hours

## 16. How long does the course run and when does it end?

**Answer:** It spans **10 weeks** total:

* 2 weeks for the Intro module
* 1 week each for Modules 2–5
* 3 weeks for the final project period
  Expect to finish by late summer.

## 17. How much will it cost to complete the course using Gro or OpenAI APIs?

**Answer:**

* **Gro:** Free tier available, suitable for initial experiments.
* **OpenAI:** Approximately \$10–\$20 for 1 million tokens in + out; in practice you’ll spend far less than your API quota.

## 18. Can you explain the steps for enrolling and completing the course?

**Answer:**

1. **Star & Fork** the GitHub repo to show support.
2. **Sign up** on the repo’s landing page (click “Sign up” button).
3. **Join** the community (Telegram/Slack) for announcements.
4. **Attend** the launch stream (May 27) for a content overview.
5. **Weekly:** Watch that week’s module videos, complete homework, submit via the platform.
6. **Final project:** Build and document your RAG application; peer-review others.
7. **Certificate:** Earned upon successful project submission and peer reviews.
