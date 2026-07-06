from pydantic import BaseModel
from thermal_brain_core.value_objects import Identifier, Temperature

class Zone(BaseModel):
    id: Identifier
    name: str
    target_temperature: Temperature = Temperature(value=21.0)
