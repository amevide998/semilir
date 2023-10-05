from fastapi import APIRouter, Depends
from app.models.Dtos.article_dto import ArticleRequest
from app.services.article_service import ArticleService


router = APIRouter()

@router.post("/article", response_model=str, tags=["article"])
async def create(request: ArticleRequest, service:ArticleService = Depends()):
    return await service.create(request)