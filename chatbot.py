def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    while True:
         user_input=input("you").lower()
         if user_input=="exit":
          print("chatbot:Good bye have a great day!")
          break
         elif "hello" in user_input or "hi" in user_input.lower():
            print("chatbot:hi there how can i help you today?") 
         elif "hoe are you" in user_input:
           print("Chatbot: I'm just a program, but I'm functioning as expected. How about you?")
         elif "your name" in user_input:
           print("Chatbot: I'm ChatBot3000. What's your name?")
         else:
          print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")
         if __name__ == "__main__":
            chatbot()