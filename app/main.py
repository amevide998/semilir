from fastapi import FastAPI, Depends
from app.delivery.user_router import router as user_router
from app.delivery.article_router import router as article_router

app = FastAPI()

app.include_router(user_router)
app.include_router(article_router)
