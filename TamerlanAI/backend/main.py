"""
TamerlanAI Backend Main Application
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
import time

from config import get_settings
from api.v1.router import api_router
from core.llm_manager_real import RealLLMManager
# from db.database import init_db  # Пока отключено для упрощения

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
    logger.info("🏹 Starting TamerlanAI...")

    # Инициализация БД (отключено для упрощения)
    # logger.info("📦 Initializing database...")
    # await init_db()

    # Инициализация НАСТОЯЩЕГО LLM с TamerlaneGPT
    logger.info("🤖 Loading TamerlaneGPT model...")
    app.state.llm_manager = RealLLMManager()
    await app.state.llm_manager.initialize()

    logger.info("✅ TamerlanAI started successfully!")

    yield

    # Shutdown
    logger.info("🛑 Shutting down TamerlanAI...")
    if hasattr(app.state, 'llm_manager'):
        await app.state.llm_manager.cleanup()
    logger.info("👋 Goodbye!")


# Создание приложения
app = FastAPI(
    title=settings.APP_NAME,
    description="Universal Multilingual AI System with focus on Turkic languages",
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip Middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)


# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if settings.DEBUG else "An error occurred"
        }
    )


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "🏹 TamerlanAI API",
        "version": settings.APP_VERSION,
        "status": "running",
        "docs": "/docs",
        "turkic_languages": len(settings.TURKIC_LANGUAGES),
        "total_languages": len(settings.TURKIC_LANGUAGES) + len(settings.OTHER_LANGUAGES),
    }


# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }


# Include routers
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
