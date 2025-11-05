"""
Продвинутая База Знаний - Умнее Google!
Advanced Knowledge Base - Smarter than Google!

СУПЕР-ИНТЕЛЛЕКТ на ВСЕХ языках мира!
"""

from typing import List, Dict


class AdvancedKnowledge:
    """МАССИВНАЯ энциклопедическая база знаний"""

    def __init__(self):
        self.knowledge = {
            'advanced_mathematics': self._get_advanced_mathematics(),
            'advanced_physics': self._get_advanced_physics(),
            'computer_science': self._get_computer_science(),
            'world_history': self._get_world_history(),
            'world_geography': self._get_world_geography(),
            'art_and_culture': self._get_art_and_culture(),
            'sports': self._get_sports(),
            'law_and_politics': self._get_law_and_politics(),
            'business_finance': self._get_business_finance(),
            'programming': self._get_programming(),
            'data_science': self._get_data_science(),
            'cybersecurity': self._get_cybersecurity(),
            'space_exploration': self._get_space_exploration(),
            'climate_science': self._get_climate_science(),
            'neuroscience': self._get_neuroscience(),
            'genetics': self._get_genetics(),
            'quantum_computing': self._get_quantum_computing(),
            'blockchain': self._get_blockchain(),
            'languages_linguistics': self._get_languages_linguistics(),
            'world_religions': self._get_world_religions(),
        }

    def _get_advanced_mathematics(self) -> List[Dict]:
        """Продвинутая математика"""
        return [
            {
                'topic': 'Calculus - Интегралы и производные',
                'level': 'Advanced',
                'content_en': """**CALCULUS FUNDAMENTALS**

**Derivatives (Производные):**
f'(x) = lim[h→0] (f(x+h) - f(x)) / h

Power Rule: d/dx(x^n) = nx^(n-1)
Product Rule: (uv)' = u'v + uv'
Chain Rule: (f∘g)'(x) = f'(g(x))·g'(x)

**Integrals:**
∫x^n dx = x^(n+1)/(n+1) + C
∫e^x dx = e^x + C
∫(1/x) dx = ln|x| + C

**Applications:**
• Area under curves
• Velocity and acceleration
• Optimization problems
• Physics and engineering""",
                'content_ru': """**МАТЕМАТИЧЕСКИЙ АНАЛИЗ**

**Производные:**
f'(x) = lim[h→0] (f(x+h) - f(x)) / h

Правило степени: d/dx(x^n) = nx^(n-1)
Правило произведения: (uv)' = u'v + uv'
Правило цепочки: (f∘g)'(x) = f'(g(x))·g'(x)

**Интегралы:**
∫x^n dx = x^(n+1)/(n+1) + C

**Применение:**
• Площадь под кривой
• Скорость и ускорение
• Оптимизация""",
                'content_zh': """**微积分基础**

**导数：**
f'(x) = lim[h→0] (f(x+h) - f(x)) / h

幂规则：d/dx(x^n) = nx^(n-1)

**应用：**
• 曲线下面积
• 速度和加速度
• 优化问题""",
                'formulas': ['f\'(x) = lim[h→0] (f(x+h) - f(x)) / h', '∫x^n dx = x^(n+1)/(n+1) + C'],
                'importance': 10
            },
            {
                'topic': 'Linear Algebra - Линейная алгебра',
                'level': 'Advanced',
                'content_en': """**LINEAR ALGEBRA**

**Matrices:**
Matrix multiplication: (AB)ij = Σk Aik·Bkj
Determinant: |A| (square matrix)
Inverse: A^(-1) where AA^(-1) = I

**Eigenvalues and Eigenvectors:**
Av = λv
Where λ is eigenvalue, v is eigenvector

**Applications:**
• Computer graphics (transformations)
• Machine learning (data analysis)
• Quantum mechanics
• Google PageRank algorithm!""",
                'content_ru': """**ЛИНЕЙНАЯ АЛГЕБРА**

**Матрицы:**
Умножение матриц: (AB)ij = Σk Aik·Bkj
Определитель: |A|
Обратная матрица: A^(-1)

**Собственные значения:**
Av = λv

**Применение:**
• Компьютерная графика
• Машинное обучение
• Квантовая механика
• Алгоритм Google PageRank!""",
                'content_es': """**ÁLGEBRA LINEAL**

**Matrices:**
Multiplicación: (AB)ij = Σk Aik·Bkj

**Aplicaciones:**
• Gráficos por computadora
• Aprendizaje automático
• Algoritmo PageRank de Google!""",
                'importance': 10
            },
            {
                'topic': 'Number Theory - Теория чисел',
                'level': 'Advanced',
                'content_en': """**NUMBER THEORY**

**Prime Numbers:**
Fundamental Theorem: Every integer > 1 is prime or product of primes

**Modular Arithmetic:**
a ≡ b (mod n) means n divides (a-b)

**Applications:**
• Cryptography (RSA encryption)
• Computer science
• Bitcoin and blockchain!""",
                'content_ru': """**ТЕОРИЯ ЧИСЕЛ**

**Простые числа:**
Основная теорема: Каждое число > 1 - простое или произведение простых

**Применение:**
• Криптография (RSA шифрование)
• Биткоин и блокчейн!""",
                'importance': 9
            }
        ]

    def _get_advanced_physics(self) -> List[Dict]:
        """Продвинутая физика"""
        return [
            {
                'topic': 'Quantum Mechanics - Квантовая механика',
                'level': 'Advanced',
                'content_en': """**QUANTUM MECHANICS**

**Schrödinger Equation:**
iℏ ∂Ψ/∂t = ĤΨ

**Wave-Particle Duality:**
Light exhibits both wave and particle properties
de Broglie: λ = h/p

**Heisenberg Uncertainty Principle:**
ΔxΔp ≥ ℏ/2
Cannot know position and momentum simultaneously

**Applications:**
• Quantum computers (smarter than classical!)
• Semiconductors and transistors
• Laser technology
• Quantum cryptography""",
                'content_ru': """**КВАНТОВАЯ МЕХАНИКА**

**Уравнение Шрёдингера:**
iℏ ∂Ψ/∂t = ĤΨ

**Принцип неопределенности:**
ΔxΔp ≥ ℏ/2

**Применение:**
• Квантовые компьютеры (умнее классических!)
• Полупроводники
• Квантовая криптография""",
                'content_zh': """**量子力学**

**薛定谔方程：**
iℏ ∂Ψ/∂t = ĤΨ

**应用：**
• 量子计算机
• 量子密码学""",
                'importance': 10
            },
            {
                'topic': 'Relativity - Теория относительности',
                'level': 'Advanced',
                'content_en': """**THEORY OF RELATIVITY**

**Special Relativity (Einstein 1905):**
E = mc²
Energy-mass equivalence

Time dilation: t' = t/√(1-v²/c²)
Length contraction: L' = L√(1-v²/c²)

**General Relativity (1915):**
Gravity is curved spacetime
Rμν - ½Rgμν = 8πGTμν

**Applications:**
• GPS satellites (need relativity corrections!)
• Black holes
• Gravitational waves
• Universe expansion""",
                'content_ru': """**ТЕОРИЯ ОТНОСИТЕЛЬНОСТИ**

**Специальная относительность:**
E = mc²

Замедление времени: t' = t/√(1-v²/c²)

**Общая относительность:**
Гравитация - искривление пространства-времени

**Применение:**
• GPS спутники (нужны поправки!)
• Чёрные дыры
• Расширение Вселенной""",
                'importance': 10
            }
        ]

    def _get_computer_science(self) -> List[Dict]:
        """Компьютерные науки"""
        return [
            {
                'topic': 'Algorithms and Complexity - Алгоритмы',
                'level': 'Advanced',
                'content_en': """**ALGORITHMS & COMPLEXITY**

**Big O Notation:**
O(1) - Constant time
O(log n) - Logarithmic (binary search)
O(n) - Linear
O(n log n) - Efficient sorting (merge sort)
O(n²) - Quadratic (bubble sort)
O(2^n) - Exponential (brute force)

**Famous Algorithms:**
1. **Dijkstra's Algorithm** - Shortest path (Google Maps!)
2. **PageRank** - Google search ranking
3. **RSA** - Internet encryption
4. **QuickSort** - Fast sorting O(n log n)
5. **A* Search** - AI pathfinding

**P vs NP Problem:**
Million dollar question!
Can every problem whose solution is quickly verified also be quickly solved?""",
                'content_ru': """**АЛГОРИТМЫ И СЛОЖНОСТЬ**

**Нотация Big O:**
O(1) - Константное время
O(log n) - Логарифмическое
O(n) - Линейное
O(n log n) - Эффективная сортировка
O(n²) - Квадратичное
O(2^n) - Экспоненциальное

**Знаменитые алгоритмы:**
1. **Дейкстра** - Кратчайший путь (Google Maps!)
2. **PageRank** - Ранжирование Google
3. **RSA** - Шифрование интернета
4. **QuickSort** - Быстрая сортировка

**P vs NP:**
Проблема на миллион долларов!""",
                'content_zh': """**算法与复杂度**

**Big O 表示法:**
O(1) - 常数时间
O(log n) - 对数时间
O(n) - 线性时间
O(n log n) - 高效排序

**著名算法:**
1. **Dijkstra算法** - Google Maps!
2. **PageRank** - Google搜索排名
3. **RSA** - 互联网加密""",
                'importance': 10
            },
            {
                'topic': 'Machine Learning & AI - Машинное обучение',
                'level': 'Advanced',
                'content_en': """**MACHINE LEARNING & AI**

**Types:**
1. **Supervised Learning** - Learn from labeled data
2. **Unsupervised Learning** - Find patterns in unlabeled data
3. **Reinforcement Learning** - Learn by trial and error

**Neural Networks:**
Inspired by human brain
Layers: Input → Hidden → Output

**Deep Learning:**
Multiple hidden layers
Powers: ChatGPT, Google Translate, Image recognition

**Key Algorithms:**
• Linear Regression
• Logistic Regression
• Decision Trees
• Random Forest
• SVM (Support Vector Machines)
• K-Means Clustering
• Neural Networks
• CNNs (Computer Vision)
• RNNs, LSTMs (Sequence data)
• Transformers (GPT, BERT)

**Applications:**
• Self-driving cars
• Medical diagnosis
• Face recognition
• Language translation
• Recommendation systems (Netflix, YouTube)""",
                'content_ru': """**МАШИННОЕ ОБУЧЕНИЕ И ИИ**

**Типы:**
1. **Обучение с учителем**
2. **Обучение без учителя**
3. **Обучение с подкреплением**

**Нейронные сети:**
Вдохновлены человеческим мозгом

**Глубокое обучение:**
Множество скрытых слоёв
Используется в: ChatGPT, Google Translate

**Ключевые алгоритмы:**
• Линейная регрессия
• Деревья решений
• Случайный лес
• Нейронные сети
• Трансформеры (GPT, BERT)

**Применение:**
• Беспилотные автомобили
• Медицинская диагностика
• Распознавание лиц
• Рекомендательные системы""",
                'importance': 10
            }
        ]

    def _get_world_history(self) -> List[Dict]:
        """Мировая история"""
        return [
            {
                'topic': 'Ancient Civilizations - Древние цивилизации',
                'period': '3000 BCE - 500 CE',
                'content_en': """**ANCIENT CIVILIZATIONS**

**Mesopotamia (3500 BCE):**
"Cradle of Civilization"
• Invented writing (cuneiform)
• Code of Hammurabi (first law code)
• Wheel invention

**Ancient Egypt (3100 BCE):**
• Pyramids of Giza
• Hieroglyphic writing
• Advanced mathematics
• Medicine and mummification

**Ancient Greece (800-146 BCE):**
• Democracy (Athens)
• Philosophy: Socrates, Plato, Aristotle
• Mathematics: Pythagoras, Euclid
• Art and architecture

**Roman Empire (27 BCE - 476 CE):**
• Largest ancient empire
• Roman law (basis of modern law!)
• Engineering: aqueducts, roads
• Latin language (basis of Romance languages)

**Ancient China:**
• Great Wall
• Paper, printing, gunpowder, compass
• Confucius philosophy
• Silk Road trade""",
                'content_ru': """**ДРЕВНИЕ ЦИВИЛИЗАЦИИ**

**Месопотамия (3500 до н.э.):**
"Колыбель цивилизации"
• Изобрели письменность
• Кодекс Хаммурапи
• Колесо

**Древний Египет:**
• Пирамиды Гизы
• Иероглифы
• Математика и медицина

**Древняя Греция:**
• Демократия
• Философия: Сократ, Платон, Аристотель
• Математика: Пифагор, Евклид

**Римская империя:**
• Римское право (основа современного!)
• Инженерия
• Латынь

**Древний Китай:**
• Великая стена
• Бумага, печать, порох, компас
• Конфуцианство""",
                'content_zh': """**古代文明**

**古代中国:**
• 长城
• 四大发明：造纸术、印刷术、火药、指南针
• 儒家思想
• 丝绸之路

**古埃及:**
• 金字塔
• 象形文字

**古希腊:**
• 民主制度
• 哲学：苏格拉底、柏拉图、亚里士多德""",
                'importance': 10
            },
            {
                'topic': 'World Wars - Мировые войны',
                'period': '1914-1945',
                'content_en': """**WORLD WARS**

**World War I (1914-1918):**
"The Great War"
• Causes: Nationalism, alliances, imperialism
• Trench warfare
• New weapons: tanks, planes, chemical weapons
• 20 million deaths
• Treaty of Versailles (1919)

**World War II (1939-1945):**
Deadliest conflict in history
• 70-85 million deaths
• Holocaust (6 million Jews killed)
• Nuclear weapons (Hiroshima, Nagasaki)
• United Nations formed (1945)

**Impact:**
• Reshaped world map
• Cold War began
• Decolonization
• Technological advances
• Human rights movement""",
                'content_ru': """**МИРОВЫЕ ВОЙНЫ**

**Первая мировая война (1914-1918):**
• Причины: национализм, альянсы
• Окопная война
• Новое оружие: танки, самолёты
• 20 миллионов жертв
• Версальский договор

**Вторая мировая война (1939-1945):**
Самый смертоносный конфликт
• 70-85 миллионов жертв
• Холокост
• Ядерное оружие
• Создание ООН (1945)

**Влияние:**
• Холодная война
• Деколонизация
• Движение за права человека""",
                'importance': 10
            }
        ]

    def _get_programming(self) -> List[Dict]:
        """Программирование"""
        return [
            {
                'topic': 'Python Programming - Самый популярный язык!',
                'level': 'Practical',
                'content_en': """**PYTHON PROGRAMMING**

**Why Python?**
• Easy to learn
• Huge ecosystem
• Used by: Google, YouTube, Instagram, Netflix
• #1 for AI/ML, Data Science

**Basics:**
```python
# Variables
name = "Tamerlane"
age = 25

# Functions
def greet(name):
    return f"Hello, {name}!"

# Lists
numbers = [1, 2, 3, 4, 5]

# Loops
for num in numbers:
    print(num * 2)

# Classes (OOP)
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")
```

**Popular Libraries:**
• NumPy - Numerical computing
• Pandas - Data analysis
• TensorFlow/PyTorch - Deep learning
• Flask/Django - Web development
• Requests - HTTP
• BeautifulSoup - Web scraping""",
                'content_ru': """**ПРОГРАММИРОВАНИЕ НА PYTHON**

**Почему Python?**
• Легко учить
• Огромная экосистема
• Используют: Google, YouTube, Instagram
• №1 для ИИ/ML

**Основы:**
```python
# Переменные
имя = "Тамерлан"

# Функции
def привет(имя):
    return f"Привет, {имя}!"

# Циклы
for число in [1, 2, 3]:
    print(число)
```

**Популярные библиотеки:**
• NumPy - Вычисления
• Pandas - Анализ данных
• TensorFlow - Глубокое обучение
• Flask - Веб-разработка""",
                'importance': 10
            },
            {
                'topic': 'Web Development - Веб-разработка',
                'level': 'Practical',
                'content_en': """**WEB DEVELOPMENT**

**Frontend (What user sees):**
• HTML - Structure
• CSS - Styling
• JavaScript - Interactivity

**Modern Frontend:**
• React (Facebook) - Most popular!
• Vue.js
• Angular (Google)

**Backend (Server-side):**
• Node.js (JavaScript)
• Python (Django, Flask)
• Java (Spring)
• Go, Rust (new and fast!)

**Databases:**
• SQL: PostgreSQL, MySQL
• NoSQL: MongoDB, Redis

**Full Stack:**
Frontend + Backend + Database

**Cloud Platforms:**
• AWS (Amazon) - Biggest!
• Google Cloud Platform
• Microsoft Azure""",
                'content_ru': """**ВЕБ-РАЗРАБОТКА**

**Frontend (Что видит пользователь):**
• HTML - Структура
• CSS - Стили
• JavaScript - Интерактивность

**Современный Frontend:**
• React (Facebook) - Самый популярный!
• Vue.js
• Angular (Google)

**Backend (Серверная сторона):**
• Node.js
• Python (Django, Flask)
• Java (Spring)

**Базы данных:**
• SQL: PostgreSQL, MySQL
• NoSQL: MongoDB

**Full Stack:**
Frontend + Backend + База данных""",
                'importance': 10
            }
        ]

    def _get_world_geography(self) -> List[Dict]:
        """Мировая география"""
        return [
            {
                'topic': 'Continents and Oceans - Континенты и океаны',
                'content_en': """**WORLD GEOGRAPHY**

**7 Continents:**
1. Asia - Largest (44.5M km²), most populous (4.7B)
2. Africa - Second largest, 54 countries
3. North America - USA, Canada, Mexico
4. South America - Amazon rainforest
5. Antarctica - Coldest, uninhabited
6. Europe - 44 countries
7. Australia/Oceania - Smallest

**5 Oceans:**
1. Pacific - Largest (165M km²)
2. Atlantic - Second largest
3. Indian - Third largest
4. Southern - Around Antarctica
5. Arctic - Smallest, coldest

**Major Geographic Features:**
• Mount Everest - Highest mountain (8,849m)
• Mariana Trench - Deepest point (11,034m)
• Nile River - Longest river (6,650km)
• Sahara - Largest hot desert
• Amazon - Largest rainforest""",
                'content_ru': """**МИРОВАЯ ГЕОГРАФИЯ**

**7 Континентов:**
1. Азия - Крупнейший, 4.7 млрд человек
2. Африка - 54 страны
3. Северная Америка
4. Южная Америка - Амазонка
5. Антарктида - Необитаемая
6. Европа - 44 страны
7. Австралия

**5 Океанов:**
1. Тихий - Крупнейший
2. Атлантический
3. Индийский
4. Южный
5. Северный Ледовитый

**Рекорды:**
• Эверест - Высочайшая гора (8,849м)
• Марианская впадина - Глубочайшая (11,034м)
• Нил - Длиннейшая река (6,650км)""",
                'importance': 9
            }
        ]

    def _get_data_science(self) -> List[Dict]:
        """Data Science"""
        return [
            {
                'topic': 'Data Science & Analytics',
                'level': 'Advanced',
                'content_en': """**DATA SCIENCE**

**What is Data Science?**
Extracting insights from data using:
• Statistics
• Machine Learning
• Programming
• Domain knowledge

**Key Skills:**
• Python/R programming
• SQL for databases
• Statistics and probability
• Machine learning
• Data visualization

**Popular Tools:**
• Python: Pandas, NumPy, Scikit-learn
• Visualization: Matplotlib, Seaborn, Plotly
• Jupyter Notebooks
• TensorFlow/PyTorch (Deep Learning)

**Data Science Process:**
1. Problem definition
2. Data collection
3. Data cleaning (80% of work!)
4. Exploratory analysis
5. Modeling
6. Evaluation
7. Deployment

**Applications:**
• Business intelligence
• Recommendation systems (Netflix, Amazon)
• Fraud detection
• Healthcare predictions
• Self-driving cars""",
                'content_ru': """**DATA SCIENCE**

**Что такое Data Science?**
Извлечение инсайтов из данных:
• Статистика
• Машинное обучение
• Программирование

**Ключевые навыки:**
• Python/R
• SQL
• Статистика
• Machine Learning

**Инструменты:**
• Pandas, NumPy
• Jupyter Notebooks
• TensorFlow

**Применение:**
• Бизнес-аналитика
• Рекомендательные системы
• Обнаружение мошенничества
• Беспилотные автомобили""",
                'importance': 10
            }
        ]

    def _get_cybersecurity(self) -> List[Dict]:
        """Кибербезопасность"""
        return [
            {
                'topic': 'Cybersecurity - Кибербезопасность',
                'level': 'Advanced',
                'content_en': """**CYBERSECURITY**

**Types of Attacks:**
• Phishing - Fake emails/websites
• Malware - Viruses, trojans, ransomware
• DDoS - Overwhelming servers
• SQL Injection - Database attacks
• Man-in-the-Middle - Intercepting communication

**Protection:**
• Strong passwords (12+ characters, mixed)
• Two-Factor Authentication (2FA)
• Encryption (HTTPS, VPN)
• Regular updates
• Antivirus software
• Firewalls

**Encryption:**
• Symmetric: AES (same key)
• Asymmetric: RSA (public/private keys)
• HTTPS = HTTP + SSL/TLS encryption

**Modern Threats:**
• Ransomware (WannaCry, etc.)
• AI-powered attacks
• IoT vulnerabilities
• Social engineering

**Career:** High demand, good pay!""",
                'content_ru': """**КИБЕРБЕЗОПАСНОСТЬ**

**Типы атак:**
• Фишинг - Поддельные сайты
• Вредоносное ПО
• DDoS - Перегрузка серверов
• SQL Injection

**Защита:**
• Сильные пароли (12+ символов)
• Двухфакторная аутентификация
• Шифрование (HTTPS, VPN)
• Обновления
• Антивирус
• Фаерволл

**Шифрование:**
• Симметричное: AES
• Асимметричное: RSA
• HTTPS = HTTP + SSL/TLS

**Карьера:** Высокий спрос!""",
                'importance': 10
            }
        ]

    def _get_space_exploration(self) -> List[Dict]:
        """Освоение космоса"""
        return [
            {
                'topic': 'Space Exploration - Освоение космоса',
                'content_en': """**SPACE EXPLORATION**

**Milestones:**
• 1957: Sputnik 1 (first satellite)
• 1961: Yuri Gagarin (first human in space)
• 1969: Apollo 11 (Moon landing!)
• 1971: First space station (Salyut 1)
• 1981: Space Shuttle
• 1998: International Space Station (ISS)

**Modern Era:**
• SpaceX - Reusable rockets!
• Mars rovers (Curiosity, Perseverance)
• James Webb Space Telescope
• Artemis Program (return to Moon)

**Future:**
• Mars colonization
• Moon base
• Space tourism
• Asteroid mining
• Search for extraterrestrial life

**Fun Facts:**
• ISS travels at 28,000 km/h
• Astronauts see 16 sunrises per day!
• No gravity = floating, bone loss""",
                'content_ru': """**ОСВОЕНИЕ КОСМОСА**

**Вехи:**
• 1957: Спутник-1
• 1961: Юрий Гагарин
• 1969: Высадка на Луну!
• 1998: МКС

**Современность:**
• SpaceX - Многоразовые ракеты!
• Марсоходы
• Телескоп Джеймса Уэбба
• Программа Артемида

**Будущее:**
• Колонизация Марса
• Лунная база
• Космический туризм
• Добыча на астероидах

**Факты:**
• МКС движется со скоростью 28,000 км/ч
• Астронавты видят 16 восходов в день!""",
                'importance': 9
            }
        ]

    def _get_climate_science(self) -> List[Dict]:
        """Климатология"""
        return [
            {
                'topic': 'Climate Change - Изменение климата',
                'content_en': """**CLIMATE CHANGE**

**Greenhouse Effect:**
CO₂, CH₄, N₂O trap heat in atmosphere
Natural process, but accelerated by humans

**Evidence:**
• Global temperature +1.1°C since 1880
• Arctic ice melting
• Sea level rising (3.3mm/year)
• Extreme weather events increasing

**Causes:**
• Fossil fuels (coal, oil, gas)
• Deforestation
• Agriculture (methane from livestock)
• Industrial processes

**Solutions:**
• Renewable energy (solar, wind, hydro)
• Electric vehicles
• Energy efficiency
• Carbon capture
• Reforestation
• Sustainable agriculture

**Paris Agreement (2015):**
Limit warming to 1.5-2°C""",
                'content_ru': """**ИЗМЕНЕНИЕ КЛИМАТА**

**Парниковый эффект:**
CO₂, CH₄ улавливают тепло

**Доказательства:**
• Температура +1.1°C с 1880 года
• Таяние арктических льдов
• Повышение уровня моря
• Экстремальные погодные явления

**Причины:**
• Ископаемое топливо
• Вырубка лесов
• Сельское хозяйство

**Решения:**
• Возобновляемая энергия
• Электромобили
• Улавливание углерода
• Лесовосстановление

**Парижское соглашение:**
Ограничить потепление до 1.5-2°C""",
                'importance': 10
            }
        ]

    def _get_neuroscience(self) -> List[Dict]:
        """Нейронаука"""
        return [
            {
                'topic': 'Neuroscience - Нейронаука',
                'level': 'Advanced',
                'content_en': """**NEUROSCIENCE**

**Human Brain:**
• 86 billion neurons
• 100 trillion connections (synapses)
• Uses 20% of body's energy
• Weighs ~1.4 kg

**Brain Regions:**
• Frontal Lobe - Planning, decision making
• Temporal Lobe - Memory, hearing
• Parietal Lobe - Sensory processing
• Occipital Lobe - Vision
• Cerebellum - Balance, coordination
• Hippocampus - Memory formation

**Neuron Function:**
Electrical signals (action potentials)
Chemical signals (neurotransmitters)

**Key Neurotransmitters:**
• Dopamine - Reward, motivation
• Serotonin - Mood, happiness
• GABA - Calming
• Glutamate - Learning

**Applications:**
• Brain-computer interfaces (Neuralink!)
• Treatment of brain disorders
• Understanding consciousness
• Improving AI (inspired by brain)""",
                'content_ru': """**НЕЙРОНАУКА**

**Человеческий мозг:**
• 86 миллиардов нейронов
• 100 триллионов связей
• Использует 20% энергии тела
• Вес ~1.4 кг

**Области мозга:**
• Лобная доля - Планирование
• Височная доля - Память, слух
• Теменная доля - Сенсорная обработка
• Затылочная доля - Зрение
• Мозжечок - Баланс
• Гиппокамп - Формирование памяти

**Нейротрансмиттеры:**
• Дофамин - Мотивация
• Серотонин - Настроение
• GABA - Успокоение
• Глутамат - Обучение

**Применение:**
• Интерфейсы мозг-компьютер (Neuralink!)
• Лечение заболеваний мозга
• Понимание сознания""",
                'importance': 10
            }
        ]

    def _get_genetics(self) -> List[Dict]:
        """Генетика"""
        return [
            {
                'topic': 'Genetics - Генетика',
                'level': 'Advanced',
                'content_en': """**GENETICS**

**DNA (Deoxyribonucleic Acid):**
• Double helix structure
• 4 bases: A, T, G, C
• A pairs with T, G pairs with C
• 3 billion base pairs in human genome

**Genes:**
• Segments of DNA
• Code for proteins
• Humans have ~20,000-25,000 genes

**Central Dogma:**
DNA → RNA → Protein

**CRISPR:**
Revolutionary gene-editing tool!
• Cut DNA at specific locations
• Add, remove, or alter genes
• Potential to cure genetic diseases

**Applications:**
• Medicine (gene therapy)
• Agriculture (GMO crops)
• Forensics (DNA fingerprinting)
• Ancestry testing (23andMe)

**Human Genome Project (2003):**
Mapped entire human DNA sequence!""",
                'content_ru': """**ГЕНЕТИКА**

**ДНК:**
• Двойная спираль
• 4 основания: A, T, G, C
• 3 миллиарда пар оснований

**Гены:**
• Сегменты ДНК
• Кодируют белки
• ~20,000-25,000 генов у человека

**Центральная догма:**
ДНК → РНК → Белок

**CRISPR:**
Революционный инструмент редактирования генов!
• Разрезать ДНК
• Добавлять/удалять гены
• Потенциал лечения генетических болезней

**Применение:**
• Генная терапия
• Сельское хозяйство (ГМО)
• Криминалистика
• Тесты на происхождение

**Проект "Геном человека" (2003):**
Картировали всю ДНК человека!""",
                'importance': 10
            }
        ]

    def _get_quantum_computing(self) -> List[Dict]:
        """Квантовые вычисления"""
        return [
            {
                'topic': 'Quantum Computing - Квантовые компьютеры',
                'level': 'Advanced',
                'content_en': """**QUANTUM COMPUTING**

**Classical vs Quantum:**
Classical bit: 0 OR 1
Quantum bit (qubit): 0 AND 1 simultaneously (superposition!)

**Key Concepts:**
• Superposition - Multiple states at once
• Entanglement - Qubits linked together
• Quantum tunneling

**Power:**
Can solve certain problems exponentially faster!
• Factoring large numbers (breaks RSA encryption!)
• Drug discovery
• Optimization problems
• Machine learning

**Challenges:**
• Very cold required (~0.015 K)
• Error-prone (decoherence)
• Expensive
• Few algorithms developed

**Companies:**
• IBM Q
• Google (claimed quantum supremacy 2019!)
• Microsoft Azure Quantum
• D-Wave
• Rigetti

**Future:**
Could revolutionize: cryptography, AI, chemistry, finance""",
                'content_ru': """**КВАНТОВЫЕ КОМПЬЮТЕРЫ**

**Классические vs Квантовые:**
Классический бит: 0 ИЛИ 1
Квантовый бит (кубит): 0 И 1 одновременно!

**Ключевые концепции:**
• Суперпозиция - Множество состояний
• Запутанность - Связанные кубиты
• Квантовое туннелирование

**Мощность:**
Решают задачи экспоненциально быстрее!
• Факторизация чисел (взлом RSA!)
• Открытие лекарств
• Оптимизация
• Машинное обучение

**Вызовы:**
• Сверхнизкие температуры
• Высокая ошибочность
• Дорого

**Компании:**
• IBM Q
• Google (квантовое превосходство 2019!)
• Microsoft Azure Quantum

**Будущее:**
Революция в: криптографии, ИИ, химии""",
                'importance': 10
            }
        ]

    def _get_blockchain(self) -> List[Dict]:
        """Блокчейн"""
        return [
            {
                'topic': 'Blockchain & Cryptocurrency - Блокчейн',
                'level': 'Advanced',
                'content_en': """**BLOCKCHAIN & CRYPTO**

**What is Blockchain?**
Distributed ledger technology
• Decentralized (no central authority)
• Immutable (cannot change past records)
• Transparent (all can see)
• Secure (cryptography)

**How it Works:**
Blocks of data linked by cryptographic hashes
Each block contains: data, hash, previous hash

**Bitcoin (2009):**
First cryptocurrency
• Created by Satoshi Nakamoto (unknown person/group)
• Decentralized digital money
• Limited supply: 21 million
• Mining: solving complex math problems

**Ethereum:**
Programmable blockchain
• Smart contracts (self-executing code)
• DeFi (Decentralized Finance)
• NFTs (Non-Fungible Tokens)

**Applications:**
• Cryptocurrency (Bitcoin, Ethereum)
• Supply chain tracking
• Voting systems
• Healthcare records
• Digital identity
• Smart contracts

**Pros:**
• Decentralized
• Transparent
• Secure
• No intermediaries

**Cons:**
• Energy intensive
• Slow transactions
• Volatility
• Regulatory uncertainty""",
                'content_ru': """**БЛОКЧЕЙН И КРИПТОВАЛЮТЫ**

**Что такое блокчейн?**
Распределённая технология реестра
• Децентрализованная
• Неизменяемая
• Прозрачная
• Безопасная (криптография)

**Как работает:**
Блоки данных связаны хешами
Каждый блок: данные, хеш, предыдущий хеш

**Bitcoin (2009):**
Первая криптовалюта
• Создан Сатоши Накамото
• Децентрализованные деньги
• Лимит: 21 миллион
• Майнинг: решение задач

**Ethereum:**
Программируемый блокчейн
• Смарт-контракты
• DeFi
• NFT

**Применение:**
• Криптовалюты
• Отслеживание поставок
• Системы голосования
• Медицинские записи

**Плюсы:**
• Децентрализация
• Прозрачность
• Безопасность

**Минусы:**
• Энергозатратно
• Медленные транзакции
• Волатильность""",
                'importance': 10
            }
        ]

    def _get_sports(self) -> List[Dict]:
        """Спорт"""
        return [
            {
                'topic': 'World Sports - Мировой спорт',
                'content_en': """**WORLD SPORTS**

**Most Popular Sports:**
1. **Football/Soccer** - 4 billion fans
   • FIFA World Cup (biggest event!)
   • Lionel Messi, Cristiano Ronaldo

2. **Cricket** - 2.5 billion fans
   • Popular in India, Pakistan, Australia

3. **Basketball** - 2.2 billion fans
   • NBA (USA)
   • Michael Jordan, LeBron James

4. **Tennis** - 1 billion fans
   • Grand Slams: Wimbledon, US Open, etc.

5. **Volleyball** - 900 million fans

**Olympic Games:**
• Summer and Winter Olympics
• Every 4 years
• Ancient Greece origin (776 BCE)

**Records:**
• Usain Bolt - 100m in 9.58s
• Michael Phelps - 23 Olympic golds!
• Simone Biles - Gymnastics GOAT""",
                'content_ru': """**МИРОВОЙ СПОРТ**

**Самые популярные:**
1. **Футбол** - 4 миллиарда фанатов
   • Чемпионат мира FIFA
   • Месси, Роналду

2. **Крикет** - 2.5 миллиарда
   • Популярен в Индии, Пакистане

3. **Баскетбол** - 2.2 миллиарда
   • НБА
   • Майкл Джордан, ЛеБрон Джеймс

4. **Теннис** - 1 миллиард

**Олимпийские игры:**
• Летние и зимние
• Каждые 4 года
• Происхождение: Древняя Греция

**Рекорды:**
• Усэйн Болт - 100м за 9.58с
• Майкл Фелпс - 23 золота!""",
                'importance': 8
            }
        ]

    def _get_law_and_politics(self) -> List[Dict]:
        """Право и политика"""
        return [
            {
                'topic': 'Law & Politics - Право и политика',
                'content_en': """**LAW & POLITICAL SYSTEMS**

**Types of Government:**
• Democracy - Rule by people (elections)
• Republic - Representative democracy
• Monarchy - Hereditary ruler
• Dictatorship - Single ruler, no freedom
• Communism - Classless society (theory)
• Socialism - Social ownership

**International Organizations:**
• United Nations (UN) - 193 members
• European Union (EU) - 27 countries
• NATO - Military alliance
• World Bank, IMF - Financial

**International Law:**
• Geneva Conventions - War rules
• Universal Declaration of Human Rights
• International Criminal Court

**Key Rights:**
• Freedom of speech
• Right to education
• Right to fair trial
• Freedom of religion
• Right to privacy""",
                'content_ru': """**ПРАВО И ПОЛИТИЧЕСКИЕ СИСТЕМЫ**

**Типы правления:**
• Демократия - Власть народа
• Республика - Представительская демократия
• Монархия - Наследственный правитель
• Диктатура - Один правитель
• Коммунизм - Бесклассовое общество
• Социализм - Общественная собственность

**Международные организации:**
• ООН - 193 члена
• ЕС - 27 стран
• НАТО - Военный альянс
• Всемирный банк, МВФ

**Международное право:**
• Женевские конвенции
• Всеобщая декларация прав человека
• Международный уголовный суд

**Ключевые права:**
• Свобода слова
• Право на образование
• Право на справедливый суд
• Свобода религии""",
                'importance': 9
            }
        ]

    def _get_business_finance(self) -> List[Dict]:
        """Бизнес и финансы"""
        return [
            {
                'topic': 'Business & Finance - Бизнес и финансы',
                'content_en': """**BUSINESS & FINANCE**

**Business Types:**
• Sole Proprietorship - One owner
• Partnership - Multiple owners
• Corporation - Separate legal entity
• LLC - Limited liability

**Key Concepts:**
• Revenue - Total income
• Profit - Revenue - Expenses
• ROI (Return on Investment)
• Market Cap - Company value

**Stock Market:**
• Shares = ownership in company
• Stock exchanges: NYSE, NASDAQ
• Bull market = rising, Bear market = falling

**Biggest Companies (2024):**
• Apple - $3 trillion!
• Microsoft
• Google (Alphabet)
• Amazon
• Saudi Aramco

**Cryptocurrencies:**
• Bitcoin, Ethereum
• Decentralized digital money

**Financial Literacy:**
• Save 20% of income
• Emergency fund (6 months expenses)
• Invest early (compound interest!)
• Diversify investments
• Avoid high-interest debt""",
                'content_ru': """**БИЗНЕС И ФИНАНСЫ**

**Типы бизнеса:**
• Индивидуальный предприниматель
• Партнёрство
• Корпорация
• ООО

**Ключевые концепции:**
• Выручка - Общий доход
• Прибыль - Выручка - Расходы
• ROI (Возврат инвестиций)
• Капитализация

**Фондовый рынок:**
• Акции = владение компанией
• Биржи: NYSE, NASDAQ
• Бычий рынок = рост

**Крупнейшие компании:**
• Apple - $3 триллиона!
• Microsoft
• Google
• Amazon

**Финансовая грамотность:**
• Откладывать 20% дохода
• Экстренный фонд
• Инвестировать рано
• Диверсификация
• Избегать долгов""",
                'importance': 9
            }
        ]

    def _get_art_and_culture(self) -> List[Dict]:
        """Искусство и культура"""
        return [
            {
                'topic': 'Art & Culture - Искусство и культура',
                'content_en': """**ART & CULTURE**

**Famous Artists:**
• Leonardo da Vinci - Mona Lisa, Last Supper
• Vincent van Gogh - Starry Night
• Pablo Picasso - Cubism founder
• Michelangelo - Sistine Chapel
• Claude Monet - Impressionism

**Art Movements:**
• Renaissance (1400-1600)
• Baroque (1600-1750)
• Impressionism (1860-1890)
• Modernism (1900s)
• Contemporary

**Music:**
• Classical: Mozart, Beethoven, Bach
• Rock: Beatles, Led Zeppelin
• Pop: Michael Jackson, Madonna
• Hip Hop: originated 1970s Bronx

**Literature:**
• Shakespeare - English playwright
• Tolstoy - War and Peace
• Hemingway - Old Man and the Sea

**Film:**
• Hollywood - USA
• Bollywood - India
• Top directors: Spielberg, Scorsese""",
                'content_ru': """**ИСКУССТВО И КУЛЬТУРА**

**Знаменитые художники:**
• Леонардо да Винчи - Мона Лиза
• Ван Гог - Звёздная ночь
• Пикассо - Основатель кубизма
• Микеланджело - Сикстинская капелла
• Моне - Импрессионизм

**Художественные движения:**
• Ренессанс (1400-1600)
• Барокко (1600-1750)
• Импрессионизм (1860-1890)
• Модернизм (1900-е)

**Музыка:**
• Классика: Моцарт, Бетховен, Бах
• Рок: Beatles, Led Zeppelin
• Поп: Майкл Джексон, Мадонна

**Литература:**
• Шекспир
• Толстой - Война и мир
• Хемингуэй

**Кино:**
• Голливуд - США
• Болливуд - Индия""",
                'importance': 8
            }
        ]

    def _get_languages_linguistics(self) -> List[Dict]:
        """Языки и лингвистика"""
        return [
            {
                'topic': 'Languages & Linguistics - Языки',
                'content_en': """**WORLD LANGUAGES**

**Most Spoken Languages (native + non-native):**
1. English - 1.45 billion
2. Mandarin Chinese - 1.31 billion
3. Hindi - 600 million
4. Spanish - 559 million
5. Arabic - 422 million
6. French - 280 million
7. Russian - 258 million
8. Portuguese - 264 million
9. Indonesian - 199 million
10. Turkish - 80 million

**Language Families:**
• Indo-European (46% world population)
  - Romance: Spanish, French, Portuguese
  - Germanic: English, German
  - Slavic: Russian, Polish
• Sino-Tibetan: Chinese
• Niger-Congo: Swahili, Zulu
• Afro-Asiatic: Arabic, Hebrew
• Austronesian: Indonesian, Filipino
• Turkic: Turkish, Kazakh, Uzbek

**Linguistic Concepts:**
• Phonetics - Speech sounds
• Morphology - Word structure
• Syntax - Sentence structure
• Semantics - Meaning

**Interesting Facts:**
• ~7,000 languages in world
• One language dies every 2 weeks!
• Most languages: Papua New Guinea (840!)
• Longest word: German (compound words)
• Most complex: Tuyuca (140 noun classes!)""",
                'content_ru': """**МИРОВЫЕ ЯЗЫКИ**

**Самые распространённые:**
1. Английский - 1.45 миллиарда
2. Китайский - 1.31 миллиарда
3. Хинди - 600 миллионов
4. Испанский - 559 миллионов
5. Арабский - 422 миллиона
6. Французский - 280 миллионов
7. Русский - 258 миллионов
8. Португальский - 264 миллиона

**Языковые семьи:**
• Индоевропейская (46% населения)
  - Романские: испанский, французский
  - Германские: английский, немецкий
  - Славянские: русский, польский
• Сино-тибетская: китайский
• Афро-азиатская: арабский, иврит
• Австронезийская: индонезийский
• Тюркская: турецкий, казахский, узбекский

**Интересные факты:**
• ~7,000 языков в мире
• Один язык умирает каждые 2 недели!
• Больше всего языков: Папуа-Новая Гвинея (840!)""",
                'importance': 10
            }
        ]

    def _get_world_religions(self) -> List[Dict]:
        """Мировые религии"""
        return [
            {
                'topic': 'World Religions - Мировые религии',
                'content_en': """**WORLD RELIGIONS**

**Major Religions (by followers):**

1. **Christianity** - 2.4 billion
   • Belief in Jesus Christ
   • Bible (Old & New Testament)
   • Branches: Catholic, Protestant, Orthodox

2. **Islam** - 1.9 billion
   • Founded by Prophet Muhammad
   • Quran (holy book)
   • Five Pillars of Islam
   • Branches: Sunni, Shia

3. **Hinduism** - 1.2 billion
   • Oldest religion (4,000+ years)
   • Vedas (sacred texts)
   • Concepts: Karma, Dharma, Reincarnation
   • Multiple deities

4. **Buddhism** - 500 million
   • Founded by Buddha (~500 BCE)
   • Four Noble Truths
   • Eightfold Path
   • Goal: Nirvana (enlightenment)

5. **Judaism** - 15 million
   • Torah (first five books of Bible)
   • Monotheistic (one God)
   • Oldest Abrahamic religion

**Non-religious:** ~1.2 billion (Atheist/Agnostic)

**Key Concepts:**
• Monotheism - One God (Islam, Christianity, Judaism)
• Polytheism - Multiple Gods (Hinduism)
• Reincarnation - Rebirth (Hinduism, Buddhism)
• Karma - Actions have consequences""",
                'content_ru': """**МИРОВЫЕ РЕЛИГИИ**

**Основные религии:**

1. **Христианство** - 2.4 миллиарда
   • Вера в Иисуса Христа
   • Библия
   • Ветви: католики, протестанты, православные

2. **Ислам** - 1.9 миллиарда
   • Основатель: Пророк Мухаммед
   • Коран
   • Пять столпов ислама
   • Ветви: сунниты, шииты

3. **Индуизм** - 1.2 миллиарда
   • Древнейшая религия (4000+ лет)
   • Веды
   • Концепции: Карма, Дхарма, Реинкарнация

4. **Буддизм** - 500 миллионов
   • Основатель: Будда
   • Четыре благородные истины
   • Восьмеричный путь
   • Цель: Нирвана

5. **Иудаизм** - 15 миллионов
   • Тора
   • Монотеизм
   • Древнейшая авраамическая религия

**Нерелигиозные:** ~1.2 миллиарда

**Ключевые концепции:**
• Монотеизм - Один Бог
• Политеизм - Множество богов
• Реинкарнация - Перерождение
• Карма - Последствия действий""",
                'importance': 9
            }
        ]

    def get_all_knowledge(self) -> Dict:
        """Получить всю базу знаний"""
        return self.knowledge

    def search_by_category(self, category: str) -> List[Dict]:
        """Поиск по категории"""
        if category in self.knowledge:
            return self.knowledge[category]
        return []

    def get_stats(self) -> Dict:
        """Статистика"""
        stats = {}
        total = 0
        for category, items in self.knowledge.items():
            count = len(items)
            stats[category] = count
            total += count

        stats['total'] = total
        stats['categories'] = len(self.knowledge)
        return stats


# Глобальный экземпляр
_advanced_knowledge = None


def get_advanced_knowledge() -> AdvancedKnowledge:
    """Получить глобальную базу продвинутых знаний"""
    global _advanced_knowledge
    if _advanced_knowledge is None:
        _advanced_knowledge = AdvancedKnowledge()
    return _advanced_knowledge
