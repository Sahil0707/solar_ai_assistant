import requests
import json
import os
from config import BASE_URL, HEADERS, API_KEY


# ✅ Define log_conversation function before calling it
def log_conversation(user_input, ai_response, log_file="conversation_logs.txt"):
    """Logs the conversation to a text file."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"AI: {ai_response}\n")
        file.write("-" * 50 + "\n")  # Separator for readability


def get_ai_response(prompt):
    if not API_KEY:
        return "Error: API key is missing. Check .env file."

    print(f"Using API Key: {API_KEY}")  # Debugging: Check if API key is loaded

    payload = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        ai_response = data["choices"][0]["message"]["content"]
        log_conversation(prompt, ai_response)  # ✅ This will now work
        return ai_response
    else:
        return f"Error: {response.status_code} - {response.text}"
