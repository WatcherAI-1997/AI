# 🏹 TamerlanAI - НАСТОЯЩАЯ LLM МОДЕЛЬ

**Автор:** Джама Ваккасов (jamavakkasoff@gmail.com)

---

## ✨ Теперь это НАСТОЯЩАЯ модель!

**ПОЛНОСТЬЮ ПЕРЕДЕЛАНО!** Никаких заглушек, никакого хардкода!

✅ **TamerlaneGPT** - собственный decoder-only трансформер (GPT-style)
✅ **3.3M параметров** - настоящая нейронная сеть
✅ **Обучаемая модель** - можно обучать на своих данных
✅ **Авторегрессивная генерация** - настоящая генерация текста
✅ **PyTorch** - профессиональный ML фреймворк
✅ **Без внешних API** - все работает локально

---

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
cd TamerlanAI/backend

# Установить PyTorch (CPU версия)
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Установить остальные зависимости
pip install fastapi uvicorn pydantic pydantic-settings python-dotenv python-multipart requests
```

### 2. Обучение модели

```bash
# Обучить модель на демо-данных (100 эпох, ~2 минуты)
python train_demo.py
```

**Результат:**
```
🏹 ОБУЧЕНИЕ TAMERLANEGPT
================================================================================
Device: cpu
Vocabulary size: 265
Model: 3.30M parameters

Epoch   1/100 | Loss: 2.5434
Epoch  10/100 | Loss: 0.2168
...
Epoch 100/100 | Loss: 0.0008

✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!
Model saved to: checkpoints/best_model.pt
```

### 3. Копирование модели

```bash
# Скопировать обученную модель в нужное место
cp checkpoints/best_model.pt models/
cp checkpoints/tokenizer.json models/
```

### 4. Запуск сервера

```bash
python main.py
```

**Вы увидите:**
```
🏹 Starting TamerlanAI...
🤖 Loading TamerlaneGPT model...
Loading tokenizer from ./models/tokenizer.json
Loading model from ./models/best_model.pt
✅ Model loaded from checkpoint (epoch 99)
📊 Model: 3.30M parameters
✅ REAL LLM Manager initialized successfully!
```

### 5. Тестирование

```bash
python test_real.py
```

---

## 📊 Архитектура модели

```python
TamerlaneGPT(
  # Эмбеддинги
  token_embedding: Embedding(vocab_size=265, d_model=256)

  # 6 трансформер блоков
  transformer_blocks: [
    TransformerBlock(
      multi_head_attention: MultiHeadAttention(heads=8)
      feed_forward: FeedForward(d_model=256, d_ff=1024)
      layer_norm: LayerNorm()
    ) x 6
  ]

  # Выход
  output: Linear(d_model=256, vocab_size=265)
)

Параметры: 3.30M
Максимальная длина: 2048 токенов
```

---

## 🧪 Примеры использования

### Python API

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/chat/",
    json={
        "messages": [
            {"role": "user", "content": "Сәлем! TamerlanAI туралы айтып бер"}
        ],
        "language": "kk",
        "temperature": 0.8,
        "max_tokens": 100
    }
)

print(response.json()["message"]["content"])
```

### cURL

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Привет!"}],
    "language": "ru"
  }'
```

---

## 🎯 Что работает

### ✅ Генерация текста
- Авторегрессивная генерация через трансформер
- Temperature sampling
- Top-K filtering
- Управление длиной генерации

### ✅ Мультиязычность
- Казахский (kk)
- Турецкий (tr)
- Русский (ru)
- Английский (en)
- Auto-detection языка

### ✅ Обучение
- Полный pipeline обучения
- Сохранение/загрузка checkpoints
- Training на CPU и GPU
- Мониторинг loss

### ✅ Токенизация
- Word-level tokenizer
- BPE tokenizer (в разработке)
- Поддержка юникода
- Специальные токены

---

## 📈 Улучшение модели

### Для лучших результатов:

**1. Больше данных**
```python
# Добавьте больше текстов в get_training_data()
texts = [
    # Тысячи предложений на каждом языке
    "...",
]
```

**2. Больше эпох**
```python
train_model(num_epochs=500)  # Вместо 100
```

**3. Больше параметров**
```python
# В model/architecture.py
model = TamerlaneGPT(
    vocab_size=vocab_size,
    d_model=512,      # Было 256
    num_layers=12,    # Было 6
    num_heads=16,     # Было 8
    d_ff=2048,        # Было 1024
)
```

**4. GPU обучение**
```bash
# Установить CUDA версию PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

---

## 🔧 Структура проекта

```
TamerlanAI/backend/
├── model/
│   ├── architecture.py       # TamerlaneGPT transformer
│   ├── simple_tokenizer.py   # Word-level tokenizer
│   ├── tokenizer.py          # BPE tokenizer
│   └── dataset.py            # Dataset loader
├── core/
│   └── llm_manager_real.py   # НАСТОЯЩИЙ LLM менеджер
├── api/v1/endpoints/
│   ├── chat.py               # Chat API
│   ├── models.py             # Models API
│   └── ...
├── train_demo.py             # Скрипт обучения
├── test_real.py              # Тесты
└── main.py                   # Сервер
```

---

## ⚠️ Важная информация

### Текущая модель - DEMO

Модель обучена на **38 предложениях** для демонстрации работы.
Результаты генерации будут **не очень осмысленными**.

Для **production** нужно:
1. Собрать большой датасет (минимум 10,000 предложений)
2. Обучить модель на 500+ эпох
3. Использовать GPU
4. Увеличить размер модели

### Производительность

- **CPU**: ~0.6s на генерацию (100 токенов)
- **GPU**: ~0.1s на генерацию (100 токенов)
- **Память**: ~200MB для модели 3.3M

---

## 🎉 Результаты тестирования

```
============================================================
🏹 TESTING TAMERLANAI - REAL MODEL
============================================================

✅ Server is healthy

Language: kk
User: Сәлем! TamerlanAI туралы айтып бер
Assistant: system қазақ..,! TamerlanAI
Model: tamerlane-gpt
Generation time: 0.62s
Tokens: 3
Device: cpu

Language: tr
User: Merhaba! Kendini tanıt
Assistant: system Türkçe. Türk., Merhaba!
Model: tamerlane-gpt
Generation time: 0.60s
Tokens: 4
Device: cpu

✅ TESTING COMPLETED
```

---

## 🔮 Roadmap

- [ ] Собрать большой multilingual датасет
- [ ] Обучить production модель (100M+ параметров)
- [ ] Добавить fine-tuning для разных задач
- [ ] Реализовать streaming generation
- [ ] Добавить RLHF (Reinforcement Learning from Human Feedback)
- [ ] Поддержка всех 14 тюркских языков

---

## 💡 Технические детали

### Генерация

```python
def generate(input_ids, max_new_tokens=50, temperature=1.0, top_k=50):
    for _ in range(max_new_tokens):
        logits = model.forward(input_ids)
        logits = logits[:, -1, :] / temperature

        # Top-K filtering
        v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
        logits[logits < v[:, [-1]]] = float('-inf')

        # Sampling
        probs = F.softmax(logits, dim=-1)
        next_token = torch.multinomial(probs, num_samples=1)

        input_ids = torch.cat([input_ids, next_token], dim=1)

    return input_ids
```

### Обучение

```python
def train_epoch():
    for x, y in dataloader:
        # Forward
        logits = model(x)
        loss = criterion(logits.view(-1, vocab_size), y.view(-1))

        # Backward
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
```

---

## 📞 Контакты

**Автор:** Джама Ваккасов
**Email:** jamavakkasoff@gmail.com
**Проект:** TamerlanAI - Тюркская LLM модель

---

**🏹 Тәңірі жарылқасын!**
