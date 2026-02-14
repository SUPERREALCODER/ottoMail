from gpt4all import GPT4All
import time
import os

model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
model_path = os.path.expanduser(f"~/.cache/gpt4all/{model_name}")

print(f"--- Force Download: {model_name} ---")
print(f"Target Path: {model_path}")

try:
    # Check if partial download exists
    if os.path.exists(model_path):
        size = os.path.getsize(model_path)
        print(f"Existing file found: {size / 1024 / 1024:.2f} MB")
    
    print("Starting download (blocking mode)...")
    # Using CPU device just for download to avoid GPU init overhead/errors during download
    model = GPT4All(model_name, device='cpu', allow_download=True)
    print("\nDownload Complete!")
    print(f"Final Size: {os.path.getsize(model_path) / 1024 / 1024:.2f} MB")
    
except Exception as e:
    print(f"\nDownload ERROR: {e}")
    print("Retrying in 5 seconds...")
    time.sleep(5)
    # Simple retry logic could be added here loop
