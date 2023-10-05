from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.models.Dtos.user_dto import UserRequest, UserResponse
from fastapi import HTTPException, status

router = APIRouter()


@router.post("/register", response_model=UserResponse, tags=["User"])
async def register_user(request: UserRequest, service: UserService = Depends()):
    user = await service.register_user(request)
    if not user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return user

