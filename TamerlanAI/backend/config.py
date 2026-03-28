"""
TamerlanAI Backend Configuration
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

from pydantic_settings import BaseSettings
from typing import List, Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Настройки приложения"""

    # Application
    APP_NAME: str = "TamerlanAI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 4

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://tamerlan:tamerlan@localhost:5432/tamerlanai"
    DB_ECHO: bool = False

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_TTL: int = 3600  # 1 hour

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"

    # AI Models
    DEFAULT_MODEL: str = "tamerlane-gpt"
    MODEL_PATH: str = "./models"
    TOKENIZER_PATH: str = "./models/tokenizer"

    # Supported Languages
    TURKIC_LANGUAGES: List[str] = [
        "tr",  # Turkish
        "az",  # Azerbaijani
        "uz",  # Uzbek
        "kk",  # Kazakh
        "ky",  # Kyrgyz
        "tt",  # Tatar
        "ba",  # Bashkir
        "sah", # Yakut/Sakha
        "tk",  # Turkmen
        "cv",  # Chuvash
        "krc", # Karachay
        "gag", # Gagauz
        "ug",  # Uyghur
        "tyv", # Tuvan
    ]

    OTHER_LANGUAGES: List[str] = [
        "ru",  # Russian
        "en",  # English
        "ar",  # Arabic
        "zh",  # Chinese
        "ja",  # Japanese
        "ko",  # Korean
        "fr",  # French
        "de",  # German
        "es",  # Spanish
    ]

    # LLM Settings
    MAX_TOKENS: int = 2048
    TEMPERATURE: float = 0.7
    TOP_P: float = 0.9
    TOP_K: int = 50

    # RAG Settings
    VECTOR_STORE_TYPE: str = "chroma"  # "chroma" или "faiss"
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50
    TOP_K_RESULTS: int = 5

    # External APIs (optional)
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None

    # Telegram Bot
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    TELEGRAM_WEBHOOK_URL: Optional[str] = None

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # File Upload
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10 MB
    ALLOWED_EXTENSIONS: List[str] = [".txt", ".pdf", ".docx", ".md"]

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "./logs/tamerlanai.log"

    # Training
    TRAINING_DATA_DIR: str = "./training/datasets"
    CHECKPOINT_DIR: str = "./training/checkpoints"
    MAX_TRAINING_EPOCHS: int = 100

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Получить настройки (кэшируется)"""
    return Settings()


# Константы
PERSONALITY_STYLES = {
    "formal": "Официальный, строгий стиль общения",
    "academic": "Академический, научный стиль",
    "casual": "Неформальный, повседневный стиль",
    "business": "Деловой, профессиональный стиль",
    "folk": "Народный, традиционный стиль",
    "poetic": "Поэтический, художественный стиль",
    "religious": "Религиозный, духовный стиль",
    "philosophical": "Философский, размышляющий стиль",
}

SUPPORTED_TASKS = [
    "chat",              # Обычный чат
    "translate",         # Перевод
    "summarize",         # Суммаризация
    "code_generation",   # Генерация кода
    "text_analysis",     # Анализ текста
    "question_answering",# Ответы на вопросы
    "classification",    # Классификация
    "sentiment",         # Анализ тональности
]
