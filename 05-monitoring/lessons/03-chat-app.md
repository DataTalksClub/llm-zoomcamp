# Chat App

Video: [Watch this lesson](https://www.youtube.com/watch?v=JCB4JZlMsIQ&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

The command line works, but we want something closer to how a person
would actually talk to the assistant. So we wrap it in a small web
interface. We use Streamlit, a Python framework for building front ends
with almost no code.

This isn't the final product, and it isn't meant to be pretty. I kept it
deliberately simple so there's nothing to explain. If you want a nicer
interface, hand it to a coding assistant like Claude Code or Codex. Ask
it to improve the layout. For now, plain is fine.

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

That's another long command, so it goes into the `Makefile` too:

```makefile
chat:
	uv run streamlit run app.py
```

Now we can run:

```bash
make chat
```

If you're in GitHub Codespaces, it detects the port and forwards it for
you. Open the link and you get a web interface. Ask a question like "How
do I join the course?" and the answer comes back.

The RAG works, but right now we track nothing about it: no response
time, no token usage, no cost. That's exactly the visibility monitoring
is supposed to give us, so that's what we add next.

[← Assistant](02-assistant-setup.md) | [Capturing Metrics →](04-metrics.md)
