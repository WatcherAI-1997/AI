#!/usr/bin/env python3
"""
TamerlanAI Test Client
Тестовый клиент для проверки API
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

import requests
import json
from typing import Dict, Any


API_URL = "http://localhost:8000"


def test_health():
    """Проверка здоровья сервера"""
    print("\n🏥 Testing health endpoint...")
    response = requests.get(f"{API_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_root():
    """Проверка корневого эндпоинта"""
    print("\n🏠 Testing root endpoint...")
    response = requests.get(f"{API_URL}/")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"App: {data['message']}")
    print(f"Version: {data['version']}")
    print(f"Status: {data['status']}")


def test_chat(message: str, language: str = "kk"):
    """Тест чата"""
    print(f"\n💬 Testing chat in {language}...")
    print(f"User: {message}")

    response = requests.post(
        f"{API_URL}/api/v1/chat/",
        json={
            "messages": [
                {"role": "user", "content": message}
            ],
            "language": language,
            "personality": "casual"
        }
    )

    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Assistant: {data['message']['content']}")
    print(f"Language: {data['language']}")
    print(f"Model: {data['model']}")


def test_translate():
    """Тест перевода"""
    print("\n🌍 Testing translation...")

    response = requests.post(
        f"{API_URL}/api/v1/translate/",
        json={
            "text": "Hello world",
            "source_lang": "en",
            "target_lang": "kk"
        }
    )

    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Translation: {data['translation']}")


def test_models():
    """Тест эндпоинта моделей"""
    print("\n🤖 Testing models endpoint...")

    response = requests.get(f"{API_URL}/api/v1/models/")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Available models: {data['models']}")


def test_languages():
    """Тест списка языков"""
    print("\n🌐 Testing languages endpoint...")

    response = requests.get(f"{API_URL}/api/v1/chat/languages")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Turkic languages: {len(data['turkic_languages'])}")
    print(f"Other languages: {len(data['other_languages'])}")
    print(f"Total: {data['total']}")


def main():
    """Главная функция"""
    print("="*80)
    print("🏹 TAMERLANAI - TEST CLIENT")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print(f"\nAPI URL: {API_URL}")
    print("\n" + "="*80)

    try:
        # Базовые проверки
        test_health()
        test_root()
        test_models()
        test_languages()

        # Тесты чата на разных языках
        test_chat("Сәлем! Қалайсың?", "kk")  # Казахский
        test_chat("Merhaba! Nasılsın?", "tr")  # Турецкий
        test_chat("Привет! Как дела?", "ru")  # Русский
        test_chat("Hello! How are you?", "en")  # Английский

        # Тест перевода
        test_translate()

        print("\n" + "="*80)
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("="*80)

    except requests.exceptions.ConnectionError:
        print("\n" + "="*80)
        print("❌ ОШИБКА: Не удается подключиться к серверу")
        print("="*80)
        print("\nУбедитесь что сервер запущен:")
        print("  cd TamerlanAI/backend")
        print("  python main_simple.py")
        print("\nИли запустите:")
        print("  ./start.sh")
        print("="*80)

    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")


if __name__ == "__main__":
    main()
