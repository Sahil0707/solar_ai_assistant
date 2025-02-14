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
