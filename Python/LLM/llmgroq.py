import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or None

model_GROQ = "llama-3.1-8b-instant"#"llama3-8b-8192"
clien_GROQ = Groq(api_key=GROQ_API_KEY)
messages_GROQ = []
messages_GROQ = [
    {
        "role": "system",
        "content": "Spreak like a human"
    },
    {
        "role": "user",
        "content": "Olá?"
    }
]

chat_GROQ = clien_GROQ.chat.completions.create(messages=messages_GROQ, model=model_GROQ)

#print(chat_GROQ.choices[0].message.content)
print(messages_GROQ[0]["content"] +f"\n"+chat_GROQ.choices[0].message.content)