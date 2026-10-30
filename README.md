
# Sentiment Analysis Web API - Lab 2

## Student Information
- **Full Name:** Nguyen Dang Hoang Ngan
- **Student ID:** 25127098
- **Class:** 25C09
- **Course:** Computational Thinking - Application Programming Interface (API)

---

## Model Details
- **Model Name:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Hugging Face Model Link:** [https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- **Task:** Sentiment Analysis (Binary classification: `POSITIVE` / `NEGATIVE`)

---

## System Overview
This project is a lightweight RESTful Web API built using **FastAPI** and **Hugging Face Transformers**. It provides real-time sentiment analysis predictions for English text, featuring robust request validation, custom exception handling, and system health monitoring endpoints.

### Project Directory Structure
```text
KHTN-Lab2-FASTAPI
├── main.py              # Main FastAPI application source code
├── test_api.py          # Python test script using requests
├── requirements.txt     # List of project dependencies
├── README.md            # Documentation and submission details
└── .gitignore           # Git ignore file configuration
```

---

## Installation & Setup

### 1. Prerequisites

* Python 3.8 or higher installed on your machine.

### 2. Clone the Repository

```bash
git clone https://github.com/ndhngan2528/khtn-lab2-fastapi.git
cd khtn-lab2-fastapi
```

### 3. Create and Activate Virtual Environment

* **Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API Server

You can start the server directly using Python or via Uvicorn:

```bash
python main.py
```

*Alternatively, run with Uvicorn CLI:*

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Once started, the API will be available at: `http://127.0.0.1:8000`

Interactive Swagger API documentation can be accessed at: `http://127.0.0.1:8000/docs`

---

## API Endpoints & Usage

### 1. `GET /` - System Overview

Returns a general introduction and available endpoints.

* **Request:** `GET http://127.0.0.1:8000/`
* **Response Example:**
```json
{
  "message": "Welcome to the Sentiment Analysis Web API!",
  "model": "distilbert-base-uncased-finetuned-sst-2-english",
  "endpoints": {
    "GET /": "System introduction and description",
    "GET /health": "Check system operational status",
    "POST /predict": "Predict sentiment label and score for input text"
  },
  "docs_url": "/docs"
}
```

### 2. `GET /health` - Health Check

Checks system operational status and model readiness.

* **Request:** `GET http://127.0.0.1:8000/health`
* **Response Example (200 OK):**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 3. `POST /predict` - Sentiment Prediction

Accepts text payload, runs inference, and returns sentiment classification label and score.

* **Request Header:** `Content-Type: application/json`
* **Request Body:**
```json
{
  "text": "I absolutely love working with FastAPI and Hugging Face!"
}
```

* **Response Example (200 OK):**
```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

* **Error Response Example (400 Bad Request):**
```json
{
  "detail": "Invalid input: Text cannot consist solely of whitespace."
}
```

---

## Automated Testing

Ensure the server is running, then execute the automated test script in another terminal window:

```bash
python test_api.py
```

---

## Demonstration Video

* **Video Link:** [INSERT_YOUR_YOUTUBE_OR_GOOGLE_DRIVE_LINK_HERE]

*(Note: Please ensure the video link is publicly accessible)*


