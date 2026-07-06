from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field

class Identifier(BaseModel):
    model_config=ConfigDict(frozen=True)
    value:UUID=Field(default_factory=uuid4)
