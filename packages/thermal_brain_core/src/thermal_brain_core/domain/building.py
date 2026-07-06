from pydantic import BaseModel, Field
from .zone import Zone

class Building(BaseModel):
    name:str
    zones:list[Zone]=Field(default_factory=list)
