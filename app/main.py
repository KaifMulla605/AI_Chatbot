import pickle
import random
import os
import nltk

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

nltk.download('punkt')

app = FastAPI(title="Chatbot API")

# ===== PATH SETUP =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model", "chatbot_model.pkl")
static_path = os.path.join(BASE_DIR, "static")

# ===== LOAD MODEL =====
with open(model_path, "rb") as f:
    vectorizer, model, intents = pickle.load(f)

# ===== STATIC FILES =====
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

# ===== REQUEST FORMAT =====
class UserInput(BaseModel):
    message: str

# ===== CHAT ENDPOINT =====
@app.post("/chat")
def chat(user_input: UserInput):

    text = user_input.message

    X = vectorizer.transform([text])

    tag = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return {
                "response": random.choice(intent["responses"])
            }

    return {
        "response": "Sorry, I didn't understand that."
    }

# ===== ROOT TEST =====
@app.get("/")
def root():
    return {"message": "Chatbot API is running!"}