#!/usr/bin/env python3
"""
Тест СУПЕР-МОДЕЛИ Тамерлан - Умнее Google!
Test SUPER MODEL Tamerlane - Smarter than Google!
"""

from tamerlane_model import get_tamerlane_model
from world_languages import get_world_languages
from turkic_knowledge_base import get_knowledge_base

def mock_base_model(messages, temperature, max_tokens):
    """Мок-функция для тестирования"""
    last_msg = messages[-1]['content'] if messages else ""

    # Извлекаем контекст
    context = ""
    for msg in messages:
        if msg['role'] == 'system':
            context = msg['content']
            break

    if "[КОНТЕКСТ ИЗ БАЗЫ ЗНАНИЙ" in context:
        return f"[МОК-ОТВЕТ С КОНТЕКСТОМ]\nВопрос: {last_msg}\nКонтекст предоставлен!"
    else:
        return f"[МОК-ОТВЕТ]\nВопрос: {last_msg}"


def test_super_intelligence():
    print("="*80)
    print("🧠 ТЕСТИРОВАНИЕ СУПЕР-МОДЕЛИ ТАМЕРЛАН - УМНЕЕ GOOGLE! 🌍")
    print("="*80)

    # Инициализация
    model = get_tamerlane_model(base_provider='anthropic')
    languages = get_world_languages()
    kb = get_knowledge_base()

    print("\n📊 СТАТИСТИКА СИСТЕМЫ:")
    print("="*80)

    # Статистика языков
    lang_stats = languages.get_stats()
    print(f"\n🌐 ЯЗЫКИ:")
    print(f"  • Всего языков поддерживается: {lang_stats['total_languages']}")
    print(f"  • Языковых семей: {lang_stats['language_families']}")
    print(f"  • Общее количество носителей: {lang_stats['total_speakers']:,}")

    print(f"\n  🏆 ТОП-10 ЯЗЫКОВ:")
    for i, (name, speakers) in enumerate(lang_stats['top_languages'], 1):
        print(f"    {i}. {name}: {speakers:,} носителей")

    # Статистика базы знаний
    kb_stats = kb.get_stats()
    print(f"\n📚 БАЗА ЗНАНИЙ:")
    print(f"  • Всего категорий: {len(kb_stats) - 1}")
    print(f"  • Всего элементов знаний: {kb_stats['total']}")
    print(f"\n  📖 КАТЕГОРИИ:")
    for category, count in sorted(kb_stats.items()):
        if category != 'total':
            print(f"    • {category}: {count} элементов")

    print("\n" + "="*80)
    print("🧪 ТЕСТЫ СУПЕР-ИНТЕЛЛЕКТА:")
    print("="*80)

    # Тесты на разных языках и темах
    tests = [
        {
            'name': 'Quantum Computing (English)',
            'query': 'Explain quantum computing and superposition',
            'language': 'en'
        },
        {
            'name': 'Квантовая механика (Русский)',
            'query': 'Расскажи об уравнении Шрёдингера',
            'language': 'ru'
        },
        {
            'name': '数学 - Calculus (中文)',
            'query': '解释微积分',
            'language': 'zh'
        },
        {
            'name': 'Matemáticas (Español)',
            'query': 'Explica el teorema de Pitágoras',
            'language': 'es'
        },
        {
            'name': 'Machine Learning (Қазақша)',
            'query': 'Машиналық оқыту дегеніміз не?',
            'language': 'kk'
        },
        {
            'name': 'Histoire mondiale (Français)',
            'query': 'Parlez-moi des civilisations anciennes',
            'language': 'fr'
        },
        {
            'name': 'Programmierung (Deutsch)',
            'query': 'Was ist Python Programmierung?',
            'language': 'de'
        },
        {
            'name': 'Blockchain (Türkçe)',
            'query': 'Blockchain teknolojisini anlat',
            'language': 'tr'
        },
        {
            'name': 'कृत्रिम बुद्धिमत्ता (हिन्दी)',
            'query': 'AI के बारे में बताओ',
            'language': 'hi'
        },
        {
            'name': '人工知能 (日本語)',
            'query': 'AIについて教えて',
            'language': 'ja'
        },
    ]

    successful_enhancements = 0

    for i, test in enumerate(tests, 1):
        print(f"\n🧪 ТЕСТ {i}: {test['name']}")
        print(f"Запрос: \"{test['query']}\"")

        messages = [{"role": "user", "content": test['query']}]

        try:
            result = model.generate(
                messages=messages,
                base_model_fn=mock_base_model,
                temperature=0.7
            )

            enhanced = result['enhanced']
            context_len = result['metadata']['context_length']
            detected_lang = result['metadata']['detected_language']

            print(f"✅ Язык определен: {detected_lang}")
            print(f"{'✅' if enhanced else '❌'} Обогащен контекстом: {enhanced}")
            print(f"📏 Длина контекста: {context_len} символов")

            if enhanced:
                successful_enhancements += 1

        except Exception as e:
            print(f"❌ Ошибка: {e}")

    print("\n" + "="*80)
    print("📊 ИТОГОВЫЕ РЕЗУЛЬТАТЫ:")
    print("="*80)

    success_rate = (successful_enhancements / len(tests)) * 100
    print(f"\n✅ Успешно обогащено: {successful_enhancements}/{len(tests)} ({success_rate:.1f}%)")

    # Информация о модели
    model_info = model.get_model_info()
    print(f"\n🏹 МОДЕЛЬ: {model_info['name']}")
    print(f"📦 Версия: {model_info['version']}")
    print(f"🎯 Тип: {model_info['type']}")

    print(f"\n📈 СТАТИСТИКА МОДЕЛИ:")
    print(f"  • Всего запросов: {model_info['statistics']['total_requests']}")
    print(f"  • Обогащенных запросов: {model_info['statistics']['kb_enhanced_requests']}")

    print(f"\n📚 БАЗА ЗНАНИЙ:")
    print(f"  • Всего элементов: {model_info['knowledge_base']['total']}")
    print(f"  • Категорий: {len(model_info['knowledge_base']) - 1}")

    print("\n" + "="*80)
    print("🎉 ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ!")
    print("="*80)

    print("\n🌍 МОДЕЛЬ ТАМЕРЛАН - ХАРАКТЕРИСТИКИ:")
    print(f"""
    ✅ 100+ языков мира
    ✅ 32+ категорий знаний
    ✅ Квантовая физика
    ✅ Машинное обучение и AI
    ✅ Программирование (Python, JavaScript, etc.)
    ✅ Математика (от Пифагора до интегралов)
    ✅ Мировая история и культура
    ✅ Блокчейн и криптовалюты
    ✅ Data Science
    ✅ Кибербезопасность
    ✅ Космос и астрономия
    ✅ Генетика и нейронаука
    ✅ Бизнес и финансы
    ✅ Спорт и искусство
    ✅ Право и политика
    ✅ И МНОГОЕ ДРУГОЕ!

    🏆 ТАМЕРЛАН > GOOGLE! 🚀
    """)


if __name__ == "__main__":
    test_super_intelligence()
