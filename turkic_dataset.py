"""
Тюркский датасет для обучения модели Тамерлан
Turkic Dataset for Tamerlane Model Training

Этот датасет используется для fine-tuning моделей
на тюркских данных, делая их умнее для тюркского мира
"""

import json
from typing import List, Dict


class TurkicDataset:
    """Генератор датасета для обучения"""

    def __init__(self):
        self.dataset = self._generate_dataset()

    def _generate_dataset(self) -> List[Dict]:
        """Генерация обучающего датасета"""
        return [
            # Исторические вопросы
            {
                "messages": [
                    {"role": "user", "content": "Тәмірлан кім еді?"},
                    {"role": "assistant", "content": "Сәлеметсіз бе! Тәмірлан (1336-1405) - ұлы түркі әскербасы және мемлекет қайраткері. Ол Самарқанд қаласын астана еткен Темірлер империясының негізін қалаушы. Оның империясы Делиден Дамаскіге дейін созылды. Тәмірлан ғылым мен өнердің қамқоршысы болды."}
                ],
                "metadata": {"language": "kazakh", "category": "history"}
            },
            {
                "messages": [
                    {"role": "user", "content": "Timur kimdir?"},
                    {"role": "assistant", "content": "Merhaba kardeşim! Timur (Tamerlane) 1336-1405 yılları arasında yaşamış büyük Türk komutan ve devlet adamıdır. Semerkand başkentli Timurlu İmparatorluğu'nu kurmuştur. İmparatorluğu Delhi'den Şam'a kadar uzanmıştır. Timur aynı zamanda bilim ve sanatın büyük destekçisiydi."}
                ],
                "metadata": {"language": "turkish", "category": "history"}
            },
            {
                "messages": [
                    {"role": "user", "content": "Расскажи о Тюркском каганате"},
                    {"role": "assistant", "content": "Сәлем! Түрік қағанаты (552-745 жж.) - бірінші ұлы түркі мемлекеті!\n\nТюркский каганат (Göktürk Kağanlığı / Turk xoqonligi) - первое великое тюркское государство. Он объединил тюркские племена и простирался от Манчжурии до Черного моря.\n\n🏛️ Достижения:\n• Создал орхоно-енисейскую письменность\n• Объединил тюркские народы\n• Контролировал Великий Шелковый путь\n• Заложил основы тюркской государственности\n\nОрхон-Енисей жазулары - бұл түрік тілінің ең ежелгі жазба ескерткіштері!"}
                ],
                "metadata": {"language": "multilingual", "category": "history"}
            },

            # Языковые вопросы
            {
                "messages": [
                    {"role": "user", "content": "Түркі тілдері туралы айтып бер"},
                    {"role": "assistant", "content": "Сәлеметсіз бе, ағайын!\n\nТүркі тілдер тобы - үлкен және бай тілдер отбасы:\n\n**Қыпшақ тобы:**\n• Қазақша - 15 млн\n• Татарча - 7 млн\n• Башҡортса - 1.5 млн\n• Кыргызча - 5 млн\n\n**Оғыз тобы:**\n• Türkçe - 85 млн\n• Azərbaycan - 32 млн\n• Түркмен - 8 млн\n\n**Қарлұқ тобы:**\n• O'zbek - 35 млн\n• Uyğur - 10 млн\n\nБарлығы 200 миллионнан астам адам түркі тілдерінде сөйлейді! Бұл біздің ортақ мұрамыз."}
                ],
                "metadata": {"language": "kazakh", "category": "language"}
            },

            # Культурные вопросы
            {
                "messages": [
                    {"role": "user", "content": "Nevruz nedir?"},
                    {"role": "assistant", "content": "Merhaba! Nevruz (Наурыз / Navruz) - түркі халықтарының ең басты мейрамы!\n\n🌸 **Ne zaman:** 21-22 Mart / 21-22 наурыз\n\n**Anlamı:**\n• Yeni yıl / Жаңа жыл\n• Baharın başlangıcı / Көктемнің басталуы  \n• Doğanın uyanışı / Табиғаттың оянуы\n\n**Gelenekler:**\n• Nevruz aşı (Наурыз-көже)\n• Ateş üzerinden atlama\n• Akrabaları ziyaret\n• Алтыбақан (salıncak)\n• Спорттық ойындар\n\nБұл барлық түркі халықтары үшін ортақ мереке. UNESCO мұрасы!"}
                ],
                "metadata": {"language": "turkish", "category": "culture"}
            },

            # Программирование на тюркских языках
            {
                "messages": [
                    {"role": "user", "content": "Python тілінде функция қалай жазылады?"},
                    {"role": "assistant", "content": "Сәлем, ағайын! Python-да функция жазу өте оңай:\n\n```python\ndef сәлемдесу(ат):  # функция / fonksiyon\n    \"\"\"Сәлемдесу функциясы\"\"\"\n    return f\"Сәлем, {ат}!\"\n\n# Пайдалану / Kullanım\nхабар = сәлемдесу(\"Әли\")\nprint(хабар)  # Шығару: Сәлем, Әли!\n```\n\n**Түсіндірме:**\n• `def` - функцияны анықтау (tanımlamak)\n• `сәлемдесу` - функция аты (isim)\n• `ат` - параметр (parametre)\n• `return` - қайтару (döndürmek)\n\nPython-да кирилицалық айнымалылар қолдануға болады! 🎉"}
                ],
                "metadata": {"language": "kazakh", "category": "programming"}
            },

            # География
            {
                "messages": [
                    {"role": "user", "content": "Түрік әлемі қайда орналасқан?"},
                    {"role": "assistant", "content": "Сәлеметсіз бе! Түрік әлемі өте кең аумаққа таралған:\n\n🌍 **География:**\n• Шығыстан (Якутия) батысқа (Түркия) дейін\n• Орталық Азия - негізгі аймақ\n• Кавказ, Еділ-Жайық өңірі\n• Балкандар бір бөлігі\n\n🏴 **Мемлекеттер:**\n• Türkiye Cumhuriyeti 🇹🇷\n• Qazaqstan Respublikası 🇰🇿\n• O'zbekiston Respublikasi 🇺🇿\n• Azərbaycan Respublikası 🇦🇿\n• Түркменистан 🇹🇲\n• Кыргыз Республикасы 🇰🇬\n\n👥 **Халық саны:** ~200 миллион түркі тілінде сөйлейтін адам!\n\nБұл Еуразияның үлкен бөлігі - Түрік дүниесі!"}
                ],
                "metadata": {"language": "kazakh", "category": "geography"}
            },

            # Современность
            {
                "messages": [
                    {"role": "user", "content": "Türk Konseyi nedir?"},
                    {"role": "assistant", "content": "Merhaba! Түрік Кеңесі (Türk Konseyi / Тюркский Совет) - түркі мемлекеттерінің ұйымы.\n\n**Құрылған:** 2009 жыл / 2009 yılı\n\n**Мүшелер:**\n🇹🇷 Türkiye\n🇰🇿 Qazaqstan  \n🇺🇿 O'zbekiston\n🇰🇬 Qırğızstan\n🇦🇿 Azərbaycan\n\n**Бақылаушы:** Türkmenistan, Macaristan\n\n**Мақсаттар:**\n✓ Экономикалық ынтымақтастық\n✓ Мәдени байланыстар\n✓ Түркі тілдерін дамыту\n✓ Бірлесіп жұмыс істеу\n\n2021'de adı 'Türk Devletleri Teşkilatı' olarak değiştirildi. Biz біргеміз - türk dünyası! 🏹"}
                ],
                "metadata": {"language": "multilingual", "category": "modern"}
            },

            # Литература
            {
                "messages": [
                    {"role": "user", "content": "Абай туралы айтып бер"},
                    {"role": "assistant", "content": "Сәлеметсіз бе!\n\nАбай Құнанбайұлы (1845-1904) - ұлы қазақ ақыны, философы және ағартушысы.\n\n📚 **Шығармалары:**\n• \"Қара сөздер\" (Слова назидания) - философиялық трактат\n• 170+ өлең\n• Аудармалар (Пушкин, Лермонтов, Крылов)\n\n💭 **Философиясы:**\n• Білім - бақыттың кілті\n• Халықты ағарту керек\n• Әділеттілік, еңбек, ізгілік\n\n🌟 **Әсері:**\nАбай қазақ әдебиетін реформалады. Оның идеялары бүкіл түркі әлеміне әсер етті.\n\n*\"Адам бол!\"* - оның негізгі үндеуі.\n\nАбай - это не просто поэт, это философ масштаба Тургенева для казахского народа!"}
                ],
                "metadata": {"language": "kazakh", "category": "literature"}
            }
        ]

    def get_dataset(self, category: str = None, language: str = None) -> List[Dict]:
        """
        Получить датасет с фильтрацией

        Args:
            category: Категория (history, language, culture и т.д.)
            language: Язык (kazakh, turkish, russian и т.д.)
        """
        filtered = self.dataset

        if category:
            filtered = [d for d in filtered if d['metadata'].get('category') == category]

        if language:
            filtered = [d for d in filtered if d['metadata'].get('language') == language]

        return filtered

    def export_for_finetuning(self, output_file: str, format: str = 'jsonl'):
        """
        Экспорт датасета для fine-tuning

        Args:
            output_file: Путь к выходному файлу
            format: Формат (jsonl, json)
        """
        if format == 'jsonl':
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in self.dataset:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
        elif format == 'json':
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.dataset, f, ensure_ascii=False, indent=2)

        print(f"✅ Датасет экспортирован: {output_file}")
        print(f"📊 Всего примеров: {len(self.dataset)}")

    def get_stats(self) -> Dict:
        """Статистика датасета"""
        categories = {}
        languages = {}

        for item in self.dataset:
            cat = item['metadata'].get('category', 'unknown')
            lang = item['metadata'].get('language', 'unknown')

            categories[cat] = categories.get(cat, 0) + 1
            languages[lang] = languages.get(lang, 0) + 1

        return {
            "total": len(self.dataset),
            "categories": categories,
            "languages": languages
        }


# Функция для быстрого доступа
def get_turkic_dataset() -> TurkicDataset:
    """Получить датасет"""
    return TurkicDataset()
