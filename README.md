# Local AI Chatbot with Streamlit and Ollama

This is a simple, privacy-focused chatbot that runs entirely on your local machine.

## Prerequisites

1. **Install Ollama**:
   - Download and install Ollama from [ollama.com](https://ollama.com).
   - Ensure the Ollama server is running.

2. **Pull a Model**:
   Open your terminal and run:
   ```bash
   ollama pull llama3
   ```
   (or any other model you prefer, e.g., `mistral`, `phi3`)

## Installation

1. **Clone this repository** (or save the files):
   ```bash
   # If you are in the project folder:
   pip install -r requirements.txt
   ```

## Running the Application

Run the Streamlit app using the following command:

```bash
streamlit run app.py
```

## How it Works

- **Streamlit**: Provides the web-based user interface.
- **Ollama**: Provides the local LLM API.
- **State Management**: The app uses `st.session_state` to remember the conversation history, allowing the AI to have context of previous messages.
- **Streaming**: Responses are streamed in real-time for a better user experience.
