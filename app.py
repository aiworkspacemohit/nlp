# app.py

from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import classify_and_assign
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Ticket(BaseModel):
    title: str
    description: str

@app.get("/")
def health():
    return {"status": "AI Model Service Running"}

@app.post("/predict")
def predict(ticket: Ticket):
    """
    Input:
    {
        "title": "Laptop overheating",
        "description": "Gets hot during use"
    }

    Output:
    {
        "category": "...",
        "priority": "...",
        "assign_to_team": "...",
        "assigned_technician": {...}
    }
    """
    result = classify_and_assign(ticket.title, ticket.description)
    return result
