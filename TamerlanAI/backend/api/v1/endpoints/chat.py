"""
Chat API Endpoints
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import APIRouter, HTTPException, Request, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import logging
import json

from core.llm_manager_real import GenerationConfig

logger = logging.getLogger(__name__)

router = APIRouter()


class ChatMessage(BaseModel):
    """Сообщение в чате"""
    role: str = Field(..., description="Роль: 'user' или 'assistant'")
    content: str = Field(..., description="Содержимое сообщения")


class ChatRequest(BaseModel):
    """Запрос на генерацию ответа"""
    messages: List[ChatMessage] = Field(..., description="История сообщений")
    model: Optional[str] = Field(None, description="Модель (если не указано, используется текущая)")
    language: Optional[str] = Field(None, description="Язык ответа (авто-определение если не указано)")
    personality: Optional[str] = Field("formal", description="Стиль личности")
    temperature: Optional[float] = Field(0.7, ge=0.0, le=2.0, description="Температура генерации")
    max_tokens: Optional[int] = Field(2048, ge=1, le=4096, description="Максимум токенов")
    stream: bool = Field(False, description="Потоковая генерация")


class ChatResponse(BaseModel):
    """Ответ чата"""
    message: ChatMessage
    model: str
    language: str
    personality: str
    metadata: Dict[str, Any]


@router.post("/", response_model=ChatResponse)
async def chat(request_data: ChatRequest, req: Request):
    """
    Генерация ответа в чате

    Поддерживает:
    - Мультиязычность (автоопределение или явное указание)
    - Адаптивную личность
    - Историю диалога
    - Различные модели
    """
    try:
        # Получение LLM Manager из app state
        llm_manager = req.app.state.llm_manager

        # Построение промпта из истории
        prompt = _build_prompt_from_messages(request_data.messages)

        # Определение языка если не указан
        language = request_data.language
        if not language:
            last_user_message = next(
                (msg.content for msg in reversed(request_data.messages) if msg.role == "user"),
                None
            )
            if last_user_message:
                language = await llm_manager.detect_language(last_user_message)

        # Конфигурация генерации
        config = GenerationConfig(
            max_tokens=request_data.max_tokens,
            temperature=request_data.temperature,
        )

        # Генерация ответа
        result = await llm_manager.generate(
            prompt=prompt,
            model=request_data.model,
            language=language,
            personality=request_data.personality,
            task="chat",
            config=config,
        )

        return ChatResponse(
            message=ChatMessage(role="assistant", content=result["response"]),
            model=result["model"],
            language=result["language"],
            personality=result["personality"],
            metadata=result["metadata"],
        )

    except Exception as e:
        logger.error(f"Chat error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.websocket("/ws")
async def chat_websocket(websocket: WebSocket):
    """
    WebSocket для потоковой генерации

    Протокол:
    Client -> Server: {"messages": [...], "language": "ru", ...}
    Server -> Client: {"type": "token", "content": "..."}
    Server -> Client: {"type": "done", "metadata": {...}}
    """
    await websocket.accept()
    logger.info("WebSocket connection established")

    try:
        while True:
            # Получение сообщения
            data = await websocket.receive_text()
            request_data = json.loads(data)

            # Валидация
            if "messages" not in request_data:
                await websocket.send_json({"error": "Missing 'messages' field"})
                continue

            # TODO: Потоковая генерация
            # Сейчас отправляем сразу весь ответ
            await websocket.send_json({
                "type": "token",
                "content": "[Streaming response будет реализован позже]"
            })

            await websocket.send_json({
                "type": "done",
                "metadata": {"model": "tamerlane"}
            })

    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception as e:
        logger.error(f"WebSocket error: {e}", exc_info=True)
        await websocket.send_json({"error": str(e)})


@router.get("/personalities")
async def get_personalities():
    """Получить список доступных стилей личности"""
    from config import PERSONALITY_STYLES
    return {
        "personalities": [
            {"id": k, "description": v}
            for k, v in PERSONALITY_STYLES.items()
        ]
    }


@router.get("/languages")
async def get_languages():
    """Получить список поддерживаемых языков"""
    from config import get_settings
    settings = get_settings()

    return {
        "turkic_languages": settings.TURKIC_LANGUAGES,
        "other_languages": settings.OTHER_LANGUAGES,
        "total": len(settings.TURKIC_LANGUAGES) + len(settings.OTHER_LANGUAGES),
    }


def _build_prompt_from_messages(messages: List[ChatMessage]) -> str:
    """Построение промпта из истории сообщений"""
    prompt_parts = []

    for msg in messages:
        if msg.role == "user":
            prompt_parts.append(f"<|user|>\n{msg.content}")
        elif msg.role == "assistant":
            prompt_parts.append(f"<|assistant|>\n{msg.content}")

    # Добавляем маркер для нового ответа
    prompt_parts.append("<|assistant|>")

    return "\n".join(prompt_parts)
