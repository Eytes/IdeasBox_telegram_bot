from uuid import uuid4

from pydantic import BaseModel, Field, UUID4


class Task(BaseModel):
    task_id: UUID4 = Field(alias="_id", default_factory=lambda: uuid4())
    description: str = Field(min_length=1)
