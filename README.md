# Kavishka ChatBot 0.1

A beautiful AI chatbot application with two frontend options: Streamlit (Python) and React (JavaScript).

## Features

- 🤖 AI-powered conversations using HuggingFace BlenderBot model
- 💬 Beautiful ChatGPT-style UI
- 📱 Responsive design for mobile and desktop
- 🎨 Modern dark theme interface
- ⚡ Fast and responsive

## Project Structure

```
.
├── app.py                 # Streamlit application (standalone)
├── requirements.txt       # Python dependencies
├── backend/
│   └── main.py           # FastAPI backend server (for React app)
├── frontend/             # React frontend application
│   ├── src/
│   │   ├── App.js        # Main React component
│   │   ├── index.js      # React entry point
│   │   └── index.css     # Tailwind CSS styles
│   ├── public/
│   │   └── index.html    # HTML template
│   ├── package.json      # Node.js dependencies
│   └── tailwind.config.js
└── README.md
```

## Setup Instructions

### Option 1: Streamlit Application (Easiest)

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

### Option 2: React + FastAPI Application

#### Backend Setup:

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI backend:**
   ```bash
   cd backend
   python main.py
   ```
   Or using uvicorn directly:
   ```bash
   uvicorn backend.main:app --reload --port 8000
   ```

   The backend will run on `http://localhost:8000`

#### Frontend Setup:

1. **Install Node.js dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the React development server:**
   ```bash
   npm start
   ```

   The frontend will run on `http://localhost:3000`

## Optional: HuggingFace API Token

To use the HuggingFace BlenderBot model (instead of fallback responses):

1. Get a free token from [HuggingFace](https://huggingface.co/settings/tokens)
2. For Streamlit: Create a `.streamlit/secrets.toml` file:
   ```toml
   HF_TOKEN = "your_token_here"
   ```
3. For FastAPI: Set environment variable:
   ```bash
   # Windows PowerShell
   $env:HF_TOKEN="your_token_here"
   
   # Windows CMD
   set HF_TOKEN=your_token_here
   
   # Linux/Mac
   export HF_TOKEN=your_token_here
   ```

## Usage

- **Streamlit App**: Just run `streamlit run app.py` and start chatting!
- **React App**: Make sure both backend (port 8000) and frontend (port 3000) are running.

## Technologies Used

- **Streamlit**: Python web framework
- **React**: JavaScript UI library
- **FastAPI**: Python web framework for API
- **Tailwind CSS**: Utility-first CSS framework
- **HuggingFace API**: AI model inference
- **Axios**: HTTP client

## Author

Made with ❤️ by **Kavishka Dileepa**

© 2026 All rights reserved
