import requests

BASE_URL = "http://127.0.0.1:8000"

def test_endpoints():
    print("--- 1. Testing GET / ---")
    res = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.json()}\n")

    print("--- 2. Testing GET /health ---")
    res = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.json()}\n")

    print("--- 3. Testing POST /predict (Positive Input) ---")
    payload_pos = {"text": "I absolutely love working with FastAPI and Hugging Face!"}
    res = requests.post(f"{BASE_URL}/predict", json=payload_pos)
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.json()}\n")

    print("--- 4. Testing POST /predict (Negative Input) ---")
    payload_neg = {"text": "The service was terrible and the experience was disappointing."}
    res = requests.post(f"{BASE_URL}/predict", json=payload_neg)
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.json()}\n")

    print("--- 5. Testing Error Handling (Whitespace Input) ---")
    payload_invalid = {"text": "   "}
    res = requests.post(f"{BASE_URL}/predict", json=payload_invalid)
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.json()}\n")

if __name__ == "__main__":
    test_endpoints()