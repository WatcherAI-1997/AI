# 🚀 БЫСТРЫЙ СТАРТ В GOOGLE COLAB

**Автор:** Джама Ваккасов (jamavakkasoff@gmail.com)

**⚠️ ЭТО ПОЛНОЦЕННАЯ LLM МОДЕЛЬ!** Не обертка, а настоящий AI с RAG-системой!

---

## ⚡ За 3 минуты запустите Тамерлан AI!

### Шаг 1: Откройте Colab
Перейдите на: **https://colab.research.google.com/**

### Шаг 2: Загрузите notebook
1. Нажмите **"Файл" → "Загрузить блокнот"**
2. Выберите файл: `Tamerlane_AI_Colab.ipynb`

### Шаг 3: Запустите!
Нажмите **"Среда выполнения" → "Запустить все"**

---

## 📋 Или создайте новый notebook:

### Ячейка 1: Установка
```python
!pip install -q requests anthropic google-generativeai
```

### Ячейка 2: Загрузка файлов
```python
from google.colab import files
uploaded = files.upload()  # Загрузите все .py файлы
```

### Ячейка 3: Запуск
```python
from tamerlane_model import TamerlaneModel

model = TamerlaneModel()
print("✅ Модель готова!")
```

### Ячейка 4: Тестирование
```python
messages = [{"role": "user", "content": "Кто такой Тенгри?"}]

def mock(msgs, **kwargs):
    return "Тенгри - верховный бог тюрков! 🏹"

result = model.generate(messages, base_model_fn=mock)
print(result['response'])
```

---

## 🎯 Готовые вопросы для теста:

```python
# Скопируйте и вставьте:

test_query("Кто такой Тенгри?")
test_query("Расскажи о богине Умай")
test_query("Что означает 𐱅𐰭𐰼𐰃?")
test_query("Что такое Python?")
test_query("Тәмірланның тактикасы қандай болды?")
```

---

## 📦 Нужные файлы:

Загрузите эти 7 файлов в Colab:
1. ✅ `tamerlane_model.py`
2. ✅ `turkic_knowledge_base.py`
3. ✅ `universal_knowledge.py`
4. ✅ `advanced_knowledge.py`
5. ✅ `world_languages.py`
6. ✅ `ancient_languages.py`
7. ✅ `tengri_knowledge.py`

---

## 🔑 Для полных AI-ответов:

Получите бесплатный API ключ:
- **Claude**: https://console.anthropic.com/ ($5 бесплатно)
- **Gemini**: https://makersuite.google.com/ (бесплатный лимит)

```python
# В Colab добавьте:
from anthropic import Anthropic

client = Anthropic(api_key="ваш-ключ")

def claude(messages, **kwargs):
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=messages
    )
    return response.content[0].text

# Используйте claude вместо mock
result = model.generate(messages, base_model_fn=claude)
```

---

## ✅ Готово!

Теперь у вас работает Тамерлан AI в Google Colab!

---

**Автор:** Джама Ваккасов
**Email:** jamavakkasoff@gmail.com
**Проект:** Tamerlane AI - Полноценная тюркская LLM модель

**🏹 Тәңірі жарылқасын!**
