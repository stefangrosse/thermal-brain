from pydantic import field_validator
from .base import Measurement

class Percentage(Measurement):
    @field_validator("value")
    @classmethod
    def validate_range(cls,v:float)->float:
        if not 0<=v<=100:
            raise ValueError("Percentage must be between 0 and 100")
        return v
