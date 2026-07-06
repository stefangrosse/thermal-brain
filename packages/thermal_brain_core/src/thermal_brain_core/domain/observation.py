from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field

class Observation(BaseModel):
    id: str
    timestamp: datetime
    source: str
    quantity: str
    value: float
    unit: str
    quality: str = "measured"
    metadata: dict[str, Any] = Field(default_factory=dict)
