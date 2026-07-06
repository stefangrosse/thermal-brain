from pydantic import BaseModel

class Zone(BaseModel):
    id:str
    name:str
    target_temperature:float=21.0
