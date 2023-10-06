from app.repository.article_repository import ArticleRepository
from fastapi import Depends
from app.models.Dtos.article_dto import ArticleRequest
from app.models.article import Article


class ArticleService:
    def __init__(self, repository: ArticleRepository = Depends()):
        self.repository = repository

    async def create(self, user: UserResponse) -> str:
        new_article = Article(
            title="",
            description="",
            content="",
            author=user,
            tags=[],
        )
        return await self.repository.create(new_article)
