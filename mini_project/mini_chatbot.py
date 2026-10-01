from ollama import chat 
print("WELCOME BACK....!!!❤️❤️")

system_msg="you are a singer. Answer in some song form.answer in one sentence"
history=[ {   "role":"system", "content":system_msg }]

questioncounter = 0


while True:
     
    question = input("You:")  
    if question == "":
        print("please type something")
        continue

    if question.lower().strip() == 'exit' or question.lower().strip == 'bye':
        history=[{"role":"system","content":"system_msg"}]
        print("Alexander😘:Good back user come back soon") 
        break 
    if question.lower().strip()=="/history":
        print("---Your Conversation so far---")
        if len(history)<2:
            print("Nothing here so far!!")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="You"
            else:
                speaker="Alexander"
            print(f"{speaker}:{msg['content']}")
        print("---------------------------------------------")
        print() 
        continue  
    if question.lower().strip()=="/clear":
        history.append({"role":"user","content":"question"})
        print("Your chat history has been cleared.start a fresh conversation!")
        print() 
        continue
    history.append({"role" : "user", "content" : question })
    # try:

    response = chat( 
            model = "llama3.2", 
            messages = history
        )


    reply=response["message"]["content"]
    history.append({"role":"assistant","content":reply})
    print(f"Alexander:{reply}")
    # except Exception as e:
    # print("unknown issue.is ollama running")
    #/personality
    