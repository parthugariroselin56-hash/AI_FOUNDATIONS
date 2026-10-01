from ollama import chat

for temp in  [0, 0.7, 1.5]:
    print(f"Temp : {temp}")
    for run in range(3):
        response = chat(
            model = "llama3.2",
            messages= [
                {
                    "role" : "user",
                    "content" : "Give me a one-line tagline for my coffeshop. Keep it short. only one tagline"
                }
            ],
            options = {"temperature" : temp}
        )
        print(f"Run : {run+1}: {response.message.content}")
        print(response.message.content)