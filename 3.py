def chatbot():
    print("Chatbot")

    while True:
        user_input = input("You:").lower().strip()

        if user_input in["hello","hi","hey"]:
            print("Chatbot:Hello!!! How can I help you?")

        elif user_input in["how are you","what's up","how's it going"]:
            print("Chatbot:I'm doing great!!How about you?")

        elif user_input in["i'm fine","i am fine","good","great"]:
            print("Chatbot:That's good to hear")

        elif user_input in["not good","sad","tired","bad","boring"]:
            print("Chatbot:Ohh!! I'm so sorry to hear that.")


        elif user_input in["who are you","what's up"]:
            print("Chatbot:I'm your friendly ai called chatbot")

        elif user_input in["what are you doing","sup"]:
            print("Chatbot:Just having a good conversation with you")

        elif user_input in["tell me a joke","ok....tell me a funny joke","joke"]:
            print("Chatbot:🗣Why did the programmer go broke?\nBecause he used up all his cache. 💸")

        elif user_input in["thank you","thank u","thanks","thnk"]:
            print("Chatbot:You're welcome!!")

        elif user_input in["bye","goodbye","see you"]:
            print("Chatbot:Goodbye! Have a fantastic day👋")

        else:
            print("Chabot:Hmmm, I didn't get that. Try saying 'hello' or 'joke'.")

chatbot()
        
        
        
        
