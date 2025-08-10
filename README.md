# ML Service (FastAPI + Docker + Helm)
End-to-end machine learning inference services using FastAPI, Docker and K8s

## Quickstart (Local)
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
# health
curl -s http://localhost:8080/healthz
# predict
curl -s -X POST http://localhost:8080/v1/predict \
  -H 'Content-Type: application/json' \
  -d '{"features":[0.1,0.2,0.3]}'
