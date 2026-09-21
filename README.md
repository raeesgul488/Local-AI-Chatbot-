# Local-AI-Chatbot-
AI chatbot built in Python, powered by Google's Gemma model through a cloud-based API


Local AI Chatbot

A simple, privacy-friendly chatbot interface built with **Streamlit** and powered by **[Ollama](https://ollama.com/)**, allowing you to chat with locally running large language models (LLMs) — no cloud API required.

  Features

- 💬 Clean, interactive chat interface using Streamlit's native chat components
- 🔄 Real-time streaming responses from the model
- 📋 Dynamic model selection — automatically detects models installed in your local Ollama instance
- 🗑️ One-click chat history clearing
- 🛡️ Graceful error handling if Ollama isn't running or a model fails to load
- 🔒 Fully local — your conversations never leave your machine

Requirements

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running locally
- At least one model pulled via Ollama (e.g. `ollama pull llama3`)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies
   ```bash
   pip install streamlit ollama
   ```

3. Make sure Ollama is running
   ```bash
   ollama serve
   ```

4. Pull a model (if you haven't already)
   ```bash
   ollama pull llama3
   ```

▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`) in your browser.

- Select your preferred model from the sidebar dropdown.
- Type your message in the chat input box and press Enter.
- Click **"Clear Chat History"** in the sidebar to start a new conversation.

Project Structure

```
your-repo-name/
│
├── app.py           # Main Streamlit application
├── README.md        # Project documentation
└── requirements.txt # Python dependencies (optional)
```

 Tech Stack

- [Streamlit](https://streamlit.io/)** — for the web UI
- [Ollama](https://ollama.com/)** — for running local LLMs (e.g. Llama 3, Mistral, Phi-3)
- Python — core application logic

Troubleshooting

- "Error connecting to Ollama" — Make sure the Ollama service is running (`ollama serve`) before starting the app.
- No models listed — Pull at least one model using `ollama pull <model-name>`, then restart the app.

License

This project is open source and available under the [MIT License](LICENSE).

Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) if you want to contribute.
