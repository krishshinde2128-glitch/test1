print("chat bot in workds to end the convoation say stop")
bot_response = "thats crazyy tell me more"
while True:
    user_input = input("You: ")
    if user_input == "stop":
        print("Chat Bot: Goodbye! Have a great day!")
        break
    else:
        print("Chat Bot:", bot_response)