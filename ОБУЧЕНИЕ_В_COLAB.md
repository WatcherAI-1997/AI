# 🏹 ОБУЧЕНИЕ В GOOGLE COLAB - БЫСТРЫЙ СТАРТ

**Автор:** Джама Ваккасов (jamavakkasoff@gmail.com)

---

## ⚡ Быстрый запуск (5 минут)

### Шаг 1: Клонирование репозитория

В Colab выполните:

```python
# Клонирование репозитория
!git clone https://github.com/ВАШ_USERNAME/AI.git
%cd AI
```

**⚠️ ВАЖНО:** Замените `ВАШ_USERNAME` на ваше имя пользователя GitHub!

---

### Шаг 2: Установка PyTorch

```python
# Проверка GPU
import torch
print(f"🖥️  GPU доступно: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"   GPU: {torch.cuda.get_device_name(0)}")
```

PyTorch уже установлен в Colab! ✅

---

### Шаг 3: Запуск обучения

```python
# ВАРИАНТ 1: Обучение Small модели (быстро, ~30-60 минут)
!python train.py
```

**ИЛИ настройте параметры:**

```python
# ВАРИАНТ 2: Изменить параметры обучения
# Откройте train.py и измените:
# - MODEL_SIZE = 'small'    # 'medium' для лучшего качества
# - NUM_EPOCHS = 10         # Меньше эпох = быстрее
# - BATCH_SIZE = 16         # Больше на GPU = быстрее

!python train.py
```

---

### Шаг 4: Генерация текста

После обучения:

```python
# Генерация с обученной моделью
!python generate.py
```

---

## 📋 Полный notebook для Colab

Используйте готовый notebook: **`Training_Colab.ipynb`**

Или создайте новый notebook и скопируйте код ниже:

---

## 🎯 Пример полного кода для Colab:

```python
# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 1: Клонирование репозитория
# ═══════════════════════════════════════════════════════════════

# Замените на ваш GitHub username!
GITHUB_USERNAME = "ВАШ_USERNAME"
REPO_NAME = "AI"

import os

if GITHUB_USERNAME == "ВАШ_USERNAME":
    print("❌ ОШИБКА: Замените ВАШ_USERNAME на ваше имя пользователя GitHub!")
else:
    repo_url = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
    print(f"📥 Клонирование: {repo_url}")

    !git clone {repo_url}
    os.chdir(REPO_NAME)

    print("\n✅ Репозиторий склонирован!")
    print(f"📂 Текущая папка: {os.getcwd()}")

    # Список файлов
    print("\n📋 Файлы для обучения:")
    !ls -lh train.py generate.py model/

# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 2: Проверка GPU
# ═══════════════════════════════════════════════════════════════

import torch

print("="*80)
print("🖥️  ПРОВЕРКА ОБОРУДОВАНИЯ")
print("="*80)

if torch.cuda.is_available():
    print(f"✅ GPU доступно: {torch.cuda.get_device_name(0)}")
    print(f"   Память: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    print(f"   CUDA версия: {torch.version.cuda}")
else:
    print("⚠️  GPU недоступно, будет использоваться CPU")
    print("   Обучение займет больше времени (~2-4 часа)")

print("="*80)

# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 3: Настройка параметров (опционально)
# ═══════════════════════════════════════════════════════════════

# Если хотите изменить параметры, отредактируйте train.py:

print("\n📝 Текущие параметры в train.py:")
!grep -A 1 "MODEL_SIZE\|NUM_EPOCHS\|BATCH_SIZE\|LEARNING_RATE" train.py | head -20

print("\n💡 Для изменения параметров:")
print("   1. Откройте train.py (двойной клик в панели файлов)")
print("   2. Найдите функцию main()")
print("   3. Измените MODEL_SIZE, NUM_EPOCHS, BATCH_SIZE и т.д.")
print("   4. Сохраните файл (Ctrl+S)")

# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 4: Запуск обучения
# ═══════════════════════════════════════════════════════════════

print("\n" + "="*80)
print("🚀 ЗАПУСК ОБУЧЕНИЯ МОДЕЛИ")
print("="*80)
print("\n⏰ Время обучения:")
print("   • Small model + GPU: ~30-60 минут")
print("   • Small model + CPU: ~2-4 часа")
print("   • Medium model + GPU: ~1-2 часа")
print("=" *80)
print()

# ЗАПУСК!
!python train.py

# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 5: Проверка результатов
# ═══════════════════════════════════════════════════════════════

import os

print("\n" + "="*80)
print("📊 ПРОВЕРКА РЕЗУЛЬТАТОВ ОБУЧЕНИЯ")
print("="*80)

# Проверка чекпоинтов
if os.path.exists('checkpoints/best_model.pt'):
    print("✅ Модель обучена успешно!")
    print(f"   📁 Чекпоинты:")
    !ls -lh checkpoints/
else:
    print("❌ Чекпоинты не найдены. Проверьте логи обучения выше.")

# Проверка токенизатора
if os.path.exists('model/tokenizer.json'):
    print("\n✅ Токенизатор создан!")
else:
    print("\n⚠️  Токенизатор не найден")

print("="*80)

# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 6: Тестирование модели
# ═══════════════════════════════════════════════════════════════

print("\n" + "="*80)
print("🧪 ТЕСТИРОВАНИЕ ОБУЧЕННОЙ МОДЕЛИ")
print("="*80)
print()

# Запуск генерации
!python generate.py

# ═══════════════════════════════════════════════════════════════
# ЯЧЕЙКА 7: Скачивание модели на компьютер
# ═══════════════════════════════════════════════════════════════

from google.colab import files
import shutil
import os

print("\n" + "="*80)
print("💾 СКАЧИВАНИЕ ОБУЧЕННОЙ МОДЕЛИ")
print("="*80)

# Архивирование чекпоинтов
if os.path.exists('checkpoints'):
    print("\n📦 Создание архива...")
    !zip -r tamerlane_model.zip checkpoints/ model/tokenizer.json

    print("\n✅ Архив создан: tamerlane_model.zip")
    print("📥 Скачивание начнется автоматически...")

    files.download('tamerlane_model.zip')

    print("\n✅ Готово! Модель скачана на ваш компьютер.")
else:
    print("\n❌ Папка checkpoints не найдена. Обучите модель сначала.")

print("="*80)
```

---

## ❓ Частые вопросы

### Q: Ошибка "No such file or directory"

**A:** Вы забыли склонировать репозиторий! Выполните:
```python
!git clone https://github.com/ВАШ_USERNAME/AI.git
%cd AI
```

### Q: Ошибка "Repository not found"

**A:**
1. Убедитесь что вы создали репозиторий на GitHub
2. Проверьте что заменили `ВАШ_USERNAME` на ваше имя
3. Убедитесь что репозиторий публичный (Public)

### Q: Out of Memory (OOM)

**A:** Уменьшите параметры:
- `BATCH_SIZE = 4` (вместо 8)
- `MAX_LENGTH = 128` (вместо 256)
- Используйте `MODEL_SIZE = 'small'`

### Q: Обучение слишком долгое

**A:**
- Включите GPU: `Runtime → Change runtime type → GPU`
- Уменьшите `NUM_EPOCHS = 10` (вместо 20)
- Используйте Small модель

### Q: Как продолжить обучение после отключения?

**A:** Colab отключается через 12 часов. Для длительного обучения:
1. Скачивайте чекпоинты периодически
2. Используйте Colab Pro для более длительных сессий
3. Или обучайте локально на своем компьютере

---

## 🎯 Рекомендуемые настройки для Colab

### Для быстрого тестирования:
```python
MODEL_SIZE = 'small'
NUM_EPOCHS = 5
BATCH_SIZE = 16  # На GPU можно больше
MAX_LENGTH = 128
```
⏰ Время: ~15-20 минут на GPU

### Для качественной модели:
```python
MODEL_SIZE = 'medium'
NUM_EPOCHS = 20
BATCH_SIZE = 8
MAX_LENGTH = 256
```
⏰ Время: ~1-2 часа на GPU

### Для максимального качества:
```python
MODEL_SIZE = 'large'
NUM_EPOCHS = 30
BATCH_SIZE = 4
MAX_LENGTH = 512
```
⏰ Время: ~4-6 часов на GPU

---

## ✅ Чеклист запуска в Colab

- [ ] Создан репозиторий на GitHub
- [ ] Код загружен в репозиторий
- [ ] Открыт Google Colab
- [ ] Склонирован репозиторий
- [ ] Проверен доступ к GPU
- [ ] Запущено обучение
- [ ] Обучение завершилось успешно
- [ ] Протестирована генерация
- [ ] Скачана обученная модель

---

**🏹 Тәңірі жарылқасын!**

**Автор:** Джама Ваккасов
**Email:** jamavakkasoff@gmail.com
**Проект:** Tamerlane AI - Тюркская AI модель
