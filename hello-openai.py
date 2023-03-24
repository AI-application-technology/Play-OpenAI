import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# create a chatbot with openai chatcompletion
# loop back to prompt for user to input message
# until user types "exit"

def chat():
    prompt = "you are a great helpful assitant!\nAI:"
    msg_history=[{"role":"system","content":prompt}]

    while True:
        response =  openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msg_history,
            )

        # print the response from the chatbot
        print("AI: " + response.choices[0].message.content)

        # get input from user
        new_message = input("You: ")

        # if user types exit, then exit the loop
        if new_message == "exit":
            break

        # add new message to message history
        # and add the role of the user
        # clear older 5 messages from history if more than 20 messages
        if len(msg_history) > 20:
            msg_history = msg_history[5:]
            
        new_message = {"role":"user","content":new_message}
        msg_history.append(new_message)

chat()