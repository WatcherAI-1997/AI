"""
Translation API
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


class TranslateRequest(BaseModel):
    text: str = Field(..., description="Текст для перевода")
    source_lang: str = Field(..., description="Исходный язык (код)")
    target_lang: str = Field(..., description="Целевой язык (код)")


@router.post("/")
async def translate(data: TranslateRequest, req: Request):
    """Перевод текста между языками"""
    llm_manager = req.app.state.llm_manager

    prompt = f"Переведи следующий текст с {data.source_lang} на {data.target_lang}:\n\n{data.text}"

    result = await llm_manager.generate(
        prompt=prompt,
        language=data.target_lang,
        task="translate"
    )

    return {
        "translation": result["response"],
        "source_lang": data.source_lang,
        "target_lang": data.target_lang,
    }
