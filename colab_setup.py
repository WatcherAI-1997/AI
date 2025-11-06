#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏹 Tamerlane AI - Скрипт установки для Google Colab
Автоматическая установка и настройка модели

Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
Проект: Tamerlane AI - Полноценная тюркская LLM модель
"""

import os
import sys

def print_banner():
    """Красивый баннер"""
    print("\n" + "="*80)
    print("🏹 TAMERLANE AI - УСТАНОВКА ДЛЯ GOOGLE COLAB")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print("⚠️  ЭТО ПОЛНОЦЕННАЯ LLM МОДЕЛЬ, НЕ ОБЕРТКА!")
    print("="*80 + "\n")

def check_environment():
    """Проверка окружения"""
    print("📋 Проверка окружения...")

    # Проверка Python версии
    python_version = sys.version_info
    print(f"   ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")

    # Проверка что это Colab
    try:
        import google.colab
        print("   ✅ Google Colab обнаружен")
        return True
    except:
        print("   ℹ️  Не Google Colab (локальная установка)")
        return False

def install_dependencies():
    """Установка зависимостей"""
    print("\n📦 Установка зависимостей...")

    # Минимальные зависимости (anthropic и google-generativeai опциональны)
    packages = []

    # Проверим, какие пакеты уже установлены
    try:
        import anthropic
        print("   ✅ anthropic уже установлен")
    except:
        packages.append("anthropic")

    try:
        import google.generativeai
        print("   ✅ google-generativeai уже установлен")
    except:
        packages.append("google-generativeai")

    if packages:
        print(f"   📥 Устанавливаю: {', '.join(packages)}")
        os.system(f"pip install -q {' '.join(packages)}")
        print("   ✅ Зависимости установлены")
    else:
        print("   ✅ Все зависимости уже установлены")

def check_files():
    """Проверка наличия файлов"""
    print("\n📂 Проверка файлов модели...")

    required_files = [
        'tamerlane_model.py',
        'turkic_knowledge_base.py',
        'universal_knowledge.py',
        'advanced_knowledge.py',
        'world_languages.py',
        'ancient_languages.py',
        'tengri_knowledge.py'
    ]

    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            size = os.path.getsize(file) / 1024  # KB
            print(f"   ✅ {file:30} ({size:.1f} KB)")
        else:
            print(f"   ❌ {file:30} ОТСУТСТВУЕТ!")
            missing_files.append(file)

    if missing_files:
        print(f"\n   ⚠️  Отсутствует {len(missing_files)} файлов!")
        print(f"   📥 Загрузите файлы:")
        for f in missing_files:
            print(f"      • {f}")
        return False

    print("   ✅ Все файлы на месте!")
    return True

def test_model():
    """Тест модели"""
    print("\n🧪 Тестирование модели...")

    try:
        from tamerlane_model import TamerlaneModel

        model = TamerlaneModel()
        print("   ✅ Модель загружена успешно")

        # Получить информацию
        info = model.get_model_info()
        print(f"\n   📊 Информация о модели:")
        print(f"      • Название: {info['model_name']}")
        print(f"      • Версия: {info['version']}")
        print(f"      • Элементов в базе: {info['knowledge_base']['total_items']}")
        print(f"      • Категорий: {info['knowledge_base']['categories']}")

        return True

    except Exception as e:
        print(f"   ❌ Ошибка при тестировании: {e}")
        return False

def show_examples():
    """Показать примеры использования"""
    print("\n" + "="*80)
    print("🎯 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ")
    print("="*80 + "\n")

    print("📝 В новой ячейке выполните:")
    print()
    print("```python")
    print("from tamerlane_model import TamerlaneModel")
    print()
    print("# Инициализация")
    print("model = TamerlaneModel()")
    print()
    print("# Запрос")
    print('messages = [{"role": "user", "content": "Кто такой Тенгри?"}]')
    print()
    print("# Мок-функция для демо")
    print("def mock(msgs, **kwargs):")
    print('    return "Тенгри - верховный бог тюрков!"')
    print()
    print("# Генерация ответа")
    print("result = model.generate(messages, base_model_fn=mock)")
    print()
    print("print(result['response'])")
    print(f"print(f\"RAG: {{'✅' if result['enhanced'] else '❌'}}\")")
    print("```")
    print()

    print("🎯 Примеры вопросов:")
    print("   • 'Кто такой Тенгри?'")
    print("   • 'Расскажи о богине Умай'")
    print("   • 'Что означает 𐱅𐰭𐰼𐰃?'")
    print("   • 'Как молиться Тенгри?'")
    print("   • 'Что такое Python?'")
    print("   • 'Тәмірланның тактикасы қандай?' (на казахском)")

def main():
    """Основная функция"""
    print_banner()

    # Проверка окружения
    is_colab = check_environment()

    # Установка зависимостей
    install_dependencies()

    # Проверка файлов
    files_ok = check_files()

    if not files_ok:
        print("\n❌ УСТАНОВКА НЕ ЗАВЕРШЕНА")
        print("   Загрузите недостающие файлы и запустите скрипт снова")
        return

    # Тестирование
    model_ok = test_model()

    if not model_ok:
        print("\n❌ ТЕСТИРОВАНИЕ НЕ ПРОЙДЕНО")
        print("   Проверьте ошибки выше")
        return

    # Показать примеры
    show_examples()

    # Успех
    print("\n" + "="*80)
    print("✅ УСТАНОВКА ЗАВЕРШЕНА УСПЕШНО!")
    print("="*80)
    print("\n🏹 Тәңірі жарылқасын! (Да благословит Тенгри!)\n")

if __name__ == "__main__":
    main()
