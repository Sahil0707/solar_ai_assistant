import streamlit as st
from utils import get_ai_response

st.title("Solar Industry AI Assistant")

user_input = st.text_input("Ask me about solar energy:")

if st.button("Get Response"):
    if user_input:
        response = get_ai_response(user_input)
        st.write("AI:", response)
    else:
        st.warning("Please enter a question.")
