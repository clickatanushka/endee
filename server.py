# server.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()
vectors = {}  # Simple in-memory vector store

class Item(BaseModel):
    id: str
    embedding: list

@app.post("/ingest")
def ingest(item: Item):
    """Store vector embedding"""
    vectors[item.id] = np.array(item.embedding)
    return {"status": "ok", "stored_id": item.id}from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()
vectors = {}

class Item(BaseModel):
    id: str
    embedding: list

@app.post("/ingest")
def ingest(item: Item):
    vectors[item.id] = np.array(item.embedding)
    return {"status": "ok"}

@app.get("/query/{item_id}")
def query(item_id: str):
    if item_id not in vectors:
        return {"error": "not found"}
    # dummy similarity: just return the same vector
    return {"vector": vectors[item_id].tolist()}

@app.get("/query/{item_id}")
def query(item_id: str):
    """Retrieve vector embedding"""
    if item_id not in vectors:
        return {"error": "not found"}
    # For simplicity, return the stored vector
    return {"vector": vectors[item_id].tolist()}

@app.get("/health")
def health():
    return {"status": "ok"}
