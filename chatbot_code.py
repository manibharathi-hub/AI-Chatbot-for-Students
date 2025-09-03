# Simple AI Chatbot for Students using Python

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "course": "You can check your courses on the Naan Mudhalvan portal.",
    "library": "The college library is open from 9 AM to 5 PM.",
    "exam": "Exams will be conducted as per the university schedule.",
    "bye": "Goodbye! Have a nice day.",
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that yet.")

if __name__ == "__main__":
    print("AI Chatbot for Students (type 'bye' to exit)")
    while True:
        user = input("You: ")
        print("Bot:", chatbot_response(user))
        if user.lower() == "bye":
            break
