"""
TamerlanAI API Router
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import APIRouter

from .endpoints import chat, models, translate, analyze

api_router = APIRouter()

# Подключение эндпоинтов
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(models.router, prefix="/models", tags=["models"])
api_router.include_router(translate.router, prefix="/translate", tags=["translate"])
api_router.include_router(analyze.router, prefix="/analyze", tags=["analyze"])
