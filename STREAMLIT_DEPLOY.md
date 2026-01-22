# Deploy to Streamlit Cloud

Your chatbot is now on GitHub: https://github.com/notyourclose/Chatbot-0.1.git

## Step-by-Step Deployment

### 1. Go to Streamlit Cloud
Visit: https://share.streamlit.io/

### 2. Sign in with GitHub
Click "Sign in" and authorize Streamlit Cloud to access your GitHub account.

### 3. Deploy Your App
1. Click **"New app"**
2. Select your repository: `notyourclose/Chatbot-0.1`
3. Select branch: `main`
4. Main file path: `app.py`
5. Click **"Deploy!"**

### 4. Add Your Hugging Face Token (IMPORTANT)
After deployment, go to your app settings:

1. Click the **"⋮"** menu (top right) → **"Settings"**
2. Scroll to **"Secrets"**
3. Add this:

```toml
HF_TOKEN = "your_huggingface_token_here"
```

**⚠️ IMPORTANT:** Replace `your_huggingface_token_here` with your actual Hugging Face token from https://huggingface.co/settings/tokens

### 5. Your App Will Be Live!
Your chatbot will be available at:
**https://chatbot-kavishka-dileepa-1.streamlit.app/**

## Troubleshooting

- **If the app doesn't load:** Check the logs in Streamlit Cloud dashboard
- **If chat doesn't work:** Make sure `HF_TOKEN` is set in Secrets
- **If you see errors:** Check that `requirements.txt` has all dependencies

## Files Included

- ✅ `app.py` - Your Streamlit chatbot
- ✅ `requirements.txt` - Python dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `.gitignore` - Excludes sensitive files

Your app is ready to deploy! 🚀
