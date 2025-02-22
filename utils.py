import requests
import json
import os
from config import BASE_URL, HEADERS, API_KEY

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
        "max_tokens": 120
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx, 5xx)

        # Debug: Print raw response
        print("Raw API Response:", response.text)

        data = response.json()  # Convert response to JSON
        print("Formatted API Response:", json.dumps(data, indent=2))  # Pretty-print response

        # ✅ Handle different response formats
        if "choices" in data and isinstance(data["choices"], list) and len(data["choices"]) > 0:
            ai_response = data["choices"][0].get("message", {}).get("content", "No content available")
        elif "message" in data and "content" in data["message"]:
            ai_response = data["message"]["content"]
        elif "error" in data:
            ai_response = f"Error from API: {data['error']}"
        else:
            ai_response = "Error: Unexpected API response format."

        log_conversation(prompt, ai_response)
        return ai_response

    except requests.exceptions.RequestException as e:
        return f"Error: Request failed. {e}"

    except json.JSONDecodeError:
        return f"Error: Unable to parse JSON. Response: {response.text}"

        log_conversation(prompt, ai_response)  # ✅ This will now work
        return ai_response
    else:
        return f"Error: {response.status_code} - {response.text}"
