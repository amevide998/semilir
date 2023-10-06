from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated

from app.models.Dtos.user_dto import UserLogin
from app.utils.auth import decode_jwt
from app.models.token import Token
from app.repository.user_repository import UserRepository
from app.utils.hash import verify

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_jwt(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
        current_user: Annotated[Token, Depends(get_current_user)],
        repository: UserRepository = Depends()
):
    user = await repository.find_user(current_user["username"])
    if user:
        return current_user



class AuthService:
    def __init__(self,repository: UserRepository = Depends()):
        self.repository = repository

    async def authenticate_user(self, user: UserLogin):
        user_result = await self.repository.get_user_password(user.username)
        if user_result:
            if verify(user.password, user_result["password"]):
                return user_result
            return False
