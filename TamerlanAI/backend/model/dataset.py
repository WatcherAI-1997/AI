"""
TAMERLANE DATASET - Обработка данных для обучения

Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
Проект: Tamerlane AI - Тюркская AI модель
"""

import torch
from torch.utils.data import Dataset, DataLoader
from typing import List
import random


class TextDataset(Dataset):
    """Dataset для обучения языковой модели"""

    def __init__(self, texts: List[str], tokenizer, max_length=512):
        """
        Args:
            texts: Список текстов
            tokenizer: Токенизатор
            max_length: Максимальная длина последовательности
        """
        self.tokenizer = tokenizer
        self.max_length = max_length

        # Токенизация всех текстов
        print(f"📝 Токенизация {len(texts)} текстов...")
        self.examples = []

        for i, text in enumerate(texts):
            # Добавляем BOS и EOS токены
            tokens = [tokenizer.special_tokens['<BOS>']]
            tokens.extend(tokenizer.encode(text))
            tokens.append(tokenizer.special_tokens['<EOS>'])

            # Разбиваем на чанки если текст длинный
            for j in range(0, len(tokens), max_length - 1):
                chunk = tokens[j:j + max_length]
                if len(chunk) > 1:  # Минимум 2 токена (вход и выход)
                    self.examples.append(chunk)

            if (i + 1) % 1000 == 0:
                print(f"   Обработано: {i + 1}/{len(texts)}")

        print(f"✅ Создано {len(self.examples)} примеров для обучения")

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        tokens = self.examples[idx]

        # Входные токены (все кроме последнего)
        input_ids = tokens[:-1]

        # Целевые токены (все кроме первого)
        target_ids = tokens[1:]

        # Padding до max_length
        pad_token = self.tokenizer.special_tokens['<PAD>']

        while len(input_ids) < self.max_length - 1:
            input_ids.append(pad_token)
            target_ids.append(pad_token)

        return {
            'input_ids': torch.tensor(input_ids, dtype=torch.long),
            'target_ids': torch.tensor(target_ids, dtype=torch.long)
        }


def create_turkic_dataset():
    """
    Создание датасета для обучения на тюркских языках

    Возвращает список текстов для обучения
    """

    # База знаний из существующих модулей
    from turkic_knowledge_base import get_knowledge_base
    from tengri_knowledge import get_tengri_knowledge
    from ancient_languages import get_ancient_languages

    texts = []

    print("📚 Сборка обучающего датасета...")

    # 1. Тюркская база знаний
    print("   Загрузка тюркской базы знаний...")
    kb = get_knowledge_base()
    for category in kb:
        for item in category['items']:
            content = item['content']
            if isinstance(content, dict):
                for key, value in content.items():
                    if isinstance(value, str):
                        texts.append(value)
                    elif isinstance(value, list):
                        texts.extend([str(v) for v in value])
            elif isinstance(content, str):
                texts.append(content)

    print(f"      Собрано из базы знаний: {len(texts)} текстов")

    # 2. Тенгрианство
    print("   Загрузка знаний о Тенгри...")
    tengri = get_tengri_knowledge()
    for item in tengri:
        content = item['content']
        if isinstance(content, dict):
            for key, value in content.items():
                if isinstance(value, str):
                    texts.append(value)
                elif isinstance(value, list):
                    texts.extend([str(v) for v in value])
        elif isinstance(content, str):
            texts.append(content)

    print(f"      Собрано о Тенгри: {len(texts) - len(texts)} текстов")

    # 3. Древние языки
    print("   Загрузка древних языков...")
    ancient = get_ancient_languages()
    for lang in ancient:
        if 'content' in lang:
            content = lang['content']
            if isinstance(content, dict):
                for key, value in content.items():
                    if isinstance(value, str):
                        texts.append(value)
                    elif isinstance(value, list):
                        texts.extend([str(v) for v in value])

    # 4. Дополнительные обучающие тексты
    additional_texts = [
        # Казахский
        "Қазақстан - Орталық Азиядағы ең үлкен мемлекет. Астана - елордасы.",
        "Тәуелсіздік күні - 16 желтоқсан. Бұл қазақ халқы үшін маңызды күн.",
        "Абай Құнанбаев - ұлы қазақ ақыны және философы.",
        "Алтын Адам - қазақстандық археологиялық табыс.",
        "Байтерек - Астанадағы белгілі монумент.",

        # Турецкий
        "Türkiye, Anadolu'da yer alan güçlü bir ülkedir. Ankara başkentidir.",
        "Mustafa Kemal Atatürk, Türkiye Cumhuriyeti'nin kurucusudur.",
        "İstanbul, Avrupa ve Asya kıtalarını birleştiren bir şehirdir.",
        "Türk dili, Altay dil ailesine aittir.",

        # Узбекский
        "O'zbekiston - Markaziy Osiyo davlati. Toshkent poytaxti.",
        "Amir Temur - buyuk sarkarda va davlat arbobi.",
        "Samarqand - qadimiy shahar va madaniy markaz.",
        "O'zbek tili - turkiy tillar oilasiga mansub.",

        # О Тенгри
        "Тенгри - верховный бог тюркских народов. Он создатель неба и земли.",
        "Умай - богиня плодородия и покровительница детей.",
        "Эрлик - владыка подземного мира в тюркской мифологии.",
        "Тенгрианство - древняя религия тюрков.",

        # История
        "Тюркский каганат существовал с VI по VIII века.",
        "Орхонские надписи - древнейшие тюркские письменные памятники.",
        "Золотая Орда была могущественным государством.",
        "Тамерлан создал великую империю в XIV веке.",

        # Наука и технологии
        "Искусственный интеллект - это область компьютерных наук.",
        "Машинное обучение позволяет компьютерам учиться на данных.",
        "Нейронные сети моделируют работу человеческого мозга.",
        "Трансформеры - это современная архитектура для обработки языка.",

        # Математика
        "Математика - наука о числах, количествах и пространствах.",
        "Алгебра изучает математические структуры и операции.",
        "Геометрия исследует свойства пространства и фигур.",
        "Математический анализ изучает пределы и производные.",

        # Повседневные фразы
        "Сәлеметсіз бе! Қалайсыз? Жақсы болыңыз!",
        "Merhaba! Nasılsınız? İyi günler!",
        "Assalomu alaykum! Qalaysiz? Yaxshi bo'ling!",
        "Здравствуйте! Как дела? Всего доброго!",
    ]

    texts.extend(additional_texts)

    print(f"✅ Всего собрано: {len(texts)} текстов")

    # Дедупликация
    texts = list(set(texts))
    print(f"   После дедупликации: {len(texts)} текстов")

    # Фильтрация пустых и слишком коротких
    texts = [t for t in texts if isinstance(t, str) and len(t.strip()) > 10]
    print(f"   После фильтрации: {len(texts)} текстов")

    # Перемешивание
    random.shuffle(texts)

    return texts


def create_dataloaders(tokenizer, batch_size=8, max_length=512, train_split=0.9):
    """
    Создание DataLoader'ов для обучения и валидации

    Args:
        tokenizer: Токенизатор
        batch_size: Размер батча
        max_length: Максимальная длина последовательности
        train_split: Доля обучающей выборки

    Returns:
        train_loader, val_loader
    """

    # Создание датасета
    texts = create_turkic_dataset()

    # Разделение на train/val
    split_idx = int(len(texts) * train_split)
    train_texts = texts[:split_idx]
    val_texts = texts[split_idx:]

    print(f"\n📊 Разделение данных:")
    print(f"   Обучение: {len(train_texts)} текстов")
    print(f"   Валидация: {len(val_texts)} текстов")

    # Создание датасетов
    train_dataset = TextDataset(train_texts, tokenizer, max_length)
    val_dataset = TextDataset(val_texts, tokenizer, max_length)

    # Создание загрузчиков
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=0
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=0
    )

    print(f"\n✅ DataLoader'ы созданы:")
    print(f"   Train batches: {len(train_loader)}")
    print(f"   Val batches: {len(val_loader)}")

    return train_loader, val_loader


if __name__ == '__main__':
    from tokenizer import TamerlaneTokenizer

    print("="*80)
    print("TAMERLANE DATASET - СОЗДАНИЕ ОБУЧАЮЩИХ ДАННЫХ")
    print("="*80)
    print()

    # Создание токенизатора
    print("🏹 Создание токенизатора...")
    tokenizer = TamerlaneTokenizer(vocab_size=10000)

    # Создание корпуса
    texts = create_turkic_dataset()

    # Обучение токенизатора
    print(f"\n📚 Обучение токенизатора на {len(texts)} текстах...")
    tokenizer.train(texts[:100], verbose=True)  # На небольшой выборке для демо

    # Создание DataLoader'ов
    print("\n📦 Создание DataLoader'ов...")
    train_loader, val_loader = create_dataloaders(
        tokenizer,
        batch_size=4,
        max_length=128
    )

    # Тест загрузки батча
    print("\n🧪 Тест загрузки батча:")
    batch = next(iter(train_loader))
    print(f"   Input IDs shape: {batch['input_ids'].shape}")
    print(f"   Target IDs shape: {batch['target_ids'].shape}")

    print("\n" + "="*80)
    print("✅ ДАТАСЕТ ГОТОВ К ОБУЧЕНИЮ!")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
