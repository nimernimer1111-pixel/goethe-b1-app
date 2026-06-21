"""أسئلة الكويز - 26 سؤال تغطي كل القواعد."""

QUIZ = [
    {
        "q": "Vergiss nicht, deinen Pass ___ nehmen.",
        "opts": ["mitzunehmen", "zu mit nehmen", "zu nehmen mit", "nehmen zu"],
        "cor": 0,
        "exp": "مع الأفعال المركبة zu في المنتصف: mit+zu+nehmen = mitzunehmen",
        "k": 1,
        "difficulty": 2
    },
    {
        "q": "Paula schlägt vor, nach Berlin ___ fahren.",
        "opts": ["zu", "zu zu", "—", "zum"],
        "cor": 0,
        "exp": "schlagen vor + Infinitiv mit zu → zu fahren",
        "k": 1,
        "difficulty": 1
    },
    {
        "q": "___ es regnet, machen wir eine Wanderung.",
        "opts": ["Obwohl", "Weil", "Deshalb", "Damit"],
        "cor": 0,
        "exp": "obwohl = رغم أن — يُعبّر عن التناقض",
        "k": 1,
        "difficulty": 1
    },
    {
        "q": "Wir bleiben zu Hause, ___ es regnet.",
        "opts": ["weil", "obwohl", "deshalb", "dass"],
        "cor": 0,
        "exp": "weil + جملة فرعية = لأن (الفعل في النهاية)",
        "k": 1,
        "difficulty": 1
    },
    {
        "q": "Ich ___ mein Auto reparieren.",
        "opts": ["lasse", "lässt", "lassen", "ließ"],
        "cor": 0,
        "exp": "lassen مع ich = lasse. ثم الفعل بلا zu",
        "k": 2,
        "difficulty": 1
    },
    {
        "q": "Caroline ___ ihr Handy reparieren ___.",
        "opts": ["hat / lassen", "hat / gelassen", "ist / lassen", "hat / reparieren lassen"],
        "cor": 3,
        "exp": "Perfekt von lassen: hat ... reparieren lassen",
        "k": 2,
        "difficulty": 3
    },
    {
        "q": "___ der hohen Kosten kaufen wir kein Smart Home.",
        "opts": ["Wegen", "Trotz", "Während", "Da"],
        "cor": 0,
        "exp": "wegen + Genitiv = بسبب",
        "k": 2,
        "difficulty": 2
    },
    {
        "q": "Die Wohnung ist gemütlich, ___ der smarten Technik.",
        "opts": ["trotz", "wegen", "während", "obwohl"],
        "cor": 0,
        "exp": "trotz + Genitiv = رغم",
        "k": 2,
        "difficulty": 2
    },
    {
        "q": "Das Gerät war ___ teuer, ___ sie es nicht kaufen konnte.",
        "opts": ["so / dass", "so / sodass", "sehr / dass", "zu / damit"],
        "cor": 0,
        "exp": "so...dass = لدرجة أن (للنتيجة)",
        "k": 2,
        "difficulty": 2
    },
    {
        "q": "Früher ___ er in einer kleinen Stadt. (Präteritum wohnen)",
        "opts": ["wohnte", "wohnen", "wohnt", "hat gewohnt"],
        "cor": 0,
        "exp": "Präteritum regelmäßig: wohnen → wohnte",
        "k": 3,
        "difficulty": 1
    },
    {
        "q": "Als Kind ___ sie viel Sport. (sein / Präteritum)",
        "opts": ["trieb", "ist getrieben", "treibt", "getrieben"],
        "cor": 0,
        "exp": "treiben غير منتظم: trieb (Präteritum)",
        "k": 3,
        "difficulty": 3
    },
    {
        "q": "Wenn ich mehr Zeit ___, ___ ich mehr lernen.",
        "opts": ["hätte / würde", "habe / werde", "hatte / wollte", "hätte / wäre"],
        "cor": 0,
        "exp": "Konjunktiv II: hätte + würde + Infinitiv",
        "k": 4,
        "difficulty": 2
    },
    {
        "q": "Das ist der Mann, ___ ich gestern gesehen habe.",
        "opts": ["den", "der", "dem", "dessen"],
        "cor": 0,
        "exp": "Relativsatz Maskulin Akkusativ = den (er→ihn→den)",
        "k": 4,
        "difficulty": 2
    },
    {
        "q": "Das ist die Frau, ___ der ich gesprochen habe.",
        "opts": ["mit", "von", "zu", "bei"],
        "cor": 0,
        "exp": "sprechen mit → mit der ich gesprochen habe",
        "k": 6,
        "difficulty": 2
    },
    {
        "q": "Mehrwegflaschen sind die ___ Alternative. (gut → Superlativ vor Nomen)",
        "opts": ["beste", "besten", "bestem", "am besten"],
        "cor": 0,
        "exp": "Superlativ vor femininem Nomen mit Artikel = beste",
        "k": 5,
        "difficulty": 2
    },
    {
        "q": "Ich kaufe regionale Produkte, ___ die Umwelt zu schützen.",
        "opts": ["um", "damit", "weil", "dass"],
        "cor": 0,
        "exp": "um...zu = من أجل أن — فاعل واحد فقط",
        "k": 5,
        "difficulty": 1
    },
    {
        "q": "Die Tafel kauft Produkte, ___ Menschen bekommen etwas zu essen.",
        "opts": ["damit", "um...zu", "weil", "obwohl"],
        "cor": 0,
        "exp": "damit = لكي — يُستخدم عندما الفاعل مختلف",
        "k": 5,
        "difficulty": 2
    },
    {
        "q": "Ich kenne einen ___, der viel reist. (n-Deklination: Student)",
        "opts": ["Studenten", "Student", "Studentes", "Students"],
        "cor": 0,
        "exp": "n-Deklination: der Student → einen Studenten (Akkusativ)",
        "k": 6,
        "difficulty": 2
    },
    {
        "q": "Nachdem Matilda ihr Studium abgeschlossen ___, fand sie eine Stelle.",
        "opts": ["hatte", "hat", "habe", "hätte"],
        "cor": 0,
        "exp": "nachdem + Plusquamperfekt: hatte + Partizip II",
        "k": 7,
        "difficulty": 2
    },
    {
        "q": "___ du arbeitest, bist du ständig erschöpft.",
        "opts": ["Seit", "Nachdem", "Bevor", "Bis"],
        "cor": 0,
        "exp": "seit = منذ أن — يُعبّر عن مدة مستمرة",
        "k": 7,
        "difficulty": 1
    },
    {
        "q": "Er trinkt ___ Kaffee ___ Tee.",
        "opts": ["weder / noch", "sowohl / als auch", "entweder / oder", "nicht nur / sondern"],
        "cor": 0,
        "exp": "weder...noch = لا...ولا (نفي مزدوج)",
        "k": 8,
        "difficulty": 2
    },
    {
        "q": "Musik ist nicht nur Unterhaltung, ___ auch Therapie.",
        "opts": ["sondern", "aber", "doch", "und"],
        "cor": 0,
        "exp": "nicht nur...sondern auch = ليس فقط...بل أيضاً",
        "k": 8,
        "difficulty": 1
    },
    {
        "q": "Die Lebensmittel ___ von der Tafel verteilt.",
        "opts": ["werden", "sind", "haben", "wurden"],
        "cor": 3,
        "exp": "Passiv Präteritum: wurden + Partizip II",
        "k": 10,
        "difficulty": 2
    },
    {
        "q": "Die Tafel ___ 1993 in Berlin ___. (Passiv Präteritum gründen)",
        "opts": ["wurde / gegründet", "wird / gegründet", "ist / gegründet", "war / gründete"],
        "cor": 0,
        "exp": "Passiv Präteritum: wurde gegründet",
        "k": 10,
        "difficulty": 2
    },
    {
        "q": "___ mehr Konkurrenz es gibt, ___ günstiger werden die Produkte.",
        "opts": ["Je / desto", "So / dass", "Wenn / dann", "Da / also"],
        "cor": 0,
        "exp": "je...desto = كلما...كلما",
        "k": 12,
        "difficulty": 2
    },
    {
        "q": "der überwiesene Betrag — überwiesene ist hier: (Partizip II als Adjektiv)",
        "opts": ["ein Adjektiv", "ein Adverb", "ein Nomen", "ein Verb"],
        "cor": 0,
        "exp": "Partizip II als Adjektiv: überweisen → überwiesen + Adjektivendung",
        "k": 12,
        "difficulty": 2
    }
]