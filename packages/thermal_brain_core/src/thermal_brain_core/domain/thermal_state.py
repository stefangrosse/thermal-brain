from pydantic import BaseModel

class ThermalState(BaseModel):
    thermal_charge: float
    estimated_heat_loss: float
    indoor_temperature: float | None = None
    outdoor_temperature: float | None = None
