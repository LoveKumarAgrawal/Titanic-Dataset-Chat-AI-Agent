import streamlit as st
import requests

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
- "What was the average ticket fare?"
- "How many passengers embarked from each port?"
- "Show me a histogram of passenger ages."
- "What percentage of passengers were male on the Titanic?"
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='height: 2px; background-color: #ffffff'></div>
    """,
    unsafe_allow_html=True
)

# Initialize message history in session state if not already present
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to display the chat history
def display_chat():
    

    for message in st.session_state.messages:
        # Display user question (right-aligned)
        if message['role'] == 'user':
            st.markdown(f"<div style='text-align: right; background-color: #000000; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>{message['text']}</div>", unsafe_allow_html=True)
        # Display bot answer (left-aligned)
        else:
            st.markdown(f"<div style='text-align: left; background-color: #000000; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>{message['text']}</div>", unsafe_allow_html=True)

# Display the chat history
display_chat()

# Get user input
user_input = st.text_input("Ask your question here:", "")

# When the user submits a question
if user_input:
    with st.spinner("Processing your query..."):
        # Append user message to chat history
        st.session_state.messages.append({'role': 'user', 'text': user_input})
        
        # Send the query to the FastAPI backend
        response = requests.post(API_URL, json={"query": user_input})
        if response:
            
            # Get the response
            answer = response.json().get(
                "response", "Sorry, I couldn't get the answer. Please try again."
            )

            # Append bot answer to chat history
            st.session_state.messages.append({'role': 'bot', 'text': answer})

            st.markdown(f"<div style='text-align: left; background-color: #000000; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>{answer}</div>", unsafe_allow_html=True)


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
