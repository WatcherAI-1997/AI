"""
AI Providers Module для Тамерлан ИИ
Поддержка множественных AI провайдеров
"""

import os
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import anthropic
import google.generativeai as genai
import requests


class AIProvider(ABC):
    """Абстрактный базовый класс для AI провайдеров"""

    @abstractmethod
    def generate_response(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        """Генерация ответа от AI модели"""
        pass

    @abstractmethod
    def is_configured(self) -> bool:
        """Проверка наличия конфигурации"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Получение имени провайдера"""
        pass


class AnthropicProvider(AIProvider):
    """
    Anthropic Claude - САМАЯ УМНАЯ модель!
    Claude 3.5 Sonnet - лучшая модель для сложных задач
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY', '')
        self.model = model
        self.client = None
        if self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_response(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 4000) -> str:
        if not self.is_configured():
            raise ValueError("Anthropic API key не настроен")

        # Извлекаем системный промпт
        system_message = ""
        chat_messages = []

        for msg in messages:
            if msg['role'] == 'system':
                system_message = msg['content']
            else:
                chat_messages.append({
                    "role": msg['role'],
                    "content": msg['content']
                })

        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_message,
            messages=chat_messages
        )

        return response.content[0].text

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def get_name(self) -> str:
        return f"Anthropic Claude ({self.model})"


class GeminiProvider(AIProvider):
    """
    Google Gemini - мощная бесплатная альтернатива
    Gemini Pro - отличная модель от Google
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-pro"):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY', '')
        self.model = model
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.client = genai.GenerativeModel(model)
        else:
            self.client = None

    def generate_response(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        if not self.is_configured():
            raise ValueError("Gemini API key не настроен")

        # Конвертируем формат сообщений для Gemini
        system_prompt = ""
        chat_history = []

        for msg in messages:
            if msg['role'] == 'system':
                system_prompt = msg['content']
            elif msg['role'] == 'user':
                chat_history.append({"role": "user", "parts": [msg['content']]})
            elif msg['role'] == 'assistant':
                chat_history.append({"role": "model", "parts": [msg['content']]})

        # Добавляем системный промпт к первому сообщению пользователя
        if chat_history and system_prompt:
            chat_history[0]['parts'][0] = f"{system_prompt}\n\n{chat_history[0]['parts'][0]}"

        # Создаем чат
        chat = self.client.start_chat(history=chat_history[:-1] if len(chat_history) > 1 else [])

        # Отправляем последнее сообщение
        last_message = chat_history[-1]['parts'][0] if chat_history else ""

        generation_config = genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )

        response = chat.send_message(last_message, generation_config=generation_config)
        return response.text

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def get_name(self) -> str:
        return f"Google Gemini ({self.model})"


class OllamaProvider(AIProvider):
    """
    Ollama - локальные open-source модели
    Запускается на вашем компьютере, полностью бесплатно!
    """

    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.1"):
        self.base_url = base_url
        self.model = model

    def generate_response(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        if not self.is_configured():
            raise ValueError("Ollama не запущен или недоступен")

        # Формируем prompt для Ollama
        prompt = self._format_messages(messages)

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "temperature": temperature,
                "stream": False,
                "options": {
                    "num_predict": max_tokens
                }
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json()['response']
        else:
            raise Exception(f"Ollama error: {response.text}")

    def _format_messages(self, messages: List[Dict]) -> str:
        """Форматирование сообщений в единый промпт"""
        formatted = []
        for msg in messages:
            role = msg['role']
            content = msg['content']
            if role == 'system':
                formatted.append(f"System: {content}")
            elif role == 'user':
                formatted.append(f"User: {content}")
            elif role == 'assistant':
                formatted.append(f"Assistant: {content}")

        formatted.append("Assistant:")
        return "\n\n".join(formatted)

    def is_configured(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False

    def get_name(self) -> str:
        return f"Ollama Local ({self.model})"


class OpenAIProvider(AIProvider):
    """
    OpenAI GPT - оригинальный провайдер (опционально)
    Оставлен для совместимости
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY', '')
        self.model = model
        if self.api_key:
            import openai
            openai.api_key = self.api_key
            self.client = openai
        else:
            self.client = None

    def generate_response(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        if not self.is_configured():
            raise ValueError("OpenAI API key не настроен")

        response = self.client.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def get_name(self) -> str:
        return f"OpenAI ({self.model})"


class AIProviderFactory:
    """Фабрика для создания AI провайдеров"""

    @staticmethod
    def create_provider(provider_name: str, model: Optional[str] = None) -> AIProvider:
        """
        Создание провайдера по имени

        Поддерживаемые провайдеры:
        - anthropic: Claude 3.5 Sonnet (САМЫЙ УМНЫЙ!)
        - gemini: Google Gemini Pro
        - ollama: Локальные модели
        - openai: OpenAI GPT (опционально)
        """
        providers = {
            'anthropic': AnthropicProvider,
            'gemini': GeminiProvider,
            'ollama': OllamaProvider,
            'openai': OpenAIProvider,
        }

        if provider_name not in providers:
            raise ValueError(f"Неизвестный провайдер: {provider_name}")

        if model:
            return providers[provider_name](model=model)
        else:
            return providers[provider_name]()

    @staticmethod
    def get_available_providers() -> Dict[str, Dict]:
        """Получение списка доступных провайдеров с их статусом"""
        providers_info = {}

        # Anthropic Claude
        anthropic_provider = AnthropicProvider()
        providers_info['anthropic'] = {
            'name': 'Anthropic Claude 3.5 Sonnet',
            'configured': anthropic_provider.is_configured(),
            'description': '🏆 САМАЯ УМНАЯ модель! Лучшая для сложных задач',
            'models': ['claude-3-5-sonnet-20241022', 'claude-3-opus-20240229', 'claude-3-sonnet-20240229'],
            'free': False
        }

        # Google Gemini
        gemini_provider = GeminiProvider()
        providers_info['gemini'] = {
            'name': 'Google Gemini Pro',
            'configured': gemini_provider.is_configured(),
            'description': '⚡ Мощная бесплатная альтернатива от Google',
            'models': ['gemini-pro', 'gemini-1.5-pro', 'gemini-1.5-flash'],
            'free': True
        }

        # Ollama
        ollama_provider = OllamaProvider()
        providers_info['ollama'] = {
            'name': 'Ollama (Локальные модели)',
            'configured': ollama_provider.is_configured(),
            'description': '💻 100% бесплатно, работает на вашем ПК',
            'models': ['llama3.1', 'mistral', 'codellama', 'gemma2'],
            'free': True
        }

        # OpenAI (опционально)
        openai_provider = OpenAIProvider()
        providers_info['openai'] = {
            'name': 'OpenAI GPT',
            'configured': openai_provider.is_configured(),
            'description': '🔷 Оригинальный ChatGPT (опционально)',
            'models': ['gpt-4', 'gpt-4-turbo-preview', 'gpt-3.5-turbo'],
            'free': False
        }

        return providers_info
