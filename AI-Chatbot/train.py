# ============================================
# AI Chatbot Training Script
# ============================================

import json
import pickle
import nltk

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

patterns = []
tags = []

# Prepare training data
for intent in intents["intents"]:
    for pattern in intent["patterns"]:

        words = nltk.word_tokenize(pattern.lower())

        words = [
            lemmatizer.lemmatize(word)
            for word in words
            if word.isalnum()
        ]

        sentence = " ".join(words)

        patterns.append(sentence)
        tags.append(intent["tag"])

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(tags)

# Better TF-IDF configuration
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(patterns)

# Better classifier
model = LogisticRegression(
    max_iter=2000,
    random_state=42
)

model.fit(X, y)

# Save everything
with open("model/chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("=" * 50)
print("✅ Model trained successfully!")
print("✅ Files saved inside 'model/'")
print("=" * 50)