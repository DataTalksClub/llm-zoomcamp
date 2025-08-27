import streamlit as st
from openai import OpenAI
import tools

from tracing import tracer
from opentelemetry.trace import Status, StatusCode  # type: ignore

client =  OpenAI()
index = tools.init_index()
search_tool = tools.SearchTool(index)
chat_tools = tools.Tools()

try:
    decorated_search = tracer.tool(name="search", description="Search course FAQ")(search_tool.search)
    chat_tools.add_tool(decorated_search, search_tool.search_tool)
except Exception:
    pass

developer_prompt = """
You're a course teaching assistant. 
You're given a question from a course student and your task is to answer it.

Use FAQ if your own knowledge is not sufficient to answer the question.

At the end of each response, ask the user a follow up question based on your answer.
""".strip()

# --- Streamlit Chat App ---

st.set_page_config(page_title="Course Chat Assistant", page_icon="💬")
st.title("Course Chat Assistant")

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "developer", "content": developer_prompt},
    ]
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
if "pending_response" not in st.session_state:
    st.session_state.pending_response = False

for msg in st.session_state.display_messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
    elif msg["role"] == "function_call":
        with st.chat_message("assistant"):
            with st.expander(f"Function call: {msg['name']}({msg['arguments']})"):
                st.markdown(f"**Call:** `{msg['name']}({msg['arguments']})`")
                st.markdown(f"**Output:**\n```json\n{msg['output']}\n```")

prompt = st.chat_input("Ask a question...")
if prompt:
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    st.session_state.display_messages.append({"role": "user", "content": prompt})
    st.session_state.pending_response = True
    st.rerun()

if st.session_state.pending_response:
    with tracer.start_as_current_span("assistant-turn", openinference_span_kind="chain") as span:
        try:
            chain_input_question = ""
            chain_output_answer = ""
            while True:
                with tracer.start_as_current_span("Responses.create", openinference_span_kind="llm") as llm_span:
                    llm_span.set_attribute("llm.model_name", "gpt-4o-mini")
                    try:
                        llm_span.set_attribute("openinference.span.kind", "LLM")
                    except Exception:
                        pass
                    llm_span.set_attribute("llm.input_messages.count", int(len(st.session_state.chat_messages)))
                    
                    last_user_message = ""
                    for msg in reversed(st.session_state.chat_messages):
                        if isinstance(msg, dict) and msg.get("role") == "user":
                            last_user_message = str(msg.get("content", ""))
                            break
                    
                    if last_user_message:
                        llm_span.set_attribute("llm.input.preview", tools.shorten(last_user_message, 500))
                        try:
                            llm_span.set_attribute("input.value", tools.shorten(last_user_message, 2000))
                        except Exception:
                            pass
                        chain_input_question = last_user_message
                    
                    available_tools = chat_tools.get_tools()
                    llm_span.set_attribute("llm.tools.count", int(len(available_tools)))
                    if available_tools:
                        tool_names = []
                        for tool in available_tools:
                            if isinstance(tool, dict) and "name" in tool:
                                tool_names.append(tool["name"])
                            elif hasattr(tool, "name"):
                                tool_names.append(tool.name)
                        if tool_names:
                            llm_span.set_attribute("llm.tools.names", ", ".join(tool_names))

                    response = client.responses.create(
                        model='gpt-4o-mini',
                        input=st.session_state.chat_messages,
                        tools=available_tools,
                    )
                    
                    has_tool_calls = False
                    tool_calls_this_turn = 0
                    assistant_message = ""
                    
                    for entry in response.output:
                        st.session_state.chat_messages.append(entry)
                        if entry.type == "function_call":
                            result = chat_tools.function_call(entry)
                            st.session_state.chat_messages.append(result)
                            st.session_state.display_messages.append({
                                "role": "function_call",
                                "name": entry.name,
                                "arguments": tools.shorten(entry.arguments),
                                "output": result["output"],
                            })
                            has_tool_calls = True
                            tool_calls_this_turn += 1
                        elif entry.type == "message":
                            try:
                                first_part = entry.content[0]
                                content_text = getattr(first_part, "text", None)
                                if content_text is None:
                                    content_text = getattr(first_part, "refusal", "")
                                if not isinstance(content_text, str):
                                    content_text = str(content_text)
                            except Exception:
                                content_text = ""
                            st.session_state.display_messages.append({
                                "role": "assistant",
                                "content": content_text,
                            })
                            assistant_message = content_text
                    
                    try:
                        if assistant_message:
                            llm_span.set_attribute("llm.output.preview", tools.shorten(assistant_message, 500))
                            try:
                                llm_span.set_attribute("output.value", tools.shorten(assistant_message, 2000))
                            except Exception:
                                pass
                            chain_output_answer = assistant_message
                        else:
                            llm_span.set_attribute("llm.output.preview", "No text response")
                        
                        message_count = len([e for e in response.output if e.type == "message"])
                        function_call_count = len([e for e in response.output if e.type == "function_call"])
                        
                        llm_span.set_attribute("llm.output_messages.count", int(message_count))
                        llm_span.set_attribute("llm.function_calls.count", int(function_call_count))
                        
                        llm_span.set_attribute("llm.output.entries.count", int(len(response.output)))
                        
                        if function_call_count > 0:
                            function_names = []
                            for e in response.output:
                                if e.type == "function_call":
                                    function_names.append(e.name)
                            if function_names:
                                llm_span.set_attribute("llm.function_calls.names", ", ".join(function_names))
                                
                    except Exception as e:
                        print(f"Error setting LLM output attributes: {e}")
                if not has_tool_calls:
                    break
        except Exception as e:
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR))
        else:
            try:
                span.set_attribute("chain.messages.count", int(len(st.session_state.chat_messages)))
                span.set_attribute("chain.tool_calls.count", int(tool_calls_this_turn))
                if chain_input_question:
                    span.set_attribute("input.value", tools.shorten(chain_input_question, 2000))
                if chain_output_answer:
                    span.set_attribute("output.value", tools.shorten(chain_output_answer, 2000))
            except Exception:
                pass
            span.set_status(Status(StatusCode.OK))
    st.session_state.pending_response = False
    st.rerun()