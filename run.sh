#!/bin/bash

# Тамерлан ИИ - Скрипт запуска

echo "🏹 Запуск Тамерлана ИИ..."
echo "================================"

# Проверка наличия Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 не установлен. Пожалуйста, установите Python 3.8+"
    exit 1
fi

# Создание виртуального окружения если его нет
if [ ! -d "venv" ]; then
    echo "📦 Создание виртуального окружения..."
    python3 -m venv venv
fi

# Активация виртуального окружения
echo "🔧 Активация виртуального окружения..."
source venv/bin/activate

# Установка зависимостей
echo "📥 Установка зависимостей..."
pip install -q -r requirements.txt

# Проверка наличия .env файла
if [ ! -f ".env" ]; then
    echo "⚠️  Файл .env не найден. Создаю из .env.example..."
    cp .env.example .env
    echo "❗ Пожалуйста, отредактируйте .env и добавьте ваш OPENAI_API_KEY"
fi

# Запуск приложения
echo "================================"
echo "🚀 Запуск Тамерлана ИИ на http://localhost:5000"
echo "================================"
python3 app.py
