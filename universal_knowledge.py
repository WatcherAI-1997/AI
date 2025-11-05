"""
Универсальная База Знаний для Модели Тамерлан
Universal Knowledge Base for Tamerlane AI

ВСЕ ЗНАНИЯ МИРА на тюркских языках:
- Математика
- Физика
- Химия
- Биология
- Военная тактика и стратегия
- Технологии
- Медицина
- Философия
- Экономика
- И многое другое!
"""

from typing import List, Dict


class UniversalKnowledge:
    """Энциклопедические знания всего мира"""

    def __init__(self):
        self.knowledge = {
            'mathematics': self._get_mathematics(),
            'physics': self._get_physics(),
            'chemistry': self._get_chemistry(),
            'biology': self._get_biology(),
            'military': self._get_military(),
            'medicine': self._get_medicine(),
            'technology': self._get_technology(),
            'philosophy': self._get_philosophy(),
            'economics': self._get_economics(),
            'engineering': self._get_engineering(),
            'astronomy': self._get_astronomy(),
            'psychology': self._get_psychology()
        }

    def _get_mathematics(self) -> List[Dict]:
        """Математика"""
        return [
            {
                'topic': 'Теорема Пифагора',
                'category': 'Геометрия',
                'level': 'Базовый',
                'content_kk': """Пифагор теоремасы - тікбұрышты үшбұрыштың қасиеті.

**Формула:** a² + b² = c²

Мұндағы:
• a, b - катеттер (тік бұрышқа іргелес қабырғалар)
• c - гипотенуза (ең ұзын қабырға)

**Мысал:**
Егер a = 3, b = 4 болса:
3² + 4² = 9 + 16 = 25
c² = 25, c = 5

**Қолдану:**
• Құрылыста - тік бұрыш тексеру
• Навигацияда - қашықтық есептеу
• Архитектурада - үйлер салу""",
                'content_tr': """Pisagor Teoremi - dik üçgenin özelliği.

**Formül:** a² + b² = c²

Burada:
• a, b - dik kenarlar (kateler)
• c - hipotenüs (en uzun kenar)

**Örnek:**
Eğer a = 3, b = 4 ise:
3² + 4² = 9 + 16 = 25
c² = 25, c = 5

**Kullanım:**
• İnşaatta - dik açı kontrolü
• Navigasyonda - mesafe hesaplama
• Mimaride - ev inşası""",
                'content_uz': """Pifagor teoremasi - to'g'ri burchakli uchburchak xossasi.

**Formula:** a² + b² = c²

Bu yerda:
• a, b - katetlar (to'g'ri burchakka yaqin tomonlar)
• c - gipotenuza (eng uzun tomon)

**Misol:**
Agar a = 3, b = 4 bo'lsa:
3² + 4² = 9 + 16 = 25
c² = 25, c = 5

**Qo'llanilishi:**
• Qurilishda - to'g'ri burchak tekshirish
• Navigatsiyada - masofa hisoblash
• Arxitekturada - uy qurish""",
                'formulas': ['a² + b² = c²'],
                'importance': 10
            },
            {
                'topic': 'Интегралдар және Туындылар',
                'category': 'Математикалық анализ',
                'level': 'Жоғары',
                'content_kk': """**ТУЫНДЫ (Türev / Hosila)**

Функцияның өзгеру жылдамдығы.

f'(x) = lim(h→0) [f(x+h) - f(x)] / h

**Негізгі ережелер:**
• (xⁿ)' = n·xⁿ⁻¹
• (sin x)' = cos x
• (cos x)' = -sin x
• (eˣ)' = eˣ
• (ln x)' = 1/x

**ИНТЕГРАЛ (İntegral / İntegral)**

Аудан мен жинақтауды табу.

∫ f(x)dx

**Негізгі интегралдар:**
• ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C
• ∫ sin x dx = -cos x + C
• ∫ cos x dx = sin x + C
• ∫ eˣ dx = eˣ + C

**Қолдану:**
• Физикада - жылдамдық пен жол
• Экономикада - шығын функциялары
• Техникада - оптимизация""",
                'content_tr': """**TÜREV (Derivative / Производная)**

Fonksiyonun değişim hızı.

f'(x) = lim(h→0) [f(x+h) - f(x)] / h

**Temel kurallar:**
• (xⁿ)' = n·xⁿ⁻¹
• (sin x)' = cos x
• (cos x)' = -sin x
• (eˣ)' = eˣ
• (ln x)' = 1/x

**İNTEGRAL (Integral / Интеграл)**

Alan ve toplama bulma.

∫ f(x)dx

**Temel integraller:**
• ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C
• ∫ sin x dx = -cos x + C
• ∫ cos x dx = sin x + C
• ∫ eˣ dx = eˣ + C

**Kullanım:**
• Fizikte - hız ve yol
• Ekonomide - maliyet fonksiyonları
• Mühendislikte - optimizasyon""",
                'importance': 9
            }
        ]

    def _get_physics(self) -> List[Dict]:
        """Физика"""
        return [
            {
                'topic': 'Ньютонның қозғалыс заңдары',
                'category': 'Механика',
                'content_kk': """**НЬЮТОННЫҢ ҮШ ЗАҢЫ**

**1-ші заң (Инерция заңы):**
Дене тыныштықта немесе тұрақты жылдамдықта қалады, егер оған күш әсер етпесе.

**2-ші заң:**
F = ma
Күш = Масса × Үдеу

**3-ші заң:**
Әрбір әрекетке тең және қарама-қарсы әрекет бар.

**Мысалдар:**
🚗 Автомобиль тежелгенде жолаушылар алға қарай қозғалады (1-заң)
🏀 Ауыр допты қозғау қиын (2-заң)
🚀 Ракета газды төмен шығарады, өзі жоғары көтеріледі (3-заң)""",
                'content_tr': """**NEWTON'UN ÜÇ YASASI**

**1. Yasa (Atalet Yasası):**
Cisim durgun veya sabit hızda kalır, eğer ona kuvvet etki etmezse.

**2. Yasa:**
F = ma
Kuvvet = Kütle × İvme

**3. Yasa:**
Her etkiye eşit ve zıt bir tepki vardır.

**Örnekler:**
🚗 Araba fren yaptığında yolcular öne gider (1. yasa)
🏀 Ağır topu hareket ettirmek zordur (2. yasa)
🚀 Roket gazı aşağı atar, kendisi yukarı çıkar (3. yasa)""",
                'content_uz': """**NYUTONNING UCH QONUNI**

**1-qonun (Inertsiya qonuni):**
Jism tinch yoki o'zgarmas tezlikda qoladi, agar unga kuch ta'sir etmasa.

**2-qonun:**
F = ma
Kuch = Massa × Tezlanish

**3-qonun:**
Har bir ta'sirga teng va qarama-qarshi reaktsiya bor.

**Misollar:**
🚗 Mashina tormozlaganda yo'lovchilar oldinga siljiydi (1-qonun)
🏀 Og'ir to'pni harakatlantirish qiyin (2-qonun)
🚀 Raketa gazni pastga chiqaradi, o'zi yuqoriga ko'tariladi (3-qonun)""",
                'formulas': ['F = ma', 'p = mv', 'E = mc²'],
                'importance': 10
            },
            {
                'topic': 'Электр және Магнетизм',
                'category': 'Электродинамика',
                'content_kk': """**ОМ ЗАҢЫ:**
V = IR
Кернеу = Ток × Кедергі

**КУЛОН ЗАҢЫ:**
F = k·(q₁·q₂)/r²
Электр күші зарядтарға пропорционал

**ФАРАДЕЙ ЗАҢЫ:**
Магнит өрісінің өзгеруі электр тогын туғызады

**Қолдану:**
⚡ Электр станциялары
🔋 Батареялар және аккумуляторлар
📡 Радио және телекоммуникация
🧲 Электр қозғалтқыштар""",
                'content_tr': """**OHM YASASI:**
V = IR
Gerilim = Akım × Direnç

**COULOMB YASASI:**
F = k·(q₁·q₂)/r²
Elektrik kuvveti yüklere orantılı

**FARADAY YASASI:**
Manyetik alanın değişimi elektrik akımı üretir

**Kullanım:**
⚡ Elektrik santralleri
🔋 Piller ve akümülatörler
📡 Radyo ve telekomünikasyon
🧲 Elektrik motorları""",
                'importance': 9
            }
        ]

    def _get_military(self) -> List[Dict]:
        """Военная тактика и стратегия"""
        return [
            {
                'topic': 'Тәмірланның әскери тактикасы',
                'category': 'Тактика',
                'content_kk': """**ТӘМІРЛАННЫҢ ӘСКЕРИ ӨНЕРІ**

🏹 **Негізгі тактикалар:**

**1. Ұтқырлық (Manevra / Manevrability)**
• Жылдам жылжу
• Жауды айналып өту
• Күтпеген жерден шабуыл

**2. Жалған шегіну (Sahte Ricat / False Retreat)**
• Қашқандай көрсету
• Жауды ұстап алу
• Кейін қоршап алу

**3. Түнгі шабуылдар (Gece Baskınları / Night Attacks)**
• Күтпеген уақытта шабуыл
• Жауды дайындықсыз ұстау

**4. Психологиялық соғыс (Psikolojik Savaş / Psychological Warfare)**
• Қорқыту
• Дезинформация
• Моральды бұзу

**5. Қоршау тактикасы (Kuşatma / Encirclement)**
• Жауды төрт жақтан қоршау
• Шығу жолын жабу
• Ашық қалдыру (қашқандарға)

**Тамерланның ұтыстары:**
✓ Анкара шайқасы (1402) - Баязидты жеңді
✓ Делиге жорық (1398-1399)
✓ Дамаск алу (1401)

**Әскери принциптер:**
• Жылдамдық - бәрінен маңызды
• Барлау - қарсыласты білу
• Бірлік - әскердің ұйымдылығы
• Тәртіп - қатаң бақылау""",
                'content_tr': """**TİMUR'UN ASKERİ SANATISüleymaniye Camii

🏹 **Ana Taktikler:**

**1. Manevra (Ұтқырлық / Harakatchanlik)**
• Hızlı hareket
• Düşmanı çevirme
• Beklenmedik yerden saldırı

**2. Sahte Ricat (Жалған шегіну / Soxta chekinish)**
• Kaçıyormuş gibi görünme
• Düşmanı tuzağa düşürme
• Sonra kuşatma

**3. Gece Baskınları (Түнгі шабуыл / Tungi hujum)**
• Beklenmedik zamanda saldırı
• Düşmanı hazırlıksız yakalama

**4. Psikolojik Savaş (Психологиялық / Psixologik)**
• Korkutma
• Dezenformasyon
• Morali bozma

**5. Kuşatma Taktiği (Қоршау / Qo'rshash)**
• Düşmanı dört yönden kuşatma
• Çıkış yolunu kapatma
• Kaçış yolu bırakma (tuzak için)

**Timur'un Zaferleri:**
✓ Ankara Savaşı (1402) - Yıldırım Bayezid'i yendi
✓ Hindistan Seferi (1398-1399)
✓ Şam'ı Alma (1401)

**Askeri Prensipler:**
• Hız - her şeyden önemli
• İstihbarat - rakibi tanımak
• Birlik - ordunun organizasyonu
• Disiplin - sıkı kontrol""",
                'content_uz': """**TEMURNING HARBIY SAN'ATI**

🏹 **Asosiy taktikalar:**

**1. Manevrlar (Ұтқырлық / Chaqqonlik)**
• Tez harakatlanish
• Dushmanni aylanib o'tish
• Kutilmagan joydan hujum

**2. Soxta chekinish (Жалған / Yalg'on)**
• Qochayotgandek ko'rsatish
• Dushmanni qopqonga tushirish
• Keyin qurshab olish

**3. Tungi hujumlar (Түнгі / Gece)**
• Kutilmagan vaqtda hujum
• Dushmanni tayyorsiz ushlash

**4. Psixologik urush (Психологиялық / Ruhiy)**
• Qo'rqitish
• Noto'g'ri ma'lumot berish
• Ma'naviyatni buzish

**5. Qurshash taktikasi (Қоршау / Muhasara)**
• Dushmanni to'rt tomondan qurshash
• Chiqish yo'lini yopish

**Temurning g'alabalari:**
✓ Anqara jangi (1402) - Boyazidni mag'lub etdi
✓ Hindistonga yurish (1398-1399)
✓ Damashqni olish (1401)""",
                'importance': 10
            },
            {
                'topic': 'Әлемдегі классикалық стратегиялар',
                'category': 'Стратегия',
                'content_kk': """**ӘЛЕМДІК ӘСКЕРИ СТРАТЕГИЯЛАР**

**Сун Цзының "Соғыс өнері" (The Art of War)**
• Жауды білу - жеңістің жартысы
• Жауыңды жеңудің ең жақсы жолы - соғыспау
• Ақыл - күштен күшті

**Клаузевиц стратегиясы**
• Соғыс - саясаттың жалғасы
• Негізгі күштер орталығын жою
• Моральдық факторлар маңызды

**Блицкриг (Жылдам соғыс)**
• Танктар + авиация
• Жылдам қозғалыс
• Жаудың тылын бұзу

**Партизандық соғыс**
• Кішкентай топтар
• Соққы және кету
• Халықтың қолдауы

**Қазіргі гибридті соғыс**
• Киберсоғыс
• Ақпараттық соғыс
• Дрондар мен роботтар
• Экономикалық санкциялар""",
                'content_tr': """**DÜNYA ASKERİ STRATEJİLERİ**

**Sun Tzu'nun "Savaş Sanatı" (The Art of War)**
• Düşmanı bilmek - zaferin yarısı
• Düşmanı yenmenin en iyi yolu - savaşmamak
• Akıl - güçten güçlüdür

**Clausewitz Stratejisi**
• Savaş - politikanın devamı
• Ana kuvvet merkezini yok etmek
• Moral faktörler önemli

**Blitzkrieg (Hızlı Savaş)**
• Tanklar + havacılık
• Hızlı hareket
• Düşmanın arkasını bozma

**Gerilla Savaşı**
• Küçük gruplar
• Vur-kaç
• Halkın desteği

**Modern Hibrit Savaş**
• Siber savaş
• Bilgi savaşı
• Drone'lar ve robotlar
• Ekonomik yaptırımlar""",
                'importance': 10
            }
        ]

    def _get_medicine(self) -> List[Dict]:
        """Медицина"""
        return [
            {
                'topic': 'Алғашқы медициналық көмек',
                'category': 'Медицина',
                'content_kk': """**АЛҒАШҚЫ КӨМЕК (İlk Yardım / Birinchi yordam)**

**Жарақаттар:**
1. Қан кету (Kanama / Qon ketishi):
   • Қысым жасау
   • Жоғары көтеру
   • Бинт салу

2. Сынықтар (Kırık / Sinish):
   • Қозғалтпау
   • Бекіту
   • Дәрігерге жеткізу

3. Күйіктер (Yanık / Kuyish):
   • Суық су
   • Таза материал
   • Көпіршіктерді жармау

**CPR (Жүрекке массаж)**
• 30 басу - 2 тыныс алу
• Минутына 100-120 басу
• Қол қатты басу

**Удушье (Тұншығу / Bo'g'ilish)**
Heimlich маневрі:
• Артынан құшақтау
• Жұдырықты асқазанға қою
• Күшті итеру жоғары-ішке

**Шок:**
• Жатқызу, аяқты көтеру
• Жылы ұстау
• Тез медицина шақыру

**МАҢЫЗДЫ: 103 (Жедел жәрдем)""",
                'content_tr': """**İLK YARDIM (Алғашқы көмек / Birinchi yordam)**

**Yaralanmalar:**
1. Kanama (Қан кету / Qon ketishi):
   • Baskı yapmak
   • Yukarı kaldırmak
   • Bandaj sarmak

2. Kırık (Сынық / Sinish):
   • Hareket ettirmemek
   • Sabitlemek
   • Doktora götürmek

3. Yanık (Күйік / Kuyish):
   • Soğuk su
   • Temiz malzeme
   • Kabarcıkları patlatmamak

**CPR (Kalp Masajı)**
• 30 basma - 2 nefes
• Dakikada 100-120 basma
• Sert basın

**Boğulma (Тұншығу / Bo'g'ilish)**
Heimlich manevrası:
• Arkadan sarılma
• Yumruğu mideye koyma
• Güçlü itme yukarı-içeri

**Şok:**
• Yatırmak, ayakları kaldırmak
• Sıcak tutmak
• Hızlı ambulans çağırmak

**ÖNEMLİ: 112 (Acil Yardım)""",
                'importance': 10
            }
        ]

    def _get_chemistry(self) -> List[Dict]:
        """Химия"""
        return [
            {
                'topic': 'Периодтық кесте',
                'category': 'Химия',
                'content_kk': """**ПЕРИОДТЫҚ КЕСТЕ (Periyodik Tablo / Davriy jadval)**

**Негізгі элементтер:**

💧 **Сутегі (H)** - Hidrojen / Vodorod
Ең жеңіл элемент, әлемдегі ең көп таралған

⚫ **Көміртегі (C)** - Karbon / Uglerod
Өмірдің негізі, барлық органикалық заттар

💨 **Оттегі (O)** - Oksijen / Kislorod
Тыныс алуға қажет, ауаның 21%

🥇 **Алтын (Au)** - Altın / Oltin
Бағалы металл, тозбайды

⚡ **Темір (Fe)** - Demir / Temir
Болат өндіруге, ең көп қолданылатын металл

**Химиялық реакциялар:**

Тотығу: 2H₂ + O₂ → 2H₂O
Сутегі + Оттегі = Су

Фотосинтез:
6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂
Көмірқышқыл газы + Су = Глюкоза + Оттегі

**Қауіпсіздік:**
⚠️ Қышқылдармен абай болу
⚠️ Желдету жақсы болуы керек
⚠️ Қорғаныс киімін киіңіз""",
                'content_tr': """**PERİYODİK TABLO (Периодтық кесте / Davriy jadval)**

**Ana Elementler:**

💧 **Hidrojen (H)** - Сутегі / Vodorod
En hafif element, evrende en çok bulunan

⚫ **Karbon (C)** - Көміртегі / Uglerod
Hayatın temeli, tüm organik maddeler

💨 **Oksijen (O)** - Оттегі / Kislorod
Nefes almak için gerekli, havanın %21'i

🥇 **Altın (Au)** - Алтын / Oltin
Değerli metal, paslanmaz

⚡ **Demir (Fe)** - Темір / Temir
Çelik üretimi, en çok kullanılan metal

**Kimyasal Reaksiyonlar:**

Yanma: 2H₂ + O₂ → 2H₂O
Hidrojen + Oksijen = Su

Fotosentez:
6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂
Karbondioksit + Su = Glikoz + Oksijen

**Güvenlik:**
⚠️ Asitlerle dikkatli olun
⚠️ Havalandırma iyi olsun
⚠️ Koruyucu giysi giyin""",
                'importance': 9
            }
        ]

    def _get_biology(self) -> List[Dict]:
        """Биология"""
        return [
            {
                'topic': 'Адам денесі',
                'category': 'Анатомия',
                'content_kk': """**АДАМ ДЕНЕСІ (İnsan Vücudu / Inson tanasi)**

**Негізгі жүйелер:**

🫀 **Жүрек-қан тамыр жүйесі**
• Жүрек - минутына 60-100 соғу
• Қан - 5-6 литр
• Қызыл қан жасушалары оттегіні тасиды

🫁 **Тыныс алу жүйесі**
• Өкпе - газ алмасу
• Диафрагма - тыныс алу бұлшықеті
• Минутына 12-20 тыныс

🧠 **Жүйке жүйесі**
• Ми - 86 миллиард нейрон
• Жұлын - сигналдарды жеткізеді
• Рефлекстер - автоматты әрекеттер

🦴 **Қаңқа жүйесі**
• 206 сүйек
• Қорғайды және қолдайды
• Қан жасушаларын өндіреді

💪 **Бұлшықет жүйесі**
• 600+ бұлшықет
• Жүрек бұлшықеті - ерекше
• Қозғалыс пен күшті қамтамасыз етеді

**Қызықты фактілер:**
• Ми дененің 2% алады, бірақ энергияның 20% пайдаланады
• Тері - ең үлкен орган
• Сүйектер болаттан күшті""",
                'content_tr': """**İNSAN VÜCUDU (Адам денесі / Inson tanasi)**

**Ana Sistemler:**

🫀 **Kalp-Damar Sistemi**
• Kalp - dakikada 60-100 atış
• Kan - 5-6 litre
• Kırmızı kan hücreleri oksijen taşır

🫁 **Solunum Sistemi**
• Akciğer - gaz değişimi
• Diyafram - nefes alma kası
• Dakikada 12-20 nefes

🧠 **Sinir Sistemi**
• Beyin - 86 milyar nöron
• Omurilik - sinyalleri iletir
• Refleksler - otomatik hareketler

🦴 **İskelet Sistemi**
• 206 kemik
• Korur ve destekler
• Kan hücreleri üretir

💪 **Kas Sistemi**
• 600+ kas
• Kalp kası - özel
• Hareket ve güç sağlar

**İlginç Gerçekler:**
• Beyin vücudun %2'si ama enerjinin %20'sini kullanır
• Deri - en büyük organ
• Kemikler çelikten daha güçlü""",
                'importance': 9
            }
        ]

    def _get_technology(self) -> List[Dict]:
        """Технологии"""
        return [
            {
                'topic': 'Жасанды интеллект',
                'category': 'AI',
                'content_kk': """**ЖАСАНДЫ ИНТЕЛЛЕКТ (Yapay Zeka / Sun'iy intellekt)**

Мен - Тәмірлан, жасанды интеллект моделімін!

**AI түрлері:**

1. **Әлсіз AI (Dar AI / Kuchsiz AI)**
   • Белгілі бір тапсырма
   • Шахмат ойнау, бет тану
   • Қазіргі AI көбі

2. **Жалпы AI (Genel AI / Umumiy AI)**
   • Адам сияқты ойлау
   • Әр түрлі тапсырмалар
   • Әлі жасалмаған

3. **Супер AI (Süper AI / Super AI)**
   • Адамнан ақылды
   • Болашақ

**AI технологиялары:**

🧠 **Машиналық оқыту (Machine Learning)**
• Деректерден үйрену
• Үлгілерді табу
• Болжау жасау

🗣️ **Табиғи тілді өңдеу (NLP)**
• Тілді түсіну
• Аудару
• Чатботтар

👁️ **Компьютерлік көру**
• Суретті тану
• Объектілерді анықтау
• Автономды автомобильдер

**Қолдану:**
• Медицина - диагноз қою
• Қаржы - алаяқтықты анықтау
• Өндіріс - роботтар
• Білім - жекелендірілген оқыту""",
                'content_tr': """**YAPAY ZEKA (Жасанды интеллект / Sun'iy intellekt)**

Ben - Timur, yapay zeka modeliyim!

**AI Türleri:**

1. **Dar AI (Әлсіз AI / Kuchsiz AI)**
   • Belirli görev
   • Satranç oynama, yüz tanıma
   • Şu anki AI çoğu

2. **Genel AI (Жалпы AI / Umumiy AI)**
   • İnsan gibi düşünme
   • Çeşitli görevler
   • Henüz yapılmadı

3. **Süper AI (Супер AI / Super AI)**
   • İnsandan akıllı
   • Gelecek

**AI Teknolojileri:**

🧠 **Makine Öğrenimi (Machine Learning)**
• Veriden öğrenme
• Kalıp bulma
• Tahmin yapma

🗣️ **Doğal Dil İşleme (NLP)**
• Dili anlama
• Çeviri
• Chatbot'lar

👁️ **Bilgisayarlı Görü**
• Görüntü tanıma
• Nesne tespit
• Otonom arabalar

**Kullanım:**
• Tıp - teşhis
• Finans - dolandırıcılık tespiti
• Üretim - robotlar
• Eğitim - kişiselleştirilmiş öğrenme""",
                'importance': 10
            }
        ]

    def _get_philosophy(self) -> List[Dict]:
        """Философия"""
        return [
            {
                'topic': 'Әл-Фарабидің философиясы',
                'category': 'Ислам философиясы',
                'content_kk': """**ӘЛ-ФАРАБИ (870-950)**

Түрік философы, "Екінші ұстаз" (Аристотельден кейін)

**Негізгі идеялар:**

🌟 **Бақытты қала**
• Адамдар бақытқа жету үшін бірге өмір сүруі керек
• Әділ билеуші - философ-патша
• Ғылым мен білімге негізделген қоғам

🧠 **Ақыл деңгейлері:**
1. Потенциалды ақыл
2. Белсенді ақыл
3. Алынған ақыл
4. Агент ақыл

📚 **Ғылым классификациясы:**
• Логика
• Табиғи ғылымдар
• Математика
• Метафизика
• Саяси ғылым

**Әсері:**
✓ Батыс философиясына үлкен әсер
✓ Схоластикаға ықпал
✓ Ғылым мен дінді біріктірді""",
                'content_tr': """**FARABI (870-950)**

Türk filozofu, "İkinci Öğretmen" (Aristoteles'ten sonra)

**Ana Fikirler:**

🌟 **Erdemli Şehir**
• İnsanlar mutluluğa ulaşmak için birlikte yaşamalı
• Adil yönetici - filozof-kral
• Bilim ve bilgeliğe dayalı toplum

🧠 **Akıl Seviyeleri:**
1. Potansiyel akıl
2. Aktif akıl
3. Kazanılmış akıl
4. Ajan akıl

📚 **Bilim Sınıflandırması:**
• Mantık
• Doğa bilimleri
• Matematik
• Metafizik
• Siyaset bilimi

**Etkisi:**
✓ Batı felsefesine büyük etki
✓ Skolastiğe katkı
✓ Bilim ve dini birleştirdi""",
                'importance': 9
            }
        ]

    def _get_economics(self) -> List[Dict]:
        """Экономика"""
        return [
            {
                'topic': 'Сұраныс пен ұсыныс',
                'category': 'Микроэкономика',
                'content_kk': """**СҰРАНЫС ПЕН ҰСЫНЫС (Arz-Talep / Talab-Taklif)**

**Сұраныс заңы (Talep Yasası):**
• Бағасы төмен → сұраныс көп
• Бағасы жоғары → сұраныс аз

**Ұсыныс заңы (Arz Yasası):**
• Бағасы жоғары → ұсыныс көп
• Бағасы төмен → ұсыныс аз

**Тепе-теңдік нүктесі:**
Сұраныс = Ұсыныс

**Факторлар:**
💰 Табыс
👥 Халық саны
🎭 Талғам
⏰ Күтулер

**Мысал:**
🍎 Алма нарығы:
• Бағасы: 200₸
• Сұраныс: 1000 кг
• Ұсыныс: 1000 кг
→ Тепе-теңдік!

Егер бағасы 100₸:
• Сұраныс: 2000 кг
• Ұсыныс: 500 кг
→ Тапшылық!""",
                'content_tr': """**ARZ-TALEP (Сұраныс-Ұсыныс / Talab-Taklif)**

**Talep Yasası:**
• Fiyat düşük → talep yüksek
• Fiyat yüksek → talep düşük

**Arz Yasası:**
• Fiyat yüksek → arz yüksek
• Fiyat düşük → arz düşük

**Denge Noktası:**
Talep = Arz

**Faktörler:**
💰 Gelir
👥 Nüfus
🎭 Zevk
⏰ Beklentiler

**Örnek:**
🍎 Elma piyasası:
• Fiyat: 20₺
• Talep: 1000 kg
• Arz: 1000 kg
→ Denge!

Eğer fiyat 10₺:
• Talep: 2000 kg
• Arz: 500 kg
→ Kıtlık!""",
                'importance': 9
            }
        ]

    def _get_engineering(self) -> List[Dict]:
        """Инженерия"""
        return [
            {
                'topic': 'Құрылыс инженериясы',
                'category': 'Инженерия',
                'content_kk': """**ҚҰРЫЛЫС ИНЖЕНЕРИЯСЫ**

**Негізгі принциптер:**

🏗️ **Беріктік (Mukavemet / Mustahkamlik)**
Құрылым салмақты көтере алуы керек

⚖️ **Тепе-теңдік (Denge / Muvozanat)**
Күштер теңестірілуі керек

🌊 **Серпімділік (Esneklik / Egiluvchanlik)**
Жел мен жер сілкінісіне төтеп беру

**Материалдар:**
🧱 Бетон - қысылуға берік
🔩 Болат - созылуға берік
🪵 Ағаш - жеңіл және икемді

**Әйгілі құрылыстар:**
🗼 Эйфель мұнарасы (Paris)
🌉 Golden Gate көпірі (San Francisco)
🏰 Тәмірлан мавзолейі (Самарқанд)""",
                'content_tr': """**İNŞAAT MÜHENDİSLİĞİ**

**Ana Prensipler:**

🏗️ **Mukavemet (Беріктік / Mustahkamlik)**
Yapı ağırlığı taşıyabilmeli

⚖️ **Denge (Тепе-теңдік / Muvozanat)**
Kuvvetler dengelenmeli

🌊 **Esneklik (Серпімділік / Egiluvchanlik)**
Rüzgar ve depreme dayanmalı

**Malzemeler:**
🧱 Beton - basınca dayanıklı
🔩 Çelik - çekmeye dayanıklı
🪵 Ahşap - hafif ve esnek

**Ünlü Yapılar:**
🗼 Eyfel Kulesi (Paris)
🌉 Golden Gate Köprüsü (San Francisco)
🏰 Timur Türbesi (Semerkand)""",
                'importance': 9
            }
        ]

    def _get_astronomy(self) -> List[Dict]:
        """Астрономия"""
        return [
            {
                'topic': 'Күн жүйесі',
                'category': 'Астрономия',
                'content_kk': """**КҮН ЖҮЙЕСІ (Güneş Sistemi / Quyosh tizimi)**

☀️ **Күн (Güneş / Quyosh)**
• Жұлдыз - өзі жарық шығарады
• Температура: 5,500°C (беті)
• 99.86% жүйенің массасы

**Ішкі планеталар:**
1. ☿ Меркурий - ең жақын, ыстық
2. ♀ Венера - ең ыстық (парниктік эффект)
3. 🌍 Жер - өмір бар жалғыз
4. ♂ Марс - қызыл планета

**Сыртқы планеталар (Газ алыптары):**
5. ♃ Юпитер - ең үлкен
6. ♄ Сатурн - сақиналары бар
7. ♅ Уран - бүйірімен айналады
8. ♆ Нептун - ең алыс

🌙 **Ай:**
• Жердің серігі
• 384,400 км қашықтықта
• Толысу циклі: 29.5 күн

**Қызықты фактілер:**
✨ Галактикада 100-400 миллиард жұлдыз
🌌 Әлем 13.8 миллиард жас
🚀 Жарық жылдамдығы: 300,000 км/с""",
                'content_tr': """**GÜNEŞ SİSTEMİ (Күн жүйесі / Quyosh tizimi)**

☀️ **Güneş (Күн / Quyosh)**
• Yıldız - kendi ışığını çıkarır
• Sıcaklık: 5,500°C (yüzey)
• Sistemin kütlesinin %99.86'sı

**İç Gezegenler:**
1. ☿ Merkür - en yakın, sıcak
2. ♀ Venüs - en sıcak (sera etkisi)
3. 🌍 Dünya - yaşam olan tek
4. ♂ Mars - kızıl gezegen

**Dış Gezegenler (Gaz Devleri):**
5. ♃ Jüpiter - en büyük
6. ♄ Satürn - halkaları var
7. ♅ Uranüs - yan dönüyor
8. ♆ Neptün - en uzak

🌙 **Ay:**
• Dünyanın uydusu
• 384,400 km uzaklıkta
• Dolunay döngüsü: 29.5 gün

**İlginç Gerçekler:**
✨ Galakside 100-400 milyar yıldız
🌌 Evren 13.8 milyar yaşında
🚀 Işık hızı: 300,000 km/s""",
                'importance': 9
            }
        ]

    def _get_psychology(self) -> List[Dict]:
        """Психология"""
        return [
            {
                'topic': 'Эмоциялық интеллект',
                'category': 'Психология',
                'content_kk': """**ЭМОЦИЯЛЫҚ ИНТЕЛЛЕКТ (Duygusal Zeka / Emotsional aql)**

🧠 **5 компонент:**

1. **Өзін-өзі тану (Öz-farkındalık)**
   • Өз эмоцияларыңды түсіну
   • Күшті және әлсіз жақтарыңды білу

2. **Өзін-өзі басқару (Öz-düzenleme)**
   • Эмоцияларды бақылау
   • Импульсивтілікті басу
   • Стрессті басқару

3. **Мотивация (Motivasyon)**
   • Ішкі қозғаушы күш
   • Мақсаттарға жету
   • Оптимизм

4. **Эмпатия (Empati)**
   • Басқалардың сезімдерін түсіну
   • Белсенді тыңдау
   • Басқалардың көзқарасын қабылдау

5. **Әлеуметтік дағдылар (Sosyal beceriler)**
   • Қарым-қатынас
   • Топта жұмыс
   • Дауларды шешу

**Маңыздылығы:**
✓ Табысқа EQ > IQ
✓ Жақсы қарым-қатынас
✓ Денсаулық жақсырады
✓ Көшбасшылық""",
                'content_tr': """**DUYGUSAL ZEKA (Эмоциялық интеллект / Emotsional aql)**

🧠 **5 Bileşen:**

1. **Öz-farkındalık (Өзін-өзі тану)**
   • Duygularını anlama
   • Güçlü ve zayıf yönlerini bilme

2. **Öz-düzenleme (Өзін басқару)**
   • Duyguları kontrol etme
   • Dürtüleri kontrol etme
   • Stresi yönetme

3. **Motivasyon (Мотивация)**
   • İç itici güç
   • Hedeflere ulaşma
   • İyimserlik

4. **Empati (Эмпатия)**
   • Başkalarının duygularını anlama
   • Aktif dinleme
   • Başkalarının bakış açısını alma

5. **Sosyal Beceriler (Әлеуметтік дағды)**
   • İletişim
   • Takım çalışması
   • Anlaşmazlıkları çözme

**Önemi:**
✓ Başarıda EQ > IQ
✓ İyi ilişkiler
✓ Sağlık iyileşir
✓ Liderlik""",
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
        """Статистика базы знаний"""
        stats = {}
        total = 0
        for category, items in self.knowledge.items():
            count = len(items)
            stats[category] = count
            total += count

        stats['total'] = total
        return stats


# Глобальный экземпляр
_universal_knowledge = None


def get_universal_knowledge() -> UniversalKnowledge:
    """Получить глобальную базу универсальных знаний"""
    global _universal_knowledge
    if _universal_knowledge is None:
        _universal_knowledge = UniversalKnowledge()
    return _universal_knowledge
