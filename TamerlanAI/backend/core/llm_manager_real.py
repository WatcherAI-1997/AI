"""
TamerlanAI LLM Manager - НАСТОЯЩАЯ ВЕРСИЯ
Использует обученную модель TamerlaneGPT
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

import torch
import torch.nn.functional as F
from typing import Optional, Dict, List, Any
from dataclasses import dataclass
import logging
import time
import os

from model.architecture import TamerlaneGPT, create_small_model
from model.simple_tokenizer import SimpleTokenizer
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


class RealLLMManager:
    """
    НАСТОЯЩИЙ менеджер LLM с использованием TamerlaneGPT

    Использует:
    - Обученную трансформер модель
    - BPE токенизатор для тюркских языков
    - Авторегрессивную генерацию
    - Без хардкода и заглушек
    """

    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.current_model_name = "tamerlane-gpt"
        self.model_path = settings.MODEL_PATH if hasattr(settings, 'MODEL_PATH') else "checkpoints"

        logger.info(f"🖥️  Device: {self.device}")
        if self.device == "cuda":
            logger.info(f"   GPU: {torch.cuda.get_device_name(0)}")

    async def initialize(self):
        """Инициализация и загрузка модели"""
        logger.info("🏹 Initializing REAL LLM Manager with TamerlaneGPT...")

        try:
            # Инициализация токенизатора
            self.tokenizer = SimpleTokenizer()

            # Попытка загрузить обученный токенизатор
            tokenizer_path = os.path.join(self.model_path, "tokenizer.json")
            if os.path.exists(tokenizer_path):
                logger.info(f"Loading tokenizer from {tokenizer_path}")
                self.tokenizer.load(tokenizer_path)
            else:
                # Создаем новый токенизатор на демо данных
                logger.warning("No trained tokenizer found, creating new one with demo data...")
                self.tokenizer = SimpleTokenizer(vocab_size=5000)
                demo_texts = self._get_demo_training_data()
                self.tokenizer.train(demo_texts, verbose=True)

                # Сохраняем
                os.makedirs(self.model_path, exist_ok=True)
                self.tokenizer.save(tokenizer_path)
                logger.info(f"✅ Tokenizer created and saved to {tokenizer_path}")

            vocab_size = len(self.tokenizer.vocab)
            logger.info(f"Vocabulary size: {vocab_size}")

            # Загрузка или создание модели
            model_checkpoint = os.path.join(self.model_path, "best_model.pt")

            if os.path.exists(model_checkpoint):
                logger.info(f"Loading model from {model_checkpoint}")
                checkpoint = torch.load(model_checkpoint, map_location=self.device)

                # Восстанавливаем модель
                self.model = create_small_model(vocab_size)
                self.model.load_state_dict(checkpoint['model_state_dict'])
                self.model.to(self.device)
                self.model.eval()

                logger.info(f"✅ Model loaded from checkpoint (epoch {checkpoint.get('epoch', 'unknown')})")
            else:
                logger.warning("No trained model found, creating new untrained model...")
                logger.warning("⚠️  Model will generate random text until trained!")

                # Создаем новую модель
                self.model = create_small_model(vocab_size)
                self.model.to(self.device)
                self.model.eval()

                logger.info("✅ New model created (UNTRAINED - needs training!)")

            # Информация о модели
            model_info = self.model.get_model_info()
            logger.info(f"📊 Model: {model_info['parameters_millions']} parameters")
            logger.info("✅ REAL LLM Manager initialized successfully!")

        except Exception as e:
            logger.error(f"Failed to initialize LLM Manager: {e}", exc_info=True)
            raise

    async def cleanup(self):
        """Очистка ресурсов"""
        logger.info("Cleaning up LLM Manager...")
        if self.model:
            del self.model
        if self.tokenizer:
            del self.tokenizer
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    def get_available_models(self) -> List[str]:
        """Список доступных моделей"""
        return [self.current_model_name]

    def set_current_model(self, model_name: str):
        """Установить текущую модель"""
        if model_name != self.current_model_name:
            raise ValueError(f"Model {model_name} not available")
        logger.info(f"Model: {model_name}")

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
        Генерация ответа с помощью TamerlaneGPT

        Использует авторегрессивную генерацию через модель
        """
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model not initialized")

        start_time = time.time()

        # Конфигурация по умолчанию
        if config is None:
            config = GenerationConfig()

        # Автоопределение языка
        detected_lang = language or await self.detect_language(prompt)

        # Построение промпта с инструкциями
        enhanced_prompt = self._build_prompt(prompt, detected_lang, personality, task)

        logger.info(f"Generating response for prompt: {enhanced_prompt[:100]}...")

        # Токенизация
        try:
            input_ids = self.tokenizer.encode(enhanced_prompt)
            if not input_ids:
                # Fallback если токенизация не удалась
                input_ids = [0]  # BOS token

            input_tensor = torch.tensor([input_ids], dtype=torch.long).to(self.device)

            # Генерация
            with torch.no_grad():
                output_ids = self.model.generate(
                    input_tensor,
                    max_new_tokens=min(config.max_tokens, 256),  # Ограничиваем для скорости
                    temperature=config.temperature,
                    top_k=config.top_k
                )

            # Декодирование
            generated_ids = output_ids[0].tolist()
            response = self.tokenizer.decode(generated_ids)

            # Очистка ответа (убираем промпт)
            if enhanced_prompt in response:
                response = response.replace(enhanced_prompt, "").strip()

            # Если модель не обучена, добавляем предупреждение
            if not os.path.exists(os.path.join(self.model_path, "best_model.pt")):
                response = f"⚠️  [Model UNTRAINED - Random output]\n\n{response}\n\n💡 Train the model using: python train.py"

        except Exception as e:
            logger.error(f"Generation error: {e}", exc_info=True)
            response = f"[Generation error: {str(e)}]"

        generation_time = time.time() - start_time

        return {
            "response": response,
            "model": model or self.current_model_name,
            "language": detected_lang,
            "personality": personality or "formal",
            "task": task,
            "metadata": {
                "generation_time": generation_time,
                "tokens_generated": len(response.split()),
                "device": self.device,
                "vocab_size": len(self.tokenizer.vocab) if self.tokenizer else 0,
            }
        }

    def _build_prompt(
        self,
        prompt: str,
        language: str,
        personality: Optional[str],
        task: str
    ) -> str:
        """Построение промпта с системными инструкциями"""

        system_parts = []

        # Языковые инструкции
        lang_instructions = {
            "kk": "Жауапты қазақ тілінде бер. Тюрк стилін қолдан.",
            "tr": "Türkçe cevap ver. Türk tarzını kullan.",
            "ru": "Отвечай на русском языке.",
            "en": "Answer in English.",
        }

        if language in lang_instructions:
            system_parts.append(lang_instructions[language])

        # Личность
        if personality and personality in PERSONALITY_STYLES:
            system_parts.append(PERSONALITY_STYLES[personality])

        # Формируем промпт
        if system_parts:
            return f"<|system|> {' '.join(system_parts)}\n<|user|> {prompt}\n<|assistant|>"
        else:
            return f"<|user|> {prompt}\n<|assistant|>"

    async def detect_language(self, text: str) -> str:
        """Определение языка текста"""
        # Тюркские символы
        kk_chars = set("ғәіңөүұқҳ")
        tr_chars = set("ğçşıöü")
        ru_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

        text_lower = text.lower()
        text_set = set(text_lower)

        # Проверка казахского
        if text_set & kk_chars:
            return "kk"

        # Проверка турецкого
        if text_set & tr_chars:
            return "tr"

        # Проверка русского
        if text_set & ru_chars:
            return "ru"

        # По умолчанию английский
        return "en"

    def get_model_info(self, model_name: Optional[str] = None) -> Dict[str, Any]:
        """Информация о модели"""
        if self.model:
            info = self.model.get_model_info()
            info["device"] = self.device
            info["status"] = "loaded"
            info["trained"] = os.path.exists(os.path.join(self.model_path, "best_model.pt"))
            return info
        else:
            return {"error": "Model not loaded"}

    def _get_demo_training_data(self) -> List[str]:
        """Демо-данные для обучения токенизатора"""
        return [
            # Казахский
            "Сәлеметсіз бе! Мен TamerlanAI - тюрк халықтары үшін жасалған жасанды интеллект.",
            "Қазақстан - Орталық Азиядағы ең үлкен мемлекет.",
            "Тәуелсіздік - ең қымбат қазына.",
            "Білім - жарық, надандық - қараңғылық.",

            # Турецкий
            "Merhaba! Ben TamerlanAI - Türk halkları için yapay zeka.",
            "Türkiye Cumhuriyeti Anadolu'da kurulmuş bir devlettir.",
            "Bilim ışıktır, cehalet karanlıktır.",

            # Русский
            "Здравствуйте! Я TamerlanAI - искусственный интеллект для тюркских народов.",
            "Знание - свет, невежество - тьма.",
            "Дружба народов - основа мира.",

            # Английский
            "Hello! I am TamerlanAI - AI for Turkic peoples.",
            "Knowledge is power.",
            "Unity in diversity.",

            # Смешанный контент
            "TamerlanAI поддерживает 14 тюркских языков.",
            "Tamerlane (Тимур) был великим правителем.",
            "Тюркский мир един в своем многообразии.",
        ]
