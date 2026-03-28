"""
Тестирование НАСТОЯЩЕЙ модели TamerlanAI
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

import requests
import json

API_URL = "http://localhost:8000"


def test_chat(message: str, language: str):
    """Тест чата"""
    print(f"\n{'='*60}")
    print(f"Language: {language}")
    print(f"User: {message}")
    print("-" * 60)

    response = requests.post(
        f"{API_URL}/api/v1/chat/",
        json={
            "messages": [{"role": "user", "content": message}],
            "language": language,
            "temperature": 0.8,
            "max_tokens": 100
        }
    )

    if response.status_code == 200:
        data = response.json()
        print(f"Assistant: {data['message']['content']}")
        print(f"Model: {data['model']}")
        print(f"Generation time: {data['metadata']['generation_time']:.2f}s")
        print(f"Tokens: {data['metadata']['tokens_generated']}")
        print(f"Device: {data['metadata']['device']}")
    else:
        print(f"ERROR {response.status_code}: {response.text}")


def test_model_info():
    """Тест информации о модели"""
    print(f"\n{'='*60}")
    print("MODEL INFO")
    print("=" * 60)

    response = requests.get(f"{API_URL}/api/v1/models/")
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    print("="*60)
    print("🏹 TESTING TAMERLANAI - REAL MODEL")
    print("="*60)
    print("Автор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print()

    # Проверка здоровья
    response = requests.get(f"{API_URL}/health")
    if response.status_code == 200:
        print("✅ Server is healthy")
    else:
        print("❌ Server is not responding")
        return

    # Тесты на разных языках
    test_chat("Сәлем! TamerlanAI туралы айтып бер", "kk")
    test_chat("Merhaba! Kendini tanıt", "tr")
    test_chat("Привет! Расскажи о себе", "ru")
    test_chat("Hello! Tell me about yourself", "en")

    # Информация о модели
    test_model_info()

    print("\n" + "="*60)
    print("✅ TESTING COMPLETED")
    print("="*60)


if __name__ == "__main__":
    main()
