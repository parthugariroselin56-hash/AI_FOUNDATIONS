from ollama import chat

messages = [
    {"role" : "system", "content" : "Classify the sentiment as positive, negative, neutral. Reply with one word only."},

    {"role" : "user", "content" : "Great Movie."},
    {"role" : "system", "content" : "positive"},

    {"role" : "user", "content" : "Waste of Money."},
    {"role" : "system", "content" : "negative"},
    
    {"role" : "user", "content" : "It was okay."},
    {"role" : "system", "content" : "neutral"},
    
    {"role" : "user", "content" : "I loved the acting but ending was dull."},
]
response = chat(
    model = "llama3.2",
    messages= messages
)
print(response.message.content)
