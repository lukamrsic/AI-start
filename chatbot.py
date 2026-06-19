from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

print("🤖 Lokalni AI Chatbot (Ollama) - exit za izlaz")

while True:
    poruka = input("Ti: ")

    if poruka.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "user", "content": poruka}
        ]
    )

    print("AI:", response.choices[0].message.content)