from pydantic import BaseModel, Field
from typing import List

class PredictRequest(BaseModel):
    features: List[float] = Field(..., description="Feature vector")

class PredictResponse(BaseModel):
    modelVersion: str
    score: float
    label: int
