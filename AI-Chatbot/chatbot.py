# ============================================
# AI Chatbot Prediction Engine
# ============================================

import json
import pickle
import random
import nltk

from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load trained model
model = pickle.load(open("model/chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("model/label_encoder.pkl", "rb"))

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)


def preprocess(text):
    """Preprocess user input."""
    words = nltk.word_tokenize(text.lower())
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)


def get_response(user_input):

    processed = preprocess(user_input)

    X = vectorizer.transform([processed])

    prediction = model.predict(X)[0]

    probabilities = model.predict_proba(X)[0]

    confidence = max(probabilities)

    predicted_tag = label_encoder.inverse_transform([prediction])[0]

    # Lower confidence threshold
    if confidence < 0.20:
        predicted_tag = "unknown"

    for intent in intents["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    return "Sorry, I couldn't understand that."