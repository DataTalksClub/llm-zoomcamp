import streamlit as st
import time
import uuid

from assistant import get_answer
from db import save_conversation, save_feedback


def print_log(message):
    print(message, flush=True)


def main():
    print_log("Starting the Course Assistant application")
    st.title("Course Assistant")

    # Session state initialization
    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
        print_log(
            f"New conversation started with ID: {st.session_state.conversation_id}"
        )
    if "count" not in st.session_state:
        st.session_state.count = 0
        print_log("Feedback count initialized to 0")

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp",
         "data-engineering-zoomcamp",
         "mlops-zoomcamp"],
    )
    print_log(f"User selected course: {course}")

    # Model selection
    model_choice = st.selectbox("Select a model:", ["Ollama", "OpenAI"])
    print_log(f"User selected model: {model_choice}")

    # Search type selection
    search_type = st.radio("Select search type:", ["Text", "Vector"])
    print_log(f"User selected search type: {search_type}")

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        print_log(f"User asked: '{user_input}'")
        with st.spinner("Processing..."):
            print_log(
                f"Getting answer from assistant using {model_choice} model and {search_type} search"
            )
            start_time = time.time()
            output = get_answer(
                user_input, course, model_choice.lower(), search_type.lower()
            )
            end_time = time.time()
            print_log(f"Answer received in {end_time - start_time:.2f} seconds")
            st.success("Completed!")
            st.write(output)

            # Save conversation to database
            print_log("Saving conversation to database")
            save_conversation(
                st.session_state.conversation_id, user_input, output, course
            )
            print_log("Conversation saved successfully")

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            print_log(
                f"Positive feedback received. New count: {st.session_state.count}"
            )
            save_feedback(st.session_state.conversation_id, 1)
            print_log("Positive feedback saved to database")
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            print_log(
                f"Negative feedback received. New count: {st.session_state.count}"
            )
            save_feedback(st.session_state.conversation_id, -1)
            print_log("Negative feedback saved to database")

    st.write(f"Current count: {st.session_state.count}")

    print_log("Streamlit app loop completed")


if __name__ == "__main__":
    print_log("Course Assistant application started")
    main()
