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

    /* Hide default Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Main Background */
    .stApp {
        background: #343541;
    }

    /* Sidebar Styling */
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

    /* Main Container */
    .main .block-container {
        padding: 0;
        max-width: 100%;
    }

    /* Header */
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

    /* Welcome Screen */
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

    .example-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 16px;
        max-width: 900px;
        width: 100%;
        margin-top: 20px;
    }

    .example-card {
        background: #444654;
        border: 1px solid #565869;
        border-radius: 12px;
        padding: 20px;
        cursor: pointer;
        transition: all 0.2s;
        text-align: left;
    }

    .example-card:hover {
        background: #4a4b5a;
        border-color: #10a37f;
        transform: translateY(-2px);
    }

    .example-icon {
        font-size: 24px;
        margin-bottom: 12px;
    }

    .example-title {
        color: white;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 6px;
    }

    .example-desc {
        color: #acacbe;
        font-size: 12px;
    }

    /* Chat Messages */
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

    /* Avatar Styling */
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

    /* Chat Input */
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
        box-shadow: 0 0 0 1px transparent;
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

    .stChatInput input:focus {
        box-shadow: 0 0 0 2px #10a37f;
    }

    /* Sidebar Content */
    .sidebar-section {
        padding: 12px;
        margin: 12px 0;
    }

    .sidebar-title {
        color: #8e8ea0;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
        padding: 0 8px;
    }

    .sidebar-item {
        color: white;
        padding: 10px 12px;
        border-radius: 6px;
        font-size: 14px;
        margin: 4px 0;
        cursor: pointer;
        transition: background 0.2s;
    }

    .sidebar-item:hover {
        background: #2a2b32;
    }

    .user-profile {
        position: absolute;
        bottom: 20px;
        left: 12px;
        right: 12px;
        background: #2a2b32;
        border-radius: 8px;
        padding: 12px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .user-avatar {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
    }

    .user-info {
        flex: 1;
    }

    .user-name {
        color: white;
        font-size: 14px;
        font-weight: 500;
    }

    .user-plan {
        color: #8e8ea0;
        font-size: 12px;
    }

    /* Typing Indicator */
    .typing-indicator {
        display: flex;
        gap: 4px;
        padding: 8px 0;
    }

    .typing-dot {
        width: 8px;
        height: 8px;
        background: #8e8ea0;
        border-radius: 50%;
        animation: typing 1.4s infinite;
    }

    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }

    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes typing {
        0%, 60%, 100% {
            transform: translateY(0);
            opacity: 0.7;
        }
        30% {
            transform: translateY(-8px);
            opacity: 1;
        }
    }

    /* Responsive */
    @media (max-width: 768px) {
        .welcome-title {
            font-size: 24px;
        }

        .example-cards {
            grid-template-columns: 1fr;
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


# Generate AI Response
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

    if any(word in prompt_lower for word in ['hello', 'hi', 'hey', 'greetings']):
        return "Hello! 👋 It's great to meet you. I'm here to help with any questions or tasks you have. What would you like to talk about?"
    elif any(word in prompt_lower for word in ['how are you', 'how r u', 'whats up']):
        return "I'm doing wonderfully, thank you for asking! As an AI, I'm always ready to assist. How can I help you today?"
    elif any(word in prompt_lower for word in ['your name', 'who are you', 'what are you']):
        return "I'm an AI assistant created by Kavishka Dileepa. I'm designed to help answer questions, provide information, and have engaging conversations. What would you like to know?"
    elif any(word in prompt_lower for word in ['thank', 'thanks']):
        return "You're very welcome! I'm happy I could help. Is there anything else you'd like to discuss? 😊"
    elif any(word in prompt_lower for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! It was a pleasure chatting with you. Feel free to return anytime you need assistance. Have a great day! 👋"
    elif any(word in prompt_lower for word in ['help', 'what can you do']):
        return "I can assist you with:\n\n• Answering questions on various topics\n• Providing explanations and information\n• Having natural conversations\n• Helping with problem-solving\n• And much more!\n\nJust ask me anything you'd like to know!"
    elif '?' in prompt:
        return "That's an interesting question! While I'm currently in simplified mode, I'd love to help you explore this topic. Could you provide more context or rephrase your question?"
    else:
        return "I understand what you're saying. I'm here to help with questions, provide information, or just have a conversation. What would you like to talk about?"


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_count += 1
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">Recent Chats</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">💬 Current Conversation</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### ⚙️ Settings")
    if st.button("🗑️ Clear All Chats", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("""
    <div class="user-profile">
        <div class="user-avatar">U</div>
        <div class="user-info">
            <div class="user-name">User</div>
            <div class="user-plan">Free Plan</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; color: #8e8ea0; font-size: 12px; padding: 20px;'>
        <p>Made with ❤️ by<br><strong style='color: #10a37f;'>Kavishka Dileepa</strong></p>
        <p style='margin-top: 8px;'>© 2026 All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)

# Main Chat Area
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-icon">🤖</div>
        <div class="welcome-title">How can I help you today?</div>
        <div class="welcome-subtitle">
            I'm here to answer questions, provide information, and have conversations. Just type your message below!
        </div>

        <div class="example-cards">
            <div class="example-card">
                <div class="example-icon">💡</div>
                <div class="example-title">Explain concepts simply</div>
                <div class="example-desc">Break down complex topics into easy-to-understand explanations</div>
            </div>
            <div class="example-card">
                <div class="example-icon">🎯</div>
                <div class="example-title">Get quick answers</div>
                <div class="example-desc">Fast and accurate responses to your questions</div>
            </div>
            <div class="example-card">
                <div class="example-icon">📚</div>
                <div class="example-title">Learn something new</div>
                <div class="example-desc">Explore any subject with detailed information</div>
            </div>
            <div class="example-card">
                <div class="example-icon">🤝</div>
                <div class="example-title">Have a conversation</div>
                <div class="example-desc">Natural dialogue on any topic you're interested in</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Message AI Chatbot..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner(""):
            st.markdown("""
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            response = generate_response(prompt)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()