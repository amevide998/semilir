from fastapi import APIRouter, Depends, HTTPException, status
from app.models.Dtos.user_dto import UserLogin
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.auth import create_access_token
from app.services.user_service import UserService
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/login", tags=["login"])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], service: AuthService = Depends()):
    payload = UserLogin(
        username=form_data.username,
        password=form_data.password
    )
    user = await service.authenticate_user(payload)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({
            "username": user["username"],
            "email": user["email"]
        })
    if access_token:
        return {"access_token": access_token, "token_type": "bearer"}
