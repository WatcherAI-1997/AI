"""
Text Analysis API
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

router = APIRouter()


class AnalyzeRequest(BaseModel):
    text: str = Field(..., description="Текст для анализа")
    analysis_type: str = Field("general", description="Тип анализа: general, sentiment, summary")


@router.post("/")
async def analyze_text(data: AnalyzeRequest, req: Request):
    """Анализ текста"""
    llm_manager = req.app.state.llm_manager

    prompts = {
        "general": f"Проанализируй следующий текст:\n\n{data.text}",
        "sentiment": f"Определи тональность (позитивная/негативная/нейтральная):\n\n{data.text}",
        "summary": f"Создай краткое резюме:\n\n{data.text}",
    }

    prompt = prompts.get(data.analysis_type, prompts["general"])

    result = await llm_manager.generate(
        prompt=prompt,
        task="text_analysis"
    )

    return {
        "analysis": result["response"],
        "type": data.analysis_type,
    }
