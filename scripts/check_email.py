from integrations.standard_email import config
import imaplib

print(f"Checking Email Connection for {config.EMAIL_USER}...")
if "your_email" in config.EMAIL_USER:
    print("SKIPPING: Please update .env with real EMAIL_USER and EMAIL_PASSWORD")
else:
    try:
        mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
        mail.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
        mail.logout()
        print("Email connection SUCCESSFUL!")
    except Exception as e:
        print(f"Email connection FAILED: {e}")
