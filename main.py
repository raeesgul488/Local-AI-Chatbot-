from ollama import chat
prompt = input("Enter prompt")

response = chat(
    model='gemma3:1b',
    messages=[{'role': 'user', 'content':prompt}],
)
print(response.message.content)