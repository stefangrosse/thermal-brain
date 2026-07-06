from pydantic import BaseModel

class WeatherSnapshot(BaseModel):
    outdoor_temperature:float
    wind_speed:float=0.0
    solar_irradiance:float=0.0
