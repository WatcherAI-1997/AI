"""
Тюркская База Знаний для Модели Тамерлан
Turkic Knowledge Base for Tamerlane AI Model

Эта система делает модель умнее через:
- RAG (Retrieval-Augmented Generation)
- Векторный поиск по тюркским данным
- Контекстное обогащение ответов
- Универсальные знания всего мира
"""

import json
from typing import List, Dict, Optional
from datetime import datetime
from universal_knowledge import UniversalKnowledge


class TurkicKnowledgeBase:
    """
    Массивная база знаний о тюркском мире
    """

    def __init__(self):
        self.knowledge = self._initialize_knowledge()
        # Интегрируем универсальные знания
        self._integrate_universal_knowledge()

    def _initialize_knowledge(self) -> Dict:
        """Инициализация базы знаний"""
        return {
            "history": self._get_history_knowledge(),
            "languages": self._get_languages_knowledge(),
            "culture": self._get_culture_knowledge(),
            "geography": self._get_geography_knowledge(),
            "famous_people": self._get_famous_people(),
            "literature": self._get_literature_knowledge(),
            "traditions": self._get_traditions_knowledge(),
            "modern_world": self._get_modern_knowledge()
        }

    def _integrate_universal_knowledge(self):
        """
        Интегрирует универсальные знания мира (математика, физика и т.д.)
        в основную базу знаний
        """
        try:
            universal = UniversalKnowledge()
            # Добавляем все категории универсальных знаний
            for category, items in universal.get_all_knowledge().items():
                if category in self.knowledge:
                    # Если категория уже существует, добавляем к ней
                    self.knowledge[category].extend(items)
                else:
                    # Иначе создаем новую категорию
                    self.knowledge[category] = items

            print(f"✅ Интегрировано {len(universal.get_all_knowledge())} категорий универсальных знаний")
        except Exception as e:
            print(f"⚠️ Ошибка при интеграции универсальных знаний: {e}")
            # Продолжаем работу с тюркской базой

    def _get_history_knowledge(self) -> List[Dict]:
        """Историческая база знаний"""
        return [
            {
                "topic": "Тимур (Тамерлан)",
                "period": "1336-1405",
                "content_ru": "Амир Тимур - великий тюркский полководец и государственный деятель. Основатель империи Тимуридов со столицей в Самарканде. Создал одну из крупнейших империй в истории, простиравшуюся от Дели до Дамаска.",
                "content_kk": "Әмір Темір - ұлы түркі әскербасы және мемлекет қайраткері. Самарқанд қаласын астана еткен Темірлер империясының негізін қалаушы. Делиден Дамаскіге дейін созылған тарихтағы ең ірі империялардың бірін құрды.",
                "content_tr": "Emir Timur - büyük Türk komutan ve devlet adamı. Başkenti Semerkand olan Timurlu İmparatorluğu'nun kurucusu. Delhi'den Şam'a kadar uzanan tarihin en büyük imparatorluklarından birini yarattı.",
                "content_uz": "Amir Temur - buyuk turk sarkarda va davlat arbobi. Samarqand poytaxtli Temuriylar imperiyasining asoschisi. Delidan Damashqgacha cho'zilgan tarixdagi eng yirik imperiyalardan birini yaratdi.",
                "keywords": ["Тимур", "Тамерлан", "Темір", "Timur", "Temur", "empire", "империя", "Самарканд"],
                "importance": 10
            },
            {
                "topic": "Тюркский каганат",
                "period": "552-745",
                "content_ru": "Первое великое тюркское государство. Тюркский каганат объединил тюркские племена и простирался от Манчжурии до Черного моря. Создал письменность - орхоно-енисейские руны.",
                "content_kk": "Бірінші ұлы түркі мемлекеті. Түрік қағанаты түркі тайпаларын біріктіріп, Манчжуриядан Қара теңізге дейін созылды. Орхон-Енисей руналары жазуын жасады.",
                "content_tr": "İlk büyük Türk devleti. Göktürk Kağanlığı Türk kabilelerini birleştirdi ve Mançurya'dan Karadeniz'e kadar uzandı. Orhun-Yenisey runları yazısını oluşturdu.",
                "content_uz": "Birinchi buyuk turk davlati. Turk xoqonligi turk qabilalarini birlashtirdi va Manchuriyadan Qora dengizgacha cho'zildi. Orxon-Yenisey runalarini yaratdi.",
                "keywords": ["каганат", "Göktürk", "руны", "орхон", "древние тюрки"],
                "importance": 9
            },
            {
                "topic": "Османская империя",
                "period": "1299-1922",
                "content_ru": "Одна из величайших империй в истории. Османская империя была основана Османом I и просуществовала более 600 лет. В пике своего могущества контролировала три континента.",
                "content_kk": "Тарихтағы ең ұлы империялардың бірі. Осман империясын I Осман құрды және 600 жылдан астам өмір сүрді. Өз қуатының шыңында үш континентті басқарды.",
                "content_tr": "Tarihin en büyük imparatorluklarından biri. Osmanlı İmparatorluğu Osman I tarafından kuruldu ve 600 yıldan fazla sürdü. Gücünün zirvesinde üç kıtayı kontrol etti.",
                "content_uz": "Tarixdagi eng buyuk imperiyalardan biri. Usmonli imperiyasi I Usmon tomonidan tashkil etildi va 600 yildan ortiq davom etdi. O'z qudratining cho'qqisida uch qit'ani nazorat qildi.",
                "keywords": ["Османская", "Ottoman", "Osmanlı", "Usmonli", "империя"],
                "importance": 10
            },
            {
                "topic": "Золотая Орда",
                "period": "1240-1502",
                "content_ru": "Средневековое государство в Евразии. Часть Монгольской империи, но с сильным тюркским влиянием. Тюркский язык стал государственным, тюркская культура доминировала.",
                "content_kk": "Еуразиядағы орта ғасырлық мемлекет. Моңғол империясының бөлігі, бірақ күшті түркі әсерімен. Түркі тілі мемлекеттік тіл болды, түркі мәдениеті үстемдік етті.",
                "content_tr": "Avrasya'da ortaçağ devleti. Moğol İmparatorluğu'nun bir parçası ama güçlü Türk etkisiyle. Türk dili resmi dil oldu, Türk kültürü hakim oldu.",
                "content_uz": "Yevroosiyo'da o'rta asr davlati. Mo'g'ul imperiyasining qismi, lekin kuchli turk ta'siri bilan. Turk tili davlat tili bo'ldi, turk madaniyati hukmronlik qildi.",
                "keywords": ["Золотая Орда", "Golden Horde", "Алтын Орда", "Altın Orda"],
                "importance": 8
            },
            {
                "topic": "Сельджуки",
                "period": "1037-1194",
                "content_ru": "Великая тюркская династия, которая создала империю от Средней Азии до Анатолии. Сельджуки защищали исламский мир и были предшественниками Османской империи.",
                "content_kk": "Орта Азиядан Анатолияға дейін империя құрған ұлы түркі әулеті. Селжұқтар ислам әлемін қорғады және Осман империясының алғашқылары болды.",
                "content_tr": "Orta Asya'dan Anadolu'ya kadar imparatorluk kuran büyük Türk hanedanı. Selçuklular İslam dünyasını korudular ve Osmanlı İmparatorluğu'nun öncüleri oldular.",
                "content_uz": "O'rta Osiyodan Anadolugacha imperiya qurgan buyuk turk sulolasi. Saljuqiylar islom dunyosini himoya qildilar va Usmonli imperiyasining o'tmishdoshlari bo'ldilar.",
                "keywords": ["Сельджуки", "Seljuk", "Селжұқ", "Saljuq"],
                "importance": 8
            }
        ]

    def _get_languages_knowledge(self) -> List[Dict]:
        """База знаний о тюркских языках"""
        return [
            {
                "language": "Қазақша (Казахский)",
                "family": "Кыпчакская группа",
                "speakers": "13-15 миллионов",
                "script": "Кириллица (переход на латиницу)",
                "features_ru": "Агглютинативный язык. 7 падежей. Сингармонизм гласных. Богатый словарный запас для описания природы степей.",
                "features_kk": "Жалғамалы тіл. 7 септік. Дауысты үндестігі. Дала табиғатын сипаттауға бай сөздік қор.",
                "common_phrases": {
                    "hello": "Сәлеметсіз бе",
                    "thank_you": "Рахмет",
                    "yes": "Иә",
                    "no": "Жоқ",
                    "brother": "Ағайын / Іні"
                },
                "importance": 10
            },
            {
                "language": "Türkçe (Турецкий)",
                "family": "Огузская группа",
                "speakers": "80-90 миллионов",
                "script": "Латиница",
                "features_ru": "Агглютинативный. 6 падежей. Порядок слов SOV. После реформ Ататюрка очищен от арабских и персидских заимствований.",
                "features_tr": "Sondan eklemeli dil. 6 hal. Kelime sırası ÖNY. Atatürk reformlarından sonra Arapça ve Farsça kelimelerden temizlendi.",
                "common_phrases": {
                    "hello": "Merhaba",
                    "thank_you": "Teşekkürler",
                    "yes": "Evet",
                    "no": "Hayır",
                    "brother": "Kardeş"
                },
                "importance": 10
            },
            {
                "language": "O'zbek (Узбекский)",
                "family": "Карлукская группа",
                "speakers": "32-35 миллионов",
                "script": "Латиница",
                "features_ru": "Смешанные черты карлукских и кыпчакских языков. 6 падежей. Влияние фарси на лексику.",
                "features_uz": "Qorluq va qipchoq tillarining aralash xususiyatlari. 6 kelishik. Forscha leksikaga ta'siri.",
                "common_phrases": {
                    "hello": "Salom",
                    "thank_you": "Rahmat",
                    "yes": "Ha",
                    "no": "Yo'q",
                    "brother": "Aka / Uka"
                },
                "importance": 10
            },
            {
                "language": "Azərbaycan (Азербайджанский)",
                "family": "Огузская группа",
                "speakers": "30-35 миллионов",
                "script": "Латиница",
                "features_ru": "Близок к турецкому. Сильное влияние персидского и русского. 6 падежей.",
                "features_az": "Türkcəyə yaxındır. Farsca və ruscanın güclü təsiri. 6 hal.",
                "common_phrases": {
                    "hello": "Salam",
                    "thank_you": "Təşəkkür edirəm",
                    "yes": "Bəli",
                    "no": "Xeyr",
                    "brother": "Qardaş"
                },
                "importance": 9
            }
        ]

    def _get_culture_knowledge(self) -> List[Dict]:
        """База знаний о культуре"""
        return [
            {
                "topic": "Наурыз мейрамы",
                "type": "Праздник",
                "content_ru": "Наурыз - главный праздник тюркских народов, отмечается 21-22 марта. Символизирует новый год, обновление природы, начало весны.",
                "content_kk": "Наурыз - түркі халықтарының басты мейрамы, 21-22 наурызда тойланады. Жаңа жылды, табиғаттың жаңаруын, көктемнің басталуын білдіреді.",
                "content_tr": "Nevruz - Türk halklarının en önemli bayramı, 21-22 Mart'ta kutlanır. Yeni yılı, doğanın yenilenmesini, baharın başlangıcını simgeler.",
                "traditions": ["Наурыз-көже", "Прыжки через костер", "Качели (алтыбақан)", "Борьба", "Айтыс"],
                "importance": 10
            },
            {
                "topic": "Гостеприимство (Қонақжайлылық)",
                "type": "Традиция",
                "content_ru": "Священная традиция всех тюркских народов. Гость - посланник Бога. Лучшая еда, почетное место для гостя.",
                "content_kk": "Барлық түркі халықтарының киелі дәстүрі. Қонақ - Құдайдың елшісі. Ең жақсы тамақ, құрметті орын қонаққа.",
                "content_tr": "Tüm Türk halklarının kutsal geleneği. Misafir - Tanrı'nın elçisi. En iyi yemek, onur yeri misafir için.",
                "importance": 10
            }
        ]

    def _get_geography_knowledge(self) -> List[Dict]:
        """Географическая база"""
        return [
            {
                "location": "Тюркский мир",
                "coordinates": "От Якутии до Турции",
                "content_ru": "Тюркский мир простирается от Восточной Сибири до Балкан. Включает Центральную Азию, Кавказ, часть России, Турцию.",
                "countries": ["Турция", "Казахстан", "Узбекистан", "Азербайджан", "Туркменистан", "Кыргызстан", "Россия (Якутия, Татарстан, Башкортостан)"],
                "population": "Около 200 миллионов носителей тюркских языков",
                "importance": 10
            }
        ]

    def _get_famous_people(self) -> List[Dict]:
        """Известные личности"""
        return [
            {
                "name": "Амир Тимур (Тамерлан)",
                "years": "1336-1405",
                "role": "Полководец, основатель империи",
                "achievements_ru": "Создал одну из крупнейших империй. Покровитель науки и искусства. Построил великолепный Самарканд.",
                "achievements_kk": "Ең ірі империялардың бірін құрды. Ғылым мен өнердің қамқоршысы. Керемет Самарқанд қаласын салдырды.",
                "importance": 10
            },
            {
                "name": "Абай Құнанбайұлы",
                "years": "1845-1904",
                "role": "Поэт, философ",
                "achievements_ru": "Великий казахский поэт и мыслитель. Реформатор казахской культуры. Автор 'Слов назидания'.",
                "achievements_kk": "Ұлы қазақ ақыны және ойшылы. Қазақ мәдениетінің реформаторы. 'Қара сөз' авторы.",
                "importance": 10
            },
            {
                "name": "Мустафа Кемаль Ататюрк",
                "years": "1881-1938",
                "role": "Основатель современной Турции",
                "achievements_ru": "Создал современную Турецкую Республику. Провел модернизацию страны. Реформировал алфавит.",
                "achievements_tr": "Modern Türkiye Cumhuriyeti'ni kurdu. Ülkeyi modernleştirdi. Alfabeyi reforme etti.",
                "importance": 10
            }
        ]

    def _get_literature_knowledge(self) -> List[Dict]:
        """Литературная база"""
        return [
            {
                "work": "Диван-и Хикмет (Дивани-Хикмет)",
                "author": "Ходжа Ахмед Яссави",
                "period": "12 век",
                "content_ru": "Сборник духовных стихов на тюрки. Оказал огромное влияние на тюркскую литературу и суфизм.",
                "importance": 9
            },
            {
                "work": "Кутадгу Билиг (Благодатное знание)",
                "author": "Юсуф Баласагуни",
                "period": "1069-1070",
                "content_ru": "Первое крупное светское произведение на тюркском языке. Трактат о государственном управлении.",
                "importance": 10
            }
        ]

    def _get_traditions_knowledge(self) -> List[Dict]:
        """Традиции и обычаи"""
        return [
            {
                "tradition": "Асар (Помощь)",
                "content_ru": "Коллективная взаимопомощь. Община собирается помочь одной семье в большой работе.",
                "content_kk": "Ұжымдық өзара көмек. Қауым бір отбасына үлкен жұмыста көмектесу үшін жиналады.",
                "importance": 9
            },
            {
                "tradition": "Шілдехана",
                "content_ru": "Праздник по случаю рождения ребенка (40 дней). Важный обряд в жизненном цикле.",
                "content_kk": "Бала туғанда (40 күн) тойлау. Өмірлік циклдегі маңызды рәсім.",
                "importance": 8
            }
        ]

    def _get_modern_knowledge(self) -> List[Dict]:
        """Современный тюркский мир"""
        return [
            {
                "topic": "Тюркский совет",
                "founded": "2009",
                "content_ru": "Организация Тюркских Государств. Объединяет Турцию, Казахстан, Узбекистан, Кыргызстан, Азербайджан. Цель - укрепление сотрудничества.",
                "members": ["Türkiye", "Qazaqstan", "O'zbekiston", "Qırğızstan", "Azərbaycan"],
                "importance": 10
            },
            {
                "topic": "Современная тюркская культура",
                "content_ru": "Возрождение тюркской идентичности. Развитие кино, музыки, литературы. Цифровизация тюркских языков.",
                "examples": ["Турецкие сериалы", "Казахский кино", "Тюркская поп-музыка"],
                "importance": 9
            }
        ]

    def search(self, query: str, category: Optional[str] = None, limit: int = 5) -> List[Dict]:
        """
        Поиск в базе знаний

        Args:
            query: Поисковый запрос
            category: Категория (history, languages, culture и т.д.)
            limit: Максимальное количество результатов
        """
        results = []
        query_lower = query.lower()

        # Определяем категории для поиска
        categories = [category] if category else self.knowledge.keys()

        for cat in categories:
            if cat not in self.knowledge:
                continue

            for item in self.knowledge[cat]:
                score = self._calculate_relevance(query_lower, item)
                if score > 0:
                    results.append({
                        "category": cat,
                        "content": item,
                        "relevance": score
                    })

        # Сортируем по релевантности
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results[:limit]

    def _calculate_relevance(self, query: str, item: Dict) -> float:
        """Расчет релевантности (поддерживает тюркские и универсальные знания)"""
        score = 0.0

        # Разбиваем запрос на отдельные слова для более умного поиска
        query_words = [w.lower() for w in query.split() if len(w) > 2]

        # Проверяем keywords если есть
        if 'keywords' in item:
            for keyword in item['keywords']:
                keyword_lower = keyword.lower()
                # Проверяем как полное совпадение
                if keyword_lower in query:
                    score += 2.0
                # Проверяем по словам
                for word in query_words:
                    if word in keyword_lower or keyword_lower in word:
                        score += 1.5

        # Проверяем topic/название (высокий приоритет)
        if 'topic' in item and isinstance(item['topic'], str):
            topic_lower = item['topic'].lower()
            # Полное совпадение
            if query in topic_lower:
                score += 3.0
            # Частичное совпадение по словам
            for word in query_words:
                if word in topic_lower:
                    score += 2.0

        # Проверяем категорию
        if 'category' in item and isinstance(item['category'], str):
            category_lower = item['category'].lower()
            if query in category_lower:
                score += 1.5
            for word in query_words:
                if word in category_lower:
                    score += 1.0

        # Проверяем все текстовые поля (content_kk, content_tr, content_uz, content_ru, и т.д.)
        for key, value in item.items():
            if isinstance(value, str):
                value_lower = value.lower()
                # Полное совпадение запроса
                if query in value_lower:
                    if key.startswith('content_'):
                        score += 1.5
                    else:
                        score += 1.0
                # Частичное совпадение по словам
                for word in query_words:
                    if word in value_lower:
                        if key.startswith('content_'):
                            score += 0.5
                        else:
                            score += 0.3

        # Проверяем списки формул (для математики/физики)
        if 'formulas' in item and isinstance(item['formulas'], list):
            for formula in item['formulas']:
                if query in formula.lower():
                    score += 2.0

        # Бонус за importance
        if 'importance' in item:
            score *= (item['importance'] / 10.0)

        return score

    def get_context_for_query(self, query: str, max_context_length: int = 2000) -> str:
        """
        Получить контекст для обогащения ответа модели

        Args:
            query: Запрос пользователя
            max_context_length: Максимальная длина контекста
        """
        # Ищем релевантную информацию
        results = self.search(query, limit=5)

        if not results:
            return ""

        # Формируем контекст
        context_parts = ["[КОНТЕКСТ ИЗ БАЗЫ ЗНАНИЙ ТЮРКСКОГО МИРА]"]

        current_length = len(context_parts[0])

        for result in results:
            item = result['content']

            # Формируем текст для этого элемента
            item_text = f"\n\n📚 Категория: {result['category']}\n"

            if 'topic' in item:
                item_text += f"Тема: {item['topic']}\n"

            # Добавляем контент на разных языках
            for lang in ['content_ru', 'content_kk', 'content_tr', 'content_uz']:
                if lang in item:
                    item_text += f"{item[lang]}\n"

            # Проверяем длину
            if current_length + len(item_text) > max_context_length:
                break

            context_parts.append(item_text)
            current_length += len(item_text)

        context_parts.append("\n[КОНЕЦ КОНТЕКСТА]\n")
        return "".join(context_parts)

    def get_stats(self) -> Dict:
        """Статистика базы знаний"""
        stats = {}
        for category, items in self.knowledge.items():
            stats[category] = len(items)

        stats['total'] = sum(stats.values())
        return stats


# Singleton экземпляр
_knowledge_base_instance = None


def get_knowledge_base() -> TurkicKnowledgeBase:
    """Получить глобальный экземпляр базы знаний"""
    global _knowledge_base_instance
    if _knowledge_base_instance is None:
        _knowledge_base_instance = TurkicKnowledgeBase()
    return _knowledge_base_instance
