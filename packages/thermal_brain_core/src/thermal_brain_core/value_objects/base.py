from pydantic import BaseModel, ConfigDict

class Measurement(BaseModel):
    model_config = ConfigDict(frozen=True)
    value: float
