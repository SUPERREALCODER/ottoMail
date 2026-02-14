# 📧 OttoMail - AI Email Copilot

A private, local-first AI agent that helps you manage emails. It runs completely offline using **Llama 3** on your GPU, or optionally connects to **Gemini API** for speed.

## 🌟 Features

*   **Dual Engine Intelligence**:
    *   **Local Mode**: Runs `Meta-Llama-3-8B` locally (Private, Free, GPU-accelerated).
    *   **Gemini Mode**: Connects to Google's Gemini Flash/Pro (Faster, requires key).
*   **Privacy First**: Emails are processed securely. Real emails are only sent when *you* click "Approve".
*   **Modern Dashboard**: View pending proposals, edit drafts, and send with one click.
*   **Smart Parsing**: Filters out spam and identifies genuine business inquiries.

## 🏗️ Architecture

The system is built on a modular "Agentic" architecture:

1.  **Frontend**:
    *   **Dashboard**: `dashboard.html` (Vanilla JS + TailwindCSS).
    *   Connects to Backend via REST API.

2.  **Backend (FastAPI)**:
    *   **API Layer**: Handles requests for emails, proposals, and approvals.
    *   **Service Layer**:
        *   `StandardEmailService`: Fetches emails via IMAP, sends via SMTP.
        *   `UnifiedLLM`: INTELLIGENCE HUB. Switches between Local (GPT4All) and Cloud (Gemini).
        *   `StorageService`: Manages SQLite database for email/proposal persistence.

3.  **AI Agent (LangGraph)**:
    *   A directed graph that processes each email:
    *   `Classify` -> `Extract Requirements` -> `Generate Plan` -> `Calculate Cost` -> `Draft Reply`.

## 🔮 Things in Making (Roadmap)

*   [ ] **RAG Integration**: Allow the AI to search past projects to give better estimates.
*   [ ] **Calendar Integration**: Auto-schedule meetings if the client asks.
*   [ ] **Docker Support**: Containerize the entire app for easy deployment.
*   [ ] **Multi-User**: Support multiple email accounts.
*   [ ] **Voice Mode**: Listen to email summaries (TTS).

## 🚀 Installation

### 1. Prerequisites
*   Python 3.10+
*   (Optional) NVIDIA GPU for Local Mode (Verified on RTX 3060).

### 2. Setup
```bash
# Clone the repository (if you haven't)
# cd ottoMail

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration (.env)
Create a `.env` file in the root directory:

```ini
# --- Email Config (Required) ---
EMAIL_USER=your-email@gmail.com
# Use an "App Password" from Google Account > Security, NOT your main password!
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx

# --- AI Provider Config ---
# Options: "local" (Private), "gemini" (Fast), "mock" (Test)
LLM_PROVIDER=local

# --- Gemini (Only if using LLM_PROVIDER=gemini) ---
GOOGLE_API_KEY=your_gemini_api_key

# --- Local LLM Config ---
LLM_MODEL_PATH=Meta-Llama-3-8B-Instruct.Q4_0.gguf
LLM_DEVICE=gpu
```

## 🏃‍♂️ How to Run

1.  **Start the Server**:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

2.  **Access Dashboard**:
    Open **[http://localhost:8000](http://localhost:8000)** in your browser.

3.  **Stop the Server**:
    *   Press `Ctrl + C` in the terminal where it's running.
    *   If it gets stuck: `fuser -k 8000/tcp` (Linux) or `taskkill /IM python.exe /F` (Windows).

## 🧠 Switching AI Modes

*   **To use Local AI (Llama 3)**:
    1.  Ensure `LLM_PROVIDER=local` in `.env`.
    2.  The model (~4.6GB) will download automatically on first run (check terminal).
    3.  Once loaded, you'll see `✅ Local LLM loaded successfully on GPU`.

*   **To use Cloud AI (Gemini)**:
    1.  Get a free key from [Google AI Studio](https://aistudio.google.com/).
    2.  Set `LLM_PROVIDER=gemini` and `GOOGLE_API_KEY` in `.env`.
    3.  Restart the server.

## 🛠️ Troubleshooting

*   **"Internal Server Error"**: Usually means an email has weird encoding. Check the terminal logs.
*   **"Model Download Failed"**: Run `python scripts/force_download.py` to manually download the model.
*   **GPU not working?**: The app automatically falls back to CPU or Mock mode if GPU fails.
