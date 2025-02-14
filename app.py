import streamlit as st
from email import email  # Importing your email.py functions

# Set page title and layout
st.set_page_config(page_title="Email Assistant", page_icon="📧", layout="wide")

st.title("📧 Smart Email Assistant")
st.write("An AI-powered assistant to help you manage your emails efficiently.")

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["📥 Inbox", "🤖 AI Assistant"])

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if page == "📥 Inbox":
    st.header("📥 Your Emails")
    
    # Fetch emails using get_email function
    emails = email.get_email()
    
    if emails:
        for i, mail in enumerate(emails):
            with st.expander(f"📩 {mail['subject']} - {mail['from']}"):
                st.write(f"**From:** {mail['from']}")
                st.write(f"**Date:** {mail['date']}")
                st.write(f"**Content:** {mail['body']}")
    else:
        st.info("No new emails found.")

elif page == "🤖 AI Assistant":
    st.header("🤖 AI Email Assistant")
    
    # Display existing chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    user_input = st.chat_input("Ask me anything about your emails...")
    
    if user_input:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Generate response using llama_call
        response = email.llama_call(user_input)
        
        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Store response in chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
