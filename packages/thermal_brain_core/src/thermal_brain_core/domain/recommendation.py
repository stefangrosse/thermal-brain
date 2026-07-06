from pydantic import BaseModel

class Recommendation(BaseModel):
    title:str
    description:str
    confidence:float
