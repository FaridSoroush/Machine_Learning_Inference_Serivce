from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.schemas import PredictRequest, PredictResponse
from app.model import MODEL
from app.instrumentation import MetricsMiddleware, metrics_endpoint, logger
from app.version import VERSION, GIT_SHA
import os

app = FastAPI(title="ml-service", version=VERSION)
app.add_middleware(MetricsMiddleware)
app.add_api_route("/metrics", metrics_endpoint, methods=["GET"])

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"ready": True}

@app.get("/metadata")
def metadata():
    return {"version": VERSION, "git_sha": GIT_SHA, "env": os.getenv("ENV", "dev")}

@app.post("/v1/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    p = MODEL.predict_proba(req.features)
    label = 1 if p >= 0.5 else 0
    logger.info(f"scored request label={label} score={p:.4f}")
    return PredictResponse(modelVersion=f"{VERSION}+{GIT_SHA}", score=p, label=label)

@app.exception_handler(Exception)
async def on_exception(_, exc):
    logger.error(f"unhandled_exception: {repr(exc)}")
    return JSONResponse(status_code=500, content={"detail": "internal_error"})
