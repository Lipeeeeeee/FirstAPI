from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_atributtes = True
        arbitrary_types_allowed = True

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="ID")]
    created_at: Annotated[datetime, Field(description="Data de criação")]