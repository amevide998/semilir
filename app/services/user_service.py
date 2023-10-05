from app.repository.user_repository import UserRepository
from app.models.user import User
from app.models.Dtos.user_dto import UserRequest
from fastapi import Depends
from app.utils.hash import hash_password


class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    async def register_user(self, user: UserRequest) -> User:
        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )
        return await self.repository.create_user(new_user)
