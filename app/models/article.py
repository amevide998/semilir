from pydantic import BaseModel
from typing import Union, List
from datetime import datetime
from .Dtos.user_dto import UserResponse


class Article(BaseModel):
    title: str
    description: str
    content: Union[str | dict]
    author: UserResponse
    created_date: datetime = datetime.now()
    tags: List[str] = []

    class Config:
        arbitrary_types_allowed = True
