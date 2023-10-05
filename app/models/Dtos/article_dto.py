from pydantic import BaseModel
from typing import Union, List
from datetime import datetime
from .user_dto import UserResponse


class ArticleRequest(BaseModel):
    title: str
    description: str
    content: Union[str | dict]
    author: UserResponse
    tags: List[str] = []

    class Config:
        arbitrary_types_allowed = True
