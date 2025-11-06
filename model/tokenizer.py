"""
TAMERLANE TOKENIZER - Токенизатор для тюркских языков
BPE (Byte Pair Encoding) токенизатор

Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
Проект: Tamerlane AI - Тюркская AI модель
"""

import re
import json
from collections import defaultdict, Counter
from typing import List, Dict, Tuple
import os


class TamerlaneTokenizer:
    """
    BPE Токенизатор для тюркских языков

    Поддерживает:
    - Казахский, турецкий, узбекский, и другие тюркские языки
    - Кириллицу и латиницу
    - Специальные символы (𐱅𐰭𐰼𐰃 и др.)
    """

    def __init__(self, vocab_size=32000):
        self.vocab_size = vocab_size

        # Специальные токены
        self.special_tokens = {
            '<PAD>': 0,    # Padding
            '<UNK>': 1,    # Unknown
            '<BOS>': 2,    # Beginning of sentence
            '<EOS>': 3,    # End of sentence
        }

        self.vocab = {}
        self.merges = []
        self.byte_encoder = self._bytes_to_unicode()
        self.byte_decoder = {v: k for k, v in self.byte_encoder.items()}

    def _bytes_to_unicode(self):
        """Создание маппинга байтов в unicode символы"""
        bs = list(range(ord("!"), ord("~")+1)) + \
             list(range(ord("¡"), ord("¬")+1)) + \
             list(range(ord("®"), ord("ÿ")+1))
        cs = bs[:]
        n = 0
        for b in range(2**8):
            if b not in bs:
                bs.append(b)
                cs.append(2**8 + n)
                n += 1
        cs = [chr(n) for n in cs]
        return dict(zip(bs, cs))

    def get_stats(self, ids):
        """Подсчет частот пар токенов"""
        counts = defaultdict(int)
        for pair in zip(ids, ids[1:]):
            counts[pair] += 1
        return counts

    def merge_pair(self, ids, pair, idx):
        """Слияние пары токенов"""
        newids = []
        i = 0
        while i < len(ids):
            if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
                newids.append(idx)
                i += 2
            else:
                newids.append(ids[i])
                i += 1
        return newids

    def train(self, texts: List[str], verbose=True):
        """
        Обучение BPE токенизатора

        Args:
            texts: Список текстов для обучения
            verbose: Показывать прогресс
        """
        if verbose:
            print("🏹 Обучение токенизатора...")
            print(f"   Текстов: {len(texts)}")
            print(f"   Целевой размер словаря: {self.vocab_size}")

        # Начальный словарь - все байты
        num_merges = self.vocab_size - 256 - len(self.special_tokens)

        # Преобразование текстов в байты
        tokens = []
        for text in texts:
            text_bytes = text.encode('utf-8')
            text_tokens = [self.byte_encoder[b] for b in text_bytes]
            tokens.extend(text_tokens)

        if verbose:
            print(f"   Токенов (байтов): {len(tokens)}")

        # Создание начального словаря
        self.vocab = self.special_tokens.copy()
        for i in range(256):
            self.vocab[chr(self.byte_encoder[i])] = len(self.special_tokens) + i

        # BPE обучение
        ids = list(tokens)
        self.merges = []

        for i in range(num_merges):
            stats = self.get_stats(ids)
            if not stats:
                break

            pair = max(stats, key=stats.get)
            idx = len(self.vocab)

            # Создание нового токена из пары
            new_token = pair[0] + pair[1]
            self.vocab[new_token] = idx
            self.merges.append(pair)

            # Слияние пары в ids
            ids = self.merge_pair(ids, pair, idx)

            if verbose and (i + 1) % 1000 == 0:
                print(f"   Merge {i+1}/{num_merges}: {pair} -> {idx} (частота: {stats[pair]})")

        if verbose:
            print(f"✅ Обучение завершено!")
            print(f"   Размер словаря: {len(self.vocab)}")
            print(f"   Merge операций: {len(self.merges)}")

    def encode(self, text: str) -> List[int]:
        """
        Кодирование текста в токены

        Args:
            text: Входной текст

        Returns:
            Список ID токенов
        """
        # Преобразование в байты
        text_bytes = text.encode('utf-8')
        text_tokens = [self.byte_encoder[b] for b in text_bytes]

        # Применение merges
        tokens = text_tokens[:]
        for pair in self.merges:
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == pair[0] and tokens[i+1] == pair[1]:
                    # Находим новый токен
                    new_token = pair[0] + pair[1]
                    if new_token in self.vocab:
                        new_tokens.append(new_token)
                        i += 2
                    else:
                        new_tokens.append(tokens[i])
                        i += 1
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            tokens = new_tokens

        # Преобразование в ID
        ids = []
        for token in tokens:
            if token in self.vocab:
                ids.append(self.vocab[token])
            else:
                ids.append(self.special_tokens['<UNK>'])

        return ids

    def decode(self, ids: List[int]) -> str:
        """
        Декодирование токенов обратно в текст

        Args:
            ids: Список ID токенов

        Returns:
            Декодированный текст
        """
        # Обратный словарь
        id_to_token = {v: k for k, v in self.vocab.items()}

        # Получение токенов
        tokens = []
        for id in ids:
            if id in id_to_token:
                token = id_to_token[id]
                # Пропускаем специальные токены
                if token not in self.special_tokens:
                    tokens.append(token)

        # Объединение токенов
        text = ''.join(tokens)

        # Декодирование байтов
        try:
            text_bytes = bytes([self.byte_decoder[c] for c in text])
            decoded = text_bytes.decode('utf-8', errors='replace')
        except:
            decoded = text

        return decoded

    def save(self, path: str):
        """Сохранение токенизатора"""
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)

        data = {
            'vocab_size': self.vocab_size,
            'vocab': self.vocab,
            'merges': [(a, b) for a, b in self.merges],
            'special_tokens': self.special_tokens
        }

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ Токенизатор сохранен: {path}")

    def load(self, path: str):
        """Загрузка токенизатора"""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.vocab_size = data['vocab_size']
        self.vocab = data['vocab']
        self.merges = [(a, b) for a, b in data['merges']]
        self.special_tokens = data['special_tokens']

        print(f"✅ Токенизатор загружен: {path}")
        print(f"   Размер словаря: {len(self.vocab)}")

    def get_vocab_size(self):
        """Размер словаря"""
        return len(self.vocab)


def create_turkic_training_corpus():
    """Создание корпуса текстов для обучения токенизатора"""
    corpus = [
        # Казахский
        "Тәңірі - қазақтардың ежелгі құдайы. Ол аспан мен жердің жаратушысы.",
        "Тәмірлан - ұлы қолбасшы және мемлекет қайраткері.",
        "Қазақстан - Орта Азиядағы ең үлкен мемлекет.",
        "Біз тюрік халқымыз. Біздің тарихымыз ұзақ және байланған.",

        # Турецкий
        "Tengri, Türklerin eski tanrısıdır. O göğün ve yerin yaratıcısıdır.",
        "Timur, büyük bir komutan ve devlet adamıdır.",
        "Türkiye, Anadolu'daki güçlü bir devlettir.",
        "Biz Türk milletiyiz. Tarihimiz uzun ve zengindir.",

        # Узбекский
        "Tangri - turklar xudosi. U osmon va yerning yaratuvchisi.",
        "Temur - buyuk sarkarda va davlat arbobi.",
        "O'zbekiston - Markaziy Osiyodagi katta davlat.",
        "Biz turk xalqimiz. Bizning tarixim iz uzun va boy.",

        # Русский (для тюркских тем)
        "Тенгри - верховный бог тюрков. Он создатель неба и земли.",
        "Тамерлан - великий полководец и государственный деятель.",
        "Тюркский мир простирается от Якутии до Турции.",

        # Английский (базовый)
        "Tengri is the supreme god of the Turks. He is the creator of heaven and earth.",
        "Tamerlane was a great commander and statesman.",
        "The Turkic world stretches from Yakutia to Turkey.",

        # Орхонские руны
        "𐱅𐰭𐰼𐰃 - это Тенгри на орхонском алфавите.",
        "𐰼𐰇𐰼𐰇𐰏 - древнетюркское письмо.",

        # Общие фразы
        "Здравствуйте! Как дела?",
        "Сәлеметсіз бе! Қалайсыз?",
        "Merhaba! Nasılsınız?",
        "Assalomu alaykum! Qalaysiz?",

        # Технические термины
        "Python - язык программирования для искусственного интеллекта.",
        "Машинное обучение - это часть искусственного интеллекта.",
        "Трансформер - это архитектура нейронной сети.",
        "Tokenizer - это инструмент для разбиения текста на токены.",

        # Математика и наука
        "Математика - царица наук.",
        "Физика изучает законы природы.",
        "Квантовая механика - это раздел физики.",

        # История
        "Тюркский каганат был великой империей.",
        "Орхонские надписи - древнейшие тюркские тексты.",
        "Золотая Орда контролировала огромные территории.",

        # Культура
        "Курай - традиционный музыкальный инструмент.",
        "Домбра - казахский национальный инструмент.",
        "Юрта - традиционное жилище кочевников.",
    ]

    return corpus


if __name__ == '__main__':
    print("="*80)
    print("TAMERLANE TOKENIZER - ОБУЧЕНИЕ И ТЕСТИРОВАНИЕ")
    print("="*80)
    print()

    # Создание корпуса
    print("📚 Создание обучающего корпуса...")
    corpus = create_turkic_training_corpus()
    print(f"   Текстов в корпусе: {len(corpus)}")
    print()

    # Создание и обучение токенизатора
    print("🏹 Создание токенизатора...")
    tokenizer = TamerlaneTokenizer(vocab_size=5000)
    tokenizer.train(corpus, verbose=True)
    print()

    # Сохранение
    tokenizer.save('model/tokenizer.json')
    print()

    # Тестирование
    print("🧪 Тестирование на разных языках:")
    print("="*80)

    test_texts = [
        "Тәңірі жарылқасын!",  # Казахский
        "Tengri korusun!",  # Турецкий
        "Тенгри - верховный бог.",  # Русский
        "𐱅𐰭𐰼𐰃",  # Орхонские руны
        "Hello world!",  # Английский
    ]

    for text in test_texts:
        print(f"\n📝 Текст: {text}")

        # Кодирование
        tokens = tokenizer.encode(text)
        print(f"   Токены: {tokens}")
        print(f"   Количество токенов: {len(tokens)}")

        # Декодирование
        decoded = tokenizer.decode(tokens)
        print(f"   Декодировано: {decoded}")
        print(f"   ✅ Совпадает: {text == decoded}")

    print("\n" + "="*80)
    print("✅ ТОКЕНИЗАТОР ГОТОВ К ИСПОЛЬЗОВАНИЮ!")
    print("="*80)
    print("\nАвтор: Джама Ваккасов (jamavakkasoff@gmail.com)")
