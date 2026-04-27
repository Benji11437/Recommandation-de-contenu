# backend
import os
import pickle
from fastapi import FastAPI
from model import get_model
from src.hybrid import hybrid

app = FastAPI()
model = None
@app.on_event("startup")
def startup_event():
    global model
    model = get_model()


@app.get("/recommend")
def recommend(user_id: int, k: int = 5):

    emb = model["emb"]
    df_rating = model["df_rating"]
    algo = model["algo"]

    results = hybrid(user_id, emb, df_rating, algo, n=k)

    return {
        "user_id": user_id,
        "recommendations": [
            {"article_id": int(a), "score": float(s)}
            for a, s in results
        ]
    }
# uvicorn main:app --reload --port 8000