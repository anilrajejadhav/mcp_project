from fastapi import FastAPI
from app.schema import SentimentRequest, SentimentResponse
from app.model import predict_sentiment

app = FastAPI(title="Sentiment Analysis API")

@app.post("/predict", response_model=SentimentResponse)
def analyze_sentiment(req: SentimentRequest):
    sentiment, confidence = predict_sentiment(req.text)
    return SentimentResponse(sentiment=sentiment, confidence=confidence)
