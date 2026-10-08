
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(override=True)

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

messages = []

print("Chatbot started! Type 'exit' to quit.\n")

while True:
    user_message = input("You: ").strip()

    if user_message.lower() == "exit":
        print("Goodbye!")
        break

    if not user_message:
        continue

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        max_tokens=200
    )

    bot_message = response.choices[0].message.content

    print(f"Bot: {bot_message}\n")

    messages.append({
        "role": "assistant",
        "content": bot_message
    })
