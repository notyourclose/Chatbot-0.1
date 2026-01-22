import time
import requests
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot - Kavishka Dileepa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Full React-style landing page CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.stApp { background: #0b0f19; }
.main .block-container { padding-top: 0; max-width: 100%; }
[data-testid="stSidebar"] { display: none; }

/* Background glows */
.bg-glow { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
.glow1 { position: absolute; top: -200px; left: 50%; transform: translateX(-50%); width: 520px; height: 520px; border-radius: 999px; background: rgba(16,185,129,0.20); filter: blur(120px); }
.glow2 { position: absolute; top: 100px; right: -140px; width: 420px; height: 420px; border-radius: 999px; background: rgba(99,102,241,0.20); filter: blur(110px); }

/* Navbar */
.navbar { position: sticky; top: 0; z-index: 100; background: rgba(11,15,25,0.70); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.10); padding: 0.75rem 0; }
.nav-inner { max-width: 1200px; margin: 0 auto; padding: 0 1rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.brand { display: flex; align-items: center; gap: 0.75rem; }
.logo { width: 36px; height: 36px; border-radius: 12px; background: linear-gradient(135deg, #34d399 0%, #059669 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(16,185,129,0.25); color: white; font-weight: 900; font-size: 18px; }
.brand-title { color: white; font-size: 14px; font-weight: 700; margin: 0; }
.brand-sub { color: rgba(255,255,255,0.60); font-size: 12px; margin: 0; }
.nav-links { display: flex; align-items: center; gap: 1.5rem; }
.nav-link { color: rgba(255,255,255,0.70); text-decoration: none; font-size: 14px; transition: color 0.2s; }
.nav-link:hover { color: white; }
.nav-right { display: flex; align-items: center; gap: 0.75rem; }
.pill { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0.7rem; border-radius: 999px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.10); color: rgba(255,255,255,0.75); font-size: 12px; font-weight: 700; }
.pill-green { background: rgba(16,185,129,0.12); border-color: rgba(16,185,129,0.30); color: rgba(167,243,208,0.95); }
.dot { width: 8px; height: 8px; border-radius: 999px; background: #34d399; box-shadow: 0 0 0 6px rgba(16,185,129,0.15); animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.6} }
.btn { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; border-radius: 8px; font-size: 14px; font-weight: 600; text-decoration: none; transition: all 0.2s; }
.btn-white { background: white; color: #0b0f19; }
.btn-white:hover { background: rgba(255,255,255,0.90); }
.btn-green { background: #10b981; color: white; box-shadow: 0 12px 30px rgba(16,185,129,0.25); }
.btn-green:hover { background: #34d399; }

/* Hero */
.hero-section { max-width: 1200px; margin: 0 auto; padding: 3rem 1rem 2rem; position: relative; z-index: 1; }
.hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: center; }
.hero-badge { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0.75rem; border-radius: 999px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); color: rgba(255,255,255,0.70); font-size: 12px; font-weight: 600; margin-bottom: 1.25rem; }
.hero-badge svg { width: 14px; height: 14px; color: #34d399; }
.hero h1 { color: white; font-size: 48px; font-weight: 800; line-height: 1.05; margin: 0; letter-spacing: -0.03em; }
.hero h1 span { color: #34d399; }
.hero p { color: rgba(255,255,255,0.70); font-size: 16px; line-height: 1.7; margin: 1rem 0 0; max-width: 60ch; }
.hero-btns { display: flex; gap: 0.75rem; margin-top: 1.75rem; }
.hero-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.75rem; margin-top: 2rem; }
.stat-card { border-radius: 12px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); padding: 1rem; }
.stat-value { color: white; font-size: 18px; font-weight: 800; }
.stat-label { color: rgba(255,255,255,0.60); font-size: 12px; margin-top: 0.25rem; }

/* Chat demo widget */
.chat-demo { border-radius: 20px; border: 1px solid rgba(255,255,255,0.10); background: linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05)); padding: 1.25rem; box-shadow: 0 25px 60px rgba(0,0,0,0.45); }
.chat-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; }
.chat-header-left { display: flex; align-items: center; gap: 0.75rem; }
.chat-logo { width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, #34d399 0%, #059669 100%); display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; }
.chat-title { color: white; font-size: 14px; font-weight: 700; }
.chat-subtitle { color: rgba(255,255,255,0.60); font-size: 12px; }
.chat-badge-demo { padding: 0.25rem 0.6rem; border-radius: 999px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); color: rgba(255,255,255,0.70); font-size: 11px; }
.chat-messages { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 1rem; }
.msg { max-width: 85%; padding: 0.75rem 1rem; border-radius: 16px; font-size: 13px; }
.msg-assistant { background: rgba(11,15,25,0.60); color: rgba(255,255,255,0.80); border: 1px solid rgba(255,255,255,0.10); }
.msg-user { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; margin-left: auto; }
.chat-input-box { display: flex; align-items: center; gap: 0.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); padding: 0.75rem; }
.chat-input-placeholder { color: rgba(255,255,255,0.50); font-size: 13px; flex: 1; }
.chat-send { width: 36px; height: 36px; border-radius: 8px; background: white; color: #0b0f19; display: flex; align-items: center; justify-content: center; cursor: pointer; }

/* Sections */
.section { max-width: 1200px; margin: 0 auto; padding: 3.5rem 1rem; position: relative; z-index: 1; }
.section-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #34d399; margin-bottom: 0.5rem; }
.section h2 { color: white; font-size: 36px; font-weight: 800; margin: 0.5rem 0 0.75rem; }
.section p { color: rgba(255,255,255,0.70); font-size: 16px; line-height: 1.7; margin-top: 0.75rem; }

/* Integrations */
.integrations-box { border-radius: 20px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); padding: 1.5rem; }
.integrations-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; }
.integrations-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 0.75rem; }
.integration-item { display: flex; align-items: center; justify-content: center; gap: 0.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.10); background: rgba(11,15,25,0.40); padding: 0.75rem; color: rgba(255,255,255,0.70); font-size: 13px; font-weight: 600; }

/* Features */
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 2rem; }
.feature-card { border-radius: 20px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); padding: 1.5rem; }
.feature-icon { width: 40px; height: 40px; border-radius: 12px; background: rgba(16,185,129,0.15); display: flex; align-items: center; justify-content: center; color: #34d399; margin-bottom: 0.75rem; }
.feature-title { color: white; font-size: 16px; font-weight: 700; margin-bottom: 0.5rem; }
.feature-desc { color: rgba(255,255,255,0.70); font-size: 14px; line-height: 1.65; }

/* Testimonials */
.testimonials-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 2rem; }
.testimonial-card { border-radius: 20px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); padding: 1.5rem; }
.testimonial-quote { color: rgba(255,255,255,0.80); font-size: 14px; line-height: 1.7; margin-bottom: 1rem; }
.testimonial-author { display: flex; justify-content: space-between; align-items: center; }
.testimonial-name { color: white; font-size: 14px; font-weight: 700; }
.testimonial-role { color: rgba(255,255,255,0.60); font-size: 12px; }

/* FAQ */
.faq-list { margin-top: 1.5rem; }
.faq-item { border-radius: 20px; border: 1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.05); padding: 1.25rem; margin-bottom: 0.75rem; cursor: pointer; transition: background 0.2s; }
.faq-item:hover { background: rgba(255,255,255,0.08); }
.faq-question { display: flex; justify-content: space-between; align-items: center; color: white; font-size: 14px; font-weight: 700; }
.faq-answer { color: rgba(255,255,255,0.70); font-size: 14px; line-height: 1.7; margin-top: 0.75rem; }

/* CTA */
.cta-box { border-radius: 28px; border: 1px solid rgba(255,255,255,0.10); background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(99,102,241,0.15)); padding: 2.5rem; text-align: center; }
.cta-buttons { display: flex; gap: 0.75rem; justify-content: center; margin-top: 1.5rem; }

/* Footer */
.footer { border-top: 1px solid rgba(255,255,255,0.10); padding: 2rem 1rem; text-align: center; color: rgba(255,255,255,0.50); font-size: 12px; }

@media (max-width: 1000px) {
  .hero-grid { grid-template-columns: 1fr; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
  .features-grid, .testimonials-grid { grid-template-columns: 1fr; }
  .integrations-grid { grid-template-columns: repeat(3, 1fr); }
  .nav-links { display: none; }
}
</style>
""", unsafe_allow_html=True)

def generate_response(prompt: str) -> str:
    try:
        if "HF_TOKEN" in st.secrets:
            api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
            headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
            payload = {"inputs": prompt, "parameters": {"max_length": 120, "temperature": 0.7}}
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
    p = prompt.lower()
    if any(w in p for w in ["hello", "hi", "hey"]):
        return "Hello! 👋 It's great to meet you. I'm here to help with any questions or tasks you have."
    if "how are you" in p:
        return "I'm doing wonderfully! As an AI, I'm always ready to assist. How can I help you today?"
    if any(w in p for w in ["your name", "who are you"]):
        return "I'm an AI assistant created by Kavishka Dileepa. I'm designed to help answer questions and have conversations!"
    if "thank" in p:
        return "You're very welcome! 😊 Happy to help!"
    if any(w in p for w in ["bye", "goodbye"]):
        return "Goodbye! 👋 It was great chatting. Come back anytime!"
    if "?" in prompt:
        return "That's interesting! Could you provide more context so I can give you a better answer?"
    return "I'm here to help! What would you like to explore?"

if "messages" not in st.session_state:
    st.session_state.messages = []
if "show_demo_chat" not in st.session_state:
    st.session_state.show_demo_chat = False

# Background glows
st.markdown('<div class="bg-glow"><div class="glow1"></div><div class="glow2"></div></div>', unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="navbar">
  <div class="nav-inner">
    <div class="brand">
      <div class="logo">AI</div>
      <div>
        <div class="brand-title">AI Chatbot</div>
        <div class="brand-sub">Kavishka Dileepa</div>
      </div>
    </div>
    <div class="nav-links">
      <a href="#features" class="nav-link">Features</a>
      <a href="#integrations" class="nav-link">Integrations</a>
      <a href="#testimonials" class="nav-link">Reviews</a>
      <a href="#demo" class="nav-link">Demo</a>
      <a href="#faq" class="nav-link">FAQ</a>
    </div>
    <div class="nav-right">
      <div class="pill pill-green">
        <span class="dot"></span>
        Online
      </div>
      <a href="#get-started" class="btn btn-white">Get started →</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
  <div class="hero-grid">
    <div>
      <div class="hero-badge">
        <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
        Modern, conversion-focused frontend
      </div>
      <h1 class="hero">Help, convert, and support with a <span>clean AI chatbot</span> experience</h1>
      <p class="hero">A premium landing page UI inspired by modern SaaS design (like <a href="https://www.chatbot.com/" style="color:#34d399;text-decoration:underline;">chatbot.com</a>) — built for your project, without the "cartoon" feel.</p>
      <div class="hero-btns">
        <a href="#get-started" class="btn btn-green">Start free →</a>
        <a href="#features" class="btn" style="border:1px solid rgba(255,255,255,0.10);background:rgba(255,255,255,0.05);color:rgba(255,255,255,0.80);">See features ↓</a>
      </div>
      <div class="hero-stats">
        <div class="stat-card"><div class="stat-value">&lt;1s</div><div class="stat-label">Avg. reply time</div></div>
        <div class="stat-card"><div class="stat-value">Website + more</div><div class="stat-label">Channels</div></div>
        <div class="stat-card"><div class="stat-value">Minutes</div><div class="stat-label">Setup time</div></div>
        <div class="stat-card"><div class="stat-value">24/7</div><div class="stat-label">Support</div></div>
      </div>
    </div>
    <div>
      <div class="chat-demo">
        <div class="chat-header">
          <div class="chat-header-left">
            <div class="chat-logo">✨</div>
            <div>
              <div class="chat-title">AI Chatbot</div>
              <div class="chat-subtitle">Online • replies instantly</div>
            </div>
          </div>
          <div class="chat-badge-demo">Demo UI</div>
        </div>
        <div class="chat-messages">
          <div class="msg msg-assistant">Hi! How can I help you today?</div>
          <div class="msg msg-user">I need a professional chatbot landing page.</div>
          <div class="msg msg-assistant">Done. Clean layout, social proof, strong CTA, and sections you can customize.</div>
        </div>
        <div class="chat-input-box">
          <div class="chat-input-placeholder">Message…</div>
          <div class="chat-send">→</div>
        </div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Integrations Section
st.markdown("""
<div class="section" id="integrations">
  <div class="integrations-box">
    <div class="integrations-header">
      <div>
        <div style="color:white;font-weight:700;font-size:14px;">Support customers on multiple channels</div>
        <div style="color:rgba(255,255,255,0.60);font-size:13px;margin-top:0.25rem;">Add the chatbot UI to your website or connect integrations later.</div>
      </div>
      <div style="color:rgba(255,255,255,0.50);font-size:11px;">Frontend-only demo • Replace with real logos anytime</div>
    </div>
    <div class="integrations-grid">
      <div class="integration-item">🌐 Website</div>
      <div class="integration-item">💬 Slack</div>
      <div class="integration-item">📱 Messenger</div>
      <div class="integration-item">🛒 Shop</div>
      <div class="integration-item">🎧 Helpdesk</div>
      <div class="integration-item">📊 CRM</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="section" id="features">
  <div class="section-title">Features</div>
  <h2 class="section">Everything you need for a modern chatbot frontend</h2>
  <p class="section">This is a clean, scalable UI foundation. You can plug in your actual chat backend later.</p>
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-icon">✨</div>
      <div class="feature-title">AI-generated replies</div>
      <div class="feature-desc">Deliver helpful answers instantly with a modern conversational UX.</div>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🔄</div>
      <div class="feature-title">Flexible flows</div>
      <div class="feature-desc">Handle FAQs, lead capture, and handoff paths without complexity.</div>
    </div>
    <div class="feature-card">
      <div class="feature-icon">📊</div>
      <div class="feature-title">Analytics built-in</div>
      <div class="feature-desc">Track engagement, top questions, and conversion-friendly actions.</div>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🛡️</div>
      <div class="feature-title">Reliable & secure</div>
      <div class="feature-desc">Designed for stability with a clean, production-ready layout.</div>
    </div>
    <div class="feature-card">
      <div class="feature-icon">💬</div>
      <div class="feature-title">Great chat UI</div>
      <div class="feature-desc">A premium chat experience your users will actually enjoy using.</div>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🌍</div>
      <div class="feature-title">Multi-language ready</div>
      <div class="feature-desc">A layout that scales globally with consistent spacing and type.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
<div class="section" id="testimonials">
  <div class="section-title">Reviews</div>
  <h2 class="section">A UI your users will trust</h2>
  <p class="section">Professional spacing, typography, and layout patterns.</p>
  <div class="testimonials-grid">
    <div class="testimonial-card">
      <div class="testimonial-quote">"Clean design, fast setup, and the UI feels premium. Exactly what we needed for a modern support experience."</div>
      <div class="testimonial-author">
        <div>
          <div class="testimonial-name">Product Lead</div>
          <div class="testimonial-role">Customer Support</div>
        </div>
        <div style="width:40px;height:40px;border-radius:12px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,0.70);">✓</div>
      </div>
    </div>
    <div class="testimonial-card">
      <div class="testimonial-quote">"The landing page looks professional and converts better than our old 'cartoon' layout. Big upgrade."</div>
      <div class="testimonial-author">
        <div>
          <div class="testimonial-name">Founder</div>
          <div class="testimonial-role">SaaS</div>
        </div>
        <div style="width:40px;height:40px;border-radius:12px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,0.70);">✓</div>
      </div>
    </div>
    <div class="testimonial-card">
      <div class="testimonial-quote">"Great structure: hero, social proof, and clear CTAs. It's easy to extend with real content later."</div>
      <div class="testimonial-author">
        <div>
          <div class="testimonial-name">Marketing Manager</div>
          <div class="testimonial-role">Growth</div>
        </div>
        <div style="width:40px;height:40px;border-radius:12px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,0.70);">✓</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Demo Chat Section
st.markdown("""
<div class="section" id="demo">
  <div class="section-title">Demo</div>
  <h2 class="section">Try chatting right here</h2>
  <p class="section">This uses your Streamlit app. Your Hugging Face token must be set in Streamlit Cloud <strong>Secrets</strong>.</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style="border-radius:20px;border:1px solid rgba(255,255,255,0.10);background:rgba(255,255,255,0.04);padding:1rem;margin-top:1.5rem;">
  <div style="display:flex;align-items:center;gap:0.75rem;padding-bottom:1rem;border-bottom:1px solid rgba(255,255,255,0.10);margin-bottom:0.75rem;">
    <div style="width:34px;height:34px;border-radius:14px;background:linear-gradient(135deg,#34d399 0%,#059669 100%);display:flex;align-items:center;justify-content:center;color:white;font-size:18px;">🤖</div>
    <div>
      <div style="color:white;font-weight:800;">Chat</div>
      <div style="color:rgba(255,255,255,0.60);font-size:12px;">Status: Ready</div>
    </div>
  </div>
""", unsafe_allow_html=True)

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.markdown("Hi! Ask me anything — I'm ready.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message AI Chatbot..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(0.6)
            response = generate_response(prompt)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# FAQ Section
st.markdown("""
<div class="section" id="faq">
  <div class="section-title">FAQ</div>
  <h2 class="section">Common questions</h2>
  <p class="section">Want it even closer to the style on <a href="https://www.chatbot.com/" style="color:#34d399;text-decoration:underline;">chatbot.com</a>? Send me a screenshot of the exact sections you like.</p>
  <div class="faq-list">
    <div class="faq-item">
      <div class="faq-question">Can I use this as just a frontend landing page? <span>▼</span></div>
      <div class="faq-answer">Yes. This is a frontend-only landing page UI. You can connect it to any backend later.</div>
    </div>
    <div class="faq-item">
      <div class="faq-question">Can we add a "Try demo chat" section? <span>▼</span></div>
      <div class="faq-answer">Yes. We can add a real chat widget or route to your existing chat screen when you're ready.</div>
    </div>
    <div class="faq-item">
      <div class="faq-question">Can you match my brand colors? <span>▼</span></div>
      <div class="faq-answer">Yes. Tell me your brand primary color + logo, and I'll update the palette and typography.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="section" id="get-started">
  <div class="cta-box">
    <div class="hero-badge" style="margin-bottom:1rem;">
      <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
      Frontend ready
    </div>
    <h2 style="color:white;font-size:32px;font-weight:800;margin:0;">Want this landing page to match your brand perfectly?</h2>
    <p style="color:rgba(255,255,255,0.70);margin-top:0.75rem;">Tell me your primary color, logo text, and the sections you want to keep/remove — I'll tailor it.</p>
    <div class="cta-buttons">
      <a href="#features" class="btn" style="border:1px solid rgba(255,255,255,0.10);background:rgba(255,255,255,0.05);color:rgba(255,255,255,0.80);">View sections ↓</a>
      <a href="#demo" class="btn btn-white">Try chat →</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
  <div style="display:flex;align-items:center;justify-content:center;gap:0.75rem;margin-bottom:0.5rem;">
    <div style="width:36px;height:36px;border-radius:12px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,0.80);">🤖</div>
    <div>
      <div style="color:white;font-weight:700;font-size:14px;">AI Chatbot</div>
      <div style="color:rgba(255,255,255,0.60);font-size:12px;">Made by Kavishka Dileepa</div>
    </div>
  </div>
  <div>© 2026 All rights reserved</div>
</div>
""", unsafe_allow_html=True)
