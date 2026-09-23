import streamlit as st
import ollama

# Page configuration
st.set_page_config(page_title="Local AI Chatbot", page_icon="🤖")

st.title("🤖 Local AI Chatbot")
st.markdown("Chat with your local LLMs powered by Ollama")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")

    # Fetch available models from Ollama
    try:
        models_info = ollama.list()
        # Handle different versions of ollama library return types
        if hasattr(models_info, 'models'):
            model_names = [m['name'] for m in models_info.models]
        elif isinstance(models_info, list):
            model_names = [m['name'] for m in models_info]
        else:
            # Fallback for older versions or different structures
            model_names = ["llama3", "mistral", "phi3"]
    except Exception as e:
        st.error(f"Error connecting to Ollama: {e}")
        model_names = []

    if model_names:
        selected_model = st.selectbox("Choose a model", model_names)
    else:
        selected_model = st.text_input("Enter model name (if list failed)", value="llama3")
        st.warning("Could not fetch models automatically. Please ensure Ollama is running.")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            # Stream response from Ollama
            stream = ollama.chat(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True,
            )

            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"An error occurred: {e}")
