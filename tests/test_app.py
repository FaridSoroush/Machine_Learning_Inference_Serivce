from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200

def test_predict():
    r = client.post("/v1/predict", json={"features": [0.1, 0.2, 0.3]})
    assert r.status_code == 200
    body = r.json()
    assert "score" in body and "label" in body
