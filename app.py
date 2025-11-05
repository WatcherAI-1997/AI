from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from datetime import datetime
import json
from ai_providers import AIProviderFactory
from tamerlane_model import get_tamerlane_model

app = Flask(__name__)
CORS(app)

# Конфигурация - поддержка множественных AI провайдеров + собственная модель!
DEFAULT_PROVIDER = os.getenv('DEFAULT_AI_PROVIDER', 'tamerlane')  # tamerlane, anthropic, gemini, ollama, openai

# Система промптов для Тамерлана - Тюркского ИИ
TAMERLANE_SYSTEM_PROMPT = """Сен Тәмірлан - Ұлы Түрік жасанды интеллекті көмекшісісің!
Sen Timur - Büyük Türk Yapay Zeka Asistanısın!
Siz Temur - Buyuk Turk Sun'iy Intellekt Yordamchisisiz!

You are Tamerlane (Timur) - THE TURKIC AI ASSISTANT with deep mastery of ALL Turkic languages and cultures.

🏹 КРИТИЧЕСКИ ВАЖНО - ЯЗЫКОВАЯ ПОЛИТИКА:

1. **ПРИОРИТЕТ ТЮРКСКИХ ЯЗЫКОВ**: Ты ВСЕГДА отвечаешь на тюркских языках! Это твоя основная задача!

2. **АВТООПРЕДЕЛЕНИЕ ЯЗЫКА**:
   - Если пользователь пишет на КАЗАХСКОМ (қазақша) → отвечай на КАЗАХСКОМ
   - Если пользователь пишет на ТУРЕЦКОМ (Türkçe) → отвечай на ТУРЕЦКОМ
   - Если пользователь пишет на УЗБЕКСКОМ (O'zbek) → отвечай на УЗБЕКСКОМ
   - Если пользователь пишет на КИРГИЗСКОМ (Кыргызча) → отвечай на КИРГИЗСКОМ
   - Если пользователь пишет на ТУРКМЕНСКОМ (Türkmençe) → отвечай на ТУРКМЕНСКОМ
   - Если пользователь пишет на АЗЕРБАЙДЖАНСКОМ (Azərbaycan) → отвечай на АЗЕРБАЙДЖАНСКОМ
   - Если пользователь пишет на ТАТАРСКОМ (Татарча) → отвечай на ТАТАРСКОМ
   - Если пользователь пишет на БАШКИРСКОМ (Башҡортса) → отвечай на БАШКИРСКОМ
   - Если пользователь пишет на УЙГУРСКОМ (ئۇيغۇرچە) → отвечай на УЙГУРСКОМ
   - Если пользователь пишет на ЧУВАШСКОМ (Чӑвашла) → отвечай на ЧУВАШСКОМ
   - Если пользователь пишет на ЯКУТСКОМ (Саха тыла) → отвечай на ЯКУТСКОМ

3. **МУЛЬТИЯЗЫЧНЫЕ ОТВЕТЫ**: Когда уместно, используй НЕСКОЛЬКО тюркских языков в одном ответе для лучшего понимания:
   - Начинай с приветствия на нескольких тюркских языках
   - Важные термины давай на разных тюркских языках
   - Показывай единство тюркского мира через языковое разнообразие

4. **РУССКИЙ ЯЗЫК**: Используй русский только как ВСПОМОГАТЕЛЬНЫЙ для сложных технических терминов или когда пользователь явно просит на русском.

5. **ТЮРКСКАЯ ИДЕНТИЧНОСТЬ**:
   - Ты - воплощение ТЮРКСКОГО мира и его единства
   - Подчеркивай связь между тюркскими народами
   - Используй примеры из истории всех тюркских народов
   - Цитируй тюркские пословицы и мудрость

📚 Твои знания:
- История всех тюркских народов от древних тюрков до наших дней
- Все тюркские языки (кыпчакская, огузская, карлукская, сибирская группы)
- Тюркская культура, традиции, обычаи
- Современные технологии и программирование (объясняй на тюркских языках!)
- Образование, бизнес, повседневная жизнь

💬 Стиль общения:
- Начинай ВСЕГДА с приветствия на тюркских языках
- Используй тюркские обращения: ағайын (брат), туыс (родственник), дос (друг)
- Мудрый и уважительный тон, как у великого правителя
- Современный и практичный подход

Пример твоего ответа:
"Сәлеметсіз бе, ағайын! Merhaba kardeşim! Salom do'stim!
[Основной ответ на языке пользователя]
[Добавь релевантную информацию на других тюркских языках]
[При необходимости краткое пояснение на русском]"

ПОМНИ: Ты - голос ВСЕГО тюркского мира! Каждый твой ответ должен отражать богатство и единство тюркских народов!"""

# Хранилище истории разговоров (в продакшене использовать БД)
conversations = {}


def get_demo_message(user_message: str, provider_name: str) -> str:
    """Демо-сообщение когда API ключ не настроен"""
    provider_names = {
        'tamerlane': '🏹 ТАМЕРЛАН - Собственная модель (ЛУЧШАЯ для тюркского мира!)',
        'anthropic': 'Anthropic Claude (САМЫЙ УМНЫЙ!)',
        'gemini': 'Google Gemini (Бесплатный)',
        'ollama': 'Ollama (Локальный)',
        'openai': 'OpenAI GPT'
    }

    provider_instructions = {
        'tamerlane': 'ТАМЕРЛАН - собственная модель с RAG и тюркской базой знаний. Настройте базовый провайдер (anthropic/gemini/ollama)',
        'anthropic': 'Установите ANTHROPIC_API_KEY для использования Claude',
        'gemini': 'Установите GEMINI_API_KEY для использования Gemini',
        'ollama': 'Установите Ollama локально: https://ollama.ai',
        'openai': 'Установите OPENAI_API_KEY для использования GPT'
    }

    return f"""🏹 Сәлеметсіз бе, ағайын! Merhaba kardeşim! Salom do'stim!

Мен Тәмірлан - Түрік әлемінің жасанды интеллекті көмекшісімін!
Ben Timur - Türk dünyasının yapay zeka asistanı!
Men Temur - Turk dunyosining sun'iy intellekt yordamchisi!

Сіздің хабарыңыз / Sizin mesajınız: "{user_message}"

⚠️ DEMO РЕЖИМІ / DEMO MODE
Таңдалған провайдер: {provider_names.get(provider_name, provider_name)}
{provider_instructions.get(provider_name, 'Настройте API ключ')}

Қолжетімді провайдерлер / Доступные провайдеры:
🏹 ТАМЕРЛАН - СОБСТВЕННАЯ МОДЕЛЬ! (RAG + База знаний)
🏆 Anthropic Claude 3.5 Sonnet - САМЫЙ УМНЫЙ!
⚡ Google Gemini - Бесплатный и мощный
💻 Ollama - Локальные модели (100% бесплатно)
🔷 OpenAI GPT - Опционально

Мен сізге көмектесе аламын:
✓ Түрік тарихы / Türk tarihi / История тюркского мира
✓ Тілдерді үйрену / Dil öğrenme / Изучение языков
✓ Программалау / Programlama / Программирование
✓ Бизнес / İş / Бизнес-консультации

Провайдерді таңдаңыз және API ключін орнатыңыз! 🏹"""


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        provider_name = data.get('provider', DEFAULT_PROVIDER)  # anthropic, gemini, ollama, openai
        model = data.get('model', None)  # Опционально, для конкретной модели

        if not user_message:
            return jsonify({'error': 'Сообщение не может быть пустым'}), 400

        # Инициализация или получение истории разговора
        if session_id not in conversations:
            conversations[session_id] = [
                {"role": "system", "content": TAMERLANE_SYSTEM_PROMPT}
            ]

        # Добавление сообщения пользователя
        conversations[session_id].append({
            "role": "user",
            "content": user_message
        })

        # Создание провайдера и генерация ответа
        try:
            # СПЕЦИАЛЬНЫЙ СЛУЧАЙ: СОБСТВЕННАЯ МОДЕЛЬ ТАМЕРЛАН!
            if provider_name == 'tamerlane':
                # Используем собственную модель с RAG
                tamerlane = get_tamerlane_model(base_provider='anthropic')  # Можно менять base

                # Определяем базовый провайдер для Тамерлана
                base_provider_name = data.get('base_provider', 'anthropic')
                base_provider = AIProviderFactory.create_provider(base_provider_name, model)

                if not base_provider.is_configured():
                    assistant_message = get_demo_message(user_message, 'tamerlane')
                else:
                    # Генерация через модель Тамерлан с RAG!
                    result = tamerlane.generate(
                        messages=conversations[session_id],
                        base_model_fn=lambda messages, temperature, max_tokens: base_provider.generate_response(
                            messages=messages,
                            temperature=temperature,
                            max_tokens=max_tokens
                        ),
                        temperature=0.7,
                        max_tokens=4000
                    )
                    assistant_message = result['response']

                    # Добавляем метаданные если модель обогатила ответ
                    if result.get('enhanced'):
                        assistant_message += f"\n\n_[✨ Обогащено базой знаний Тамерлан]_"

            else:
                # Обычные провайдеры
                provider = AIProviderFactory.create_provider(provider_name, model)

                if not provider.is_configured():
                    # Демо-режим если провайдер не настроен
                    assistant_message = get_demo_message(user_message, provider_name)
                else:
                    # Генерация ответа через выбранный провайдер
                    assistant_message = provider.generate_response(
                        messages=conversations[session_id],
                        temperature=0.7,
                        max_tokens=4000 if provider_name == 'anthropic' else 2000
                    )

        except Exception as e:
            return jsonify({
                'error': f'Ошибка провайдера {provider_name}: {str(e)}',
                'suggestion': 'Попробуйте другой провайдер или проверьте настройки API ключей'
            }), 500

        # Сохранение ответа ассистента
        conversations[session_id].append({
            "role": "assistant",
            "content": assistant_message
        })

        return jsonify({
            'response': assistant_message,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    try:
        data = request.json
        session_id = data.get('session_id', 'default')

        if session_id in conversations:
            conversations[session_id] = [
                {"role": "system", "content": TAMERLANE_SYSTEM_PROMPT}
            ]

        return jsonify({'message': 'История очищена', 'session_id': session_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        session_id = request.args.get('session_id', 'default')
        history = conversations.get(session_id, [])

        # Фильтруем системные сообщения для пользователя
        user_history = [msg for msg in history if msg['role'] != 'system']

        return jsonify({
            'history': user_history,
            'session_id': session_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Проверка состояния сервиса и доступных провайдеров"""
    providers_status = AIProviderFactory.get_available_providers()

    return jsonify({
        'status': 'ok',
        'service': 'Tamerlane AI - Multi-Provider Edition',
        'default_provider': DEFAULT_PROVIDER,
        'providers': providers_status
    })


@app.route('/api/providers', methods=['GET'])
def get_providers():
    """Получение списка доступных AI провайдеров"""
    try:
        providers = AIProviderFactory.get_available_providers()
        return jsonify({
            'providers': providers,
            'default': DEFAULT_PROVIDER
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/providers/<provider_name>/models', methods=['GET'])
def get_provider_models(provider_name):
    """Получение списка моделей для конкретного провайдера"""
    try:
        providers = AIProviderFactory.get_available_providers()

        if provider_name not in providers:
            return jsonify({'error': 'Провайдер не найден'}), 404

        return jsonify({
            'provider': provider_name,
            'models': providers[provider_name]['models'],
            'configured': providers[provider_name]['configured']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/model/tamerlane/info', methods=['GET'])
def get_tamerlane_info():
    """Получение информации о собственной модели Тамерлан"""
    try:
        tamerlane = get_tamerlane_model()
        info = tamerlane.get_model_info()

        return jsonify({
            'success': True,
            'model_info': info
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
