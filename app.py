import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Chatbot", layout="centered")


@st.cache_resource
def load_chatbot():
    return pipeline("text-generation", model="microsoft/DialoGPT-medium")


st.title("🤖 AI Chatbot")
chatbot = load_chatbot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chatbot(prompt, max_length=100)[0]['generated_text']
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})