from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import requests
import os

app = FastAPI()

# CORS middleware to allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def generate_response(prompt: str) -> str:
    """Generate response using HuggingFace API or fallback to rule-based responses"""
    try:
        # Try with HuggingFace token if available
        hf_token = os.getenv("HF_TOKEN")
        if hf_token:
            API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
            headers = {"Authorization": f"Bearer {hf_token}"}
            payload = {"inputs": prompt, "parameters": {"max_length": 100, "temperature": 0.7}}
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', '').strip()
    except:
        pass

    try:
        # Try without token
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers={}, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', '').strip()
    except:
        pass

    # Fallback to rule-based responses
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

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Chat endpoint"""
    response_text = generate_response(request.message)
    return {
        "response": response_text,
        "timestamp": datetime.now().strftime("%H:%M")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
