# 🏹 Тамерлан ИИ - Тюркский AI Ассистент

**Tamerlane AI** - современный искусственный интеллект с глубоким знанием тюркской истории, культуры и языков, созданный по образу великого полководца и государственного деятеля Тамерлана (Тимура).

<div align="center">

```
┌────────────────────────────────────────────────┐
│   🏹 ТАМЕРЛАН ИИ                               │
│   Түрік Жасанды Интеллект                      │
│   Turkic AI Assistant                          │
└────────────────────────────────────────────────┘
```

</div>

## 🌟 Возможности

- 🗣️ **Мультиязычность**: Поддержка русского, казахского, турецкого, узбекского и других тюркских языков
- 🏛️ **Знание культуры**: Экспертные знания по истории и культуре тюркских народов
- 💻 **Программирование**: Помощь в разработке и технических вопросах
- 📚 **Образование**: Консультации по обучению и саморазвитию
- 💼 **Бизнес**: Стратегические советы и бизнес-консультации
- 🎨 **Современный интерфейс**: Красивый веб-интерфейс в тюркском стиле

## 🚀 Быстрый старт

### Вариант 1: Локальный запуск (рекомендуется)

```bash
# Клонирование репозитория
git clone <repository-url>
cd AI

# Запуск скрипта установки и запуска
./run.sh
```

Приложение будет доступно по адресу: **http://localhost:5000**

### Вариант 2: Docker

```bash
# Создайте .env файл с вашим API ключом
cp .env.example .env
# Отредактируйте .env и добавьте OPENAI_API_KEY

# Запуск через Docker Compose
docker-compose up -d

# Просмотр логов
docker-compose logs -f
```

### Вариант 3: Ручная установка

```bash
# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Настройка переменных окружения
cp .env.example .env
# Отредактируйте .env и добавьте ваш OPENAI_API_KEY

# Запуск приложения
python app.py
```

## 🔑 Получение OpenAI API ключа

1. Зарегистрируйтесь на [OpenAI Platform](https://platform.openai.com/)
2. Перейдите в раздел [API Keys](https://platform.openai.com/api-keys)
3. Создайте новый ключ
4. Скопируйте его в файл `.env`:

```env
OPENAI_API_KEY=sk-ваш-ключ-здесь
```

**Примечание**: Без API ключа приложение будет работать в демо-режиме с ограниченной функциональностью.

## 📁 Структура проекта

```
AI/
├── app.py                  # Основной файл Flask приложения
├── requirements.txt        # Python зависимости
├── Dockerfile             # Docker конфигурация
├── docker-compose.yml     # Docker Compose конфигурация
├── run.sh                 # Скрипт быстрого запуска
├── .env.example           # Пример файла переменных окружения
├── .gitignore            # Git ignore файл
├── README.md             # Документация
├── templates/
│   └── index.html        # HTML шаблон интерфейса
└── static/
    ├── css/
    │   └── style.css     # Стили приложения
    └── js/
        └── app.js        # Frontend логика
```

## 🎨 Особенности интерфейса

- **Адаптивный дизайн**: Работает на desktop, планшетах и мобильных устройствах
- **Тюркская цветовая палитра**: Вдохновлена традиционными цветами и орнаментами
- **Плавные анимации**: Современные переходы и эффекты
- **История разговоров**: Сохранение контекста диалога
- **Выбор модели**: Поддержка GPT-3.5, GPT-4 и GPT-4 Turbo

## 🌐 API Endpoints

### POST /api/chat
Отправка сообщения и получение ответа от ИИ

```json
{
  "message": "Расскажи о Тамерлане",
  "session_id": "session_123",
  "model": "gpt-3.5-turbo"
}
```

**Ответ:**
```json
{
  "response": "Тамерлан (Тимур) был великим...",
  "session_id": "session_123",
  "timestamp": "2025-11-05T10:30:00"
}
```

### POST /api/clear
Очистка истории разговора

```json
{
  "session_id": "session_123"
}
```

### GET /api/history?session_id=session_123
Получение истории разговора

### GET /api/health
Проверка состояния сервиса

## 🔧 Технологический стек

### Backend
- **Flask** - веб-фреймворк
- **OpenAI API** - интеграция с GPT моделями
- **Flask-CORS** - поддержка CORS

### Frontend
- **Vanilla JavaScript** - без фреймворков для максимальной производительности
- **HTML5/CSS3** - современная верстка
- **Fetch API** - асинхронные запросы

### DevOps
- **Docker** - контейнеризация
- **Gunicorn** - WSGI сервер для продакшена

## 🎯 Примеры использования

### Вопросы по истории
```
Пользователь: Расскажи об империи Тамерлана
Тамерлан ИИ: [Подробный ответ о государстве Тимуридов...]
```

### Изучение языков
```
Пользователь: Как сказать "Привет, как дела?" на казахском?
Тамерлан ИИ: На казахском это будет "Сәлем, қалың қалай?"
```

### Программирование
```
Пользователь: Напиши функцию сортировки массива на Python
Тамерлан ИИ: [Код с объяснениями...]
```

## 🔐 Безопасность

- API ключи хранятся в переменных окружения
- Никогда не коммитьте `.env` файл в репозиторий
- Используйте HTTPS в продакшене
- Регулярно обновляйте зависимости

## 🚀 Деплой в продакшн

### На VPS/Dedicated сервере

```bash
# Установка с использованием systemd
sudo nano /etc/systemd/system/tamerlane-ai.service

[Unit]
Description=Tamerlane AI Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/AI
Environment="PATH=/path/to/AI/venv/bin"
ExecStart=/path/to/AI/venv/bin/gunicorn --bind 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target

# Запуск сервиса
sudo systemctl enable tamerlane-ai
sudo systemctl start tamerlane-ai
```

### Nginx конфигурация

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта!

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit изменений (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📝 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.

## 📧 Контакты

Вопросы и предложения:
- GitHub Issues: [Создать issue](../../issues)
- Email: your-email@example.com

## 🙏 Благодарности

- OpenAI за API
- Тюркскому сообществу за вдохновение
- Всем контрибьюторам проекта

---

<div align="center">

**Создано с ❤️ для тюркского мира**

Түрік әлемі үшін ❤️-пен жасалған

</div>
