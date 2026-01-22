import streamlit as st
import requests
import time

# Page config
st.set_page_config(
    page_title="AI Chatbot | Kavishka Dileepa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Modern Professional Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Main App Background */
    .stApp {
        background: #0a0e27;
        background-image: 
            radial-gradient(at 20% 30%, rgba(88, 86, 214, 0.15) 0px, transparent 50%),
            radial-gradient(at 80% 70%, rgba(74, 144, 226, 0.15) 0px, transparent 50%);
    }

    /* Main Container */
    .main .block-container {
        padding: 0;
        max-width: 100%;
    }

    /* Header Section */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 3rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        position: sticky;
        top: 0;
        z-index: 1000;
    }

    .header-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .logo-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .logo-icon {
        width: 50px;
        height: 50px;
        background: white;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .logo-text h1 {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
    }

    .logo-text p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 0.9rem;
        margin: 0;
        font-weight: 400;
    }

    .header-stats {
        display: flex;
        gap: 2rem;
        color: white;
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
    }

    .stat-label {
        font-size: 0.8rem;
        opacity: 0.9;
    }

    /* Chat Container */
    .chat-container {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 2rem;
        min-height: 60vh;
    }

    /* Welcome Banner */
    .welcome-banner {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }

    .welcome-banner h2 {
        color: #667eea;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .welcome-banner p {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
        line-height: 1.8;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .feature-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }

    .feature-box:hover {
        background: rgba(102, 126, 234, 0.1);
        border-color: rgba(102, 126, 234, 0.3);
        transform: translateY(-5px);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .feature-box h3 {
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .feature-box p {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
    }

    /* Chat Messages */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* User Message Styling */
    [data-testid="stChatMessageContent"] {
        color: white;
    }

    .stChatMessage[data-testid*="user"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
    }

    /* Assistant Message Styling */
    .stChatMessage[data-testid*="assistant"] {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(102, 126, 234, 0.2);
    }

    /* Chat Input */
    .stChatInput {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #0a0e27;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        z-index: 999;
    }

    .stChatInput > div {
        max-width: 1200px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        backdrop-filter: blur(10px);
    }

    .stChatInput input {
        background: transparent;
        border: none;
        color: white;
        font-size: 1rem;
    }

    .stChatInput input::placeholder {
        color: rgba(255, 255, 255, 0.5);
    }

    /* Avatar Styling */
    [data-testid="stChatMessageAvatarUser"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    [data-testid="stChatMessageAvatarAssistant"] {
        background: linear-gradient(135deg, #4a90e2 0%, #5856d6 100%);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(10, 14, 39, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    .sidebar-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .sidebar-card h3 {
        color: #667eea;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .sidebar-card p {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* Button Styling */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }

    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .stChatMessage {
        animation: fadeIn 0.4s ease-out;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .header-container {
            padding: 1.5rem 1rem;
        }

        .header-content {
            flex-direction: column;
            gap: 1rem;
        }

        .header-stats {
            gap: 1rem;
        }

        .logo-text h1 {
            font-size: 1.4rem;
        }

        .welcome-banner {
            padding: 2rem 1rem;
        }

        .welcome-banner h2 {
            font-size: 1.8rem;
        }

        .chat-container {
            padding: 0 1rem;
            margin-bottom: 100px;
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }
    }

    /* Loading Spinner */
    .stSpinner > div {
        border-top-color: #667eea;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }

    ::-webkit-scrollbar-thumb {
        background: rgba(102, 126, 234, 0.5);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: rgba(102, 126, 234, 0.7);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <div class="header-content">
        <div class="logo-section">
            <div class="logo-icon">🤖</div>
            <div class="logo-text">
                <h1>AI Chatbot</h1>
                <p>Powered by Kavishka Dileepa</p>
            </div>
        </div>
        <div class="header-stats">
            <div class="stat-item">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Available</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">⚡</div>
                <div class="stat-label">Fast Response</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">🔒</div>
                <div class="stat-label">Secure</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Generate response function
def generate_response(prompt, conversation_history):
    try:
        if "HF_TOKEN" in st.secrets:
            API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
            headers = {"Authorization": f"Bearer {st.secrets['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']}"}
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
        elif response.status_code == 503:
            time.sleep(2)
            response = requests.post(API_URL, headers={}, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', '').strip()
    except:
        pass

    prompt_lower = prompt.lower()

    if any(word in prompt_lower for word in ['hello', 'hi', 'hey', 'greetings']):
        return "Hello! 👋 I'm your AI assistant. How can I help you today?"
    elif any(word in prompt_lower for word in ['how are you', 'how r u', 'whats up']):
        return "I'm doing great, thank you for asking! 😊 I'm here to help you with any questions you have."
    elif any(word in prompt_lower for word in ['your name', 'who are you', 'what are you']):
        return "I'm an AI chatbot created by Kavishka Dileepa. I'm designed to assist you with information, answer questions, and have meaningful conversations! 🤖"
    elif any(word in prompt_lower for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! 👋 It was nice chatting with you. Feel free to come back anytime you need help!"
    elif any(word in prompt_lower for word in ['thank', 'thanks']):
        return "You're very welcome! 😊 I'm always happy to help. Is there anything else you'd like to know?"
    elif any(word in prompt_lower for word in ['help', 'what can you do']):
        return "I can help you with many things! 🌟 I can answer questions, provide information, have conversations, and assist with various topics. Just ask me anything!"
    elif '?' in prompt:
        return f"That's an interesting question! While I'm currently in simplified mode, I can still try to help. Could you provide more details or rephrase your question? 🤔"
    else:
        return "I understand what you're saying! I'm here to help with questions and conversations. Feel free to ask me anything specific! 💬"


# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main content area
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Show welcome banner if no messages
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-banner">
        <h2>👋 Welcome to AI Chatbot</h2>
        <p>Your intelligent conversation partner, available 24/7 to answer questions, provide information, and engage in meaningful conversations.</p>

        <div class="feature-grid">
            <div class="feature-box">
                <div class="feature-icon">⚡</div>
                <h3>Lightning Fast</h3>
                <p>Get instant responses to your questions</p>
            </div>
            <div class="feature-box">
                <div class="feature-icon">🎯</div>
                <h3>Accurate Answers</h3>
                <p>Reliable and helpful information</p>
            </div>
            <div class="feature-box">
                <div class="feature-icon">💡</div>
                <h3>Smart AI</h3>
                <p>Powered by advanced AI technology</p>
            </div>
            <div class="feature-box">
                <div class="feature-icon">🔒</div>
                <h3>Secure & Private</h3>
                <p>Your conversations are safe</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("💬 Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🤔 Thinking..."):
            response = generate_response(prompt, st.session_state.messages)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-card">
        <h3>✨ Features</h3>
        <p>
        🎯 Natural conversations<br>
        🧠 Context-aware responses<br>
        ⚡ Lightning-fast replies<br>
        🌍 Available 24/7<br>
        🔒 Secure & private
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <h3>💡 Pro Tips</h3>
        <p>
        • Ask clear, specific questions<br>
        • Use natural language<br>
        • Be conversational<br>
        • Explore different topics
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div class="sidebar-card">
        <h3>🚀 Upgrade</h3>
        <p>Add your <strong>HF_TOKEN</strong> in Streamlit Secrets for advanced AI-powered responses!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; padding: 1rem;'>
        <p>Made with ❤️ by<br><strong style='color: #667eea;'>Kavishka Dileepa</strong></p>
        <p style='margin-top: 0.5rem;'>© 2026 All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)