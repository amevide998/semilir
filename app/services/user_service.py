from app.repository.user_repository import UserRepository
from app.models.user import User
from app.models.password import Password
from app.models.Dtos.user_dto import UserRequest
from fastapi import Depends


class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    async def register_user(self, user: UserRequest) -> User:
        user_password = Password(
            hashed_password=user.password,
            salt='random'
        )
        new_user = User(
            username=user.username,
            email=user.email,
            password=user_password
        )
        return await self.repository.create_user(new_user)
