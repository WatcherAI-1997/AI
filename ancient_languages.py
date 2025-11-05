"""
Древние Языки с Алфавитами - Ancient Languages with Alphabets
Для модели Тамерлан

Включает:
- Орхонский алфавит (древнетюркская руница)
- Древнерусский язык
- Латынь, древнегреческий, санскрит и другие
"""

from typing import Dict, List, Optional


class AncientLanguages:
    """Система древних языков с алфавитами и текстами"""

    def __init__(self):
        self.languages = self._initialize_ancient_languages()

    def _initialize_ancient_languages(self) -> Dict:
        """Инициализация древних языков"""
        return {
            'orkhon_turkic': self._get_orkhon_turkic(),
            'old_russian': self._get_old_russian(),
            'old_church_slavonic': self._get_old_church_slavonic(),
            'latin': self._get_latin(),
            'ancient_greek': self._get_ancient_greek(),
            'sanskrit': self._get_sanskrit(),
            'ancient_egyptian': self._get_ancient_egyptian(),
            'sumerian': self._get_sumerian(),
            'phoenician': self._get_phoenician(),
            'aramaic': self._get_aramaic(),
            'old_norse': self._get_old_norse(),
            'classical_chinese': self._get_classical_chinese(),
        }

    def _get_orkhon_turkic(self) -> Dict:
        """Орхонский алфавит - Древнетюркская руница"""
        return {
            'name': 'Орхоно-енисейская руница',
            'name_en': 'Orkhon-Yenisei Runes',
            'name_native': '𐰼𐰇𐰚 𐰋𐰃𐱅𐰃𐰏',
            'period': '8-10 века н.э.',
            'family': 'Тюркская',
            'script': 'Орхонская руница',

            'alphabet': {
                'description': 'Древнетюркское руническое письмо',
                'letters': {
                    # Реальные орхонские руны (Unicode)
                    '𐰀': 'a',
                    '𐰁': 'ä',
                    '𐰂': 'b',
                    '𐰃': 'i',
                    '𐰄': 'ï',
                    '𐰅': 'o',
                    '𐰆': 'ö',
                    '𐰇': 'u',
                    '𐰈': 'ü',
                    '𐰉': 'p',
                    '𐰊': 't',
                    '𐰋': 'd',
                    '𐰌': 'k',
                    '𐰍': 'g',
                    '𐰎': 'n',
                    '𐰏': 'ng',
                    '𐰐': 'l',
                    '𐰑': 'r',
                    '𐰒': 's',
                    '𐰓': 'š',
                    '𐰔': 'z',
                    '𐰕': 'y',
                    '𐰖': 'č',
                    '𐰗': 'ñ',
                    '𐰘': 'm',
                },
                'full_alphabet': '𐰀𐰁𐰂𐰃𐰄𐰅𐰆𐰇𐰈𐰉𐰊𐰋𐰌𐰍𐰎𐰏𐰐𐰑𐰒𐰓𐰔𐰕𐰖𐰗𐰘'
            },

            'famous_texts': [
                {
                    'name': 'Кюль-Тегинская надпись',
                    'name_en': 'Kül Tigin Inscription',
                    'year': '732 г. н.э.',
                    'original': '𐱅𐰇𐰼𐰜 𐰋𐰃𐰠𐰏𐰀 𐰴𐰍𐰣',
                    'transliteration': 'Türk bilge qağan',
                    'translation_ru': 'Тюркский мудрый каган',
                    'translation_en': 'Turkic wise khagan',
                    'content': """𐱅𐰇𐰼𐰜 𐰋𐰃𐰠𐰏𐰀 𐰴𐰍𐰣 𐰇𐰠𐰏𐰀𐰤 𐰘𐰀𐰼𐰍𐰣
(Türk bilge qağan ölgen yarğan)

Тюркский мудрый каган умер и был похоронен.

Это одна из старейших тюркских надписей!"""
                },
                {
                    'name': 'Орхонские надписи - Начало',
                    'original': '𐱅𐰭𐰼𐰃 𐰚𐰇𐰚𐰀 𐰋𐰃𐰼 𐱅𐰇𐰼𐰜',
                    'transliteration': 'Tengri kökä bir Türk',
                    'translation_ru': 'Тенгри на небесах, один тюрк',
                    'translation_en': 'Tengri in heaven, one Turk',
                    'content': """Полный текст:

𐱅𐰭𐰼𐰃 𐰚𐰇𐰚𐰀 𐰋𐰃𐰼 𐱅𐰇𐰼𐰜 𐰚𐰇𐰚𐰀 𐰋𐰃𐰼 𐱅𐰇𐰼𐰜

(Tengri kökä bir Türk, kökä bir Türk)

Тенгри на небесах, тюрк один, на небесах тюрк один."""
                }
            ],

            'common_phrases': {
                'tengri': {'runes': '𐱅𐰭𐰼𐰃', 'meaning': 'Тенгри (Бог Неба)'},
                'turk': {'runes': '𐱅𐰇𐰼𐰜', 'meaning': 'Тюрк'},
                'qagan': {'runes': '𐰴𐰍𐰣', 'meaning': 'Каган'},
                'bilge': {'runes': '𐰋𐰃𐰠𐰏𐰀', 'meaning': 'Мудрый'},
                'el': {'runes': '𐰀𐰠', 'meaning': 'Народ, государство'},
                'kök': {'runes': '𐰚𐰇𐰚', 'meaning': 'Небо, синий'},
            },

            'grammar': """**ГРАММАТИКА ДРЕВНЕТЮРКСКОГО:**

Агглютинативный язык (как все тюркские)
Порядок слов: Подлежащее - Дополнение - Сказуемое

Примеры аффиксов:
-ïm (мой): qağan-ïm (мой каган)
-ïmïz (наш): el-imiz (наш народ)
-ta/-te (в): kök-te (на небе)
-dan/-den (от): türk-ten (от тюрка)
""",

            'importance': 10
        }

    def _get_old_russian(self) -> Dict:
        """Древнерусский язык"""
        return {
            'name': 'Древнерусский язык',
            'name_en': 'Old East Slavic',
            'name_native': 'Роусьскыи ѩзыкъ',
            'period': '10-14 века н.э.',
            'family': 'Славянская',
            'script': 'Кириллица (старая)',

            'alphabet': {
                'description': 'Кириллица с юсами, ятями и ижицами',
                'letters': 'А Б В Г Д Е Ж Ѕ З И І К Л М Н О П Р С Т У Ф Х Ѡ Ц Ч Ш Щ Ъ Ы Ь Ѣ Ю Ѫ Ѭ Ѧ Ѩ Ѯ Ѱ Ѳ Ѵ',
                'special_letters': {
                    'Ѣ': 'ять (yat) - широкое "е"',
                    'Ѫ': 'большой юс - носовой звук',
                    'Ѧ': 'малый юс - носовой звук',
                    'Ѳ': 'фита - "ф" в греческих словах',
                    'Ѵ': 'ижица - "и" в греческих словах',
                    'І': 'и десятеричное',
                    'Ѡ': 'омега',
                }
            },

            'famous_texts': [
                {
                    'name': 'Остромирово Евангелие',
                    'year': '1056-1057 гг.',
                    'original': 'Въ начѧлѣ бѣ слово и слово бѣ къ богоу и богъ бѣ слово',
                    'modern': 'В начале было слово и слово было к богу и бог был слово',
                    'translation_en': 'In the beginning was the Word, and the Word was with God, and the Word was God'
                },
                {
                    'name': 'Слово о полку Игореве',
                    'year': '12 век',
                    'original': 'Не лѣпо ли ны бяшетъ, братие, начяти старыми словесы трудныхъ повѣстий о пълку Игоревѣ',
                    'modern': 'Не лучше ли нам, братья, начать старыми словами трудных повестей о полку Игореве',
                    'translation_en': 'Would it not be better for us, brothers, to begin with ancient words the difficult tale of Igor\'s campaign'
                },
                {
                    'name': 'Русская Правда',
                    'year': '11 век',
                    'original': 'Аще оубиеть моуж моужа то мьстити братоу брата',
                    'modern': 'Если убьет муж мужа, то мстить брату брата',
                    'translation_en': 'If a man kills a man, then brother shall avenge brother'
                }
            ],

            'common_phrases': {
                'greeting': {'old': 'Здравьствуй, братѣ', 'modern': 'Здравствуй, брат'},
                'god': {'old': 'Богъ', 'modern': 'Бог'},
                'prince': {'old': 'Кънѧзь', 'modern': 'Князь'},
                'land': {'old': 'Землѧ', 'modern': 'Земля'},
                'word': {'old': 'Слово', 'modern': 'Слово'},
            },

            'grammar': """**ГРАММАТИКА ДРЕВНЕРУССКОГО:**

7 падежей (включая звательный!)
3 числа: единственное, двойственное, множественное
3 рода: мужской, женский, средний

Двойственное число (утрачено в современном русском):
рука - руцѣ (две руки)
око - очи (два глаза)

Звательный падеже:
братъ → брате! (о, брат!)
богъ → боже! (о, Боже!)
""",

            'importance': 10
        }

    def _get_old_church_slavonic(self) -> Dict:
        """Старославянский язык"""
        return {
            'name': 'Старославянский язык',
            'name_en': 'Old Church Slavonic',
            'name_native': 'Словѣньскъ ѩзꙑкъ',
            'period': '9-11 века н.э.',
            'family': 'Славянская',
            'script': 'Глаголица/Кириллица',

            'alphabet': {
                'cyrillic': 'А Б В Г Д Е Ж Ѕ З И І К Л М Н О П Р С Т У Ф Х Ѡ Ц Ч Ш Щ Ъ Ы Ь Ѣ Ю Ѫ Ѭ Ѧ Ѩ',
                'glagolitic': 'Ⰰ Ⰱ Ⰲ Ⰳ Ⰴ Ⰵ Ⰶ Ⰷ Ⰸ Ⰹ Ⰺ Ⰻ Ⰼ Ⰽ Ⰾ Ⰿ Ⱀ Ⱁ Ⱂ Ⱃ Ⱄ Ⱅ Ⱆ Ⱇ Ⱈ Ⱉ',
            },

            'famous_texts': [
                {
                    'name': 'Отче наш (глаголица)',
                    'original_glagolitic': 'Ⱁⱅⱐⱍⰵ ⱀⰰⱎⱐ',
                    'original_cyrillic': 'Отьче нашь',
                    'translation': 'Отче наш'
                }
            ],

            'importance': 9
        }

    def _get_latin(self) -> Dict:
        """Латинский язык"""
        return {
            'name': 'Латинский язык',
            'name_en': 'Latin',
            'name_native': 'Lingua Latina',
            'period': '700 до н.э. - 600 н.э.',
            'family': 'Италийская (Индоевропейская)',
            'script': 'Латиница',

            'alphabet': {
                'classical': 'A B C D E F G H I K L M N O P Q R S T V X',
                'medieval': 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z',
                'note': 'Классическая латынь не имела J, U, W'
            },

            'famous_texts': [
                {
                    'name': 'Veni, vidi, vici',
                    'author': 'Юлий Цезарь',
                    'translation_ru': 'Пришел, увидел, победил',
                    'translation_en': 'I came, I saw, I conquered'
                },
                {
                    'name': 'Carpe diem',
                    'author': 'Гораций',
                    'translation_ru': 'Лови день (живи настоящим)',
                    'translation_en': 'Seize the day'
                },
                {
                    'name': 'Cogito, ergo sum',
                    'author': 'Декарт',
                    'translation_ru': 'Мыслю, следовательно существую',
                    'translation_en': 'I think, therefore I am'
                },
                {
                    'name': 'Alea iacta est',
                    'author': 'Юлий Цезарь',
                    'translation_ru': 'Жребий брошен',
                    'translation_en': 'The die is cast'
                },
                {
                    'name': 'In vino veritas',
                    'translation_ru': 'Истина в вине',
                    'translation_en': 'In wine, there is truth'
                }
            ],

            'common_phrases': {
                'hello': {'latin': 'Salve', 'meaning': 'Здравствуй'},
                'goodbye': {'latin': 'Vale', 'meaning': 'Прощай'},
                'thank_you': {'latin': 'Gratias tibi ago', 'meaning': 'Благодарю тебя'},
                'god': {'latin': 'Deus', 'meaning': 'Бог'},
                'peace': {'latin': 'Pax', 'meaning': 'Мир'},
            },

            'importance': 10
        }

    def _get_ancient_greek(self) -> Dict:
        """Древнегреческий язык"""
        return {
            'name': 'Древнегреческий язык',
            'name_en': 'Ancient Greek',
            'name_native': 'Ἑλληνική',
            'period': '9 век до н.э. - 6 век н.э.',
            'family': 'Греческая (Индоевропейская)',
            'script': 'Греческий алфавит',

            'alphabet': {
                'letters': 'Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω',
                'lowercase': 'α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ/ς τ υ φ χ ψ ω',
                'names': {
                    'Α': 'alpha', 'Β': 'beta', 'Γ': 'gamma', 'Δ': 'delta',
                    'Ε': 'epsilon', 'Ζ': 'zeta', 'Η': 'eta', 'Θ': 'theta',
                    'Ι': 'iota', 'Κ': 'kappa', 'Λ': 'lambda', 'Μ': 'mu',
                    'Ν': 'nu', 'Ξ': 'xi', 'Ο': 'omicron', 'Π': 'pi',
                    'Ρ': 'rho', 'Σ': 'sigma', 'Τ': 'tau', 'Υ': 'upsilon',
                    'Φ': 'phi', 'Χ': 'chi', 'Ψ': 'psi', 'Ω': 'omega'
                }
            },

            'famous_texts': [
                {
                    'name': 'Γνῶθι σεαυτόν',
                    'transliteration': 'Gnōthi seauton',
                    'translation_ru': 'Познай самого себя',
                    'translation_en': 'Know thyself',
                    'source': 'Дельфийский оракул'
                },
                {
                    'name': 'Ἓν οἶδα ὅτι οὐδὲν οἶδα',
                    'transliteration': 'Hen oida hoti ouden oida',
                    'translation_ru': 'Я знаю, что ничего не знаю',
                    'translation_en': 'I know that I know nothing',
                    'author': 'Сократ'
                },
                {
                    'name': 'Εὐρηκα!',
                    'transliteration': 'Eureka!',
                    'translation_ru': 'Нашел!',
                    'translation_en': 'I have found it!',
                    'author': 'Архимед'
                }
            ],

            'importance': 10
        }

    def _get_sanskrit(self) -> Dict:
        """Санскрит"""
        return {
            'name': 'Санскрит',
            'name_en': 'Sanskrit',
            'name_native': 'संस्कृतम्',
            'period': '1500 до н.э. - настоящее время',
            'family': 'Индоарийская',
            'script': 'Деванагари',

            'alphabet': {
                'vowels': 'अ आ इ ई उ ऊ ऋ ॠ ऌ ॡ ए ऐ ओ औ',
                'consonants': 'क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह',
            },

            'famous_texts': [
                {
                    'name': 'ॐ',
                    'transliteration': 'Om',
                    'translation': 'Священный звук, символ вселенной'
                },
                {
                    'name': 'नमस्ते',
                    'transliteration': 'Namaste',
                    'translation_ru': 'Приветствие (кланяюсь тебе)',
                    'translation_en': 'Greetings (I bow to you)'
                },
                {
                    'name': 'सत्यमेव जयते',
                    'transliteration': 'Satyameva jayate',
                    'translation_ru': 'Истина побеждает',
                    'translation_en': 'Truth alone triumphs'
                }
            ],

            'importance': 9
        }

    def _get_ancient_egyptian(self) -> Dict:
        """Древнеегипетский - иероглифы"""
        return {
            'name': 'Древнеегипетский',
            'name_en': 'Ancient Egyptian',
            'name_native': 'r n kmt (язык Кемета)',
            'period': '3200 до н.э. - 4 век н.э.',
            'family': 'Афро-азиатская',
            'script': 'Иероглифы',

            'alphabet': {
                'description': 'Иероглифическое письмо',
                'sample': '𓂀 𓃀 𓃰 𓅓 𓆑 𓇋 𓈖 𓉐 𓊪 𓋴',
                'note': 'Более 700 иероглифических знаков!'
            },

            'famous_symbols': {
                '𓂀': 'Человек',
                '𓃀': 'Нога',
                '𓅓': 'Сова (звук М)',
                '𓆑': 'Гадюка (звук Ф)',
                '𓇋': 'Тростник (звук И)',
                '𓈖': 'Вода (звук Н)',
                '𓊪': 'Циновка (звук П)',
                '𓋴': 'Засов (звук С)',
            },

            'famous_phrases': {
                'ankh': {'symbol': '𓋹', 'meaning': 'Жизнь, вечная жизнь'},
                'ra': {'symbol': '𓂋𓄿', 'meaning': 'Ра (бог солнца)'},
            },

            'importance': 9
        }

    def _get_sumerian(self) -> Dict:
        """Шумерский - клинопись"""
        return {
            'name': 'Шумерский',
            'name_en': 'Sumerian',
            'name_native': '𒅴𒂠 (eme-ĝir)',
            'period': '3100 - 2000 до н.э.',
            'family': 'Изолированный язык',
            'script': 'Клинопись',

            'alphabet': {
                'description': 'Клинописные знаки',
                'sample': '𒀀 𒀭 𒁹 𒂗 𒃻 𒆠 𒈗 𒊕',
            },

            'famous_words': {
                '𒀭': 'dingir - бог',
                '𒂗': 'en - господин',
                '𒈗': 'lugal - царь',
                '𒆠': 'ki - земля',
            },

            'importance': 8
        }

    def _get_phoenician(self) -> Dict:
        """Финикийский"""
        return {
            'name': 'Финикийский',
            'name_en': 'Phoenician',
            'period': '1050 - 300 до н.э.',
            'family': 'Семитская',
            'script': 'Финикийский алфавит',

            'alphabet': {
                'letters': '𐤀 𐤁 𐤂 𐤃 𐤄 𐤅 𐤆 𐤇 𐤈 𐤉 𐤊 𐤋 𐤌 𐤍 𐤎 𐤏 𐤐 𐤑 𐤒 𐤓 𐤔 𐤕',
                'note': 'Предок греческого и латинского алфавитов!'
            },

            'importance': 8
        }

    def _get_aramaic(self) -> Dict:
        """Арамейский"""
        return {
            'name': 'Арамейский',
            'name_en': 'Aramaic',
            'name_native': 'ܐܪܡܝܐ',
            'period': '1100 до н.э. - настоящее время',
            'family': 'Семитская',
            'script': 'Арамейское письмо',

            'alphabet': {
                'letters': 'ܐ ܒ ܓ ܕ ܗ ܘ ܙ ܚ ܛ ܝ ܟ ܠ ܡ ܢ ܣ ܥ ܦ ܨ ܩ ܪ ܫ ܬ',
                'note': 'Язык Иисуса Христа!'
            },

            'famous_phrases': {
                'peace': {'aramaic': 'ܫܠܡܐ', 'transliteration': 'shlama', 'meaning': 'Мир'},
            },

            'importance': 8
        }

    def _get_old_norse(self) -> Dict:
        """Древнескандинавский - руны"""
        return {
            'name': 'Древнескандинавский',
            'name_en': 'Old Norse',
            'name_native': 'Dǫnsk tunga',
            'period': '800-1300 н.э.',
            'family': 'Германская',
            'script': 'Футарк (руны)',

            'alphabet': {
                'younger_futhark': 'ᚠ ᚢ ᚦ ᚬ ᚱ ᚴ ᚼ ᚾ ᛁ ᛅ ᛋ ᛏ ᛒ ᛘ ᛚ ᛦ',
                'names': {
                    'ᚠ': 'fehu', 'ᚢ': 'ur', 'ᚦ': 'thurs', 'ᚬ': 'oss',
                    'ᚱ': 'reid', 'ᚴ': 'kaun', 'ᚼ': 'hagall', 'ᚾ': 'naud',
                    'ᛁ': 'iss', 'ᛅ': 'ar', 'ᛋ': 'sol', 'ᛏ': 'tyr',
                    'ᛒ': 'bjarkan', 'ᛘ': 'madr', 'ᛚ': 'logr', 'ᛦ': 'yr'
                }
            },

            'importance': 8
        }

    def _get_classical_chinese(self) -> Dict:
        """Классический китайский (вэньянь)"""
        return {
            'name': 'Классический китайский',
            'name_en': 'Classical Chinese',
            'name_native': '文言文',
            'period': '5 век до н.э. - 20 век н.э.',
            'family': 'Сино-тибетская',
            'script': 'Ханьцзы (иероглифы)',

            'famous_texts': [
                {
                    'name': '道可道，非常道',
                    'transliteration': 'Dào kě dào, fēi cháng dào',
                    'translation_ru': 'Дао, которое может быть выражено словами, не есть постоянное Дао',
                    'translation_en': 'The Dao that can be told is not the eternal Dao',
                    'source': 'Дао Дэ Цзин'
                }
            ],

            'importance': 9
        }

    def generate_text(self, language: str, text: str) -> Dict:
        """Генерация/перевод текста на древний язык"""
        if language not in self.languages:
            return {'error': f'Язык {language} не найден'}

        lang_data = self.languages[language]

        return {
            'language': lang_data['name'],
            'language_native': lang_data.get('name_native', ''),
            'period': lang_data['period'],
            'original_text': text,
            'alphabet': lang_data.get('alphabet', {}),
            'note': f'Текст на языке: {lang_data["name"]} ({lang_data["period"]})'
        }

    def get_all_languages(self) -> List[str]:
        """Получить список всех древних языков"""
        return list(self.languages.keys())

    def get_language_info(self, language: str) -> Optional[Dict]:
        """Получить информацию о языке"""
        return self.languages.get(language)

    def get_stats(self) -> Dict:
        """Статистика"""
        return {
            'total_languages': len(self.languages),
            'languages': [lang['name'] for lang in self.languages.values()],
            'oldest': 'Шумерский (3100 до н.э.)',
            'scripts': ['Орхонская руница', 'Кириллица', 'Латиница', 'Греческая',
                       'Деванагари', 'Иероглифы', 'Клинопись', 'Руны']
        }


# Глобальный экземпляр
_ancient_languages = None


def get_ancient_languages() -> AncientLanguages:
    """Получить глобальный экземпляр древних языков"""
    global _ancient_languages
    if _ancient_languages is None:
        _ancient_languages = AncientLanguages()
    return _ancient_languages
