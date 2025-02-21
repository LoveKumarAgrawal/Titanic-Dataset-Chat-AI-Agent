import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/query/"

# Title of the app with styling
st.markdown(
    """
    <h1 style='text-align: center; color: #00bcd4;'>🛳️ Titanic Dataset Chatbot 🤖</h1>
    <h3 style='text-align: center; color: #8e44ad;'>Ask me any question about the Titanic dataset!</h3>
""",
    unsafe_allow_html=True,
)

# Description with styling
st.markdown(
    """
Welcome to the **Titanic Dataset Chatbot**. I can help you analyze the Titanic dataset and provide insightful answers and visualizations.

Just ask me a question, and I'll respond with data-backed answers and charts!

💬 **Examples of questions**:
- "What percentage of passengers were male on the Titanic?"
- "Show me a histogram of passenger ages."
- "What was the average ticket fare?"
- "How many passengers embarked from each port?"

""",
    unsafe_allow_html=True,
)

# Get user input
user_input = st.text_input("Ask your question here:", "")

# When the user submits a question
if user_input:
    with st.spinner("Processing your query..."):
        # Send the query to the FastAPI backend
        response = requests.post(API_URL, json={"query": user_input})
        print(response.text)

        # Get the response
        answer = response.json().get(
            "response", "Sorry, I couldn't get the answer. Please try again."
        )

        # Display the text answer
        st.markdown("### Answer:")
        st.write(answer)

# Footer with some styling and personal branding
st.markdown(
    """
---
<div style="text-align: center;">
    <h4>Made with ❤️ by <span style="color: #f39c12;">Love Kumar Agrawal</span></h4>
    <p>🎓 Tech Enthusiast | 🖥️ Passionate about AI</p>
</div>
""",
    unsafe_allow_html=True,
)

# Add some background color or layout tweaks
st.markdown(
    """
    <style>
        .main {
            background-color: #f0f8ff;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Add a subtle border for the user input box for better aesthetics
st.markdown(
    """
    <style>
        .stTextInput>div>div>input {
            border: 2px solid #8e44ad;
            border-radius: 8px;
        }
    </style>
""",
    unsafe_allow_html=True,
)
