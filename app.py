import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Page config with custom theme
st.set_page_config(
    page_title="AI Chatbot | Knavish Dileepa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, responsive design
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main container */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }

    /* Chat container */
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Custom header */
    .custom-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        text-align: center;
        animation: slideDown 0.5s ease-out;
    }

    .custom-header h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }

    .custom-header p {
        color: #6b7280;
        font-size: 1rem;
        margin-top: 0.5rem;
        font-weight: 500;
    }

    /* Chat messages container */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.3s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* User message */
    [data-testid="stChatMessageContent"]:has(div[data-testid="stMarkdownContainer"]) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 16px;
        padding: 1rem;
    }

    /* Chat input */
    .stChatInput {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 0.5rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }

    .stChatInput > div {
        background: transparent;
    }

    .stChatInput input {
        background: transparent;
        border: none;
        color: #1f2937;
        font-size: 1rem;
    }

    .stChatInput input::placeholder {
        color: #9ca3af;
    }

    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea;
    }

    /* Feature cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    }

    .feature-card h3 {
        color: #667eea;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .feature-card p {
        color: #6b7280;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* Animations */
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .custom-header h1 {
            font-size: 1.8rem;
        }

        .custom-header {
            padding: 1.5rem;
        }

        .stChatMessage {
            padding: 1rem;
        }

        .main .block-container {
            padding: 1rem 0.5rem;
        }
    }

    @media (max-width: 480px) {
        .custom-header h1 {
            font-size: 1.5rem;
        }

        .custom-header p {
            font-size: 0.9rem;
        }

        .feature-card {
            padding: 1rem;
        }
    }

    /* Loading animation */
    .loading-dots {
        display: inline-flex;
        gap: 4px;
    }

    .loading-dots span {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #667eea;
        animation: bounce 1.4s infinite ease-in-out both;
    }

    .loading-dots span:nth-child(1) {
        animation-delay: -0.32s;
    }

    .loading-dots span:nth-child(2) {
        animation-delay: -0.16s;
    }

    @keyframes bounce {
        0%, 80%, 100% {
            transform: scale(0);
        }
        40% {
            transform: scale(1);
        }
    }

    /* Scroll animations */
    .stChatMessage {
        animation: slideUp 0.4s ease-out;
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

# Custom header
st.markdown("""
<div class="custom-header">
    <h1>🤖 AI Chatbot</h1>
    <p>Powered by Kavishka Dileepa | Your intelligent conversation partner</p>
</div>
""", unsafe_allow_html=True)


@st.cache_resource
def load_chatbot():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return tokenizer, model


# Show welcome message or load model
if "model_loaded" not in st.session_state:
    with st.spinner("🚀 Loading AI model... This may take a moment"):
        tokenizer, model = load_chatbot()
        st.session_state.tokenizer = tokenizer
        st.session_state.model = model
        st.session_state.model_loaded = True
else:
    tokenizer = st.session_state.tokenizer
    model = st.session_state.model

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Welcome message
    welcome_msg = """👋 Hello! I'm your AI chatbot assistant. I'm here to help you with:

✨ Answering your questions
💡 Having meaningful conversations
🎯 Providing information and insights
🤝 Being your friendly chat companion

Feel free to ask me anything! Let's start chatting."""

    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("💬 Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Generate bot response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            # Encode the new user input
            new_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

            # Append to chat history
            bot_input_ids = torch.cat([st.session_state.chat_history_ids, new_input_ids],
                                      dim=-1) if st.session_state.chat_history_ids is not None else new_input_ids

            # Generate response
            st.session_state.chat_history_ids = model.generate(
                bot_input_ids,
                max_length=1000,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                do_sample=True,
                top_k=100,
                top_p=0.7,
                temperature=0.8
            )

            # Decode response
            response = tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0],
                                        skip_special_tokens=True)

            if not response.strip():
                response = "I'm here to help! Could you please rephrase your question?"

            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with features
with st.sidebar:
    st.markdown("""
    <div class="feature-card">
        <h3>✨ Features</h3>
        <p>• Natural conversations<br>
        • Context-aware responses<br>
        • Fast and intelligent<br>
        • Available 24/7</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>💡 Tips</h3>
        <p>• Ask clear questions<br>
        • Be specific<br>
        • Use natural language<br>
        • Have fun chatting!</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_history_ids = None
        st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>
        <p>Made with ❤️ by<br><strong>Kavishka Dileepa</strong></p>
    </div>
    """, unsafe_allow_html=True)