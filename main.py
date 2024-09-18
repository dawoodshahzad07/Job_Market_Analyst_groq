import streamlit as st
from response import res  # Assuming 'response' is the correct module

def main():
    st.title("Job Analyst Chatbot")
    
    # Initialize chat history if not already initialized
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display chat history
    for message in st.session_state.chat_messages:
        if message["role"] == "user":
            st.text_area("User:", message["content"], height=40, key=f"user_{message['content']}", disabled=True)
        else:
            st.text_area("AI:", message["content"], height=40, key=f"ai_{message['content']}", disabled=True)

    # User input
    if prompt := st.chat_input("Welcome - How can I help you?"):
        # Add user message to chat history
        st.session_state.chat_messages.append({"role": "user", "content": prompt})

        # Simulate AI response (replace this with your actual AI response logic)
        response = res(prompt)

        # Display user's message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant's response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)

        # Add assistant's response to chat history
        st.session_state.chat_messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
