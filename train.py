"""
TAMERLANE AI - ОБУЧЕНИЕ МОДЕЛИ
Скрипт для обучения собственной языковой модели

Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
Проект: Tamerlane AI - Тюркская AI модель
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import os
import time
from datetime import datetime
import json

from model.architecture import create_small_model, create_medium_model, create_large_model
from model.tokenizer import TamerlaneTokenizer, create_turkic_training_corpus
from model.dataset import create_dataloaders


class Trainer:
    """Класс для обучения модели"""

    def __init__(
        self,
        model,
        tokenizer,
        train_loader,
        val_loader,
        learning_rate=3e-4,
        device='cpu'
    ):
        self.model = model.to(device)
        self.tokenizer = tokenizer
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.device = device

        # Оптимизатор (AdamW как в GPT)
        self.optimizer = optim.AdamW(
            model.parameters(),
            lr=learning_rate,
            betas=(0.9, 0.98),
            eps=1e-9
        )

        # Loss function (CrossEntropy для языковых моделей)
        self.criterion = nn.CrossEntropyLoss(
            ignore_index=tokenizer.special_tokens['<PAD>']
        )

        # История обучения
        self.history = {
            'train_loss': [],
            'val_loss': [],
            'learning_rate': []
        }

    def train_epoch(self, epoch):
        """Обучение на одной эпохе"""
        self.model.train()
        total_loss = 0
        num_batches = len(self.train_loader)

        start_time = time.time()

        for batch_idx, batch in enumerate(self.train_loader):
            # Перенос на device
            input_ids = batch['input_ids'].to(self.device)
            target_ids = batch['target_ids'].to(self.device)

            # Прямой проход
            logits = self.model(input_ids)

            # Вычисление loss
            loss = self.criterion(
                logits.view(-1, self.model.vocab_size),
                target_ids.view(-1)
            )

            # Обратное распространение
            self.optimizer.zero_grad()
            loss.backward()

            # Gradient clipping (предотвращение взрыва градиентов)
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)

            self.optimizer.step()

            total_loss += loss.item()

            # Прогресс
            if (batch_idx + 1) % 10 == 0:
                avg_loss = total_loss / (batch_idx + 1)
                elapsed = time.time() - start_time
                print(f"   Эпоха {epoch} | Батч {batch_idx + 1}/{num_batches} | "
                      f"Loss: {avg_loss:.4f} | Время: {elapsed:.1f}s")

        avg_loss = total_loss / num_batches
        return avg_loss

    @torch.no_grad()
    def validate(self):
        """Валидация модели"""
        self.model.eval()
        total_loss = 0
        num_batches = len(self.val_loader)

        for batch in self.val_loader:
            input_ids = batch['input_ids'].to(self.device)
            target_ids = batch['target_ids'].to(self.device)

            logits = self.model(input_ids)

            loss = self.criterion(
                logits.view(-1, self.model.vocab_size),
                target_ids.view(-1)
            )

            total_loss += loss.item()

        avg_loss = total_loss / num_batches
        return avg_loss

    def train(self, num_epochs, save_dir='checkpoints'):
        """
        Основной цикл обучения

        Args:
            num_epochs: Количество эпох
            save_dir: Директория для сохранения чекпоинтов
        """
        os.makedirs(save_dir, exist_ok=True)

        print("\n" + "="*80)
        print("🏹 НАЧАЛО ОБУЧЕНИЯ TAMERLANE AI")
        print("="*80)
        print(f"   Устройство: {self.device}")
        print(f"   Эпох: {num_epochs}")
        print(f"   Параметров модели: {self.model.get_num_parameters():,}")
        print(f"   Батчей обучения: {len(self.train_loader)}")
        print(f"   Батчей валидации: {len(self.val_loader)}")
        print("="*80)
        print()

        best_val_loss = float('inf')

        for epoch in range(1, num_epochs + 1):
            print(f"\n📊 Эпоха {epoch}/{num_epochs}")
            print("-" * 80)

            # Обучение
            train_loss = self.train_epoch(epoch)

            # Валидация
            val_loss = self.validate()

            # Сохранение истории
            self.history['train_loss'].append(train_loss)
            self.history['val_loss'].append(val_loss)

            print(f"\n   ✅ Эпоха {epoch} завершена:")
            print(f"      Train Loss: {train_loss:.4f}")
            print(f"      Val Loss: {val_loss:.4f}")

            # Сохранение лучшей модели
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                checkpoint_path = os.path.join(save_dir, 'best_model.pt')
                self.save_checkpoint(checkpoint_path, epoch, train_loss, val_loss)
                print(f"      💾 Сохранена лучшая модель: {checkpoint_path}")

            # Сохранение каждые 5 эпох
            if epoch % 5 == 0:
                checkpoint_path = os.path.join(save_dir, f'model_epoch_{epoch}.pt')
                self.save_checkpoint(checkpoint_path, epoch, train_loss, val_loss)
                print(f"      💾 Чекпоинт сохранен: {checkpoint_path}")

        print("\n" + "="*80)
        print("✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!")
        print("="*80)
        print(f"   Лучший Val Loss: {best_val_loss:.4f}")
        print()

    def save_checkpoint(self, path, epoch, train_loss, val_loss):
        """Сохранение чекпоинта"""
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'train_loss': train_loss,
            'val_loss': val_loss,
            'history': self.history,
            'model_info': self.model.get_model_info()
        }
        torch.save(checkpoint, path)

    def load_checkpoint(self, path):
        """Загрузка чекпоинта"""
        checkpoint = torch.load(path, map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        self.history = checkpoint['history']
        print(f"✅ Чекпоинт загружен: {path}")
        print(f"   Эпоха: {checkpoint['epoch']}")
        print(f"   Train Loss: {checkpoint['train_loss']:.4f}")
        print(f"   Val Loss: {checkpoint['val_loss']:.4f}")


def main():
    """Основная функция обучения"""

    print("\n" + "="*80)
    print("🏹 TAMERLANE AI - ОБУЧЕНИЕ СОБСТВЕННОЙ МОДЕЛИ")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print("Проект: Tamerlane AI - Тюркская AI модель")
    print("="*80)
    print()

    # Настройки
    VOCAB_SIZE = 10000
    BATCH_SIZE = 8
    MAX_LENGTH = 256
    NUM_EPOCHS = 20
    LEARNING_RATE = 3e-4
    MODEL_SIZE = 'small'  # 'small', 'medium', 'large'

    # Определение устройства
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"🖥️  Устройство: {device}")
    if device == 'cuda':
        print(f"   GPU: {torch.cuda.get_device_name(0)}")
        print(f"   Память: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    print()

    # 1. Создание/загрузка токенизатора
    tokenizer_path = 'model/tokenizer.json'

    if os.path.exists(tokenizer_path):
        print(f"📖 Загрузка токенизатора: {tokenizer_path}")
        tokenizer = TamerlaneTokenizer(vocab_size=VOCAB_SIZE)
        tokenizer.load(tokenizer_path)
    else:
        print("🏗️  Создание и обучение токенизатора...")
        tokenizer = TamerlaneTokenizer(vocab_size=VOCAB_SIZE)

        # Создание корпуса для обучения токенизатора
        corpus = create_turkic_training_corpus()

        # Добавляем тексты из базы знаний
        from model.dataset import create_turkic_dataset
        corpus.extend(create_turkic_dataset()[:500])  # Первые 500 текстов

        tokenizer.train(corpus, verbose=True)
        tokenizer.save(tokenizer_path)

    print()

    # 2. Создание DataLoader'ов
    print("📦 Создание DataLoader'ов...")
    train_loader, val_loader = create_dataloaders(
        tokenizer,
        batch_size=BATCH_SIZE,
        max_length=MAX_LENGTH
    )
    print()

    # 3. Создание модели
    print(f"🏗️  Создание модели ({MODEL_SIZE})...")

    vocab_size = tokenizer.get_vocab_size()

    if MODEL_SIZE == 'small':
        model = create_small_model(vocab_size)
    elif MODEL_SIZE == 'medium':
        model = create_medium_model(vocab_size)
    elif MODEL_SIZE == 'large':
        model = create_large_model(vocab_size)
    else:
        raise ValueError(f"Неизвестный размер модели: {MODEL_SIZE}")

    info = model.get_model_info()
    print(f"   ✅ Модель создана:")
    print(f"      Параметры: {info['parameters_millions']}")
    print(f"      d_model: {info['d_model']}")
    print(f"      Слоев: {info['num_layers']}")
    print()

    # 4. Создание Trainer'а
    print("🎯 Создание Trainer'а...")
    trainer = Trainer(
        model=model,
        tokenizer=tokenizer,
        train_loader=train_loader,
        val_loader=val_loader,
        learning_rate=LEARNING_RATE,
        device=device
    )
    print("   ✅ Trainer готов")
    print()

    # 5. Обучение
    trainer.train(num_epochs=NUM_EPOCHS, save_dir='checkpoints')

    # 6. Сохранение финальной модели
    print("\n💾 Сохранение финальной модели...")
    final_path = 'checkpoints/final_model.pt'
    trainer.save_checkpoint(
        final_path,
        NUM_EPOCHS,
        trainer.history['train_loss'][-1],
        trainer.history['val_loss'][-1]
    )
    print(f"   ✅ Сохранено: {final_path}")

    # 7. Сохранение истории обучения
    history_path = 'checkpoints/training_history.json'
    with open(history_path, 'w') as f:
        json.dump(trainer.history, f, indent=2)
    print(f"   ✅ История сохранена: {history_path}")

    print("\n" + "="*80)
    print("🎉 ВСЁ ГОТОВО! МОДЕЛЬ ОБУЧЕНА!")
    print("="*80)
    print("\nТеперь вы можете использовать модель для генерации текста:")
    print("   python generate.py")
    print()


if __name__ == '__main__':
    main()
