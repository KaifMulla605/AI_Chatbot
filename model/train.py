import json
import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download("punkt")

# Load intents
with open("data/intents.json", "r") as f:
    intents = json.load(f)

texts = []
labels = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Vectorization
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, labels)

# Save model
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model, intents), f)

print("✅ Chatbot model trained and saved.")
