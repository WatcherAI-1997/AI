"""
Быстрое обучение TamerlaneGPT на демо-данных
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import os
import sys
from pathlib import Path

# Добавляем путь к модулям
sys.path.append(str(Path(__file__).parent))

from model.architecture import create_small_model
from model.simple_tokenizer import SimpleTokenizer


class SimpleTextDataset(Dataset):
    """Простой датасет для обучения"""

    def __init__(self, texts, tokenizer, max_length=128):
        self.tokenizer = tokenizer
        self.max_length = max_length

        # Токенизация всех текстов
        self.examples = []
        for text in texts:
            tokens = tokenizer.encode(text)
            if len(tokens) > 1:
                # Разбиваем на чанки если длинный
                for i in range(0, len(tokens) - 1, max_length // 2):
                    chunk = tokens[i:i + max_length]
                    if len(chunk) > 5:  # Минимум 5 токенов
                        self.examples.append(chunk)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        tokens = self.examples[idx]

        # Pad если нужно
        if len(tokens) < self.max_length:
            tokens = tokens + [0] * (self.max_length - len(tokens))
        else:
            tokens = tokens[:self.max_length]

        x = torch.tensor(tokens[:-1], dtype=torch.long)
        y = torch.tensor(tokens[1:], dtype=torch.long)

        return x, y


def get_training_data():
    """Получить тренировочные данные"""
    return [
        # Казахский язык
        "Сәлеметсіз бе! Мен TamerlanAI - тюрк халықтары үшін арнайы жасалған жасанды интеллект жүйесімін.",
        "Қазақстан - Орталық Азиядағы ең үлкен мемлекет. Астана - оның астанасы.",
        "Тәуелсіздік - халықтың ең қымбат қазынасы. Біз тәуелсіз елміз.",
        "Білім - жарық, надандық - қараңғылық. Оқу - бақытқа жету жолы.",
        "Абай Құнанбаев - ұлы қазақ ақыны және ойшылы.",
        "Қазақ тілі - менің ана тілім. Мен қазақша сөйлеймін.",

        # Турецкий язык
        "Merhaba! Ben TamerlanAI - Türk halkları için özel olarak tasarlanmış yapay zeka sistemiyim.",
        "Türkiye Cumhuriyeti Anadolu ve Trakya'da kurulmuş bir devlettir.",
        "Bilim ışıktır, cehalet karanlıktır. Öğrenmek mutluluğa giden yoldur.",
        "Mustafa Kemal Atatürk Türkiye Cumhuriyeti'nin kurucusudur.",
        "Türk dili çok zengin bir dildir. Ben Türkçe konuşuyorum.",

        # Русский язык
        "Здравствуйте! Я TamerlanAI - система искусственного интеллекта, созданная специально для тюркских народов.",
        "Знание - свет, невежество - тьма. Учиться - путь к счастью.",
        "Дружба народов - основа мира и процветания.",
        "Россия - многонациональная страна с богатой историей.",
        "Русский язык - один из мировых языков. Я говорю по-русски.",

        # Английский язык
        "Hello! I am TamerlanAI - an artificial intelligence system designed specifically for Turkic peoples.",
        "Knowledge is power. Learning is the path to happiness.",
        "Unity in diversity is the foundation of peace.",
        "English is an international language. I speak English.",

        # Общие фразы
        "TamerlanAI поддерживает 14 тюркских языков: казахский, турецкий, узбекский, азербайджанский и другие.",
        "Tamerlane (Тимур) был великим завоевателем и правителем XIV века.",
        "Тюркский мир един в своем культурном и историческом многообразии.",
        "Искусственный интеллект помогает людям решать сложные задачи.",

        # Вопросы и ответы
        "Вопрос: Что такое TamerlanAI? Ответ: TamerlanAI - это искусственный интеллект для тюркских языков.",
        "Вопрос: Сколько языков поддерживает TamerlanAI? Ответ: TamerlanAI поддерживает 23 языка.",
        "Сұрақ: TamerlanAI не үшін қажет? Жауап: Ол тюрк халықтарына көмектесу үшін қажет.",
        "Soru: TamerlanAI kaç dili destekliyor? Cevap: TamerlanAI 23 dili destekliyor.",

        # Больше контента для лучшего обучения
        "Программирование - это искусство создания программ на компьютере.",
        "Python - популярный язык программирования для искусственного интеллекта.",
        "Нейронные сети обучаются на больших объемах данных.",
        "Трансформеры - это современная архитектура нейронных сетей.",
        "GPT означает Generative Pre-trained Transformer.",
        "Машинное обучение - подраздел искусственного интеллекта.",

        # Еще больше примеров для разнообразия
        "Орталық Азия - көне өркениеттер мекені.",
        "Anadolu medeniyetlerin beşiğidir.",
        "Культура тюркских народов очень богата и разнообразна.",
        "The Turkic world spans from Eastern Europe to Siberia.",
    ]


def train_model(num_epochs=50, batch_size=4, learning_rate=0.001):
    """Обучение модели"""

    print("="*80)
    print("🏹 ОБУЧЕНИЕ TAMERLANEGPT")
    print("="*80)
    print(f"Автор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🖥️  Device: {device}")
    if device == "cuda":
        print(f"   GPU: {torch.cuda.get_device_name(0)}")
    print()

    # Подготовка данных
    print("📚 Preparing training data...")
    texts = get_training_data()
    print(f"   Training examples: {len(texts)}")

    # Создание и обучение токенизатора
    print("\n🔤 Training tokenizer...")
    tokenizer = SimpleTokenizer(vocab_size=5000)
    tokenizer.train(texts, verbose=True)
    print(f"   Vocabulary size: {len(tokenizer.vocab)}")

    # Сохранение токенизатора
    os.makedirs("checkpoints", exist_ok=True)
    tokenizer.save("checkpoints/tokenizer.json")
    print("   ✅ Tokenizer saved to checkpoints/tokenizer.json")

    # Создание датасета
    print("\n📦 Creating dataset...")
    dataset = SimpleTextDataset(texts, tokenizer, max_length=64)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    print(f"   Dataset size: {len(dataset)} examples")

    # Создание модели
    print("\n🧠 Creating model...")
    vocab_size = len(tokenizer.vocab)
    model = create_small_model(vocab_size)
    model.to(device)

    model_info = model.get_model_info()
    print(f"   Model: {model_info['parameters_millions']} parameters")

    # Optimizer и loss
    optimizer = optim.AdamW(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()

    print(f"\n🚀 Starting training for {num_epochs} epochs...")
    print()

    best_loss = float('inf')

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        num_batches = 0

        for batch_idx, (x, y) in enumerate(dataloader):
            x, y = x.to(device), y.to(device)

            # Forward pass
            optimizer.zero_grad()
            logits = model(x)

            # Compute loss
            loss = criterion(logits.view(-1, vocab_size), y.view(-1))

            # Backward pass
            loss.backward()

            # Gradient clipping
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

            optimizer.step()

            total_loss += loss.item()
            num_batches += 1

        avg_loss = total_loss / num_batches

        # Логирование
        if (epoch + 1) % 10 == 0 or epoch == 0:
            print(f"Epoch {epoch+1:3d}/{num_epochs} | Loss: {avg_loss:.4f}")

        # Сохранение лучшей модели
        if avg_loss < best_loss:
            best_loss = avg_loss
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': avg_loss,
            }, 'checkpoints/best_model.pt')

    print()
    print("="*80)
    print("✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!")
    print("="*80)
    print(f"Best loss: {best_loss:.4f}")
    print("Model saved to: checkpoints/best_model.pt")
    print("Tokenizer saved to: checkpoints/tokenizer.json")
    print()
    print("Теперь можете запустить сервер:")
    print("  python main.py")
    print()


if __name__ == "__main__":
    train_model(num_epochs=100, batch_size=8, learning_rate=0.001)
