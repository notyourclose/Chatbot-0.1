import time
import requests
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot - Kavishka Dileepa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Exact ChatGPT.com styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sohne:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Sohne', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

.stApp {
    background: #343541;
    overflow: hidden;
}

/* Sidebar - Exact ChatGPT style */
[data-testid="stSidebar"] {
    background: #202123;
    border-right: 1px solid rgba(255,255,255,0.1);
    min-width: 260px !important;
    max-width: 320px !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 8px;
}

[data-testid="stSidebar"] .stButton {
    width: 100%;
}

[data-testid="stSidebar"] .stButton > button {
    background: transparent;
    border: 1px solid rgba(255,255,255,0.2);
    color: white;
    border-radius: 8px;
    padding: 12px;
    width: 100%;
    text-align: left;
    font-size: 14px;
    font-weight: 500;
    transition: background-color 0.2s;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.1);
    border-color: rgba(255,255,255,0.3);
}

[data-testid="stSidebar"] .stMarkdown {
    color: rgba(255,255,255,0.8);
    font-size: 13px;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.1);
    margin: 16px 0;
}

/* Main container */
.main .block-container {
    padding: 0;
    max-width: 100%;
    padding-bottom: 140px;
    height: 100vh;
    overflow-y: auto;
}

/* Header bar */
.chat-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: #343541;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding: 12px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
}

.chat-header-title {
    color: white;
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
}

.chat-header-model {
    color: rgba(255,255,255,0.6);
    font-size: 12px;
    padding: 4px 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 4px;
}

/* Chat messages - ChatGPT style */
.stChatMessage {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

.stChatMessage[data-testid*="user"] {
    background: #343541 !important;
}

.stChatMessage[data-testid*="assistant"] {
    background: #444654 !important;
}

[data-testid="stChatMessageContent"] {
    color: #ececf1;
    font-size: 16px;
    line-height: 1.75;
    max-width: 768px;
    margin: 0 auto;
    padding: 24px 16px;
    word-wrap: break-word;
}

[data-testid="stChatMessageAvatarAssistant"] {
    background: #10a37f;
    width: 30px;
    height: 30px;
    margin-right: 16px;
    margin-left: 16px;
    border-radius: 2px;
}

[data-testid="stChatMessageAvatarUser"] {
    background: #5436da;
    width: 30px;
    height: 30px;
    margin-left: 16px;
    margin-right: 16px;
    border-radius: 2px;
}

/* Chat input - Fixed bottom like ChatGPT */
.stChatInput {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    background: #343541 !important;
    border-top: 1px solid rgba(255,255,255,0.1) !important;
    padding: 16px !important;
    z-index: 1000 !important;
}

.stChatInput > div {
    max-width: 768px;
    margin: 0 auto;
    background: #40414f;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px;
    padding: 12px;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
}

.stChatInput textarea {
    background: transparent !important;
    border: none !important;
    color: white !important;
    font-size: 16px !important;
    padding: 0 !important;
    resize: none !important;
    line-height: 1.5;
    min-height: 24px;
    max-height: 200px;
}

.stChatInput textarea::placeholder {
    color: #8e8ea0 !important;
}

.stChatInput textarea:focus {
    outline: none !important;
    box-shadow: none !important;
}

.stChatInput button {
    background: transparent !important;
    border: none !important;
    color: #8e8ea0 !important;
    padding: 4px !important;
}

.stChatInput button:hover {
    color: white !important;
}

.stChatInput button svg {
    width: 20px;
    height: 20px;
}

/* Welcome screen - ChatGPT style */
.welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: calc(100vh - 200px);
    padding: 40px 20px;
    text-align: center;
    max-width: 768px;
    margin: 0 auto;
}

.welcome-title {
    color: white;
    font-size: 36px;
    font-weight: 600;
    margin-bottom: 8px;
    line-height: 1.2;
    letter-spacing: -0.02em;
}

.welcome-subtitle {
    color: rgba(236,236,241,0.8);
    font-size: 16px;
    margin-bottom: 32px;
    line-height: 1.6;
}

.example-prompts {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    width: 100%;
    max-width: 768px;
    margin-top: 24px;
}

.example-prompt {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 16px;
    text-align: left;
    cursor: pointer;
    transition: all 0.2s;
    color: white;
}

.example-prompt:hover {
    background: rgba(255,255,255,0.1);
    border-color: rgba(255,255,255,0.2);
}

.example-prompt-icon {
    font-size: 20px;
    margin-bottom: 8px;
    display: block;
}

.example-prompt-title {
    font-weight: 600;
    margin-bottom: 4px;
    color: white;
    font-size: 14px;
}

.example-prompt-desc {
    color: rgba(236,236,241,0.6);
    font-size: 13px;
    line-height: 1.5;
}

/* Sidebar styling */
.sidebar-header {
    padding: 8px;
    margin-bottom: 8px;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px;
    color: white;
    font-size: 14px;
    font-weight: 600;
}

.sidebar-logo-icon {
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%);
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 800;
    font-size: 16px;
}

.sidebar-section-title {
    padding: 8px 12px;
    color: rgba(255,255,255,0.5);
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 16px;
    margin-bottom: 4px;
}

.sidebar-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 16px;
    border-top: 1px solid rgba(255,255,255,0.1);
    text-align: center;
}

.sidebar-footer-text {
    color: rgba(255,255,255,0.5);
    font-size: 12px;
    margin: 0;
}

.sidebar-footer-name {
    color: #10a37f;
    font-weight: 600;
    font-size: 12px;
}

/* Responsive */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        position: fixed;
        z-index: 2000;
        transform: translateX(-100%);
        transition: transform 0.3s;
    }
    
    .welcome-title {
        font-size: 28px;
    }
    
    .example-prompts {
        grid-template-columns: 1fr;
    }
    
    [data-testid="stChatMessageContent"] {
        font-size: 15px;
        padding: 20px 12px;
    }
    
    .stChatInput {
        padding: 12px !important;
    }
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #202123;
}

::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.2);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255,255,255,0.3);
}

/* Loading */
.stSpinner > div {
    border-color: #10a37f transparent transparent transparent !important;
}

/* Remove Streamlit default spacing */
.stChatMessage > div {
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

def generate_response(prompt: str) -> str:
    """Generate AI response using HuggingFace API or fallback"""
    try:
        if "HF_TOKEN" in st.secrets:
            api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
            headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
            payload = {"inputs": prompt, "parameters": {"max_length": 150, "temperature": 0.7}}
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    text = (result[0].get("generated_text") or "").strip()
                    if text:
                        return text
    except Exception:
        pass
    
    try:
        api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        response = requests.post(api_url, json={"inputs": prompt}, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                text = (result[0].get("generated_text") or "").strip()
                if text:
                    return text
    except Exception:
        pass
    
    # Fallback responses
    p = prompt.lower()
    if any(w in p for w in ["hello", "hi", "hey"]):
        return "Hello! 👋 It's great to meet you. I'm here to help with any questions or tasks you have. What would you like to know?"
    if "how are you" in p:
        return "I'm doing wonderfully! As an AI, I'm always ready to assist. How can I help you today?"
    if any(w in p for w in ["your name", "who are you"]):
        return "I'm an AI assistant created by Kavishka Dileepa. I'm designed to help answer questions, explain concepts, and have meaningful conversations!"
    if "thank" in p:
        return "You're very welcome! 😊 Happy to help!"
    if any(w in p for w in ["bye", "goodbye"]):
        return "Goodbye! 👋 It was great chatting. Come back anytime!"
    if any(w in p for w in ["help", "what can you"]):
        return "I can help with:\n- Answering questions\n- Explaining concepts\n- Having conversations\n- Providing information\n- And much more!\n\nWhat would you like to explore?"
    if "?" in prompt:
        return "That's an interesting question! Could you provide a bit more context so I can give you a more helpful answer?"
    return "I'm here to help! Feel free to ask me anything — questions, explanations, or just chat. What would you like to know?"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# Sidebar - ChatGPT style
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-logo">
            <div class="sidebar-logo-icon">AI</div>
            <div>
                <div style="color: white; font-size: 14px; font-weight: 600;">AI Chatbot</div>
                <div style="color: rgba(255,255,255,0.6); font-size: 12px;">by Kavishka Dileepa</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("➕ New Chat", use_container_width=True, key="new_chat"):
        st.session_state.messages = []
        st.session_state.chat_count += 1
        st.rerun()
    
    st.markdown('<div class="sidebar-section-title">Recent</div>', unsafe_allow_html=True)
    
    if st.session_state.chat_count > 0:
        st.markdown(f"**Chat #{st.session_state.chat_count}**")
    else:
        st.markdown("**Current Conversation**")
    
    st.markdown("---")
    
    if st.button("🗑️ Clear All Chats", use_container_width=True, key="clear_chat"):
        st.session_state.messages = []
        st.session_state.chat_count = 0
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    <div class="sidebar-footer">
        <p class="sidebar-footer-text">Made with ❤️ by</p>
        <p class="sidebar-footer-name">Kavishka Dileepa</p>
        <p class="sidebar-footer-text" style="margin-top: 8px;">© 2026 All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)

# Header bar
st.markdown("""
<div class="chat-header">
    <div class="chat-header-title">
        <span>🤖</span>
        <span>AI Chatbot</span>
    </div>
    <div class="chat-header-model">GPT-3.5</div>
</div>
""", unsafe_allow_html=True)

# Main chat area
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-title">How can I help you today?</div>
        <div class="welcome-subtitle">
            I'm here to answer questions, provide information, and have conversations. 
            Try one of these examples:
        </div>
        <div class="example-prompts">
            <div class="example-prompt" onclick="const textarea = document.querySelector('[data-testid=stChatInput] textarea'); if(textarea) { textarea.value='Can you explain quantum physics in simple terms?'; textarea.dispatchEvent(new Event('input', {bubbles: true})); }">
                <span class="example-prompt-icon">💡</span>
                <div class="example-prompt-title">Explain concepts</div>
                <div class="example-prompt-desc">Break down complex topics into easy-to-understand explanations</div>
            </div>
            <div class="example-prompt" onclick="const textarea = document.querySelector('[data-testid=stChatInput] textarea'); if(textarea) { textarea.value='What can you help me with?'; textarea.dispatchEvent(new Event('input', {bubbles: true})); }">
                <span class="example-prompt-icon">⚡</span>
                <div class="example-prompt-title">Get quick answers</div>
                <div class="example-prompt-desc">Fast and accurate responses to your questions</div>
            </div>
            <div class="example-prompt" onclick="const textarea = document.querySelector('[data-testid=stChatInput] textarea'); if(textarea) { textarea.value='Teach me something interesting about space'; textarea.dispatchEvent(new Event('input', {bubbles: true})); }">
                <span class="example-prompt-icon">📚</span>
                <div class="example-prompt-title">Learn something new</div>
                <div class="example-prompt-desc">Explore any subject with detailed information</div>
            </div>
            <div class="example-prompt" onclick="const textarea = document.querySelector('[data-testid=stChatInput] textarea'); if(textarea) { textarea.value='Let\\'s chat about technology trends'; textarea.dispatchEvent(new Event('input', {bubbles: true})); }">
                <span class="example-prompt-icon">💬</span>
                <div class="example-prompt-title">Have a conversation</div>
                <div class="example-prompt-desc">Natural dialogue on any topic you're interested in</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Message AI Chatbot..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(0.5)
            response = generate_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
