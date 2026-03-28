"""
TamerlanAI LLM Manager
Управление AI моделями и генерацией
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

import torch
from typing import Optional, Dict, List, Any
from dataclasses import dataclass
import logging

from config import get_settings, PERSONALITY_STYLES

logger = logging.getLogger(__name__)
settings = get_settings()


@dataclass
class GenerationConfig:
    """Конфигурация генерации"""
    max_tokens: int = 2048
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 50
    repetition_penalty: float = 1.1
    stop_sequences: List[str] = None


class TamerlanModel:
    """Обертка для собственной модели Tamerlane GPT"""

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    async def load(self):
        """Загрузка модели"""
        logger.info(f"Loading Tamerlane GPT from {self.model_path}")
        try:
            # Здесь будет загрузка нашей обученной модели
            # from model.architecture import TamerlaneGPT
            # from model.tokenizer import TamerlaneTokenizer

            # self.tokenizer = TamerlaneTokenizer()
            # self.tokenizer.load(f"{self.model_path}/tokenizer.json")

            # checkpoint = torch.load(f"{self.model_path}/best_model.pt", map_location=self.device)
            # self.model = TamerlaneGPT(...)
            # self.model.load_state_dict(checkpoint['model_state_dict'])
            # self.model.to(self.device)
            # self.model.eval()

            logger.info("✅ Tamerlane GPT loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load Tamerlane GPT: {e}")
            raise

    async def generate(self, prompt: str, config: GenerationConfig) -> str:
        """Генерация текста"""
        if self.model is None:
            raise RuntimeError("Model not loaded")

        # Токенизация
        # input_ids = self.tokenizer.encode(prompt)
        # input_tensor = torch.tensor([input_ids], dtype=torch.long).to(self.device)

        # Генерация
        # with torch.no_grad():
        #     output = self.model.generate(
        #         input_tensor,
        #         max_new_tokens=config.max_tokens,
        #         temperature=config.temperature,
        #         top_k=config.top_k
        #     )

        # return self.tokenizer.decode(output[0].tolist())

        # Заглушка для демо
        return f"[Tamerlane GPT Response to: {prompt}]"


class LLMManager:
    """
    Менеджер LLM моделей

    Управляет:
    - Загрузкой моделей
    - Переключением между моделями
    - Генерацией текста
    - Адаптивной личностью
    - Мультиязычностью
    """

    def __init__(self):
        self.models: Dict[str, Any] = {}
        self.current_model: Optional[str] = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        logger.info(f"🖥️  Device: {self.device}")
        if self.device == "cuda":
            logger.info(f"   GPU: {torch.cuda.get_device_name(0)}")

    async def initialize(self):
        """Инициализация менеджера"""
        logger.info("Initializing LLM Manager...")

        # Загрузка основной модели Tamerlane
        try:
            tamerlane_model = TamerlanModel(settings.MODEL_PATH)
            # await tamerlane_model.load()  # Раскомментировать когда модель готова
            self.models["tamerlane"] = tamerlane_model
            self.current_model = "tamerlane"
            logger.info("✅ Tamerlane model initialized")
        except Exception as e:
            logger.warning(f"Tamerlane model not available: {e}")

        # Можно добавить другие модели
        # await self._load_llama_model()
        # await self._load_external_models()

        logger.info(f"✅ LLM Manager initialized with {len(self.models)} models")

    async def cleanup(self):
        """Очистка ресурсов"""
        logger.info("Cleaning up LLM Manager...")
        self.models.clear()

    def get_available_models(self) -> List[str]:
        """Получить список доступных моделей"""
        return list(self.models.keys())

    def set_current_model(self, model_name: str):
        """Установить текущую модель"""
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not available")
        self.current_model = model_name
        logger.info(f"Switched to model: {model_name}")

    async def generate(
        self,
        prompt: str,
        model: Optional[str] = None,
        language: Optional[str] = None,
        personality: Optional[str] = None,
        task: str = "chat",
        config: Optional[GenerationConfig] = None,
    ) -> Dict[str, Any]:
        """
        Генерация ответа

        Args:
            prompt: Входной промпт
            model: Модель (если None, используется текущая)
            language: Язык ответа
            personality: Стиль личности
            task: Тип задачи
            config: Конфигурация генерации

        Returns:
            Dict с ответом и метаданными
        """
        # Выбор модели
        model_name = model or self.current_model
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not available")

        # Конфигурация по умолчанию
        if config is None:
            config = GenerationConfig(
                max_tokens=settings.MAX_TOKENS,
                temperature=settings.TEMPERATURE,
                top_p=settings.TOP_P,
                top_k=settings.TOP_K,
            )

        # Построение промпта с учетом языка и личности
        enhanced_prompt = self._build_prompt(prompt, language, personality, task)

        # Генерация
        start_time = torch.cuda.Event(enable_timing=True)
        end_time = torch.cuda.Event(enable_timing=True)

        start_time.record()
        response_text = await self.models[model_name].generate(enhanced_prompt, config)
        end_time.record()

        torch.cuda.synchronize()
        generation_time = start_time.elapsed_time(end_time) / 1000  # ms to seconds

        return {
            "response": response_text,
            "model": model_name,
            "language": language or "auto",
            "personality": personality or "formal",
            "task": task,
            "metadata": {
                "generation_time": generation_time,
                "tokens_generated": len(response_text.split()),  # Приблизительно
                "device": self.device,
            }
        }

    def _build_prompt(
        self,
        prompt: str,
        language: Optional[str],
        personality: Optional[str],
        task: str
    ) -> str:
        """Построение промпта с учетом контекста"""
        system_instructions = []

        # Языковая инструкция
        if language:
            if language in settings.TURKIC_LANGUAGES:
                system_instructions.append(
                    f"Ответь на {self._get_language_name(language)} языке. "
                    "Используй аутентичный тюркский стиль общения."
                )
            else:
                system_instructions.append(
                    f"Respond in {self._get_language_name(language)} language."
                )

        # Личность
        if personality and personality in PERSONALITY_STYLES:
            system_instructions.append(
                f"Стиль общения: {PERSONALITY_STYLES[personality]}"
            )

        # Тип задачи
        task_instructions = {
            "chat": "Веди естественный диалог, будь полезным и дружелюбным.",
            "translate": "Выполни точный перевод, сохраняя смысл и стиль.",
            "summarize": "Создай краткое резюме, выделяя ключевые моменты.",
            "code_generation": "Генерируй чистый, хорошо документированный код.",
            "text_analysis": "Проанализируй текст детально и структурированно.",
            "question_answering": "Дай точный и полный ответ на вопрос.",
        }

        if task in task_instructions:
            system_instructions.append(task_instructions[task])

        # Построение финального промпта
        if system_instructions:
            return (
                "<|system|>\n"
                + "\n".join(system_instructions)
                + "\n<|user|>\n"
                + prompt
                + "\n<|assistant|>\n"
            )
        else:
            return prompt

    def _get_language_name(self, code: str) -> str:
        """Получить название языка по коду"""
        language_names = {
            "tr": "турецкий",
            "az": "азербайджанский",
            "uz": "узбекский",
            "kk": "казахский",
            "ky": "киргизский",
            "tt": "татарский",
            "ba": "башкирский",
            "ru": "русский",
            "en": "English",
            "ar": "Arabic",
            "zh": "Chinese",
            "ja": "Japanese",
            "ko": "Korean",
        }
        return language_names.get(code, code)

    async def detect_language(self, text: str) -> str:
        """Определение языка текста"""
        # Простая эвристика (можно улучшить с помощью langdetect или модели)
        turkic_chars = set("ğçşıöüĞÇŞİÖÜәіңүқҳӘІҢҮҚҲ")
        russian_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        arabic_chars = set("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")

        text_lower = text.lower()
        has_turkic = any(c in turkic_chars for c in text_lower)
        has_russian = any(c in russian_chars for c in text_lower)
        has_arabic = any(c in arabic_chars for c in text_lower)

        if has_turkic:
            # Определяем конкретный тюркский язык
            if "ә" in text_lower or "ң" in text_lower:
                return "kk"  # Казахский
            elif "ğ" in text_lower or "ş" in text_lower:
                return "tr"  # Турецкий
            return "tr"  # По умолчанию турецкий
        elif has_russian:
            return "ru"
        elif has_arabic:
            return "ar"
        else:
            return "en"  # По умолчанию английский

    def get_model_info(self, model_name: Optional[str] = None) -> Dict[str, Any]:
        """Получить информацию о модели"""
        model_name = model_name or self.current_model

        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not available")

        return {
            "name": model_name,
            "type": "transformer",
            "device": self.device,
            "status": "loaded",
            "capabilities": {
                "text_generation": True,
                "translation": True,
                "code_generation": True,
                "analysis": True,
            }
        }
