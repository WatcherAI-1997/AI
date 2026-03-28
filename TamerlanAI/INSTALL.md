# 🏹 TamerlanAI - Инструкция по установке

**Автор:** Джама Ваккасов (jamavakkasoff@gmail.com)

---

## ⚡ САМЫЙ ПРОСТОЙ СПОСОБ (Рекомендуется!)

### Одна команда - все готово!

```bash
cd TamerlanAI
chmod +x install.sh
./install.sh
```

**Что делает скрипт:**
1. ✅ Проверяет Python 3.8+
2. ✅ Устанавливает PyTorch (CPU версия)
3. ✅ Устанавливает все зависимости (FastAPI, Uvicorn, etc.)
4. ✅ Создает необходимые директории
5. ✅ Обучает модель TamerlaneGPT (~2 минуты)
6. ✅ Создает скрипты start.sh и test.sh

**Время установки:** ~3-5 минут

---

## 🚀 Запуск после установки

```bash
cd TamerlanAI/backend
./start.sh
```

Или:

```bash
cd TamerlanAI/backend
python3 main.py
```

**Сервер запустится на:** http://localhost:8000

---

## 🧪 Проверка работы

```bash
cd TamerlanAI/backend
./test.sh
```

Или:

```bash
cd TamerlanAI/backend
python3 test_real.py
```

**Вы должны увидеть:**
```
🏹 TESTING TAMERLANAI - REAL MODEL
✅ Server is healthy
Language: kk | User: Сәлем! TamerlanAI туралы айтып бер
Assistant: system қазақ..,! TamerlanAI
✅ TESTING COMPLETED
```

---

## 📦 Ручная установка (если нужно)

### Шаг 1: Установка PyTorch

```bash
cd TamerlanAI/backend
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Для GPU:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Шаг 2: Установка зависимостей

```bash
pip install -r requirements-full.txt
```

Или вручную:
```bash
pip install fastapi uvicorn pydantic pydantic-settings python-dotenv python-multipart requests
```

### Шаг 3: Обучение модели

```bash
python3 train_demo.py
```

**Результат:**
```
🏹 ОБУЧЕНИЕ TAMERLANEGPT
Device: cpu
Training examples: 38
Vocabulary size: 265
Model: 3.30M parameters

Epoch   1/100 | Loss: 2.5434
...
Epoch 100/100 | Loss: 0.0008

✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!
Model saved to: checkpoints/best_model.pt
```

### Шаг 4: Копирование модели

```bash
mkdir -p models
cp checkpoints/best_model.pt models/
cp checkpoints/tokenizer.json models/
```

### Шаг 5: Запуск сервера

```bash
python3 main.py
```

---

## 🔍 Проверка установки

### 1. Проверка здоровья сервера

```bash
curl http://localhost:8000/health
```

**Ожидаемый ответ:**
```json
{
  "status": "healthy",
  "app": "TamerlanAI",
  "version": "1.0.0"
}
```

### 2. Тест чата (казахский)

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Сәлем!"}], "language": "kk"}'
```

### 3. Тест чата (турецкий)

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Merhaba!"}], "language": "tr"}'
```

### 4. Список моделей

```bash
curl http://localhost:8000/api/v1/models/
```

---

## 📚 Документация API

После запуска сервера откройте в браузере:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## ⚙️ Системные требования

### Минимальные:
- Python 3.8+
- 1GB RAM
- 500MB свободного места на диске
- Интернет для установки зависимостей

### Рекомендуемые:
- Python 3.10+
- 2GB RAM
- 1GB свободного места
- CPU с AVX2 для ускорения PyTorch

### Для GPU (опционально):
- NVIDIA GPU с CUDA 11.8+
- 2GB+ VRAM

---

## 🐛 Решение проблем

### Ошибка: "ModuleNotFoundError: No module named 'torch'"

**Решение:**
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Ошибка: "python3: command not found"

**Решение:**
Установите Python 3.8+:
- Ubuntu/Debian: `sudo apt install python3 python3-pip`
- macOS: `brew install python3`
- Windows: Скачайте с python.org

### Ошибка: "Address already in use"

**Решение:**
Порт 8000 занят. Используйте другой порт:
```bash
uvicorn main:app --port 8001
```

### Модель не обучается / очень медленно

**Решение:**
- Уменьшите количество эпох в train_demo.py (строка 227)
- Уменьшите batch_size (строка 227)
- Для ускорения используйте GPU

### Ошибка: "Out of memory"

**Решение:**
- Уменьшите batch_size в train_demo.py
- Закройте другие программы
- Увеличьте swap память

---

## 📁 Структура после установки

```
TamerlanAI/
├── install.sh              # ✅ Скрипт установки
├── README.md              # Краткое описание
├── INSTALL.md             # Этот файл
└── backend/
    ├── models/            # ✅ Обученная модель
    │   ├── best_model.pt      # TamerlaneGPT модель (40MB)
    │   └── tokenizer.json     # Токенизатор (6KB)
    ├── checkpoints/       # Backup модели
    ├── start.sh          # ✅ Запуск сервера
    ├── test.sh           # ✅ Тесты
    ├── main.py           # Сервер
    ├── train_demo.py     # Обучение
    └── test_real.py      # Тесты
```

---

## 🔄 Переобучение модели

Если хотите переобучить модель с другими данными:

1. Отредактируйте `backend/train_demo.py`
2. Добавьте свои тексты в функцию `get_training_data()`
3. Запустите обучение:
   ```bash
   cd TamerlanAI/backend
   python3 train_demo.py
   ```
4. Скопируйте новую модель:
   ```bash
   cp checkpoints/best_model.pt models/
   cp checkpoints/tokenizer.json models/
   ```

---

## ⏱️ Время работы

- **Установка зависимостей:** 1-2 минуты
- **Обучение модели:** 2-3 минуты (CPU)
- **Запуск сервера:** 5-10 секунд
- **Генерация ответа:** ~0.6 секунд (CPU)

---

## 🎯 Что дальше?

После успешной установки:

1. **Изучите API:** http://localhost:8000/docs
2. **Прочитайте документацию:** [backend/README_RU.md](backend/README_RU.md)
3. **Протестируйте:** `python3 test_real.py`
4. **Интегрируйте в свой проект**

---

## 📞 Поддержка

Если возникли проблемы:
- Email: jamavakkasoff@gmail.com
- Проверьте логи: `backend/logs/`
- Перечитайте документацию

---

## 🏹 Тәңірі жарылқасын!

Удачи в использовании TamerlanAI!
