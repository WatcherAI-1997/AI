from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Конфигурация
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        model = data.get('model', 'gpt-3.5-turbo')

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

        # Вызов OpenAI API
        if OPENAI_API_KEY:
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model=model,
                messages=conversations[session_id],
                temperature=0.7,
                max_tokens=2000
            )

            assistant_message = response.choices[0].message.content
        else:
            # Демо-режим без API ключа
            assistant_message = f"""🏹 Сәлеметсіз бе, ағайын! Merhaba kardeşim! Salom do'stim!

Мен Тәмірлан - Түрік әлемінің жасанды интеллекті көмекшісімін!
Ben Timur - Türk dünyasının yapay zeka asistanıyım!
Men Temur - Turk dunyosining sun'iy intellekt yordamchisiman!

Сіздің хабарыңыз / Sizin mesajınız / Sizning xabaringiz: "{user_message}"

⚠️ DEMO РЕЖИМІ / DEMO MODE:
Толық қызмет үшін OPENAI_API_KEY қажет.
Tam işlev için OPENAI_API_KEY gerekli.
To'liq xizmat uchun OPENAI_API_KEY kerak.

Для полноценной работы установите OPENAI_API_KEY!

Мен сізге көмектесе аламын / Size yardım edebilirim:
✓ Түрік тарихы туралы сұрақтар / Türk tarihi soruları
✓ Түркі тілдерін үйрену / Türk dillerini öğrenme
✓ Программалау және технология / Programlama ve teknoloji
✓ Бизнес кеңестері / İş tavsiyeleri
✓ Мәдениет және дәстүрлер / Kültür ve gelenekler

Түрік әлеміне қош келдіңіз! Türk dünyasına hoş geldiniz! 🏹"""

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
    return jsonify({
        'status': 'ok',
        'service': 'Tamerlane AI',
        'api_configured': bool(OPENAI_API_KEY)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
