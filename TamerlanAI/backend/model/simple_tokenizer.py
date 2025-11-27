"""
Простой Word-Level Токенизатор
Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
"""

import json
import re
from typing import List, Dict
from collections import Counter


class SimpleTokenizer:
    """Простой word-level токенизатор для демо"""

    def __init__(self, vocab_size=5000):
        self.vocab_size = vocab_size
        self.special_tokens = {
            '<PAD>': 0,
            '<UNK>': 1,
            '<BOS>': 2,
            '<EOS>': 3,
        }
        self.vocab = self.special_tokens.copy()
        self.inverse_vocab = {v: k for k, v in self.vocab.items()}

    def train(self, texts: List[str], verbose=True):
        """Обучение токенизатора"""
        if verbose:
            print("🏹 Обучение токенизатора...")
            print(f"   Текстов: {len(texts)}")

        # Собираем все слова и символы
        all_tokens = []
        for text in texts:
            # Разбиваем на слова и символы
            tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
            all_tokens.extend(tokens)

        # Подсчет частот
        token_counts = Counter(all_tokens)

        if verbose:
            print(f"   Уникальных токенов: {len(token_counts)}")

        # Берем топ токенов
        max_tokens = self.vocab_size - len(self.special_tokens)
        most_common = token_counts.most_common(max_tokens)

        # Добавляем в vocab
        for token, _ in most_common:
            if token not in self.vocab:
                self.vocab[token] = len(self.vocab)

        self.inverse_vocab = {v: k for k, v in self.vocab.items()}

        if verbose:
            print(f"✅ Словарь создан: {len(self.vocab)} токенов")

    def encode(self, text: str) -> List[int]:
        """Кодирование текста"""
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        ids = []
        for token in tokens:
            ids.append(self.vocab.get(token, self.vocab['<UNK>']))
        return ids

    def decode(self, ids: List[int]) -> str:
        """Декодирование токенов"""
        tokens = []
        for id in ids:
            token = self.inverse_vocab.get(id, '<UNK>')
            if token not in self.special_tokens:
                tokens.append(token)

        # Склеиваем токены
        text = ""
        for i, token in enumerate(tokens):
            if i > 0 and token not in ",.!?;:-–—" and tokens[i-1] not in "([{":
                text += " "
            text += token

        return text

    def save(self, path: str):
        """Сохранение токенизатора"""
        data = {
            'vocab': self.vocab,
            'vocab_size': self.vocab_size,
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, path: str):
        """Загрузка токенизатора"""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.vocab = data['vocab']
        self.vocab_size = data['vocab_size']
        self.inverse_vocab = {v: k for k, v in self.vocab.items()}
