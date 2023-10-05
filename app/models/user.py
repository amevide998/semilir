from pydantic import BaseModel
from bson import ObjectId
from .password import Password


class User(BaseModel):
    username: str
    email: str
    password: Password

    class Config:
        arbitrary_types_allowed = True


