"""
TamerlanAI Backend - Simplified Version
Упрощенная версия для быстрого запуска и тестирования
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging

from config import get_settings
from api.v1.router import api_router
from core.llm_manager_simple import SimpleLLMManager

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle events"""
    # Startup
    logger.info("🏹 Starting TamerlanAI (Simple Mode)...")

    # Инициализация LLM (упрощенная версия)
    logger.info("🤖 Initializing LLM Manager (demo mode)...")
    app.state.llm_manager = SimpleLLMManager()
    await app.state.llm_manager.initialize()

    logger.info("✅ TamerlanAI started successfully!")
    logger.info("📖 API Docs: http://localhost:8000/docs")

    yield

    # Shutdown
    logger.info("🛑 Shutting down TamerlanAI...")
    if hasattr(app.state, 'llm_manager'):
        await app.state.llm_manager.cleanup()
    logger.info("👋 Goodbye!")


# Создание приложения
app = FastAPI(
    title="TamerlanAI",
    description="Universal Multilingual AI System (Simple Demo Mode)",
    version="1.0.0-demo",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретные origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "🏹 TamerlanAI API",
        "version": "1.0.0-demo",
        "status": "running",
        "mode": "simplified demo",
        "docs": "/docs",
        "supported_languages": {
            "turkic": ["tr", "az", "uz", "kk", "ky", "tt", "ba", "sah", "tk", "cv", "krc", "gag", "ug", "tyv"],
            "other": ["ru", "en", "ar", "zh", "ja", "ko", "fr", "de", "es"]
        },
        "features": [
            "Multilingual chat",
            "Translation",
            "Text analysis",
            "Adaptive personality",
            "Auto language detection"
        ]
    }


# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": "TamerlanAI",
        "mode": "demo"
    }


# Include API routes
app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    print("\n" + "="*80)
    print("🏹 TAMERLANAI - UNIVERSAL MULTILINGUAL AI SYSTEM")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print("\n📊 Режим: Упрощенная демо-версия")
    print("🌍 Языки: 14 тюркских + 9 других")
    print("🎭 Стили: 8 адаптивных личностей")
    print("\n🚀 Запуск сервера...")
    print("📖 Документация: http://localhost:8000/docs")
    print("="*80 + "\n")

    uvicorn.run(
        "main_simple:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
