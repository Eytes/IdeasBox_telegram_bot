from pydantic import BaseModel, Field, PositiveInt

from .task import Task


class User(BaseModel):
    tg_id: PositiveInt = Field(alias="_id")
    tasks: list[Task | None] = []
