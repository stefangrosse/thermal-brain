from pydantic import BaseModel
from thermal_brain_core.value_objects import Temperature

class WeatherObservation(BaseModel):
    outdoor_temperature: Temperature

class WeatherForecast(BaseModel):
    minimum_temperature: Temperature
    maximum_temperature: Temperature
