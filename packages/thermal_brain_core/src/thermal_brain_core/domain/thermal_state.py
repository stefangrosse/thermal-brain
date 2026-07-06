from pydantic import BaseModel
from thermal_brain_core.value_objects import Percentage, Power

class ThermalState(BaseModel):
    thermal_charge: Percentage
    estimated_heat_loss: Power
