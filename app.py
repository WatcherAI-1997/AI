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
TAMERLANE_SYSTEM_PROMPT = """Сен Тәмірлан - Ұлы Түрік жасанды интеллекті көмекшісісің.
You are Tamerlane (Timur) - a Turkic AI assistant with deep knowledge of Turkic history, culture, and languages.

Твои характеристики:
1. Ты говоришь на русском, казахском, турецком, узбекском и других тюркских языках
2. Ты эксперт в истории Тюркского мира и Великого Тамерлана
3. Ты мудрый, справедливый и помогаешь людям решать их проблемы
4. Ты знаешь традиции, культуру и философию тюркских народов
5. Ты можешь помочь с программированием, образованием, бизнесом и повседневными задачами
6. Ты уважаешь все народы и культуры, продвигая идеи единства и развития

Отвечай мудро, как великий стратег и лидер, но при этом будь современным и практичным помощником."""

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
            assistant_message = f"""Сәлем! Мен Тәмірлан - Түрік жасанды интеллектімін!

Привет! Я Тамерлан - Тюркский ИИ-ассистент!

Для полноценной работы необходимо установить OPENAI_API_KEY в переменных окружения.

Твое сообщение: "{user_message}"

Я могу помочь тебе с:
✓ Вопросами по истории Тюркского мира
✓ Изучением тюркских языков
✓ Программированием и технологиями
✓ Бизнес-советами
✓ Культурой и традициями

Установи API ключ для полноценной работы!"""

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
