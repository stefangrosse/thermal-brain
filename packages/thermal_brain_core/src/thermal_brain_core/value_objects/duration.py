from pydantic import BaseModel, ConfigDict

class Duration(BaseModel):
    model_config=ConfigDict(frozen=True)
    seconds:int
