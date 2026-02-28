from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import requests
import numpy as np
import os

app = FastAPI()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

ENDEE_URL = "http://localhost:8080"

class Document(BaseModel):
    text: str

class Query(BaseModel):
    question: str

def embed(text):
    return model.encode(text).tolist()

@app.post("/add_document")
def add_document(doc: Document):
    vector = embed(doc.text)

    payload = {
        "vector": vector,
        "metadata": {"text": doc.text}
    }

    r = requests.post(f"{ENDEE_URL}/insert", json=payload)
    return {"status": "inserted", "endee_response": r.text}

@app.post("/ask")
def ask_question(query: Query):
    vector = embed(query.question)

    search_payload = {
        "vector": vector,
        "top_k": 3
    }

    r = requests.post(f"{ENDEE_URL}/search", json=search_payload)
    print("Endee Status:", r.status_code)
    print("Endee response:", r.text)
    results = r.json()

    context = " ".join([item["metadata"]["text"] for item in results])

    # Simple mock LLM answer (for now)
    return {
        "question": query.question,
        "retrieved_context": context,
        "note": "Connect to OpenAI here if allowed."
    }
