# Lecture 1.2: Preparing the Environment

> **Important Links:**
> - [Lecture recording](https://youtu.be/ozCpmkbJNJE?si=34j_bVRL_iliM_E4)

## Table of Contents
1. [Overview](#overview)
2. [Setup Options Overview](#setup-options-overview)
3. [Setup Option 1: GitHub Codespaces (Recommended)](#setup-option-1-github-codespaces-recommended)
4. [Common Setup Steps (All Options)](#common-setup-steps-all-options)
5. [Setup Option 2: Anaconda/Miniconda](#setup-option-2-anacondaminiconda)
6. [Setup Option 3: Local Machine with Docker](#setup-option-3-local-machine-with-docker)
7. [Summary & Next Steps](#summary-and-next-steps)

## Overview
This lecture covers setting up the development environment for the LLM course. You have three main setup options, each with different advantages depending on your experience level and requirements.

# Setup Option 1: GitHub Codespaces (Recommended)

Codespaces comes with Docker and Python pre-installed:

- **Python**: The programming language we'll use for the entire course
- **Docker**: Containerization platform for running isolated applications (like databases)

Without Codespaces, you'd need to manually install:
1. **Python** (correct version, package manager, virtual environments)
2. **Docker Desktop** (can be tricky on some systems, requires admin rights)
3. **Git** (for version control)
4. **Code editor** (VS Code or similar)

**With Codespaces, you get:**
- Everything ready in ~30 seconds
- Consistent environment for all students  
- No installation headaches
- Works on any computer with a browser

## When to Choose This Option
- You're new to development environments
- You want to get started quickly
- You don't want to install software locally
- You're comfortable with browser-based development

## Creating Your Repository
1. Go to your GitHub account
2. Create new repository:
   - **Name**: `llm-zoomcamp` (or your preferred name)
   - **Visibility**: Must be **public** (for homework sharing)
   - **Add**: Python .gitignore
   - **License**: Optional

## Launching Codespace
1. Click **Code** button in your repository
2. Switch to **Codespaces** tab  
3. Click **Create codespace on main**
4. Choose browser or VS Code desktop

### Using VS Code Desktop
1. Install VS Code desktop application
2. Install GitHub Codespaces extension
3. Click "Open in VS Code Desktop" when prompted

## Installing Required Libraries
As mentioned already, Codespaces comes with Docker and Python pre-installed, so we only need to install some Python libraries that are not yet installed.

### Install the Python Libraries
```bash
pip install notebook==7.1.2 openai elasticsearch scikit-learn pandas
```

**Library breakdown:**
- **`notebook==7.1.2`**: Jupyter notebook environment for interactive coding and completing homework assignments
- **`openai`**: Official OpenAI Python client for accessing GPT models and other OpenAI APIs
- **`elasticsearch`**: Search engine for document retrieval in RAG (Retrieval-Augmented Generation) systems
- **`scikit-learn`**: Machine learning library for text processing, similarity calculations, and embeddings
- **`pandas`**: Data manipulation library for handling CSV files, datasets, and structured data processing

# Common Setup Steps (All Options)

## OpenAI API Configuration

### Getting Your API Key
1. Visit [platform.openai.com](https://platform.openai.com)
2. Register/login to your account
3. Navigate to **API Keys** section
4. Create new API key with descriptive name
5. **Critical**: Keep key secure, never expose it by showing it to others or committing it to Git

### Setting Environment Variable with OpenAI API Key
Use this command:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Now we have the key in our environment.

## Jupyter Notebook Setup

### Starting Jupyter
```bash
jupyter notebook
```

### Accessing Notebook
- **Codespaces**: Automatically forwards port 8888 to `localhost:8888`
- **Local**: Access via `localhost:8888` in browser  
- **Token**: Copy from terminal if prompted
- **Alternative ports**: 8889, 8890 if 8888 is occupied

When you go to `localhost:8888`, you'll need to paste your token output in the terminal to enter your environment. Alternatively, you can directly use the link output in the terminal and follow it.

When Jupyter Notebook is open, it will show your created llm-zoomcamp repo with all the files you've created. In our case, it's just the README.

Create a new Python 3 file to start working there.

## Testing Your Setup

In your new Python 3 file in the Jupyter notebook, you can test the OpenAI API key by running one API call to the model.

You can do this like that:

### OpenAI API Test
```python
from openai import OpenAI

# Create client (uses environment variable)
client = OpenAI()

# Or you can explicitly write your API key here
client = OpenAI(api_key='your-api-key-here')
```

You can test whether the OpenAI API key is set as an environment variable by running:
```python
import os
print(os.environ.get('OPENAI_API_KEY'))
```

<details open>
<summary>If you encounter an issue - Important: Environment Variables in Jupyter</summary>

**Common Issue**: If you started Jupyter Notebook from another terminal (not the one where you exported the OpenAI API key), the terminal finds the key, but Jupyter shows `None` when you check `os.environ.get('OPENAI_API_KEY')`.

**Why this happens:**
- Environment variables are specific to each terminal session
- If you set the variable in Terminal A but start Jupyter from Terminal B, Jupyter won't see it
- Even in the same terminal: if you start Jupyter FIRST, then export the variable, Jupyter won't see it (since it was already running)

This happens because Jupyter runs as a separate process and might not inherit your terminal's environment variables.

**Solutions:**

**Option 1: Set the key directly in Jupyter (Easiest)**
```python
import os
os.environ['OPENAI_API_KEY'] = 'your-actual-api-key-here'

# Verify it worked
print(os.environ.get('OPENAI_API_KEY'))
```

**Option 2: Restart Jupyter from the same terminal**
```bash
# In terminal where you set the environment variable
jupyter notebook
```
</details>

### Test API Call
```python
# Test API call
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Is it too late to join the course?"}
    ]
)

# Check the answer
print(response.choices[0].message.content)
```

**Parameters explained:**
- **`model`**: The model you're calling (e.g., "gpt-4o")
- **`messages`**: List of message objects with `role` and `content`
- **`role`**: Commonly used roles include “system,” “user,” and “assistant.” The “system” provides high-level instructions, the “user” presents queries or prompts, and the “assistant” is the model’s response. By differentiating these roles, we can set the context and direct the conversation efficiently.

## Git Workflow

### Project Structure
```
llm-zoomcamp/
├── 01-intro/
│   └── homework.ipynb
├── 02-rag/
└── README.md
```

### Committing Your Work
```bash
# Stage changes
git add .

# Commit with meaningful message
git commit -m "Module 1 homework completed"

# Push to GitHub
git push
```

**Note**: Stop the codespace when you're done to conserve your free hours.

# Setup Option 2: Anaconda/Miniconda

## When to Choose This Option
- You prefer a Python-focused environment
- You want many libraries pre-installed
- You're familiar with conda package management

## Installation Steps
1. **Anaconda** (larger, more libraries): Visit [docs.anaconda.com](https://docs.anaconda.com/anaconda/install/)
2. **Miniconda** (smaller, minimal): Visit [docs.conda.io](https://docs.conda.io/en/latest/miniconda.html)

### Installing Anaconda/Miniconda
```bash
# Download installer for Miniconda (Linux example)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install
bash Miniconda3-latest-Linux-x86_64.sh

# Accept the terms and conditions

# Initialize conda
conda init
```

### Installing Required Packages
With Anaconda/Miniconda, you only need to install:
```bash
pip install openai elasticsearch tqdm
```

**Pre-installed libraries**: `jupyter`, `pandas`, `scikit-learn`

When this is ready, follow the steps from [Common Setup Steps](#common-setup-steps-all-options).

# Setup Option 3: Local Machine with Docker

Docker delivers software in packages called **containers** that are isolated from each other. This is crucial for data engineering workflows.

**Think of containers as:**
- Lightweight, portable boxes containing everything needed to run an application
- Isolated environments that don't interfere with your host system
- Reproducible environments that work identically everywhere

## When to Choose This Option
- You want full control over your environment
- You plan to work offline frequently
- You have a machine with GPU for Module 2
- You're comfortable with command-line tools

## The Problem Docker Solves

**Without Docker (Traditional Problems):**
- **Version Conflicts**: Multiple Python versions causing PATH issues
- **Library Conflicts**: Project A needs pandas 1.0, Project B needs pandas 2.0
- **"Works on My Machine"**: Code works locally but fails in production
- **Installation Nightmares**: Complex setup procedures for each tool
- **System Pollution**: Leftover files and configurations cluttering your system

**With Docker (Clean Solution):**
```
Your Computer:
├── Container 1: Python 3.9 + LLM libraries + your scripts
├── Container 2: PostgreSQL 13 database
├── Container 3: Elasticsearch for document search  
├── Container 4: Another project (completely isolated)
└── Host machine stays clean and unaffected
```

## Installing Docker

1. Visit [Docker's official website](https://docs.docker.com/get-docker/)
2. Download installer for your operating system
3. Follow installation instructions
4. Test installation: `docker run hello-world`

For detailed Docker learning, check the [Data Engineering Zoomcamp Docker module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform).

## Terminal Setup by OS
- **Windows**: Git Bash (recommended), WSL, or PowerShell
- **macOS**: Built-in Terminal
- **Linux**: Built-in terminal

## Creating Your Environment

### Method A: Using Dockerfile (Recommended)
Create a `Dockerfile`:
```dockerfile
FROM python:3.9

# Install required libraries
RUN pip install jupyter==7.1.2 openai elasticsearch scikit-learn pandas

# Set working directory
WORKDIR /app

# Default to bash for interactive use
ENTRYPOINT ["/bin/bash"]
```

Build and run:
```bash
# Build your image
docker build -t llm-course .

# Run interactive container
docker run -it llm-course
```

### Method B: Direct Installation
```bash
# Run Python container
docker run -it python:3.9 bash

# Inside container, install libraries
pip install jupyter==7.1.2 openai elasticsearch scikit-learn pandas
```

**Important**: Changes in running containers are lost when stopped. Use Dockerfiles for permanent setups.

When this is ready, follow the steps from [Common Setup Steps](#common-setup-steps-all-options).

# Summary and Next Steps

## What You Should Have Now
- ✅ Working development environment (one of the three options)
- ✅ All required Python libraries installed
- ✅ OpenAI API key configured
- ✅ Jupyter notebook running
- ✅ Git repository set up

## Key Takeaways
1. **Multiple paths work**: Choose the setup that matches your experience level
2. **Reproducibility matters**: Docker ensures consistent environments
3. **Security first**: Protect your API keys
4. **Version control**: Use Git for tracking your progress

## Next Steps
Module 1.3 will cover:
- Document indexing with search engines
- Building your first RAG (Retrieval-Augmented Generation) pipeline
- Working with the search implementation

**Recommended**: Complete a simple test notebook to verify everything works before proceeding.
