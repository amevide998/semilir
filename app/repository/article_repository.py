from pymongo.database import Database
from ..database import get_db_connection
from fastapi import Depends
from app.models.article import Article


class ArticleRepository:
    def __init__(self, db: Database = Depends(get_db_connection)):
        self.collection = db["articles"]

    async def create(self, article: Article) -> str:
        article_dict = article.model_dump()
        self.collection.insert_one(article_dict)
        return article.title
