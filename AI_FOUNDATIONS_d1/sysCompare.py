from ollama import chat

roles = [
    "You are a strict math teacher. Answer in one line.",
    "You are a 10 year old. Answer accordingly. Answer in one line.",
    "You are an IT professional. Answer in one line.",
]
for role in roles:
    response = chat(
    model = "llama3.2",
    messages= [
                {
                    "role" : "user",
                    "content" : role
                },
                {
                    "role" : "user",
                    "content" : "what are the 7 colours in a rainbow? Answer in one line."
                }
            ]
        )
    print(f"Role : {role}")
    print(response.message.content)
    print()