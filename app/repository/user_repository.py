from ..database import get_db_connection
from app.models.user import User
from pymongo.database import Database
from fastapi import Depends


class UserRepository:
    def __init__(self, db: Database = Depends(get_db_connection)):
        self.collection = db['users']

    async def create_user(self, user: User) -> User:
        user_dict = user.model_dump()
        self.collection.insert_one(user_dict)
        return user
