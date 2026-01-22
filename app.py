import streamlit as st
import requests
import time
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Chatbot - Kavishka Dileepa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - ChatGPT Style
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    .stApp {
        background: #343541;
    }
    
    [data-testid="stSidebar"] {
        background: #202123;
        border-right: 1px solid #444654;
    }
    
    [data-testid="stSidebar"] .stButton button {
        background: transparent;
        border: 1px solid #444654;
        color: white;
        border-radius: 6px;
        padding: 10px 16px;
        width: 100%;
        text-align: left;
        transition: all 0.2s;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background: #2a2b32;
    }
    
    .main .block-container {
        padding: 0;
        max-width: 100%;
    }
    
    .chat-header {
        background: #343541;
        border-bottom: 1px solid #444654;
        padding: 12px 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .chat-header h1 {
        color: white;
        font-size: 16px;
        font-weight: 600;
        margin: 0;
    }
    
    .chat-header .status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #19c37d;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .status-dot {
        width: 6px;
        height: 6px;
        background: white;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 60vh;
        padding: 20px;
        text-align: center;
    }
    
    .welcome-icon {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(16, 163, 127, 0.3);
    }
    
    .welcome-title {
        color: white;
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .welcome-subtitle {
        color: #acacbe;
        font-size: 16px;
        margin-bottom: 40px;
        max-width: 500px;
    }
    
    .stChatMessage {
        background: #444654;
        border: none;
        border-radius: 0;
        padding: 24px;
        margin: 0;
    }
    
    .stChatMessage[data-testid*="user"] {
        background: #343541;
    }
    
    [data-testid="stChatMessageContent"] {
        color: white;
        font-size: 15px;
        line-height: 1.6;
    }
    
    [data-testid="stChatMessageAvatarAssistant"] {
        background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%);
        width: 32px;
        height: 32px;
    }
    
    [data-testid="stChatMessageAvatarUser"] {
        background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
        width: 32px;
        height: 32px;
    }
    
    .stChatInput {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #343541;
        border-top: 1px solid #444654;
        padding: 20px;
        z-index: 100;
    }
    
    .stChatInput > div {
        max-width: 768px;
        margin: 0 auto;
        background: #40414f;
        border: 1px solid #565869;
        border-radius: 12px;
    }
    
    .stChatInput input {
        background: transparent;
        border: none;
        color: white;
        font-size: 15px;
        padding: 12px 16px;
    }
    
    .stChatInput input::placeholder {
        color: #8e8ea0;
    }
    
    @media (max-width: 768px) {
        .welcome-title {
            font-size: 24px;
        }
        .stChatMessage {
            padding: 16px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="chat-header">
    <h1>🤖 AI Chatbot</h1>
    <div class="status">
        <div class="status-dot"></div>
        Online
    </div>
</div>
""", unsafe_allow_html=True)

def generate_response(prompt):
    try:
        if "HF_TOKEN" in st.secrets:
            API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
            headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
            payload = {"inputs": prompt, "parameters": {"max_length": 100, "temperature": 0.7}}
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', '').strip()
    except:
        pass

    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers={}, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', '').strip()
    except:
        pass

    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! 👋 It's great to meet you. I'm here to help with any questions or tasks you have."
    elif any(word in prompt_lower for word in ['how are you']):
        return "I'm doing wonderfully! As an AI, I'm always ready to assist. How can I help you today?"
    elif any(word in prompt_lower for word in ['your name', 'who are you']):
        return "I'm an AI assistant created by Kavishka Dileepa. I'm designed to help answer questions and have conversations!"
    elif any(word in prompt_lower for word in ['thank']):
        return "You're very welcome! 😊 Happy to help!"
    elif any(word in prompt_lower for word in ['bye', 'goodbye']):
        return "Goodbye! 👋 It was great chatting. Come back anytime!"
    elif any(word in prompt_lower for word in ['help', 'what can you']):
        return "I can help with answering questions, explaining concepts, having conversations, and more!"
    elif '?' in prompt:
        return "That's interesting! Could you provide more context so I can give you a better answer?"
    else:
        return "I'm here to help! What would you like to explore?"

if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

with st.sidebar:
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_count += 1
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 💬 Recent Chats")
    st.markdown("Current Conversation")
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    
    if st.button("🗑️ Clear All Chats", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #8e8ea0; font-size: 12px; padding: 20px;'>
        <p>Made with ❤️ by<br><strong style='color: #10a37f;'>Kavishka Dileepa</strong></p>
        <p style='margin-top: 8px;'>© 2026 All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)

if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-icon">🤖</div>
        <div class="welcome-title">How can I help you today?</div>
        <div class="welcome-subtitle">
            I'm here to answer questions, provide information, and have conversations. Just type your message below!
        </div>
    </div>
    """, unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message AI Chatbot..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)
            response = generate_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
