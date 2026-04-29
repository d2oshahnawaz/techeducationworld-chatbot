from flask import Flask, render_template, request, jsonify
import random
import pickle
from chatbot_model import responses

app = Flask(__name__)

# 🔥 Load trained model (M.Tech level improvement)
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Prediction function
def predict_intent(text):
    text_vector = vectorizer.transform([text])
    return model.predict(text_vector)[0]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    try:
        user_input = request.json["message"].strip().lower()

        if user_input == "":
            return jsonify({"reply": "Please enter a valid query."})

        intent = predict_intent(user_input)

        if intent in responses:
            reply = random.choice(responses[intent])
        else:
            reply = "Sorry, I don't understand your question."

        # 🔥 Branding added
        reply = "Tech Education World: " + reply

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Something went wrong. Please try again."})


if __name__ == "__main__":
    app.run(debug=True)