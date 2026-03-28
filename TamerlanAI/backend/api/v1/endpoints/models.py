"""
Models Management API
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import APIRouter, Request, HTTPException
from typing import List, Dict, Any

router = APIRouter()


@router.get("/")
async def list_models(req: Request) -> Dict[str, List[str]]:
    """Список доступных моделей"""
    llm_manager = req.app.state.llm_manager
    return {"models": llm_manager.get_available_models()}


@router.get("/{model_name}")
async def get_model_info(model_name: str, req: Request) -> Dict[str, Any]:
    """Информация о модели"""
    try:
        llm_manager = req.app.state.llm_manager
        return llm_manager.get_model_info(model_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/switch/{model_name}")
async def switch_model(model_name: str, req: Request):
    """Переключить текущую модель"""
    try:
        llm_manager = req.app.state.llm_manager
        llm_manager.set_current_model(model_name)
        return {"message": f"Switched to {model_name}", "current_model": model_name}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
