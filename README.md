# Solar AI Assistant

A chatbot assistant for the solar industry that uses OpenRouter AI API to generate responses.

## 📌 Features
- Uses OpenRouter AI API (`gpt-4`) for intelligent responses.
- Logs conversations in a text file.
- Built with Python and Streamlit for a simple UI.

## 🛠 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Sahil0707/solar-ai-assistant.git
   cd solar-ai-assistant
2. Create a virtual environment and activate it:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
3. Install Dependencies:
   ```sh
   pip install -r requirements.txt
4. Set up your .env file(create a .env file and add your api key):
   ```sh
   API_KEY=your_openrouter_api_key
   BASE_URL=https://openrouter.ai/api/v1/chat/completions
5. Run the application
   ```sh
   streamlit run app.py

## 🚀 Usage
Enter your prompt in the Streamlit UI.
The AI will generate a response using OpenRouter API.
Conversations are logged in conversation_logs.txt.

## 📄 File Structure
   ```sh
      solar-ai-assistant/
   │-- .venv/                     # Virtual environment (not included in Git)
   │-- .env                        # API keys (DO NOT SHARE THIS!)
   │-- app.py                      # Main Streamlit app
   │-- config.py                   # Configuration settings
   │-- utils.py                    # Helper functions (API calls, logging)
   │-- requirements.txt             # Dependencies
   │-- conversation_logs.txt        # Conversation logs
   │-- README.md                    # Project documentation
