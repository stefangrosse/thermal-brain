from datetime import datetime
from pydantic import BaseModel

class Observation(BaseModel):
    timestamp:datetime
    source:str
    metric:str
    value:float
    unit:str
