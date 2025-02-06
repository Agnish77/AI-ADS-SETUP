from fastapi import FastAPI
from chatbot import get_chatbot_response
from google_ads import create_google_ad

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Chatbot for Google Ads"}

@app.post("/chatbot")
def chatbot_response(user_input: str):
    response = get_chatbot_response(user_input)
    return {"response": response}

@app.post("/create-ad")
def create_ad(data: dict):
    ad_response = create_google_ad(data)
    return {"status": "success", "ad_data": ad_response}
