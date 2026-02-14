import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integrations.local_llm import LocalLLMService
from integrations.standard_email import StandardEmailService, config
import imaplib

def setup_model():
    print("Initializing Local LLM Service (this will download the model if missing)...")
    try:
        llm = LocalLLMService()
        print("Model loaded successfully!")
        return True
    except Exception as e:
        print(f"Failed to load model: {e}")
        return False

def check_email_auth():
    print(f"Checking Email Connection for {config.EMAIL_USER}...")
    if "your_email" in config.EMAIL_USER or "your_app_password" in config.EMAIL_PASSWORD:
        print("SKIPPING: Please update .env with real EMAIL_USER and EMAIL_PASSWORD")
        return False
        
    try:
        mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
        mail.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
        mail.logout()
        print("Email connection SUCCESSFUL!")
        return True
    except Exception as e:
        print(f"Email connection FAILED: {e}")
        return False

if __name__ == "__main__":
    print("--- Setting up Local Components ---")
    model_ok = setup_model()
    email_ok = check_email_auth()
    
    if model_ok and email_ok:
        print("\nAll systems GO! You can run 'python main.py' now.")
    else:
        print("\nPlease fix the issues above before running the app.")
