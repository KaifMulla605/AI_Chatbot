import pickle
import random
import nltk
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

nltk.download("punkt")

app = FastAPI(title="Chatbot API")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load model
with open("model/chatbot_model.pkl", "rb") as f:
    vectorizer, model, intents = pickle.load(f)

class ChatInput(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/chat")
def chat(data: ChatInput):
    X = vectorizer.transform([data.message])
    tag = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return {"response": random.choice(intent["responses"])}

    return {"response": "Sorry, I didn't understand that."}
