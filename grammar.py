"""القواعد النحوية - 18 قاعدة من Netzwerk neu B1."""

GRAMMAR = [
    {
        "id": "g1",
        "k": 1,
        "title_de": "Infinitiv mit zu",
        "title_ar": "المصدر مع zu",
        "explanation": """بعد أفعال: anfangen, aufhören, planen, vergessen, versuchen, vorhaben, empfehlen
بعد صفات: Es ist gut/wichtig/schön + zu
بعد أسماء: Lust/Zeit/Angst haben + zu""",
        "table": {
            "headers": ["السياق", "المثال"],
            "rows": [
                ["Verb", "Anna schlägt vor, nach Berlin zu fahren."],
                ["Adjektiv + sein", "Es ist gut, sich im Urlaub auszuruhen."],
                ["Nomen + haben", "Anna hat keine Zeit, ins Reisebüro zu gehen."]
            ]
        },
        "examples": [
            {"de": "Vergiss nicht, deinen Pass mitzunehmen!", "ar": "لا تنسَ أخذ جواز سفرك!"},
            {"de": "Es macht Spaß, Deutsch zu lernen.", "ar": "يُسعدني تعلّم الألمانية."},
            {"de": "Ich habe Lust, im Urlaub zu faulenzen.", "ar": "أشتاق إلى الاسترخاء في العطلة."}
        ],
        "tip": "مع الأفعال المركبة: zu في المنتصف → mit+zu+nehmen = mitzunehmen | auf+zu+hören = aufzuhören",
        "order_index": 0
    },
    {
        "id": "g2",
        "k": 1,
        "title_de": "Nebensatz: da/weil & obwohl",
        "title_ar": "لأن / رغم أن",
        "explanation": "da/weil = لأن (السبب). obwohl = رغم أن (التناقض). الفعل في نهاية الجملة الفرعية دائماً.",
        "examples": [
            {"de": "Da/Weil Rothenburg sehr bekannt ist, kommen viele Touristen.", "ar": "لأن روتنبورغ مشهورة يأتي كثير من السياح."},
            {"de": "Melina hatte schöne Tage, obwohl das Wetter schlecht war.", "ar": "كان لدى ميلينا أيام جميلة رغم الطقس السيئ."},
            {"de": "Ich bleibe zu Hause, weil ich krank bin.", "ar": "أبقى في البيت لأنني مريض."}
        ],
        "tip": "da و weil = نفس المعنى | da أكثر في بداية الجملة | وweil في الوسط",
        "order_index": 1
    },
    {
        "id": "g3",
        "k": 2,
        "title_de": "lassen + Infinitiv",
        "title_ar": "فعل lassen",
        "explanation": """lassen + Infinitiv بدون zu
① يجعل شخصاً يفعل شيئاً ② يسمح بفعل ③ يترك""",
        "table": {
            "headers": ["الزمن", "المثال"],
            "rows": [
                ["Präsens", "Sie lässt ihr Handy reparieren."],
                ["Perfekt", "Sie hat ihr Handy reparieren lassen."]
            ]
        },
        "examples": [
            {"de": "Ich lasse mein Auto reparieren.", "ar": "أجعل سيارتي تُصلَح."},
            {"de": "Lass mich das erklären!", "ar": "دعني أشرح هذا!"}
        ],
        "tip": "❌ lasse es ZU reparieren — خطأ! دائماً بدون zu",
        "order_index": 0
    },
    {
        "id": "g4",
        "k": 2,
        "title_de": "Folgen ausdrücken",
        "title_ar": "deshalb | sodass | so...dass",
        "explanation": """deshalb/deswegen/darum/daher = في الجملة الرئيسية، الفعل في المكان الثاني
sodass / so...dass = جملة فرعية، الفعل في النهاية""",
        "examples": [
            {"de": "Tarik ist viel unterwegs, darum braucht er eine Powerbank.", "ar": "تاريك في تنقل دائم لذا يحتاج شاحناً محمولاً."},
            {"de": "Online gibt es keine Beratung, sodass er lieber ins Geschäft geht.", "ar": "عبر الإنترنت لا استشارة لذا يفضل المحل."},
            {"de": "Der Kopfhörer war so teuer, dass sie lange sparen musste.", "ar": "كانت السماعة غالية جداً لدرجة أنها اضطرت للادخار."}
        ],
        "tip": "deshalb → فعل في المكان 2 | sodass → فعل في النهاية",
        "order_index": 1
    },
    {
        "id": "g5",
        "k": 2,
        "title_de": "Genitiv",
        "title_ar": "حالة الملكية",
        "explanation": "للتعبير عن الملكية وبعد: wegen, trotz, während, innerhalb, außerhalb",
        "table": {
            "headers": ["الجنس", "المعرّف", "مثال"],
            "rows": [
                ["Maskulin/Neutrum", "des + (e)s", "der Inhalt des Kühlschranks"],
                ["Feminin/Plural", "der", "das Haus der Familie | die Nachrichten der Gäste"]
            ]
        },
        "examples": [
            {"de": "wegen der hohen Kosten", "ar": "بسبب التكاليف العالية"},
            {"de": "trotz der smarten Technik", "ar": "رغم التقنية الذكية"},
            {"de": "während des Urlaubs", "ar": "خلال الإجازة"}
        ],
        "tip": "wegen + Gen | trotz + Gen | während + Gen | innerhalb + Gen | außerhalb + Gen",
        "order_index": 2
    },
    {
        "id": "g6",
        "k": 3,
        "title_de": "Präteritum",
        "title_ar": "الماضي البسيط",
        "explanation": "للنصوص المكتوبة (روايات، صحف). sein/haben/Modalverben نستخدمها دائماً في المحادثة.",
        "table": {
            "headers": ["النوع", "القاعدة", "مثال"],
            "rows": [
                ["منتظم", "-te Endung", "machen→machte, leben→lebte"],
                ["غير منتظم", "تغيير الجذر", "sehen→sah, kommen→kam, gehen→ging"],
                ["sein", "", "ich/er war — wir/sie waren"],
                ["haben", "", "ich/er hatte — wir/sie hatten"],
                ["können", "", "ich/er konnte"],
                ["müssen", "", "ich/er musste"],
                ["wissen", "!", "wusste"],
                ["denken", "!", "dachte"]
            ]
        },
        "examples": [
            {"de": "Sie suchte einen Platz auf der Alm.", "ar": "كانت تبحث عن مكان في المرعى."},
            {"de": "Von einem Tag auf den anderen veränderte sich ihr Leben radikal.", "ar": "تغيّرت حياتها تغيّراً جذرياً."},
            {"de": "Als Kind spielte er immer draußen.", "ar": "كطفل كان يلعب دائماً في الخارج."}
        ],
        "tip": "للامتحان: احفظ sein/haben/Modalverben! راجع قائمة الأفعال غير المنتظمة ص170 من الكتاب",
        "order_index": 0
    },
    {
        "id": "g7",
        "k": 4,
        "title_de": "Konjunktiv II",
        "title_ar": "الأسلوب الشرطي",
        "explanation": "للتعبير عن: الأمنيات، النصائح، الفرضيات، الأدب الزائد",
        "table": {
            "headers": ["الفعل", "Konjunktiv II"],
            "rows": [
                ["sein", "wäre"],
                ["haben", "hätte"],
                ["können", "könnte"],
                ["müssen", "müsste"],
                ["dürfen", "dürfte"],
                ["wollen", "wollte"],
                ["sollen", "sollte"],
                ["werden", "würde"],
                ["andere Verben", "würde + Infinitiv"]
            ]
        },
        "examples": [
            {"de": "Wenn ich Zeit hätte, würde ich noch einen Kaffee trinken.", "ar": "لو كان لديّ وقت لشربت قهوة أخرى."},
            {"de": "Wenn Boris nicht so gestresst wäre, wäre die Pause lustiger.", "ar": "لو لم يكن بوريس متوتراً لكانت الاستراحة ممتعة."},
            {"de": "Du solltest mehr schlafen.", "ar": "يجب أن تنام أكثر."}
        ],
        "tip": "للنصح: Du solltest/könntest... | للأمنية: Ich würde gern... | للفرضية: Wenn...",
        "order_index": 0
    },
    {
        "id": "g8",
        "k": 4,
        "title_de": "Pronomen & Pronominaladverbien",
        "title_ar": "الضمائر وظروف الجر",
        "explanation": """الأشخاص: حرف الجر + ضمير الشخص
الأشياء والأحداث: da(r) + حرف الجر""",
        "table": {
            "headers": ["النوع", "مثال"],
            "rows": [
                ["شخص", "mit ihm / mit ihr / mit ihnen"],
                ["شيء/حدث", "damit / davon / daran / darüber"],
                ["فعل + Infinitiv", "darauf, eine Antwort zu bekommen"]
            ]
        },
        "examples": [
            {"de": "Rufen Sie den Personalchef an. Mit ihm können Sie sprechen.", "ar": "اتصل بمدير الموظفين. يمكنك الحديث معه."},
            {"de": "Es gibt eine freie Stelle. Er hat sich danach erkundigt.", "ar": "هناك وظيفة شاغرة. استفسر عنها."},
            {"de": "Er wartet darauf, dass er eine Antwort bekommt.", "ar": "ينتظر الحصول على رد."}
        ],
        "tip": "الحرف يبدأ بمتحرك: dar + حرف الجر → darauf, darin, darüber (وليس daauf)",
        "order_index": 1
    },
    {
        "id": "g9",
        "k": 5,
        "title_de": "Komparativ & Superlativ vor Nomen",
        "title_ar": "المقارنة والتفضيل أمام اسم",
        "explanation": "عند استخدام Komparativ/Superlativ قبل اسم تأتي نفس نهايات الصفة. استثناء: mehr و weniger بدون نهايات",
        "table": {
            "headers": ["الدرجة", "مثال"],
            "rows": [
                ["Positiv", "Das ist eine gute Alternative."],
                ["Komparativ", "Das ist eine bessere Alternative."],
                ["Superlativ", "Das ist die beste Alternative."],
                ["Ausnahme", "Der Geschirrspüler verbraucht weniger Wasser."]
            ]
        },
        "examples": [
            {"de": "Mehrwegflaschen sind die beste Alternative.", "ar": "زجاجات إعادة الاستخدام هي الخيار الأفضل."},
            {"de": "Ich hätte gern ein besseres Fahrrad.", "ar": "أودّ الحصول على دراجة أفضل."},
            {"de": "Das modernste Handy kauft er immer.", "ar": "دائماً يشتري أحدث هاتف."}
        ],
        "tip": "mehr / weniger = بدون أي نهايات أمام الاسم!",
        "order_index": 0
    },
    {
        "id": "g10",
        "k": 5,
        "title_de": "Nebensatz: damit & um … zu",
        "title_ar": "جمل الغاية",
        "explanation": """damit: لكي — يُستخدم عندما يختلف فاعل الجملتين أو يتطابقان
um…zu: من أجل أن — فقط عندما يتطابق الفاعل في الجملتين""",
        "table": {
            "headers": ["الرابط", "الفاعل", "مثال"],
            "rows": [
                ["damit", "مختلف أو متطابق", "Die SUNNYBAG-Tasche hat Akku, damit man das Handy aufladen kann."],
                ["um...zu", "متطابق فقط", "Ich kaufe regionale Produkte, um die Umwelt zu schützen."]
            ]
        },
        "examples": [
            {"de": "Viele Kunden kaufen die Tasche, damit sie in der Natur Strom haben.", "ar": "يشتري كثيرون الحقيبة لكي يكون لديهم طاقة في الطبيعة."},
            {"de": "Ich lerne Deutsch, um in Deutschland zu arbeiten.", "ar": "أتعلم الألمانية لكي أعمل في ألمانيا."}
        ],
        "tip": "um...zu = فاعل واحد فقط | damit = يمكن استخدامه دائماً (الأضمن)",
        "order_index": 1
    },
    {
        "id": "g11",
        "k": 6,
        "title_de": "Futur I",
        "title_ar": "المستقبل",
        "explanation": "للتعبير عن: المستقبل، التوقعات، الوعود. werden + Infinitiv. في المحادثة نستخدم Präsens + ظرف زمان أكثر",
        "table": {
            "headers": ["الضمير", "Futur I"],
            "rows": [
                ["ich", "werde + Inf."],
                ["du", "wirst + Inf."],
                ["er/sie/es", "wird + Inf."],
                ["wir", "werden + Inf."],
                ["ihr", "werdet + Inf."],
                ["sie/Sie", "werden + Inf."]
            ]
        },
        "examples": [
            {"de": "In der Zukunft werden Menschen auf dem Mars leben.", "ar": "في المستقبل سيعيش البشر على المريخ."},
            {"de": "Ich werde nächstes Jahr mehr Sport machen.", "ar": "سأمارس الرياضة أكثر العام القادم."}
        ],
        "tip": "Präsens + Zeit = auch Futur: Ich fahre morgen nach München. ← محادثة يومية",
        "order_index": 0
    },
    {
        "id": "g12",
        "k": 6,
        "title_de": "n-Deklination",
        "title_ar": "الأسماء الضعيفة",
        "explanation": "بعض الأسماء المذكرة تأخذ -en / -n في كل الحالات ما عدا Nominativ Singular",
        "table": {
            "headers": ["الحالة", "مثال"],
            "rows": [
                ["Nominativ", "der Student / ein Student"],
                ["Akkusativ", "den Studenten / einen Studenten"],
                ["Dativ", "dem Studenten / einem Studenten"],
                ["Genitiv", "des Studenten / eines Studenten"]
            ]
        },
        "examples": [
            {"de": "Ich kenne einen Studenten, der viel reist.", "ar": "أعرف طالباً يسافر كثيراً."},
            {"de": "Ich wollte den Kollegen anrufen.", "ar": "أردت الاتصال بالزميل."}
        ],
        "tip": "قائمة: der Student, der Kollege, der Mensch, der Nachbar, der Experte, der Journalist, der Herr",
        "order_index": 1
    },
    {
        "id": "g13",
        "k": 6,
        "title_de": "Relativsätze im Dativ",
        "title_ar": "جمل الوصف في حالة الجر",
        "explanation": "الضمير الوصفي يتبع جنس وحالة الاسم الموصوف. مع حرف جر يأتي أولاً",
        "table": {
            "headers": ["الجنس", "Nom", "Akk", "Dativ"],
            "rows": [
                ["Maskulin", "der", "den", "dem"],
                ["Feminin", "die", "die", "der"],
                ["Neutrum", "das", "das", "dem"],
                ["Plural", "die", "die", "denen"]
            ]
        },
        "examples": [
            {"de": "Das ist der Mann, dem ich geholfen habe.", "ar": "هذا هو الرجل الذي ساعدته."},
            {"de": "Das ist die Frau, mit der ich gesprochen habe.", "ar": "هذه هي المرأة التي تحدثت معها."}
        ],
        "tip": "حرف الجر يأتي دائماً قبل الضمير الوصفي: mit der | auf dem | für den",
        "order_index": 2
    },
    {
        "id": "g14",
        "k": 7,
        "title_de": "Plusquamperfekt",
        "title_ar": "الماضي البعيد",
        "explanation": "للأحداث التي حدثت قبل حدث آخر في الماضي. hatte/war + Partizip II",
        "examples": [
            {"de": "Wir hatten uns fast jeden Tag getroffen. (noch früher)", "ar": "كنا نلتقي كل يوم تقريباً (قبل ذلك)."},
            {"de": "Nachdem Matilda ihr Studium abgeschlossen hatte, fand sie eine Stelle.", "ar": "بعد أن أتمّت دراستها وجدت وظيفة."}
        ],
        "tip": "nachdem + Plusquamperfekt → Präteritum في الجملة الرئيسية",
        "order_index": 0
    },
    {
        "id": "g15",
        "k": 7,
        "title_de": "Temporale Nebensätze",
        "title_ar": "روابط الزمان",
        "table": {
            "headers": ["الرابط", "المعنى", "مثال"],
            "rows": [
                ["nachdem", "بعد أن", "Nachdem Matilda umgezogen war, fühlte sie sich einsam."],
                ["bevor", "قبل أن", "Bevor ich putze, koche ich Kaffee."],
                ["während", "بينما", "Während ich aufräume, kochst du für uns."],
                ["seit/seitdem", "منذ أن", "Seit du arbeitest, bist du gestresst."],
                ["bis", "حتى", "Wir warten, bis du zurückkommst."]
            ]
        },
        "examples": [
            {"de": "Nachdem sie in Freiburg neue Freunde gefunden hat, gefällt es ihr dort sehr gut.", "ar": "بعد أن وجدت أصدقاء جدداً أعجبها المكان."},
            {"de": "Bevor ich putze, mache ich einen Kaffee.", "ar": "قبل أن أنظّف أصنع قهوة."}
        ],
        "tip": "nachdem + Plusquamperfekt | während + Präsens في كلتا الجملتين",
        "order_index": 1
    },
    {
        "id": "g16",
        "k": 8,
        "title_de": "Zweiteilige Konnektoren",
        "title_ar": "الروابط الثنائية",
        "table": {
            "headers": ["الرابط", "المعنى", "مثال"],
            "rows": [
                ["sowohl … als auch", "كلٌّ من ... و", "Er spricht sowohl Arabisch als auch Deutsch."],
                ["entweder … oder", "إما ... أو", "Entweder Klassik oder Metal."],
                ["weder … noch", "لا ... ولا", "Er trinkt weder Kaffee noch Tee."],
                ["nicht nur … sondern auch", "ليس فقط ... بل أيضاً", "Musik ist nicht nur Unterhaltung, sondern auch Therapie."],
                ["zwar … aber", "صحيح ... لكن", "Das ist zwar teuer, aber gut."]
            ]
        },
        "examples": [
            {"de": "Das Gehirn verarbeitet Musik sowohl im Bereich für Sprache als auch für Gefühle.", "ar": "يعالج الدماغ الموسيقى في منطقة اللغة وكذلك المشاعر."},
            {"de": "Er trinkt weder Kaffee noch Tee.", "ar": "لا يشرب قهوة ولا شاياً."}
        ],
        "tip": "هذه الروابط مهمة جداً في Schreiben وSprechen في B1!",
        "order_index": 0
    },
    {
        "id": "g17",
        "k": 10,
        "title_de": "Passiv",
        "title_ar": "المبني للمجهول",
        "explanation": "يُركّز على الفعل لا على الفاعل. werden + Partizip II. لذكر الفاعل: von + Dativ",
        "table": {
            "headers": ["الزمن", "التكوين", "مثال"],
            "rows": [
                ["Präsens", "wird + Part.II", "Die Lebensmittel werden verteilt."],
                ["Präteritum", "wurde + Part.II", "Die Tafel wurde 1993 gegründet."],
                ["Perfekt", "ist + Part.II + worden", "Viele Tafeln sind gegründet worden."],
                ["mit Modalverb", "müssen/können/sollen + Part.II + werden", "Die Lebensmittel müssen verteilt werden."]
            ]
        },
        "examples": [
            {"de": "Die Lebensmittel werden von der Tafel verteilt.", "ar": "يتم توزيع الغذاء من قِبَل جمعية Tafel."},
            {"de": "Das Konzept wurde aus den USA übernommen.", "ar": "اقتُبس المفهوم من الولايات المتحدة."}
        ],
        "tip": "Passiv Perfekt: ist/sind + Partizip II + worden (وليس geworden)",
        "order_index": 0
    },
    {
        "id": "g18",
        "k": 12,
        "title_de": "Partizip I & II als Adjektiv",
        "title_ar": "اسم الفاعل واسم المفعول صفةً",
        "explanation": """Partizip I = Infinitiv + d → فعل جارٍ
Partizip II = فعل منتهٍ
كلاهما يأخذان نهايات الصفة""",
        "table": {
            "headers": ["النوع", "التكوين", "مثال"],
            "rows": [
                ["Partizip I", "sinken + d → sinkend", "sinkende Preise = Preise, die sinken"],
                ["Partizip I", "steigen + d → steigend", "steigende Temperaturen"],
                ["Partizip II", "überweisen → überwiesen", "der überwiesene Betrag"],
                ["Partizip II", "speichern → gespeichert", "eine gespeicherte PIN"]
            ]
        },
        "examples": [
            {"de": "Je mehr Konkurrenz, desto günstiger werden die sinkenden Preise.", "ar": "كلما زادت المنافسة كلما انخفضت الأسعار."},
            {"de": "Den überwiesenen Betrag erhalten Sie innerhalb eines Tages.", "ar": "ستحصل على المبلغ المحوَّل خلال يوم."}
        ],
        "tip": "Partizip I = فعل في نفس الوقت | Partizip II = فعل قبله أو مبني للمجهول",
        "order_index": 0
    }
]