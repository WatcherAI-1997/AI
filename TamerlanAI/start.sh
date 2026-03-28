#!/bin/bash
# TamerlanAI Quick Start Script
# Автор: Джама Ваккасов (jamavakkasoff@gmail.com)

echo "================================================================="
echo "🏹 TAMERLANAI - UNIVERSAL MULTILINGUAL AI SYSTEM"
echo "================================================================="
echo ""
echo "Автор: Джама Ваккасов (jamavakkasoff@gmail.com)"
echo ""

# Переход в папку backend
cd "$(dirname "$0")/backend" || exit

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 не найден!"
    echo "Установите Python 3.8+ и попробуйте снова"
    exit 1
fi

echo "✅ Python найден: $(python3 --version)"
echo ""

# Проверка зависимостей
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "📦 Установка минимальных зависимостей..."
    pip install -r requirements-minimal.txt || {
        echo "❌ Ошибка установки зависимостей"
        exit 1
    }
    echo "✅ Зависимости установлены"
else
    echo "✅ Зависимости уже установлены"
fi

echo ""
echo "🚀 Запуск TamerlanAI..."
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "================================================================="
echo ""

# Запуск сервера
python3 main_simple.py
