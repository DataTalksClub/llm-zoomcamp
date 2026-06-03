# Chat App

Wrap the assistant in a web interface. Streamlit is a Python
framework that makes it easy to build web apps with minimal code.

Add Streamlit to your project:

```bash
uv add streamlit
```

Create `app.py`:

```python
import streamlit as st
from assistant import create_assistant

assistant = create_assistant()

st.title("Course Assistant")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Processing..."):
        answer = assistant.rag(user_input)
        st.success("Completed!")
        st.write(answer)
```

Run the app:

```bash
uv run streamlit run app.py
```

Add a `chat` target to the `Makefile`:

```makefile
chat:
	uv run streamlit run app.py
```

Now we can run:

```bash
make chat
```

You should see a web interface where you can ask questions and see
the answer.

Right now we don't track anything - no response time, no token usage,
no cost. In the next lesson, we'll add metrics capture to monitor the
LLM calls.

[← Assistant](02-assistant-setup.md) | [Capturing Metrics →](04-metrics.md)
