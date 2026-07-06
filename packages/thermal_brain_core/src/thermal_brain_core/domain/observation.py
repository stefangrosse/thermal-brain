from datetime import datetime
from pydantic import BaseModel, Field
from thermal_brain_core.value_objects import Identifier

class Observation(BaseModel):
    id: Identifier = Field(default_factory=Identifier)
    timestamp: datetime
    source: str
    quantity: str
    value: float
    unit: str
