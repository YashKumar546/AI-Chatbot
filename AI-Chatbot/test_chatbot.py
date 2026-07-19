from chatbot import get_response

print("=" * 50)
print("🤖 AI Chatbot")
print("Type 'quit' to exit.")
print("=" * 50)

while True:

    user = input("You: ")

    if user.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break

    response = get_response(user)

    print("Bot:", response)