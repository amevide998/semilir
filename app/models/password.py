from pydantic import BaseModel


class Password(BaseModel):
    hashed_password: str
    salt: str
