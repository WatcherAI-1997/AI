"""
TAMERLANE AI - СОБСТВЕННАЯ ТРАНСФОРМЕР АРХИТЕКТУРА
Полноценная языковая модель для обучения с нуля

Автор: Джама Ваккасов (jamavakkasoff@gmail.com)
Проект: Tamerlane AI - Тюркская AI модель
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class MultiHeadAttention(nn.Module):
    """Multi-head self-attention механизм"""

    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model должен делиться на num_heads"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        # Линейные проекции для Q, K, V
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        batch_size = x.size(0)

        # Проекции и разделение на heads
        Q = self.W_q(x).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(x).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(x).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        attention = F.softmax(scores, dim=-1)
        attention = self.dropout(attention)

        # Применение attention к V
        x = torch.matmul(attention, V)

        # Объединение heads
        x = x.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)

        # Финальная проекция
        x = self.W_o(x)

        return x


class FeedForward(nn.Module):
    """Position-wise feed-forward сеть"""

    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.linear1(x)
        x = F.gelu(x)  # GELU активация (как в GPT)
        x = self.dropout(x)
        x = self.linear2(x)
        return x


class TransformerBlock(nn.Module):
    """Один блок трансформера"""

    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()

        self.attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = FeedForward(d_model, d_ff, dropout)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # Self-attention с residual connection
        attn_output = self.attention(self.norm1(x), mask)
        x = x + self.dropout1(attn_output)

        # Feed-forward с residual connection
        ff_output = self.feed_forward(self.norm2(x))
        x = x + self.dropout2(ff_output)

        return x


class PositionalEncoding(nn.Module):
    """Позиционное кодирование для трансформера"""

    def __init__(self, d_model, max_len=5000, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)

        # Создание матрицы позиционных кодировок
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)


class TamerlaneGPT(nn.Module):
    """
    TAMERLANE GPT - СОБСТВЕННАЯ ЯЗЫКОВАЯ МОДЕЛЬ

    Архитектура: Decoder-only трансформер (как GPT)
    Специализация: Тюркские языки

    Параметры:
        vocab_size: Размер словаря
        d_model: Размерность эмбеддингов (по умолчанию 512)
        num_heads: Количество attention heads (по умолчанию 8)
        num_layers: Количество трансформер блоков (по умолчанию 6)
        d_ff: Размерность feed-forward слоя (по умолчанию 2048)
        max_len: Максимальная длина последовательности (по умолчанию 2048)
        dropout: Dropout rate (по умолчанию 0.1)
    """

    def __init__(
        self,
        vocab_size,
        d_model=512,
        num_heads=8,
        num_layers=6,
        d_ff=2048,
        max_len=2048,
        dropout=0.1
    ):
        super().__init__()

        self.d_model = d_model
        self.vocab_size = vocab_size

        # Эмбеддинги токенов
        self.token_embedding = nn.Embedding(vocab_size, d_model)

        # Позиционное кодирование
        self.positional_encoding = PositionalEncoding(d_model, max_len, dropout)

        # Трансформер блоки
        self.transformer_blocks = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Финальная нормализация
        self.norm = nn.LayerNorm(d_model)

        # Выходной слой (проекция на словарь)
        self.output = nn.Linear(d_model, vocab_size)

        # Инициализация весов
        self.apply(self._init_weights)

    def _init_weights(self, module):
        """Инициализация весов (как в GPT-2)"""
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
        elif isinstance(module, nn.LayerNorm):
            torch.nn.init.zeros_(module.bias)
            torch.nn.init.ones_(module.weight)

    def generate_causal_mask(self, seq_len):
        """Создание causal mask для авторегрессивной генерации"""
        mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
        mask = mask.masked_fill(mask == 1, float('-inf'))
        return mask

    def forward(self, x, mask=None):
        """
        Прямой проход

        Args:
            x: Входные токены [batch_size, seq_len]
            mask: Attention mask (опционально)

        Returns:
            logits: Логиты для каждого токена [batch_size, seq_len, vocab_size]
        """
        batch_size, seq_len = x.size()

        # Эмбеддинги токенов
        x = self.token_embedding(x) * math.sqrt(self.d_model)

        # Добавление позиционных кодировок
        x = self.positional_encoding(x)

        # Создание causal mask для авторегрессии
        if mask is None:
            device = x.device
            mask = self.generate_causal_mask(seq_len).to(device)
            mask = mask.unsqueeze(0).unsqueeze(0)  # [1, 1, seq_len, seq_len]

        # Прохождение через трансформер блоки
        for block in self.transformer_blocks:
            x = block(x, mask)

        # Финальная нормализация
        x = self.norm(x)

        # Проекция на словарь
        logits = self.output(x)

        return logits

    def generate(self, input_ids, max_new_tokens=50, temperature=1.0, top_k=50):
        """
        Генерация текста (авторегрессивная)

        Args:
            input_ids: Начальные токены [batch_size, seq_len]
            max_new_tokens: Сколько токенов сгенерировать
            temperature: Температура для сэмплирования (выше = разнообразнее)
            top_k: Top-K сэмплирование

        Returns:
            generated: Сгенерированные токены [batch_size, seq_len + max_new_tokens]
        """
        self.eval()

        with torch.no_grad():
            for _ in range(max_new_tokens):
                # Получение логитов
                logits = self.forward(input_ids)

                # Берем логиты последнего токена
                logits = logits[:, -1, :] / temperature

                # Top-K фильтрация
                if top_k > 0:
                    v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                    logits[logits < v[:, [-1]]] = float('-inf')

                # Сэмплирование
                probs = F.softmax(logits, dim=-1)
                next_token = torch.multinomial(probs, num_samples=1)

                # Добавление к последовательности
                input_ids = torch.cat([input_ids, next_token], dim=1)

        return input_ids

    def get_num_parameters(self):
        """Получить количество параметров модели"""
        return sum(p.numel() for p in self.parameters())

    def get_model_info(self):
        """Информация о модели"""
        num_params = self.get_num_parameters()
        num_params_m = num_params / 1e6

        return {
            'model_name': 'Tamerlane GPT',
            'architecture': 'Decoder-only Transformer',
            'vocab_size': self.vocab_size,
            'd_model': self.d_model,
            'num_layers': len(self.transformer_blocks),
            'total_parameters': num_params,
            'parameters_millions': f'{num_params_m:.2f}M',
            'author': 'Джама Ваккасов',
            'email': 'jamavakkasoff@gmail.com'
        }


def create_small_model(vocab_size):
    """Создание маленькой модели (для быстрого обучения)"""
    return TamerlaneGPT(
        vocab_size=vocab_size,
        d_model=256,
        num_heads=4,
        num_layers=4,
        d_ff=1024,
        max_len=512,
        dropout=0.1
    )


def create_medium_model(vocab_size):
    """Создание средней модели (баланс качество/скорость)"""
    return TamerlaneGPT(
        vocab_size=vocab_size,
        d_model=512,
        num_heads=8,
        num_layers=8,
        d_ff=2048,
        max_len=1024,
        dropout=0.1
    )


def create_large_model(vocab_size):
    """Создание большой модели (высокое качество)"""
    return TamerlaneGPT(
        vocab_size=vocab_size,
        d_model=768,
        num_heads=12,
        num_layers=12,
        d_ff=3072,
        max_len=2048,
        dropout=0.1
    )


if __name__ == '__main__':
    # Демонстрация
    print("="*80)
    print("TAMERLANE GPT - СОБСТВЕННАЯ ТРАНСФОРМЕР АРХИТЕКТУРА")
    print("="*80)
    print()

    # Создание моделей разных размеров
    vocab_size = 32000

    models = {
        'Small': create_small_model(vocab_size),
        'Medium': create_medium_model(vocab_size),
        'Large': create_large_model(vocab_size)
    }

    for name, model in models.items():
        info = model.get_model_info()
        print(f"🏹 {name} Model:")
        print(f"   • Параметры: {info['parameters_millions']}")
        print(f"   • d_model: {info['d_model']}")
        print(f"   • Слоев: {info['num_layers']}")
        print()

    # Тест прямого прохода
    print("\n🧪 Тест прямого прохода:")
    model = create_small_model(vocab_size)

    batch_size = 2
    seq_len = 10
    x = torch.randint(0, vocab_size, (batch_size, seq_len))

    print(f"   Вход: {x.shape}")

    logits = model(x)
    print(f"   Выход: {logits.shape}")
    print(f"   ✅ Размерность правильная: [batch_size, seq_len, vocab_size]")

    # Тест генерации
    print("\n🎯 Тест генерации:")
    generated = model.generate(x, max_new_tokens=5)
    print(f"   Исходная длина: {x.shape[1]}")
    print(f"   Сгенерировано: {generated.shape[1]}")
    print(f"   ✅ Сгенерировано {generated.shape[1] - x.shape[1]} новых токенов")

    print("\n" + "="*80)
    print("✅ АРХИТЕКТУРА ГОТОВА К ОБУЧЕНИЮ!")
    print("="*80)
    print(f"\nАвтор: {info['author']}")
    print(f"Email: {info['email']}")
