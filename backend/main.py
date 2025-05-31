from pydantic import BaseModel
import pickle
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Review(BaseModel):
    text: str


with open("../tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("../sentiment_classifier.pkl", "rb") as f:
    clf = pickle.load(f)


@app.post("/api/review")
def evaluate_review(review: Review):
    X = vectorizer.transform([review.text])
    pred = clf.predict(X)
    return {"evaluation": pred[0]}
