# Course Chat Assistant (Streamlit)

This project provides a Streamlit web app for interacting with a course teaching assistant powered by OpenAI and custom tools.

## Features
- Chat interface in your browser
- Uses OpenAI's GPT models
- Supports custom tools (see `tools.py`)

## Setup

Install dependencies
```
pip install streamlit openai requests minsearch
```


Run the Streamlit app
```
streamlit run chat.py
```

This will open a browser window at `http://localhost:8501` where you can chat with the assistant.

## Customization
- Edit `tools.py` to add more tools.
- Modify the prompt in `chat.py` to change the assistant's behavior.