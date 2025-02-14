import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Debug: Print API key to check if it's loaded
print(f"DEBUG: API Key Loaded - {os.getenv('OPENROUTER_API_KEY')}")

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Make sure it is set in the .env file.")

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
