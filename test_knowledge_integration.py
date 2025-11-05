#!/usr/bin/env python3
"""
Тест интеграции универсальных знаний
"""

from turkic_knowledge_base import get_knowledge_base

def test_knowledge_integration():
    print("🧪 Тестирование интеграции универсальных знаний...\n")

    # Получаем базу знаний
    kb = get_knowledge_base()

    # Статистика
    stats = kb.get_stats()

    print("📊 СТАТИСТИКА БАЗЫ ЗНАНИЙ:")
    print(f"Всего категорий: {len(stats) - 1}")
    print(f"Всего элементов: {stats['total']}\n")

    print("📚 КАТЕГОРИИ:")
    for category, count in sorted(stats.items()):
        if category != 'total':
            print(f"  • {category}: {count} элементов")

    print("\n" + "="*60)

    # Тестируем поиск по математике
    print("\n🔍 ТЕСТ ПОИСКА: Пифагор теоремасы")
    results = kb.search("Пифагор", limit=2)
    print(f"Найдено результатов: {len(results)}")
    if results:
        print(f"Релевантность: {results[0]['relevance']}")
        print(f"Категория: {results[0]['category']}")

    # Тестируем поиск по военной тактике
    print("\n🔍 ТЕСТ ПОИСКА: Тәмірланның әскери тактикасы")
    results = kb.search("военная тактика Тимур", limit=2)
    print(f"Найдено результатов: {len(results)}")
    if results:
        print(f"Релевантность: {results[0]['relevance']}")
        print(f"Категория: {results[0]['category']}")

    # Тестируем поиск по физике
    print("\n🔍 ТЕСТ ПОИСКА: Ньютон заңдары")
    results = kb.search("Ньютон физика", limit=2)
    print(f"Найдено результатов: {len(results)}")
    if results:
        print(f"Релевантность: {results[0]['relevance']}")
        print(f"Категория: {results[0]['category']}")

    print("\n✅ Тестирование завершено!")

if __name__ == "__main__":
    test_knowledge_integration()
