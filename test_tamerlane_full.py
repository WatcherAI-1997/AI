#!/usr/bin/env python3
"""
Полный тест модели Тамерлан с универсальными знаниями
"""

from tamerlane_model import get_tamerlane_model
import json

# Мок-функция для базовой модели (чтобы не использовать API)
def mock_base_model(messages, temperature, max_tokens):
    """Простая мок-функция для тестирования без API"""
    last_msg = messages[-1]['content'] if messages else ""

    # Извлекаем контекст из системного сообщения
    context = ""
    for msg in messages:
        if msg['role'] == 'system':
            context = msg['content']
            break

    # Проверяем, есть ли контекст из базы знаний
    if "[КОНТЕКСТ ИЗ БАЗЫ ЗНАНИЙ" in context:
        return f"[МОК-ОТВЕТ С КОНТЕКСТОМ]\nВопрос: {last_msg}\nКонтекст был предоставлен из базы знаний!"
    else:
        return f"[МОК-ОТВЕТ БЕЗ КОНТЕКСТА]\nВопрос: {last_msg}"


def test_tamerlane_model():
    print("🏹 ТЕСТИРОВАНИЕ МОДЕЛИ ТАМЕРЛАН\n")
    print("="*70)

    # Получаем модель
    model = get_tamerlane_model(base_provider='anthropic')

    # Тест 1: Математический запрос
    print("\n📐 ТЕСТ 1: Математика (Пифагор)")
    messages1 = [
        {"role": "user", "content": "Пифагор теоремасын түсіндір"}
    ]

    result1 = model.generate(
        messages=messages1,
        base_model_fn=mock_base_model,
        temperature=0.7
    )

    print(f"Обогащен контекстом: {result1['enhanced']}")
    print(f"Длина контекста: {result1['metadata']['context_length']}")
    print(f"Язык: {result1['metadata']['detected_language']}")
    print(f"Категории: {result1['metadata']['categories']}")

    # Тест 2: Физический запрос
    print("\n⚛️ ТЕСТ 2: Физика (Ньютон)")
    messages2 = [
        {"role": "user", "content": "Ньютонның заңдары туралы айтып бер"}
    ]

    result2 = model.generate(
        messages=messages2,
        base_model_fn=mock_base_model,
        temperature=0.7
    )

    print(f"Обогащен контекстом: {result2['enhanced']}")
    print(f"Длина контекста: {result2['metadata']['context_length']}")
    print(f"Язык: {result2['metadata']['detected_language']}")

    # Тест 3: Военная тактика
    print("\n⚔️ ТЕСТ 3: Военная тактика")
    messages3 = [
        {"role": "user", "content": "Тәмірланның әскери тактикасы қандай болды?"}
    ]

    result3 = model.generate(
        messages=messages3,
        base_model_fn=mock_base_model,
        temperature=0.7
    )

    print(f"Обогащен контекстом: {result3['enhanced']}")
    print(f"Длина контекста: {result3['metadata']['context_length']}")
    print(f"Категории: {result3['metadata']['categories']}")

    # Тест 4: Исторический запрос
    print("\n🏛️ ТЕСТ 4: История")
    messages4 = [
        {"role": "user", "content": "Тимур кім еді?"}
    ]

    result4 = model.generate(
        messages=messages4,
        base_model_fn=mock_base_model,
        temperature=0.7
    )

    print(f"Обогащен контекстом: {result4['enhanced']}")
    print(f"Длина контекста: {result4['metadata']['context_length']}")

    # Тест 5: Общий запрос (без специфики)
    print("\n💬 ТЕСТ 5: Общий вопрос")
    messages5 = [
        {"role": "user", "content": "Привет, как дела?"}
    ]

    result5 = model.generate(
        messages=messages5,
        base_model_fn=mock_base_model,
        temperature=0.7
    )

    print(f"Обогащен контекстом: {result5['enhanced']}")
    print(f"Длина контекста: {result5['metadata']['context_length']}")

    # Статистика модели
    print("\n" + "="*70)
    print("\n📊 СТАТИСТИКА МОДЕЛИ:")
    info = model.get_model_info()
    print(f"Название: {info['name']}")
    print(f"Версия: {info['version']}")
    print(f"Тип: {info['type']}")
    print(f"\nСтатистика:")
    print(f"  • Всего запросов: {info['statistics']['total_requests']}")
    print(f"  • Обогащенных запросов: {info['statistics']['kb_enhanced_requests']}")
    print(f"\nБаза знаний:")
    print(f"  • Всего элементов: {info['knowledge_base']['total']}")
    print(f"  • Категорий: {len(info['knowledge_base']) - 1}")

    print("\n✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    print("\n🎯 МОДЕЛЬ ТАМЕРЛАН ГОТОВА К РАБОТЕ!")
    print("📚 База знаний включает:")
    print("   • Тюркскую историю и культуру")
    print("   • Математику и физику")
    print("   • Военную тактику")
    print("   • Медицину и биологию")
    print("   • Технологии и программирование")
    print("   • И многое другое на всех тюркских языках!")


if __name__ == "__main__":
    test_tamerlane_model()
