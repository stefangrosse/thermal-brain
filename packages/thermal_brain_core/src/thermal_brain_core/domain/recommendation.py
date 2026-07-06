from typing import Protocol

class Recommendation(Protocol):
    title: str
    description: str
    confidence: float
