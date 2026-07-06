from pydantic import BaseModel

class Building(BaseModel):
    id: str
    name: str
    construction_year: int | None = None
