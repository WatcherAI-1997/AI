# 🚀 TamerlanAI - БЫСТРЫЙ СТАРТ

**Автор:** Джама Ваккасов (jamavakkasoff@gmail.com)

---

## ⚡ Запуск за 3 минуты

### Шаг 1: Переход в папку

```bash
cd /home/user/AI/TamerlanAI/backend
```

### Шаг 2: Установка минимальных зависимостей

```bash
pip install -r requirements-minimal.txt
```

**Что установится:**
- FastAPI (веб-фреймворк)
- Uvicorn (сервер)
- Pydantic (валидация)
- python-dotenv (конфигурация)

Всего ~20MB, установка ~1 минута.

### Шаг 3: Запуск сервера

```bash
python main_simple.py
```

**Готово!** Сервер запущен на http://localhost:8000

---

## 📖 Использование

### 1. Откройте API документацию

http://localhost:8000/docs

Здесь интерактивный интерфейс для тестирования всех эндпоинтов!

### 2. Проверьте статус

```bash
curl http://localhost:8000/health
```

### 3. Тест чата

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Сәлем! Қалайсың?"}
    ],
    "language": "kk"
  }'
```

**Ответ:**
```json
{
  "message": {
    "role": "assistant",
    "content": "Сәлеметсіз бе! Мен TamerlanAI..."
  },
  "model": "tamerlane-demo",
  "language": "kk",
  "metadata": {...}
}
```

---

## 🧪 Примеры запросов

### Казахский язык

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Сәлем!"}],
    "language": "kk",
    "personality": "casual"
  }'
```

### Турецкий язык

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Merhaba!"}],
    "language": "tr"
  }'
```

### Русский язык

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Привет!"}],
    "language": "ru"
  }'
```

### Перевод

```bash
curl -X POST "http://localhost:8000/api/v1/translate/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "source_lang": "en",
    "target_lang": "kk"
  }'
```

---

## 🎯 Доступные эндпоинты

### Chat
- `POST /api/v1/chat/` - Чат с AI
- `WS /api/v1/chat/ws` - WebSocket для streaming
- `GET /api/v1/chat/personalities` - Список стилей
- `GET /api/v1/chat/languages` - Список языков

### Models
- `GET /api/v1/models/` - Список моделей
- `GET /api/v1/models/{name}` - Информация о модели
- `POST /api/v1/models/switch/{name}` - Переключить модель

### Translation
- `POST /api/v1/translate/` - Перевод текста

### Analysis
- `POST /api/v1/analyze/` - Анализ текста

---

## 🌍 Поддерживаемые языки

### Тюркские (14):
- Турецкий (tr)
- Азербайджанский (az)
- Узбекский (uz)
- Казахский (kk)
- Киргизский (ky)
- Татарский (tt)
- Башкирский (ba)
- Якутский (sah)
- Туркменский (tk)
- Чувашский (cv)
- Карачаевский (krc)
- Гагаузский (gag)
- Уйгурский (ug)
- Тувинский (tyv)

### Другие (9):
- Русский (ru)
- Английский (en)
- Арабский (ar)
- Китайский (zh)
- Японский (ja)
- Корейский (ko)
- Французский (fr)
- Немецкий (de)
- Испанский (es)

---

## 🎭 Стили личности

- `formal` - Официальный
- `academic` - Академический
- `casual` - Неформальный
- `business` - Деловой
- `folk` - Народный
- `poetic` - Поэтический
- `religious` - Религиозный
- `philosophical` - Философский

---

## 📝 Python пример

```python
import requests

# Чат на казахском
response = requests.post(
    "http://localhost:8000/api/v1/chat/",
    json={
        "messages": [
            {"role": "user", "content": "Тәмірлан туралы айтып бер"}
        ],
        "language": "kk",
        "personality": "formal"
    }
)

print(response.json()["message"]["content"])
```

---

## ❓ Решение проблем

### Ошибка: "ModuleNotFoundError"

```bash
# Убедитесь что установили зависимости
pip install -r requirements-minimal.txt
```

### Ошибка: "Address already in use"

```bash
# Порт 8000 занят, используйте другой
python main_simple.py --port 8001
```

### Ошибка: "Import error"

```bash
# Убедитесь что находитесь в папке backend
cd /home/user/AI/TamerlanAI/backend
python main_simple.py
```

---

## 🔄 Перезапуск

Для перезапуска сервера:

1. Нажмите `Ctrl+C` в терминале
2. Запустите снова: `python main_simple.py`

---

## 📊 Режимы работы

### 🎮 Demo Mode (текущий)
- **Файл:** `main_simple.py`
- **Зависимости:** минимальные
- **Модель:** демо-ответы
- **Запуск:** `python main_simple.py`

### 🚀 Production Mode (для продакшена)
- **Файл:** `main.py`
- **Зависимости:** полные (PyTorch, Transformers)
- **Модель:** обученная Tamerlane GPT
- **Запуск:** `python main.py`

---

## ✅ Что работает

- ✅ FastAPI сервер
- ✅ REST API эндпоинты
- ✅ Мультиязычность (23 языка)
- ✅ Автоопределение языка
- ✅ Адаптивная личность
- ✅ API документация (Swagger)
- ✅ CORS поддержка
- ✅ Error handling
- ✅ Health checks

---

## 🎉 Готово!

Теперь у вас запущен **TamerlanAI** в демо-режиме!

Для интеграции с обученной моделью см. [INTEGRATION.md](INTEGRATION.md)

---

**🏹 Тәңірі жарылқасын!**

**Автор:** Джама Ваккасов
**Email:** jamavakkasoff@gmail.com
