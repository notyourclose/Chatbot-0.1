import time
import requests
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot - Kavishka Dileepa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ChatGPT-style CSS - Clean, responsive, modern
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* { 
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    box-sizing: border-box;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

.stApp {
    background: #343541;
}

/* Sidebar - ChatGPT style */
[data-testid="stSidebar"] {
    background: #202123;
    border-right: 1px solid #444654;
    min-width: 260px !important;
}

[data-testid="stSidebar"] .stButton button {
    background: transparent;
    border: 1px solid #444654;
    color: white;
    border-radius: 8px;
    padding: 12px 16px;
    width: 100%;
    text-align: left;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s;
    margin-bottom: 8px;
}

[data-testid="stSidebar"] .stButton button:hover {
    background: #2a2b32;
    border-color: #565869;
}

[data-testid="stSidebar"] .stMarkdown {
    color: rgba(255,255,255,0.8);
}

/* Main container */
.main .block-container {
    padding: 0;
    max-width: 100%;
    padding-bottom: 120px;
}

/* Chat messages */
.stChatMessage {
    background: transparent !important;
    border: none !important;
    padding: 20px 0 !important;
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
    padding: 0 20px;
}

[data-testid="stChatMessageAvatarAssistant"] {
    background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%);
    width: 30px;
    height: 30px;
    margin-right: 12px;
}

[data-testid="stChatMessageAvatarUser"] {
    background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
    width: 30px;
    height: 30px;
    margin-left: 12px;
}

/* Chat input - Fixed at bottom */
.stChatInput {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    background: #343541 !important;
    border-top: 1px solid #444654 !important;
    padding: 20px !important;
    z-index: 1000 !important;
}

.stChatInput > div {
    max-width: 768px;
    margin: 0 auto;
    background: #40414f;
    border: 1px solid #565869;
    border-radius: 12px;
    padding: 4px;
}

.stChatInput textarea {
    background: transparent !important;
    border: none !important;
    color: white !important;
    font-size: 16px !important;
    padding: 12px 16px !important;
    resize: none !important;
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
}

.stChatInput button:hover {
    color: white !important;
}

/* Welcome screen */
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

.welcome-icon {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(16, 163, 127, 0.3);
}

.welcome-title {
    color: white;
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 12px;
    line-height: 1.2;
}

.welcome-subtitle {
    color: #acacbe;
    font-size: 16px;
    margin-bottom: 32px;
    line-height: 1.6;
}

.example-prompts {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 12px;
    width: 100%;
    max-width: 768px;
    margin-top: 24px;
}

.example-prompt {
    background: #40414f;
    border: 1px solid #565869;
    border-radius: 12px;
    padding: 16px;
    text-align: left;
    cursor: pointer;
    transition: all 0.2s;
    color: white;
    font-size: 14px;
}

.example-prompt:hover {
    background: #4a4b5a;
    border-color: #10a37f;
    transform: translateY(-2px);
}

.example-prompt-title {
    font-weight: 600;
    margin-bottom: 4px;
    color: white;
}

.example-prompt-desc {
    color: #acacbe;
    font-size: 13px;
    line-height: 1.5;
}

/* Sidebar content */
.sidebar-section {
    padding: 12px 16px;
    color: rgba(255,255,255,0.6);
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 16px;
    margin-bottom: 8px;
}

.sidebar-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 16px;
    border-top: 1px solid #444654;
    text-align: center;
    color: rgba(255,255,255,0.5);
    font-size: 12px;
}

.sidebar-footer strong {
    color: #10a37f;
    font-weight: 600;
}

/* Responsive */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        min-width: 0 !important;
        width: 100% !important;
    }
    
    .welcome-title {
        font-size: 24px;
    }
    
    .example-prompts {
        grid-template-columns: 1fr;
    }
    
    [data-testid="stChatMessageContent"] {
        font-size: 15px;
        padding: 0 16px;
    }
    
    .stChatInput {
        padding: 16px !important;
    }
}

/* Loading spinner */
.stSpinner > div {
    border-color: #10a37f transparent transparent transparent !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #202123;
}

::-webkit-scrollbar-thumb {
    background: #565869;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #6e6f7f;
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

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="padding: 16px 0;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <div style="width: 32px; height: 32px; border-radius: 10px; background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 18px;">AI</div>
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
    
    st.markdown('<div class="sidebar-section">Recent Chats</div>', unsafe_allow_html=True)
    
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
        <p style="margin: 0 0 4px 0;">Made with ❤️ by</p>
        <p style="margin: 0;"><strong>Kavishka Dileepa</strong></p>
        <p style="margin: 8px 0 0 0; font-size: 11px;">© 2026 All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)

# Main chat area
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-icon">🤖</div>
        <div class="welcome-title">How can I help you today?</div>
        <div class="welcome-subtitle">
            I'm here to answer questions, provide information, and have conversations. 
            Just type your message below or try one of these examples:
        </div>
        <div class="example-prompts">
            <div class="example-prompt" onclick="document.querySelector('[data-testid=stChatInput] textarea').value='Can you explain quantum physics in simple terms?'; document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles: true}));">
                <div class="example-prompt-title">💡 Explain concepts</div>
                <div class="example-prompt-desc">Break down complex topics into easy-to-understand explanations</div>
            </div>
            <div class="example-prompt" onclick="document.querySelector('[data-testid=stChatInput] textarea').value='What can you help me with?'; document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles: true}));">
                <div class="example-prompt-title">⚡ Quick answers</div>
                <div class="example-prompt-desc">Get fast and accurate responses to your questions</div>
            </div>
            <div class="example-prompt" onclick="document.querySelector('[data-testid=stChatInput] textarea').value='Teach me something interesting about space'; document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles: true}));">
                <div class="example-prompt-title">📚 Learn something new</div>
                <div class="example-prompt-desc">Explore any subject with detailed information</div>
            </div>
            <div class="example-prompt" onclick="document.querySelector('[data-testid=stChatInput] textarea').value='Let\\'s chat about technology trends'; document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles: true}));">
                <div class="example-prompt-title">💬 Have a conversation</div>
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
