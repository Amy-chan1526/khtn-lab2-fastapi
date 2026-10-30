from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from transformers import pipeline
import uvicorn

# 1. Initialize FastAPI Application
app = FastAPI(
    title="Sentiment Analysis API",
    description="Web API for text sentiment analysis using Hugging Face Transformers model",
    version="1.0.0"
)

# Load Hugging Face Pipeline
try:
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    classifier = None


# 2. Define Request & Response Schemas using Pydantic
class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text for sentiment analysis. Cannot be empty.")

class SentimentResponse(BaseModel):
    label: str
    score: float


# 3. Define API Endpoints
@app.get("/", summary="System Overview")
def root():
    """
    Root endpoint returning a brief introduction and API documentation details.
    """
    return {
        "message": "Welcome to the Sentiment Analysis Web API!",
        "model": "distilbert-base-uncased-finetuned-sst-2-english",
        "endpoints": {
            "GET /": "System introduction and description",
            "GET /health": "Check system operational status",
            "POST /predict": "Predict sentiment label and score for input text"
        },
        "docs_url": "/docs"
    }


@app.get("/health", summary="Health Check")
def health_check():
    """
    Checks operational status of the system and whether the Hugging Face model is loaded.
    """
    if classifier is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Hugging Face model failed to load properly."
        )
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict", response_model=SentimentResponse, summary="Predict Sentiment")
def predict_sentiment(payload: TextRequest):
    """
    Receives text input, runs model inference, and returns JSON sentiment classification result.
    """
    # Basic input validation
    if not payload.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid input: Text cannot consist solely of whitespace."
        )

    try:
        results = classifier(payload.text)
        result = results[0]
        return SentimentResponse(
            label=result["label"],
            score=round(result["score"], 4)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Model inference failed: {str(e)}"
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)