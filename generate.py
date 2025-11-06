"""
TAMERLANE AI - ГЕНЕРАЦИЯ ТЕКСТА
Использование обученной модели для генерации текста

Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
Проект: Tamerlane AI - Тюркская AI модель
"""

import torch
import os

from model.architecture import TamerlaneGPT
from model.tokenizer import TamerlaneTokenizer


class TamerlaneGenerator:
    """Класс для генерации текста с помощью обученной модели"""

    def __init__(self, model_path, tokenizer_path, device='cpu'):
        """
        Args:
            model_path: Путь к чекпоинту модели
            tokenizer_path: Путь к токенизатору
            device: Устройство ('cpu' или 'cuda')
        """
        self.device = device

        # Загрузка токенизатора
        print(f"📖 Загрузка токенизатора...")
        self.tokenizer = TamerlaneTokenizer()
        self.tokenizer.load(tokenizer_path)

        # Загрузка модели
        print(f"🏗️  Загрузка модели...")
        checkpoint = torch.load(model_path, map_location=device)

        model_info = checkpoint['model_info']
        vocab_size = self.tokenizer.get_vocab_size()

        # Создание модели с параметрами из чекпоинта
        self.model = TamerlaneGPT(
            vocab_size=vocab_size,
            d_model=model_info['d_model'],
            num_layers=model_info['num_layers']
        )

        # Загрузка весов
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.model.to(device)
        self.model.eval()

        print(f"✅ Модель загружена успешно!")
        print(f"   Эпоха: {checkpoint['epoch']}")
        print(f"   Val Loss: {checkpoint['val_loss']:.4f}")
        print()

    def generate(self, prompt, max_length=100, temperature=1.0, top_k=50):
        """
        Генерация текста

        Args:
            prompt: Начальный текст (промпт)
            max_length: Максимальная длина генерируемого текста
            temperature: Температура сэмплирования (выше = более случайно)
            top_k: Top-K сэмплирование

        Returns:
            Сгенерированный текст
        """
        # Токенизация промпта
        input_ids = self.tokenizer.encode(prompt)

        # Добавление BOS токена
        bos_token = self.tokenizer.special_tokens['<BOS>']
        input_ids = [bos_token] + input_ids

        # Преобразование в тензор
        input_tensor = torch.tensor([input_ids], dtype=torch.long).to(self.device)

        # Генерация
        with torch.no_grad():
            output_tensor = self.model.generate(
                input_tensor,
                max_new_tokens=max_length,
                temperature=temperature,
                top_k=top_k
            )

        # Декодирование
        output_ids = output_tensor[0].tolist()

        # Убираем специальные токены
        bos = self.tokenizer.special_tokens['<BOS>']
        eos = self.tokenizer.special_tokens['<EOS>']
        pad = self.tokenizer.special_tokens['<PAD>']

        filtered_ids = []
        for id in output_ids:
            if id == eos:
                break
            if id not in [bos, pad]:
                filtered_ids.append(id)

        # Декодирование текста
        generated_text = self.tokenizer.decode(filtered_ids)

        return generated_text

    def interactive_mode(self):
        """Интерактивный режим генерации"""
        print("\n" + "="*80)
        print("🏹 TAMERLANE AI - ИНТЕРАКТИВНАЯ ГЕНЕРАЦИЯ")
        print("="*80)
        print("\nВведите начальный текст (или 'exit' для выхода)")
        print("Параметры: max_length=100, temperature=0.8, top_k=50")
        print("="*80)
        print()

        while True:
            try:
                prompt = input("\n📝 Промпт: ").strip()

                if prompt.lower() in ['exit', 'quit', 'выход']:
                    print("\n👋 До свидания!")
                    break

                if not prompt:
                    print("⚠️  Пустой промпт. Попробуйте еще раз.")
                    continue

                print("\n⏳ Генерация...")

                generated = self.generate(
                    prompt=prompt,
                    max_length=100,
                    temperature=0.8,
                    top_k=50
                )

                print("\n" + "-"*80)
                print("💬 Сгенерированный текст:")
                print("-"*80)
                print(generated)
                print("-"*80)

            except KeyboardInterrupt:
                print("\n\n👋 До свидания!")
                break
            except Exception as e:
                print(f"\n❌ Ошибка: {e}")


def main():
    """Основная функция"""

    print("\n" + "="*80)
    print("🏹 TAMERLANE AI - ГЕНЕРАЦИЯ ТЕКСТА С ОБУЧЕННОЙ МОДЕЛЬЮ")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
    print("Проект: Tamerlane AI - Тюркская AI модель")
    print("="*80)
    print()

    # Пути к файлам
    model_path = 'checkpoints/best_model.pt'
    tokenizer_path = 'model/tokenizer.json'

    # Проверка наличия файлов
    if not os.path.exists(model_path):
        print(f"❌ Модель не найдена: {model_path}")
        print("Сначала обучите модель: python train.py")
        return

    if not os.path.exists(tokenizer_path):
        print(f"❌ Токенизатор не найден: {tokenizer_path}")
        print("Сначала обучите модель: python train.py")
        return

    # Определение устройства
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"🖥️  Устройство: {device}")
    print()

    # Создание генератора
    generator = TamerlaneGenerator(
        model_path=model_path,
        tokenizer_path=tokenizer_path,
        device=device
    )

    # Демонстрация
    print("🧪 Демонстрация генерации:")
    print("="*80)

    demo_prompts = [
        "Тенгри",
        "Тәмірлан",
        "Искусственный интеллект",
        "Математика",
        "Тюркский мир",
    ]

    for i, prompt in enumerate(demo_prompts, 1):
        print(f"\n{i}. Промпт: '{prompt}'")
        print("-"*80)

        generated = generator.generate(
            prompt=prompt,
            max_length=50,
            temperature=0.8,
            top_k=50
        )

        print(f"Результат: {generated}")

    print("\n" + "="*80)

    # Интерактивный режим
    print("\n🎯 Хотите попробовать сами? (y/n)")
    choice = input("Ответ: ").strip().lower()

    if choice in ['y', 'yes', 'д', 'да']:
        generator.interactive_mode()
    else:
        print("\n👋 До свидания!")


if __name__ == '__main__':
    main()
