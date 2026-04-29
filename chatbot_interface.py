import random
from train_model import predict_intent
from chatbot_model import responses

print("\n🤖 Tech Education World Chatbot")
print("Ask about courses, internships, webinars, events, etc.")
print("Type 'bye' or 'exit' to quit\n")

while True:

    user_input = input("You: ").strip().lower()

    # Exit condition
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Thank you for visiting Tech Education World 🚀")
        break

    # Empty input check
    if user_input == "":
        print("Bot: Please enter a valid query.")
        continue

    try:
        # Predict intent
        intent = predict_intent(user_input)

        # Generate response
        if intent in responses:
            reply = random.choice(responses[intent])
        else:
            reply = "Sorry, I don't understand your question."

        print("Bot:", reply)

    except Exception as e:
        print("Bot: Something went wrong. Please try again.")
        print("Error:", e)