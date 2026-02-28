from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()
vectors = {}  # simple in-memory vector storage

class Item(BaseModel):
    id: str
    embedding: list

@app.post("/ingest")
def ingest(item: Item):
    vectors[item.id] = np.array(item.embedding)
    return {"status": "ok", "stored_id": item.id}

@app.get("/query/{item_id}")
def query(item_id: str):
    if item_id not in vectors:
        return {"error": "not found"}
    return {"vector": vectors[item_id].tolist()}

@app.get("/health")
def health():
    return {"status": "ok"}
