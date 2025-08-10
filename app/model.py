import math
from typing import List

class ToyModel:
    """Deterministic placeholder model."""
    def __init__(self, bias: float = 0.0):
        self.bias = bias

    def predict_proba(self, x: List[float]) -> float:
        if not x:
            return 0.5
        z = sum(x) / len(x) + self.bias
        return 1 / (1 + math.exp(-z))

MODEL = ToyModel(bias=0.1)