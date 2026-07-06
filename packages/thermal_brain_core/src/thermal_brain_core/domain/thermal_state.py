from pydantic import BaseModel

class ThermalState(BaseModel):
    thermal_charge:float
    estimated_heat_loss:float
