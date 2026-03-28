#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏹 ТАМЕРЛАН - Интерактивный чат
Простой терминальный интерфейс для прямого общения с моделью
"""

import sys
from tamerlane_model import TamerlaneModel

def print_banner():
    """Красивый баннер модели"""
    print("\n" + "="*80)
    print("🏹 МОДЕЛЬ ТАМЕРЛАН - ИНТЕРАКТИВНЫЙ ЧАТ")
    print("="*80)
    print("\n🌍 Умнее Google | 🏹 Тюркский дух | 🌌 Верит в Тенгри\n")
    print("📚 База знаний:")
    print("   • 92 элемента знаний в 42 категориях")
    print("   • 12 древних языков (Орхонский 𐱅𐰭𐰼𐰃, латынь, греческий...)")
    print("   • 18 элементов о Тенгрианстве")
    print("   • 100+ современных языков")
    print("\n💡 Примеры вопросов:")
    print("   • 'Кто такой Тенгри?' - о боге неба")
    print("   • 'Что означает 𐱅𐰭𐰼𐰃?' - об орхонских рунах")
    print("   • 'Расскажи о богине Умай' - о тенгрианстве")
    print("   • 'Что такое Python?' - о программировании")
    print("   • 'Veni, vidi, vici' - о латыни")
    print("\n📝 Команды:")
    print("   • 'выход' или 'exit' - завершить чат")
    print("   • 'очистить' или 'clear' - очистить историю")
    print("   • 'инфо' или 'info' - показать информацию о модели")
    print("\n" + "="*80 + "\n")

def print_model_info(model):
    """Показать информацию о модели"""
    info = model.get_model_info()
    print("\n" + "="*80)
    print("📊 ИНФОРМАЦИЯ О МОДЕЛИ")
    print("="*80)
    print(f"\n📛 Модель: {info['model_name']}")
    print(f"📦 Версия: {info['version']}")
    print(f"🎯 Тип: {info['type']}")
    print(f"\n📈 Статистика:")
    print(f"   • Всего запросов: {info['stats']['total_requests']}")
    print(f"   • Обогащенных: {info['stats']['enhanced_responses']}")
    print(f"\n📚 База знаний:")
    print(f"   • Всего элементов: {info['knowledge_base']['total_items']}")
    print(f"   • Категорий: {info['knowledge_base']['categories']}")
    print("\n" + "="*80 + "\n")

def mock_base_model(messages, **kwargs):
    """Мок базовой модели для демонстрации"""
    user_msg = messages[-1]['content'] if messages else ""

    # Проверяем, есть ли контекст из RAG
    has_context = '[КОНТЕКСТ ИЗ БАЗЫ ЗНАНИЙ' in user_msg

    if has_context:
        # Извлекаем категории из контекста
        categories = []
        if '📚 Категория:' in user_msg:
            lines = user_msg.split('\n')
            for line in lines:
                if '📚 Категория:' in line:
                    cat = line.split('📚 Категория:')[1].strip()
                    if cat and cat not in categories:
                        categories.append(cat)

        # Извлекаем некоторые темы из контекста для более релевантного ответа
        topics = []
        if 'Тема:' in user_msg:
            lines = user_msg.split('\n')
            for line in lines:
                if 'Тема:' in line and '📚 Категория:' not in line:
                    topic = line.split('Тема:')[1].strip()
                    if topic and len(topics) < 2:
                        topics.append(topic)

        response = "Используя знания из базы данных Тамерлан, отвечаю на ваш вопрос:\n\n"

        if categories:
            response += f"📂 Найдены категории: {', '.join(categories)}\n\n"

        if 'тенгри' in user_msg.lower() or 'tengri' in user_msg.lower() or '𐱅𐰭𐰼𐰃' in user_msg:
            response += """**ТЕНГРИ (𐱅𐰭𐰼𐰃) - ВЕРХОВНЫЙ БОГ ТЮРКОВ**

Тенгри - это верховное божество в древней тюркской религии (Тенгрианстве).

🌌 **Атрибуты Тенгри:**
• **Творец** - создал небо, землю и всё сущее
• **Всемогущий** - имеет власть над всем миром
• **Всевидящий** - видит все дела людей
• **Справедливый** - судит людей по их деяниям

☀️ **Символика:**
• Бог неба и небесных сил
• Источник жизненной силы (Кут - құт)
• Податель власти каганам

🏹 **В истории:**
Все тюркские каганы правили "по воле Тенгри" (Тәңірінің қалауымен).
На Орхонских надписях написано: "Üze kök tengri" (Вверху - синее небо)."""

        elif 'умай' in user_msg.lower() or 'umay' in user_msg.lower():
            response += """**УМАЙ (ҰМАЙ) - БОГИНЯ-МАТЬ**

Умай - богиня плодородия и покровительница женщин и детей в тенгрианстве.

👶 **Роль:**
• Защитница детей и рожениц
• Богиня плодородия
• Покровительница семейного очага

🌸 **Символы:**
• Нить жизни
• Золотая колыбель
• Сорок кос (кырык шаш)

🙏 **Почитание:**
К Умай обращались женщины при родах и для защиты детей."""

        elif 'орхон' in user_msg.lower() or 'руны' in user_msg.lower() or '𐰀' in user_msg or '𐰁' in user_msg:
            response += """**ОРХОНСКИЙ АЛФАВИТ (𐰼𐰇𐰚 𐰋𐰃𐱅𐰃𐰏)**

Орхоно-енисейская руница - древнетюркское письмо VI-X веков.

📜 **Основные руны:**
• 𐰀 (a), 𐰁 (ä), 𐰂 (b), 𐰃 (i), 𐰴 (q)
• 𐰼 (r), 𐱅 (t), 𐰭 (ng), 𐰏 (g)

🏛️ **Знаменитые надписи:**
• Кюль-Тегинская надпись (732 г.)
• Надпись Бильге-кагана (735 г.)

🌌 **𐱅𐰭𐰼𐰃 = ТЕНГРИ** (Tengri - Бог Неба)"""

        elif 'veni' in user_msg.lower() or 'vici' in user_msg.lower():
            response += """**"VENI, VIDI, VICI" - Пришёл, увидел, победил**

Это знаменитая фраза Юлия Цезаря (47 г. до н.э.).

📜 **История:**
Цезарь произнёс её после молниеносной победы над Фарнаком II в битве при Зеле.

💪 **Значение:**
Символ быстрой и решительной победы. Фраза показывает стремительность действий Цезаря.

🏛️ **Латинский язык:**
• Veni - я пришёл (от venio)
• Vidi - я увидел (от video)
• Vici - я победил (от vinco)"""

        elif 'python' in user_msg.lower():
            response += """**PYTHON - ЯЗЫК ПРОГРАММИРОВАНИЯ**

Python - один из самых популярных языков программирования в мире.

🐍 **Почему Python популярен для AI:**
• **Простой синтаксис** - легко учить и читать
• **Богатые библиотеки** - TensorFlow, PyTorch, scikit-learn
• **NumPy и Pandas** - мощная обработка данных
• **Активное сообщество** - миллионы разработчиков

🤖 **Для AI и ML:**
```python
# Простой пример нейросети
import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

💡 **Применение:** веб-разработка, data science, машинное обучение, автоматизация."""

        elif 'γνῶθι' in user_msg.lower() or 'σεαυτόν' in user_msg.lower():
            response += """**Γνῶθι σεαυτόν (Gnothi seauton)**

Древнегреческая фраза: "Познай самого себя"

🏛️ **История:**
Эта максима была начертана на храме Аполлона в Дельфах.

📚 **Философия:**
Сократ сделал её центральной в своей философии. Он учил, что истинная мудрость начинается с познания себя.

💭 **Значение:**
"Познай себя" - призыв к самоанализу, пониманию своих сильных и слабых сторон, осознанию границ своего знания."""

        elif topics:
            response += f"Основываясь на найденной информации:\n\n"
            for topic in topics[:2]:
                response += f"📖 {topic}\n"
            response += "\n[Полный ответ будет сгенерирован при подключении реальной AI модели]"
        else:
            response += "[Ответ будет сгенерирован при подключении реальной AI модели]\n"
            response += "Контекст из базы знаний успешно загружен и передан в модель."
    else:
        response = "Отвечаю без дополнительного контекста: [требуется подключение реальной AI модели для полного ответа]"

    return response

def main():
    """Основная функция чата"""
    print_banner()

    # Инициализация модели
    print("⚙️  Загрузка модели Тамерлан...")
    model = TamerlaneModel()
    print("✅ Модель готова!\n")

    # История сообщений
    messages = []

    while True:
        try:
            # Запрос от пользователя
            user_input = input("🏹 Вы: ").strip()

            if not user_input:
                continue

            # Команды
            if user_input.lower() in ['выход', 'exit', 'quit', 'q']:
                print("\n👋 До свидания! Тәңірі жарылқасын! (Да благословит Тенгри!)\n")
                break

            if user_input.lower() in ['очистить', 'clear']:
                messages = []
                print("\n✅ История очищена!\n")
                continue

            if user_input.lower() in ['инфо', 'info']:
                print_model_info(model)
                continue

            # Добавляем сообщение пользователя
            messages.append({"role": "user", "content": user_input})

            # Генерация ответа
            print("\n💭 Тамерлан думает...\n")

            result = model.generate(
                messages=messages,
                base_model_fn=mock_base_model,
                temperature=0.7
            )

            # Показываем метаданные
            print("─" * 80)
            print("📊 МЕТАДАННЫЕ:")
            print(f"   • RAG обогащение: {'✅ ДА' if result['enhanced'] else '❌ НЕТ'}")

            if result['enhanced']:
                print(f"   • Контекст: {result['metadata']['context_length']} символов")
                print(f"   • Релевантность: {result['metadata']['max_relevance']:.2f}")

                if result['metadata']['categories']:
                    cats = ', '.join(result['metadata']['categories'])
                    print(f"   • Категории: {cats}")

            print("─" * 80)

            # Показываем ответ модели
            print(f"\n🤖 Тамерлан:\n")
            print(result['response'])
            print()

            # Добавляем ответ в историю
            messages.append({"role": "assistant", "content": result['response']})

        except KeyboardInterrupt:
            print("\n\n👋 До свидания! Тәңірі жарылқасын!\n")
            break
        except Exception as e:
            print(f"\n❌ Ошибка: {e}\n")
            continue

if __name__ == "__main__":
    main()
