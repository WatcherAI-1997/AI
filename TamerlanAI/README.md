# 🏹 TamerlanAI

**Универсальная мультиязычная LLM модель для тюркских языков**

**Автор:** Джама Ваккасов (jamavakkasoff@gmail.com)

---

## ⚡ БЫСТРАЯ УСТАНОВКА (ОДНА КОМАНДА!)

```bash
cd TamerlanAI
chmod +x install.sh
./install.sh
```

**Это все! Скрипт сделает:**
- ✅ Проверит Python
- ✅ Установит PyTorch и все зависимости
- ✅ Обучит модель (~2 минуты)
- ✅ Настроит окружение

---

## 🚀 ЗАПУСК

```bash
cd TamerlanAI/backend
./start.sh
```

Сервер: http://localhost:8000
API Docs: http://localhost:8000/docs

---

## 📖 ЧТО ЭТО?

**TamerlanAI** - настоящая обучаемая LLM модель (не заглушка!)

- **🧠 3.3M параметров** - decoder-only трансформер (GPT-style)
- **🌍 23 языка** - 14 тюркских + 9 других
- **⚡ Локально** - без внешних API
- **📚 Обучаемая** - на своих данных

---

## 🧪 БЫСТРЫЙ ТЕСТ

```bash
cd TamerlanAI/backend
python3 test_real.py
```

---

## 📝 ПРИМЕР

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/chat/",
    json={
        "messages": [{"role": "user", "content": "Сәлем!"}],
        "language": "kk"
    }
)

print(response.json()["message"]["content"])
```

---

## 📚 ДОКУМЕНТАЦИЯ

- [Полная документация](backend/README_RU.md)
- [API Docs](http://localhost:8000/docs)

---

## 🏹 Тәңірі жарылқасын!
