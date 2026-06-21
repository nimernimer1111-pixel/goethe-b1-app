"""محتوى الـ 12 Kapitel الكامل."""

# ═══════════════════════════════════════════════════════════
# Kapitel 1: Gute Reise!
# ═══════════════════════════════════════════════════════════

KAP_1 = {
    "number": 1,
    "title_de": "Gute Reise!",
    "title_ar": "رحلة سعيدة!",
    "icon": "✈️",
    "description_de": "Reisen, Urlaubsplanung und Unterkunft",
    "description_ar": "السفر، تخطيط الإجازات، والإقامة",
    "grammar_focus": "Infinitiv mit zu | da/weil | obwohl",
    "page_start": 8,
    "page_end": 17,
    "themen": [
        {
            "name_de": "Urlaubsarten",
            "name_ar": "أنواع الإجازات",
            "icon": "🏖️",
            "order_index": 0,
            "vocab": [
                {"external_id": 101, "de": "der Pauschalurlaub (-e)", "ar": "إجازة شاملة (كل شيء مدفوع)",
                 "ex": "Im letzten Sommer haben wir einen Pauschalurlaub in der Türkei gemacht.", "tp": "N"},
                {"external_id": 102, "de": "der Aktivurlaub", "ar": "إجازة نشاط وحركة",
                 "ex": "Ich mache gern Aktivurlaub in den Bergen.", "tp": "N"},
                {"external_id": 103, "de": "der Strandurlaub", "ar": "إجازة شاطئية",
                 "ex": "Strandurlaub ist sehr entspannend.", "tp": "N"},
                {"external_id": 104, "de": "der Familienurlaub", "ar": "إجازة عائلية",
                 "ex": "Wir planen einen Familienurlaub in Spanien.", "tp": "N"},
                {"external_id": 105, "de": "der Kurzurlaub", "ar": "إجازة قصيرة (ويك إند)",
                 "ex": "Nächste Woche fahren wir für einen Kurzurlaub nach München.", "tp": "N"},
                {"external_id": 106, "de": "der Kultururlaub", "ar": "إجازة ثقافية",
                 "ex": "Ein Kultururlaub in Italien wäre toll!", "tp": "N"},
                {"external_id": 107, "de": "Typ 1: Ganz spontan", "ar": "النوع 1: عفوي — يسافرون بدون خطة",
                 "ex": "Sie fahren einfach los. Sie wollen sehen, was passiert.", "tp": "Ausdruck"},
                {"external_id": 108, "de": "Typ 2: Gern zu Hause", "ar": "النوع 2: يفضل البقاء في البيت",
                 "ex": "Reisen finden Sie anstrengend. Sie machen gern Ausflüge.", "tp": "Ausdruck"},
                {"external_id": 109, "de": "Typ 3: Gut geplant", "ar": "النوع 3: يخطط مسبقاً ودقيقاً",
                 "ex": "Sie suchen immer neue Urlaubsziele, auch in großer Entfernung.", "tp": "Ausdruck"},
                {"external_id": 110, "de": "Typ 4: Immer gleich", "ar": "النوع 4: دائماً نفس المكان",
                 "ex": "Sie fahren immer an denselben Ort. Dort fühlen Sie sich wie zu Hause.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Reiseplanung",
            "name_ar": "التخطيط للرحلة",
            "icon": "🗺️",
            "order_index": 1,
            "vocab": [
                {"external_id": 111, "de": "buchen (bucht - buchte - gebucht)", "ar": "يحجز",
                 "ex": "Ich möchte ein Zimmer im Hotel buchen.", "tp": "V"},
                {"external_id": 112, "de": "reservieren", "ar": "يحجز مسبقاً",
                 "ex": "Haben Sie einen Tisch für zwei Personen reserviert?", "tp": "V"},
                {"external_id": 113, "de": "empfehlen (empfiehlt)", "ar": "يوصي / ينصح",
                 "ex": "Können Sie mir ein Hotel empfehlen?", "tp": "V"},
                {"external_id": 114, "de": "die Buchung (-en)", "ar": "الحجز",
                 "ex": "Die Buchung des Fluges war einfach.", "tp": "N"},
                {"external_id": 115, "de": "die Reservierung (-en)", "ar": "الحجز المسبق",
                 "ex": "Ich möchte eine Reservierung für morgen.", "tp": "N"},
                {"external_id": 116, "de": "der Vorschlag (Vorschläge)", "ar": "الاقتراح",
                 "ex": "Hast du einen guten Vorschlag für den Urlaub?", "tp": "N"},
                {"external_id": 117, "de": "die Sehenswürdigkeit (-en)", "ar": "معلم سياحي",
                 "ex": "Das Brandenburger Tor ist eine berühmte Sehenswürdigkeit.", "tp": "N"},
                {"external_id": 118, "de": "die Wanderung (-en)", "ar": "رحلة مشي / تنزّه",
                 "ex": "Am Sonntag machen wir eine Wanderung im Wald.", "tp": "N"},
                {"external_id": 119, "de": "die Stadtrundfahrt (-en)", "ar": "جولة في المدينة",
                 "ex": "Wir machen eine Stadtrundfahrt mit dem Bus.", "tp": "N"},
                {"external_id": 120, "de": "stornieren", "ar": "يلغي الحجز",
                 "ex": "Ich möchte gern stornieren.", "tp": "V"},
                {"external_id": 121, "de": "umbuchen", "ar": "يغيّر الحجز",
                 "ex": "Kann ich die Reise umbuchen?", "tp": "V"},
                {"external_id": 122, "de": "die Buchungsbestätigung", "ar": "تأكيد الحجز",
                 "ex": "Hier ist Ihre Buchungsbestätigung.", "tp": "N"},
            ]
        },
        {
            "name_de": "Transport",
            "name_ar": "وسائل النقل",
            "icon": "🚆",
            "order_index": 2,
            "vocab": [
                {"external_id": 123, "de": "der Flug (Flüge)", "ar": "رحلة طيران",
                 "ex": "Der Flug von Berlin nach Madrid dauert drei Stunden.", "tp": "N"},
                {"external_id": 124, "de": "der Linienflug", "ar": "رحلة مجدولة",
                 "ex": "Ich nehme einen Linienflug nach Wien.", "tp": "N"},
                {"external_id": 125, "de": "der Charterflug", "ar": "رحلة مستأجرة",
                 "ex": "Charterflüge sind oft günstiger.", "tp": "N"},
                {"external_id": 126, "de": "die Abfahrt (-en)", "ar": "المغادرة",
                 "ex": "Die Abfahrt des Zuges ist um 8 Uhr.", "tp": "N"},
                {"external_id": 127, "de": "die Ankunft", "ar": "الوصول",
                 "ex": "Die Ankunft in Hamburg war pünktlich.", "tp": "N"},
                {"external_id": 128, "de": "die Verspätung (-en)", "ar": "التأخير",
                 "ex": "Der Zug hat leider 30 Minuten Verspätung.", "tp": "N"},
                {"external_id": 129, "de": "verpassen", "ar": "يفوّت",
                 "ex": "Ich habe meinen Bus verpasst.", "tp": "V"},
                {"external_id": 130, "de": "umsteigen", "ar": "يغيّر وسيلة النقل",
                 "ex": "In Frankfurt müssen wir umsteigen.", "tp": "V"},
                {"external_id": 131, "de": "der Anschluss (Anschlüsse)", "ar": "الوسيلة التالية / الربط",
                 "ex": "Ich habe meinen Anschluss verpasst.", "tp": "N"},
                {"external_id": 132, "de": "die Fahrkarte (-n)", "ar": "تذكرة السفر",
                 "ex": "Haben Sie schon eine Fahrkarte gekauft?", "tp": "N"},
                {"external_id": 133, "de": "die Hin- und Rückfahrt", "ar": "الذهاب والعودة",
                 "ex": "Eine Hin- und Rückfahrt kostet 60 Euro.", "tp": "N"},
                {"external_id": 134, "de": "das Gleis (-e)", "ar": "الرصيف",
                 "ex": "Ihr Zug fährt von Gleis 7 ab.", "tp": "N"},
                {"external_id": 135, "de": "die Durchsage (-n)", "ar": "الإعلان / النداء",
                 "ex": "Achten Sie auf die wichtigen Informationen der Durchsage.", "tp": "N"},
            ]
        },
        {
            "name_de": "Unterkunft",
            "name_ar": "الإقامة",
            "icon": "🏨",
            "order_index": 3,
            "vocab": [
                {"external_id": 136, "de": "die Pension (-en)", "ar": "بيت الضيافة",
                 "ex": "Wir übernachten in einer kleinen Pension.", "tp": "N"},
                {"external_id": 137, "de": "die Jugendherberge (-n)", "ar": "بيت الشباب",
                 "ex": "Die Jugendherberge ist sehr günstig.", "tp": "N"},
                {"external_id": 138, "de": "die Ferienwohnung (-en)", "ar": "شقة العطلة",
                 "ex": "Wir haben eine Ferienwohnung gemietet.", "tp": "N"},
                {"external_id": 139, "de": "das Einzelzimmer (-)", "ar": "غرفة فردية",
                 "ex": "Ich hätte gern ein Einzelzimmer mit Frühstück.", "tp": "N"},
                {"external_id": 140, "de": "das Doppelzimmer (-)", "ar": "غرفة مزدوجة",
                 "ex": "Ein Doppelzimmer bitte, mit Blick auf das Meer.", "tp": "N"},
                {"external_id": 141, "de": "das Frühstück", "ar": "الإفطار",
                 "ex": "Das Frühstück ist im Preis inklusive.", "tp": "N"},
                {"external_id": 142, "de": "die Halbpension", "ar": "نصف إقامة (إفطار+عشاء)",
                 "ex": "Ich habe Halbpension gebucht.", "tp": "N"},
                {"external_id": 143, "de": "die Vollpension", "ar": "إقامة كاملة (3 وجبات)",
                 "ex": "Vollpension ist sehr bequem.", "tp": "N"},
                {"external_id": 144, "de": "die Übernachtung (-en)", "ar": "المبيت / ليلة",
                 "ex": "Die Übernachtung kostet 80 Euro.", "tp": "N"},
                {"external_id": 145, "de": "die Rezeption", "ar": "الاستقبال",
                 "ex": "An der Rezeption können Sie einchecken.", "tp": "N"},
                {"external_id": 146, "de": "der Meerblick", "ar": "إطلالة على البحر",
                 "ex": "Haben Sie ein Zimmer mit Meerblick?", "tp": "N"},
                {"external_id": 147, "de": "belegt", "ar": "محجوز / ممتلئ",
                 "ex": "Alle Zimmer mit Meerblick sind belegt.", "tp": "Adj"},
                {"external_id": 148, "de": "inklusive", "ar": "شامل",
                 "ex": "Das Frühstück ist inklusive.", "tp": "Adj"},
            ]
        },
        {
            "name_de": "Gut gesagt",
            "name_ar": "تعابير مفيدة",
            "icon": "💡",
            "order_index": 4,
            "vocab": [
                {"external_id": 149, "de": "Ich habe keinen Bock mehr.", "ar": "لم يعد لديّ رغبة في ذلك.",
                 "ex": "Wenn etwas nicht gut läuft.", "tp": "Umgangssprache"},
                {"external_id": 150, "de": "Der ganze Urlaub ist im Eimer.", "ar": "العطلة كلها ضاعت!",
                 "ex": "Umgangssprachlich für: alles ist kaputt.", "tp": "Umgangssprache"},
                {"external_id": 151, "de": "Heute geht echt alles schief.", "ar": "اليوم كل شيء يسير بشكل خاطئ.",
                 "ex": "Ausdruck der Frustration.", "tp": "Umgangssprache"},
                {"external_id": 152, "de": "Das klingt gut!", "ar": "يبدو هذا جيداً!",
                 "ex": "Beim Buchen: Das klingt gut! Kann ich es buchen?", "tp": "Ausdruck"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Im Reisebüro",
            "situation_de": "Anna geht zum Reisebüro, um einen Urlaub zu buchen.",
            "lines": [
                {"speaker": "R", "text_de": "Guten Tag! Was kann ich für Sie tun?", "text_ar": "مساء الخير! ماذا أستطيع أن أفعل لك؟"},
                {"speaker": "K", "text_de": "Hallo! Ich möchte gern einen Urlaub buchen.", "text_ar": "مرحباً! أودّ حجز إجازة."},
                {"speaker": "R", "text_de": "Wohin möchten Sie denn reisen? Und wann?", "text_ar": "إلى أين تريد السفر؟ ومتى؟"},
                {"speaker": "K", "text_de": "Ich würde gern im August nach Spanien fahren. Für zwei Wochen.", "text_ar": "أودّ السفر إلى إسبانيا في أغسطس. لمدة أسبوعين."},
                {"speaker": "R", "text_de": "Haben Sie eine bestimmte Region im Sinn?", "text_ar": "هل لديك منطقة معينة في ذهنك؟"},
                {"speaker": "K", "text_de": "Ja, am liebsten an die Costa del Sol. Ich mag Strandurlaub.", "text_ar": "نعم، أفضل ساحل الشمس. أحب الإجازات الشاطئية."},
                {"speaker": "R", "text_de": "Gut. Möchten Sie ein Hotel oder eine Ferienwohnung?", "text_ar": "حسناً. هل تريد فندقاً أم شقة؟"},
                {"speaker": "K", "text_de": "Ein Hotel mit Halbpension wäre schön. Und nicht zu teuer, bitte.", "text_ar": "فندق مع نصف إقامة سيكون جميلاً. وغير مكلف من فضلك."},
                {"speaker": "R", "text_de": "Ich habe hier ein tolles Angebot: 7 Nächte im Drei-Sterne-Hotel mit Frühstück für 850 Euro pro Person.", "text_ar": "لديّ هنا عرض رائع: 7 ليالٍ في فندق 3 نجوم مع إفطار بـ 850 يورو للشخص."},
                {"speaker": "K", "text_de": "Gibt es auch ein günstigeres Angebot?", "text_ar": "هل هناك عرض أرخص؟"},
                {"speaker": "R", "text_de": "Ja, eine Pension in Strandnähe. 7 Nächte mit Frühstück für 550 Euro.", "text_ar": "نعم، بيت ضيافة قريب من الشاطئ. 7 ليالٍ مع إفطار بـ 550 يورو."},
                {"speaker": "K", "text_de": "Das klingt gut! Kann ich es buchen?", "text_ar": "هذا يبدو جيداً! هل يمكنني حجزه؟"},
                {"speaker": "R", "text_de": "Natürlich. Darf ich Ihren Ausweis sehen, bitte?", "text_ar": "بالتأكيد. هل يمكنني رؤية هويتك؟"},
                {"speaker": "R", "text_de": "Hier ist Ihre Buchungsbestätigung. Gute Reise!", "text_ar": "إليك تأكيد الحجز. رحلة سعيدة!"},
            ]
        },
        {
            "title_de": "Am Bahnhof",
            "situation_de": "Markus möchte eine Fahrkarte nach München kaufen.",
            "lines": [
                {"speaker": "K", "text_de": "Entschuldigung, ich möchte eine Fahrkarte nach München.", "text_ar": "عذراً، أريد تذكرة إلى ميونخ."},
                {"speaker": "S", "text_de": "Einfache Fahrt oder Hin und Rückfahrt?", "text_ar": "ذهاب فقط أم ذهاب وعودة؟"},
                {"speaker": "K", "text_de": "Hin und Rückfahrt, bitte. Für übermorgen.", "text_ar": "ذهاب وعودة، من فضلك. ليوم بعد غد."},
                {"speaker": "S", "text_de": "Welche Klasse? Erste oder zweite?", "text_ar": "أي درجة؟ الأولى أم الثانية؟"},
                {"speaker": "K", "text_de": "Zweite Klasse, bitte. Was kostet das?", "text_ar": "الدرجة الثانية من فضلك. كم السعر؟"},
                {"speaker": "S", "text_de": "98 Euro. Möchten Sie auch eine Platzreservierung?", "text_ar": "98 يورو. هل تريد حجز مقعد أيضاً؟"},
                {"speaker": "K", "text_de": "Ja, bitte. Am Fenster, wenn möglich.", "text_ar": "نعم، من فضلك. بجانب النافذة إن أمكن."},
                {"speaker": "S", "text_de": "Der Zug fährt um 14:30 Uhr von Gleis 7. Sie haben noch 20 Minuten.", "text_ar": "القطار يغادر 14:30 من الرصيف 7. لديك 20 دقيقة."},
                {"speaker": "K", "text_de": "Wann komme ich in München an?", "text_ar": "متى أصل إلى ميونخ؟"},
                {"speaker": "S", "text_de": "Um 18:45 Uhr. Hier ist Ihre Fahrkarte. Gute Fahrt!", "text_ar": "الساعة 18:45. تذكرتك. رحلة موفقة!"},
            ]
        },
        {
            "title_de": "Im Hotel einchecken",
            "situation_de": "Familie Schmidt kommt im Hotel an.",
            "lines": [
                {"speaker": "R", "text_de": "Guten Abend! Haben Sie eine Reservierung?", "text_ar": "مساء الخير! هل لديكم حجز؟"},
                {"speaker": "F", "text_de": "Ja, auf den Namen Schmidt. Wir haben ein Doppelzimmer und ein Einzelzimmer gebucht.", "text_ar": "نعم، باسم شميت. حجزنا غرفة مزدوجة وغرفة فردية."},
                {"speaker": "R", "text_de": "Einen Moment bitte... Ja, drei Nächte mit Frühstück, richtig?", "text_ar": "لحظة... نعم، ثلاث ليالٍ مع إفطار، صحيح؟"},
                {"speaker": "F", "text_de": "Genau. Können wir ein Zimmer mit Meerblick bekommen?", "text_ar": "بالضبط. هل يمكننا الحصول على غرفة تطل على البحر؟"},
                {"speaker": "R", "text_de": "Es tut mir leid, alle Zimmer mit Meerblick sind belegt.", "text_ar": "آسف، جميع الغرف المطلة على البحر محجوزة."},
                {"speaker": "F", "text_de": "Das ist auch schön. Wann gibt es Frühstück?", "text_ar": "لا بأس. متى يقدّم الإفطار؟"},
                {"speaker": "R", "text_de": "Von 7 bis 10 Uhr im Restaurant im Erdgeschoss.", "text_ar": "من 7 إلى 10 في المطعم بالطابق الأرضي."},
                {"speaker": "F", "text_de": "Gibt es WLAN im Zimmer?", "text_ar": "هل هناك واي فاي في الغرفة؟"},
                {"speaker": "R", "text_de": "Ja, das Passwort finden Sie auf dem Schreibtisch. Genießen Sie Ihren Aufenthalt!", "text_ar": "نعم، ستجد كلمة المرور على المكتب. استمتع بإقامتك!"},
            ]
        },
    ],
    "redemittel": {
        "im Reisebüro": [
            {"de": "Ich möchte einen Urlaub / eine Reise buchen.", "ar": "أودّ حجز إجازة / رحلة."},
            {"de": "Haben Sie ein Angebot für ...?", "ar": "هل لديكم عرض لـ ...؟"},
            {"de": "Was kostet die Reise insgesamt?", "ar": "كم تكلفة الرحلة الإجمالية؟"},
            {"de": "Ist das Frühstück / die Halbpension inklusive?", "ar": "هل الإفطار / نصف الإقامة مشمول؟"},
            {"de": "Gibt es auch ein günstigeres Angebot?", "ar": "هل هناك عرض أرخص؟"},
            {"de": "Ich möchte gern stornieren.", "ar": "أودّ إلغاء الحجز."},
            {"de": "Wie wäre es mit ...?", "ar": "كيف يكون ...؟ / ماذا لو ...؟"},
            {"de": "Dann buchen wir das.", "ar": "إذن سنحجز هذا."},
        ],
        "am Bahnhof / Flughafen": [
            {"de": "Wann fährt der nächste Zug nach ...?", "ar": "متى يغادر القطار التالي إلى ...؟"},
            {"de": "Von welchem Gleis fährt der Zug?", "ar": "من أي رصيف يغادر القطار؟"},
            {"de": "Wie lange dauert die Fahrt / der Flug?", "ar": "كم تستغرق الرحلة (بالقطار / بالطائرة)؟"},
            {"de": "Muss ich umsteigen?", "ar": "هل يجب أن أغير القطار؟"},
            {"de": "Der Zug hat Verspätung.", "ar": "القطار متأخر."},
            {"de": "An welchem Gepäckband finde ich meinen Koffer?", "ar": "في أي حزام أمتعة أجد حقيبتي؟"},
        ],
        "im Hotel": [
            {"de": "Ich habe eine Reservierung auf den Namen ...", "ar": "لديّ حجز باسم ..."},
            {"de": "Können wir ein Zimmer mit Meerblick / Balkon bekommen?", "ar": "هل يمكننا الحصول على غرفة تطل على البحر / بشرفة؟"},
            {"de": "Wann gibt es Frühstück?", "ar": "متى يقدّم الإفطار؟"},
            {"de": "Gibt es WLAN im Zimmer?", "ar": "هل هناك واي فاي في الغرفة؟"},
            {"de": "Ich hätte gern die Rechnung.", "ar": "أريد الفاتورة من فضلك."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 2: Das ist ja praktisch!
# ═══════════════════════════════════════════════════════════

KAP_2 = {
    "number": 2,
    "title_de": "Das ist ja praktisch!",
    "title_ar": "هذا عملي جداً!",
    "icon": "📱",
    "description_de": "Technik, Reklamation und Werbung",
    "description_ar": "التقنية، الشكاوى، والإعلانات",
    "grammar_focus": "lassen + Inf | deshalb/sodass | Genitiv | wegen/trotz",
    "page_start": 18,
    "page_end": 27,
    "themen": [
        {
            "name_de": "Technik & Geräte",
            "name_ar": "التقنية والأجهزة",
            "icon": "🔧",
            "order_index": 0,
            "vocab": [
                {"external_id": 201, "de": "das Lastenfahrrad (-räder)", "ar": "دراجة شحن",
                 "ex": "Transport ohne Motor, praktisch für alle!", "tp": "N"},
                {"external_id": 202, "de": "der Steh-Sitz-Tisch (-e)", "ar": "مكتب للوقوف والجلوس",
                 "ex": "Der Rücken dankt!", "tp": "N"},
                {"external_id": 203, "de": "der Funkkopfhörer (-)", "ar": "سماعة لاسلكية",
                 "ex": "Alles hören und keinen stören!", "tp": "N"},
                {"external_id": 204, "de": "der Sprachassistent (-en)", "ar": "المساعد الصوتي",
                 "ex": "Nie wieder Tasten drücken!", "tp": "N"},
                {"external_id": 205, "de": "der Türöffner mit Fingerabdruck", "ar": "فتّاحة باب ببصمة الإصبع",
                 "ex": "Schlüssel vergessen? Das Problem kenne ich nicht!", "tp": "N"},
                {"external_id": 206, "de": "die Powerbank (-s)", "ar": "شاحن محمول",
                 "ex": "Tarik ist viel unterwegs, darum braucht er eine Powerbank.", "tp": "N"},
                {"external_id": 207, "de": "das Ladekabel (-)", "ar": "كابل الشحن",
                 "ex": "Das Ladekabel ist so alt, sodass es nicht mehr funktioniert.", "tp": "N"},
                {"external_id": 208, "de": "der Lautsprecher (-)", "ar": "السماعة",
                 "ex": "Max' Lautsprecher geht nicht mehr.", "tp": "N"},
                {"external_id": 209, "de": "der USB-Stick (-s)", "ar": "USB فلاش",
                 "ex": "Elena hat ihren Stick verloren.", "tp": "N"},
                {"external_id": 210, "de": "die Smartwatch (-es)", "ar": "الساعة الذكية",
                 "ex": "Ich finde meine Smartwatch total praktisch.", "tp": "N"},
                {"external_id": 211, "de": "das Smart Home", "ar": "المنزل الذكي",
                 "ex": "Familie Singer hat ihr Zuhause zu einem Smart Home gemacht.", "tp": "N"},
            ]
        },
        {
            "name_de": "Reklamation",
            "name_ar": "الشكاوى والإعادة",
            "icon": "📞",
            "order_index": 1,
            "vocab": [
                {"external_id": 212, "de": "reklamieren", "ar": "يشكو / يطالب بحقه",
                 "ex": "Ich möchte dieses Produkt reklamieren.", "tp": "V"},
                {"external_id": 213, "de": "umtauschen", "ar": "يستبدل",
                 "ex": "Kann ich diesen Kopfhörer umtauschen?", "tp": "V"},
                {"external_id": 214, "de": "zurückgeben", "ar": "يُعيد",
                 "ex": "Ich möchte das Gerät zurückgeben.", "tp": "V"},
                {"external_id": 215, "de": "reparieren lassen", "ar": "يجعل شخصاً يُصلح",
                 "ex": "Caroline lässt ihr Handy reparieren.", "tp": "V"},
                {"external_id": 216, "de": "kaputt / defekt", "ar": "معطوب / خراب",
                 "ex": "Mein Handy ist kaputt.", "tp": "Adj"},
                {"external_id": 217, "de": "die Quittung (-en)", "ar": "الإيصال / الفاتورة",
                 "ex": "Haben Sie noch die Quittung?", "tp": "N"},
                {"external_id": 218, "de": "die Garantie (-n)", "ar": "الضمان",
                 "ex": "Das Produkt hat noch ein Jahr Garantie.", "tp": "N"},
                {"external_id": 219, "de": "der Kassenzettel (-)", "ar": "فاتورة الشراء",
                 "ex": "Haben Sie den Kassenzettel noch?", "tp": "N"},
                {"external_id": 220, "de": "zufrieden / unzufrieden", "ar": "راضٍ / غير راضٍ",
                 "ex": "Ich bin mit dem Produkt leider gar nicht zufrieden.", "tp": "Adj"},
            ]
        },
        {
            "name_de": "Werbung",
            "name_ar": "الإعلانات",
            "icon": "📺",
            "order_index": 2,
            "vocab": [
                {"external_id": 221, "de": "die Werbung (-en)", "ar": "الإعلان",
                 "ex": "Werbung soll gefallen oder zumindest auffallen.", "tp": "N"},
                {"external_id": 222, "de": "der Slogan (-s)", "ar": "الشعار الإعلاني",
                 "ex": "Werbung arbeitet oft mit Slogans.", "tp": "N"},
                {"external_id": 223, "de": "das Kaufverhalten", "ar": "سلوك الشراء",
                 "ex": "Werbung will unser Kaufverhalten beeinflussen.", "tp": "N"},
                {"external_id": 224, "de": "neugierig machen", "ar": "يثير الفضول",
                 "ex": "Werbung macht Menschen neugierig.", "tp": "Ausdruck"},
                {"external_id": 225, "de": "witzig / langweilig / modern", "ar": "ظريف / ممل / حديث",
                 "ex": "Ich finde die Werbung witzig.", "tp": "Adj"},
                {"external_id": 226, "de": "der Markenname (-n)", "ar": "اسم العلامة التجارية",
                 "ex": "Taschentücher → Tempo. Schmerztabletten → Aspirin.", "tp": "N"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Im Elektrogeschäft — Reklamation",
            "situation_de": "Max möchte seinen Kopfhörer umtauschen.",
            "lines": [
                {"speaker": "V", "text_de": "Guten Tag! Kann ich Ihnen helfen?", "text_ar": "مساء الخير! هل أستطيع مساعدتك؟"},
                {"speaker": "K", "text_de": "Ja, ich möchte diesen Kopfhörer reklamieren. Er funktioniert nicht richtig.", "text_ar": "نعم، أريد الشكوى بشأن هذه السماعة. لا تعمل بشكل صحيح."},
                {"speaker": "V", "text_de": "Was ist denn das Problem?", "text_ar": "ما المشكلة بالضبط؟"},
                {"speaker": "K", "text_de": "Der Ton ist sehr leise, obwohl ich die Lautstärke voll aufgedreht habe.", "text_ar": "الصوت خافت جداً رغم أنني رفعت الصوت لأقصاه."},
                {"speaker": "V", "text_de": "Haben Sie ihn schon kontrolliert? Ist er richtig geladen?", "text_ar": "هل تحققت من ذلك؟ هل هو مشحون بشكل صحيح؟"},
                {"speaker": "K", "text_de": "Ja, ich habe alles probiert. Ich bin damit leider gar nicht zufrieden.", "text_ar": "نعم، جربت كل شيء. للأسف أنا غير راضٍ عنه أبداً."},
                {"speaker": "V", "text_de": "Haben Sie die Quittung und die Garantiekarte noch?", "text_ar": "هل لا يزال لديك الإيصال وبطاقة الضمان؟"},
                {"speaker": "K", "text_de": "Ja, hier bitte.", "text_ar": "نعم، تفضل."},
                {"speaker": "V", "text_de": "Möchten Sie einen neuen Kopfhörer oder das Geld zurück?", "text_ar": "تريد سماعة جديدة أم استرداد المبلغ؟"},
                {"speaker": "K", "text_de": "Ich möchte lieber das Geld zurück.", "text_ar": "أفضل استرداد المبلغ."},
                {"speaker": "V", "text_de": "Kein Problem. Ich erledige das sofort.", "text_ar": "لا مشكلة. سأعالج هذا فوراً."},
            ]
        },
    ],
    "redemittel": {
        "etwas reklamieren — Kunde": [
            {"de": "... funktioniert nicht (richtig).", "ar": "... لا يعمل (بشكل صحيح)."},
            {"de": "... ist kaputt / defekt.", "ar": "... معطوب."},
            {"de": "Ich bin mit ... leider gar nicht zufrieden.", "ar": "للأسف أنا غير راضٍ عن ... أبداً."},
            {"de": "Ich möchte ... umtauschen.", "ar": "أريد استبدال ..."},
            {"de": "Kann ich ... zurückgeben?", "ar": "هل يمكنني إعادة ...؟"},
            {"de": "Ich habe noch die Quittung / die Garantie.", "ar": "لا يزال لديّ الإيصال / الضمان."},
        ],
        "etwas reklamieren — Verkäufer/in": [
            {"de": "Was ist denn das Problem?", "ar": "ما المشكلة بالضبط؟"},
            {"de": "Kann ich ... bitte mal sehen?", "ar": "هل يمكنني رؤية ...؟"},
            {"de": "Haben Sie den Kassenzettel / die Garantie noch?", "ar": "هل لا يزال لديك الإيصال / الضمان؟"},
            {"de": "Möchten Sie ein neues Gerät oder das Geld zurück?", "ar": "تريد جهازاً جديداً أم استرداد المبلغ؟"},
        ],
        "Werbung bewerten": [
            {"de": "Ich finde die Werbung witzig/interessant, weil ...", "ar": "أجد الإعلان ظريفاً/مثيراً لأن ..."},
            {"de": "Die Werbung für ... gefällt mir am besten, weil ...", "ar": "إعلان ... يعجبني أكثر لأن ..."},
            {"de": "Ich finde den Text/die Idee ausgezeichnet/lustig.", "ar": "أجد النص/الفكرة رائعاً/مضحكاً."},
            {"de": "... wirkt auf mich am modernsten/kreativsten.", "ar": "... يبدو لي الأكثر حداثةً/إبداعاً."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 3: Veränderungen
# ═══════════════════════════════════════════════════════════

KAP_3 = {
    "number": 3,
    "title_de": "Veränderungen",
    "title_ar": "تغييرات",
    "icon": "🔄",
    "description_de": "Lebensveränderungen, Glück und Zeit",
    "description_ar": "تغييرات الحياة، السعادة، والزمن",
    "grammar_focus": "Präteritum | Zeitangaben (Dativ & Genitiv)",
    "page_start": 28,
    "page_end": 37,
    "themen": [
        {
            "name_de": "Ereignisse im Leben",
            "name_ar": "أحداث الحياة",
            "icon": "⭐",
            "order_index": 0,
            "vocab": [
                {"external_id": 301, "de": "die Veränderung (-en)", "ar": "التغيير",
                 "ex": "Das war eine große Veränderung in meinem Leben.", "tp": "N"},
                {"external_id": 302, "de": "der Umzug (Umzüge)", "ar": "الانتقال للسكن",
                 "ex": "Seit meinem Umzug nach Berlin unternehme ich viel.", "tp": "N"},
                {"external_id": 303, "de": "die Entscheidung (-en)", "ar": "القرار",
                 "ex": "Er ist glücklich mit seiner Entscheidung.", "tp": "N"},
                {"external_id": 304, "de": "der Höhepunkt (-e)", "ar": "الذروة",
                 "ex": "Sie war auf dem Höhepunkt ihrer Karriere.", "tp": "N"},
                {"external_id": 305, "de": "der Unfall (Unfälle)", "ar": "الحادث",
                 "ex": "Im Sommer 2018 ereignete sich ein schrecklicher Unfall.", "tp": "N"},
                {"external_id": 306, "de": "radikal", "ar": "جذري / كلي",
                 "ex": "Von einem Tag auf den anderen veränderte sich ihr Leben radikal.", "tp": "Adj"},
                {"external_id": 307, "de": "kämpfen für", "ar": "يناضل / يكافح من أجل",
                 "ex": "Sie kämpfte für ihre Selbstständigkeit.", "tp": "V"},
                {"external_id": 308, "de": "bewundern", "ar": "يُعجب بـ",
                 "ex": "Für ihre Energie bewundern sie viele.", "tp": "V"},
                {"external_id": 309, "de": "sich verändern", "ar": "يتغير",
                 "ex": "Das Leben hat sich stark verändert.", "tp": "V"},
                {"external_id": 310, "de": "seitdem", "ar": "منذ ذلك الحين",
                 "ex": "Seitdem ist sie vom Oberkörper abwärts gelähmt.", "tp": "Adv"},
                {"external_id": 311, "de": "sich selbst fahren", "ar": "يقود بنفسه",
                 "ex": "Sie kann mittlerweile wieder alleine Auto fahren.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Glück",
            "name_ar": "السعادة",
            "icon": "😊",
            "order_index": 1,
            "vocab": [
                {"external_id": 312, "de": "das Glück", "ar": "السعادة / الحظ",
                 "ex": "Was bedeutet Glück für euch?", "tp": "N"},
                {"external_id": 313, "de": "glücklich sein", "ar": "يكون سعيداً",
                 "ex": "Glücklich bin ich, wenn ich im Wald laufen kann.", "tp": "Ausdruck"},
                {"external_id": 314, "de": "schwach", "ar": "ضعيف",
                 "ex": "Ich hatte große Probleme und war oft schwach.", "tp": "Adj"},
                {"external_id": 315, "de": "verliebt", "ar": "واقع في الحب",
                 "ex": "Ich bin gerade frisch verliebt.", "tp": "Adj"},
                {"external_id": 316, "de": "frisch verliebt", "ar": "حديث الوقوع في الحب",
                 "ex": "Sie schickt mir mindestens drei liebevolle Nachrichten.", "tp": "Ausdruck"},
                {"external_id": 317, "de": "Was will man mehr?", "ar": "ماذا يريد المرء أكثر من ذلك؟",
                 "ex": "Wir essen in einem guten Restaurant. Was will man mehr?", "tp": "Ausdruck"},
                {"external_id": 318, "de": "Zum Glück / Leider", "ar": "لحسن الحظ / للأسف",
                 "ex": "Zum Glück hat es nicht geregnet.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Zeitangaben",
            "name_ar": "ظروف الزمان",
            "icon": "⏰",
            "order_index": 2,
            "vocab": [
                {"external_id": 319, "de": "vor einer Prüfung", "ar": "قبل اختبار",
                 "ex": "Vor einer Prüfung bin ich nervös.", "tp": "Präp+Dativ"},
                {"external_id": 320, "de": "während des Kurses", "ar": "خلال الدورة",
                 "ex": "Während des Kurses lerne ich viel.", "tp": "Präp+Genitiv"},
                {"external_id": 321, "de": "seit der Schulzeit", "ar": "منذ أيام المدرسة",
                 "ex": "Seit der Schulzeit sind wir Freunde.", "tp": "Präp+Dativ"},
                {"external_id": 322, "de": "innerhalb einer Stunde", "ar": "في غضون ساعة",
                 "ex": "Sie schickt innerhalb einer Stunde eine Nachricht.", "tp": "Präp+Genitiv"},
                {"external_id": 323, "de": "außerhalb des Urlaubs", "ar": "خارج أوقات الإجازة",
                 "ex": "Außerhalb des Urlaubs treffe ich Freunde.", "tp": "Präp+Genitiv"},
                {"external_id": 324, "de": "im letzten Sommer", "ar": "في الصيف الماضي",
                 "ex": "Im letzten Sommer war ich in Wien.", "tp": "Zeitangabe"},
                {"external_id": 325, "de": "nach dem Studium", "ar": "بعد الجامعة",
                 "ex": "Nach dem Studium zog er nach Leipzig.", "tp": "Zeitangabe"},
            ]
        },
        {
            "name_de": "Gut gesagt",
            "name_ar": "تعابير مفيدة",
            "icon": "💡",
            "order_index": 3,
            "vocab": [
                {"external_id": 326, "de": "... hat sich stark/minimal verändert.", "ar": "... تغيّر تغيّراً كبيراً/طفيفاً.",
                 "ex": "Früher und heute vergleichen.", "tp": "Ausdruck"},
                {"external_id": 327, "de": "Im Gegensatz zu heute/früher ...", "ar": "على عكس اليوم/الماضي ...",
                 "ex": "Vergleich ausdrücken.", "tp": "Ausdruck"},
                {"external_id": 328, "de": "Früher war ... besser/schlechter.", "ar": "في الماضي كان ... أفضل/أسوأ.",
                 "ex": "Früher war die Arbeit viel schwerer.", "tp": "Ausdruck"},
                {"external_id": 329, "de": "Ich hab' dich gern. / Ich mag dich.", "ar": "أنا أحبك (عموماً).",
                 "ex": "Zuneigung ausdrücken.", "tp": "Ausdruck"},
                {"external_id": 330, "de": "Ich liebe dich.", "ar": "أحبك (للشريك الحميم فقط).",
                 "ex": "Nur zum Partner / zur Partnerin.", "tp": "Ausdruck"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Neue Liebe, neues Glück — Radiosendung",
            "situation_de": "Davide Romano erzählt über sein Leben in Leipzig.",
            "lines": [
                {"speaker": "M", "text_de": "Willkommen in der Sendung, Davide! Wie lange leben Sie schon in Leipzig?", "text_ar": "مرحباً في البرنامج يا دافيده! منذ متى تعيش في لايبزيغ؟"},
                {"speaker": "D", "text_de": "Seit zwei Jahren. Ich bin hergezogen, weil meine Freundin hier lebt.", "text_ar": "منذ سنتين. انتقلت إلى هنا لأن صديقتي تعيش هنا."},
                {"speaker": "M", "text_de": "Und wie haben Sie Ihre Freundin kennengelernt?", "text_ar": "وكيف تعرّفت على صديقتك؟"},
                {"speaker": "D", "text_de": "Wir lernten uns im Urlaub kennen. Das war vor fünf Jahren.", "text_ar": "تعارفنا في الإجازة. كان ذلك منذ خمس سنوات."},
                {"speaker": "M", "text_de": "Der Umzug nach Leipzig — war das schwer?", "text_ar": "الانتقال إلى لايبزيغ — هل كان صعباً؟"},
                {"speaker": "D", "text_de": "Ja, am Anfang gab es einige Probleme. Die Sprache war zum Glück kein Problem.", "text_ar": "نعم، في البداية كانت هناك بعض المشاكل. لكن اللغة لحسن الحظ لم تكن مشكلة."},
                {"speaker": "M", "text_de": "Was ist wichtig bei einem Neuanfang in einem neuen Land?", "text_ar": "ما الأهم عند البداية الجديدة في بلد جديد؟"},
                {"speaker": "D", "text_de": "Ich finde, es ist wichtig, beruflich aktiv zu sein und neue Leute kennenzulernen.", "text_ar": "أرى أنه من المهم أن تكون نشطاً مهنياً وتتعرف على أشخاص جدد."},
            ]
        },
    ],
    "redemittel": {
        "über Veränderungen sprechen": [
            {"de": "... hat sich stark / minimal verändert.", "ar": "... تغيّر بشكل كبير / طفيف."},
            {"de": "Im Vergleich zu früher ist / gibt es heute ...", "ar": "مقارنةً بالماضي اليوم هناك ..."},
            {"de": "Früher war ... leichter / schwieriger.", "ar": "في الماضي كان ... أسهل / أصعب."},
            {"de": "Heute ist ... viel besser / schlechter.", "ar": "اليوم ... أفضل / أسوأ بكثير."},
        ],
        "über Glück sprechen": [
            {"de": "Glücklich bin ich, wenn ...", "ar": "أنا سعيد عندما ..."},
            {"de": "Für mich ist das größte Glück ...", "ar": "بالنسبة لي أعظم سعادة هي ..."},
            {"de": "Was will man mehr?", "ar": "ماذا يريد المرء أكثر؟"},
            {"de": "Zum Glück / Leider ...", "ar": "لحسن الحظ / للأسف ..."},
        ],
    }
}


# ═══════════════════════════════════════════════════════════
# تجميع كل الـ Kapitel في قاموس واحد
# ═══════════════════════════════════════════════════════════

ALL_KAPITEL = {
    1: KAP_1,
    2: KAP_2,
    3: KAP_3,
    # 4-12 ستضاف لاحقاً
}
# ═══════════════════════════════════════════════════════════
# Kapitel 4: Arbeitswelt
# ═══════════════════════════════════════════════════════════

KAP_4 = {
    "number": 4,
    "title_de": "Arbeitswelt",
    "title_ar": "عالم العمل",
    "icon": "💼",
    "description_de": "Berufe, Bewerbung und Arbeitsplatz",
    "description_ar": "المهن، التقديم للوظيفة، ومكان العمل",
    "grammar_focus": "Konjunktiv II | Pronominaladverbien | Verben mit Präposition",
    "page_start": 38,
    "page_end": 47,
    "themen": [
        {
            "name_de": "Berufe",
            "name_ar": "المهن",
            "icon": "👷",
            "order_index": 0,
            "vocab": [
                {"external_id": 401, "de": "die Briefträgerin / der Briefträger", "ar": "ساعية/ساعي البريد",
                 "ex": "Die Briefträgerin stellt Briefe und Pakete zu.", "tp": "N"},
                {"external_id": 402, "de": "die Chemikerin / der Chemiker", "ar": "الكيميائية / الكيميائي",
                 "ex": "Die Chemikerin arbeitet im Labor.", "tp": "N"},
                {"external_id": 403, "de": "die Mechatronikerin / der Mechatroniker", "ar": "مهندس/ة الميكاترونيك",
                 "ex": "Die Mechatronikerin repariert komplexe Maschinen.", "tp": "N"},
                {"external_id": 404, "de": "die Taxifahrerin / der Taxifahrer", "ar": "سائق/ة تاكسي",
                 "ex": "Meine erste Stelle war als Taxifahrerin.", "tp": "N"},
                {"external_id": 405, "de": "die Ausbildung (-en)", "ar": "التدريب المهني",
                 "ex": "Er macht eine Ausbildung als Koch.", "tp": "N"},
                {"external_id": 406, "de": "gut verdienen", "ar": "يكسب جيداً",
                 "ex": "Als Chemikerin verdient man gut.", "tp": "Ausdruck"},
                {"external_id": 407, "de": "geregelte Arbeitszeiten haben", "ar": "عمل بساعات منتظمة",
                 "ex": "Ich habe geregelte Arbeitszeiten — das ist wichtig.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Bewerbung",
            "name_ar": "التقديم للوظيفة",
            "icon": "📄",
            "order_index": 1,
            "vocab": [
                {"external_id": 408, "de": "das Vorstellungsgespräch (-e)", "ar": "مقابلة العمل",
                 "ex": "Morgen habe ich ein Vorstellungsgespräch.", "tp": "N"},
                {"external_id": 409, "de": "die Bewerbung (-en)", "ar": "طلب التوظيف",
                 "ex": "Ich schicke meine Bewerbung per E-Mail.", "tp": "N"},
                {"external_id": 410, "de": "der Lebenslauf (Lebensläufe)", "ar": "السيرة الذاتية",
                 "ex": "Der Lebenslauf muss aktuell sein.", "tp": "N"},
                {"external_id": 411, "de": "das Zeugnis (-se)", "ar": "الشهادة / التقرير المدرسي",
                 "ex": "Man schickt Zeugnisse von der Schule mit.", "tp": "N"},
                {"external_id": 412, "de": "die Bewerbungsunterlagen (Pl.)", "ar": "ملف التقديم",
                 "ex": "Schicken Sie Ihre Bewerbungsunterlagen.", "tp": "N"},
                {"external_id": 413, "de": "die Stelle (-n)", "ar": "الوظيفة",
                 "ex": "Ich bewerbe mich um die Stelle als Programmierer.", "tp": "N"},
                {"external_id": 414, "de": "sich bewerben (um)", "ar": "يتقدم لـ",
                 "ex": "Ich bewerbe mich um diese Stelle.", "tp": "V"},
                {"external_id": 415, "de": "der Personalchef (-s)", "ar": "مدير شؤون الموظفين",
                 "ex": "Sie können den Personalchef anrufen.", "tp": "N"},
                {"external_id": 416, "de": "die Qualität (-en)", "ar": "الجودة / المهارة",
                 "ex": "Was sind Ihre Qualitäten?", "tp": "N"},
                {"external_id": 417, "de": "sich erkundigen (nach)", "ar": "يستفسر عن",
                 "ex": "Er erkundigt sich, wie der Stand der Dinge ist.", "tp": "V"},
            ]
        },
        {
            "name_de": "Am Arbeitsplatz",
            "name_ar": "في مكان العمل",
            "icon": "🏢",
            "order_index": 2,
            "vocab": [
                {"external_id": 418, "de": "die Besprechung (-en)", "ar": "الاجتماع",
                 "ex": "Die nächste Besprechung ist morgen früh.", "tp": "N"},
                {"external_id": 419, "de": "die Präsentation (-en)", "ar": "العرض التقديمي",
                 "ex": "Boris bereitet die Präsentation vor.", "tp": "N"},
                {"external_id": 420, "de": "die Datei (-en)", "ar": "الملف (كمبيوتر)",
                 "ex": "Ich suche eine wichtige Datei.", "tp": "N"},
                {"external_id": 421, "de": "sich entschuldigen", "ar": "يعتذر",
                 "ex": "Entschuldigung! Ich wollte nicht stören.", "tp": "V"},
                {"external_id": 422, "de": "peinlich", "ar": "محرج",
                 "ex": "Das ist mir wirklich peinlich.", "tp": "Adj"},
                {"external_id": 423, "de": "aus Versehen", "ar": "عن طريق الخطأ",
                 "ex": "Ich habe aus Versehen Kaffee verschüttet.", "tp": "Ausdruck"},
                {"external_id": 424, "de": "Das war keine Absicht.", "ar": "لم يكن مقصوداً.",
                 "ex": "Entschuldigung! Das war keine Absicht.", "tp": "Ausdruck"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Am Telefon — Stellenanzeige",
            "situation_de": "Frau König ruft wegen einer Stellenanzeige an.",
            "lines": [
                {"speaker": "F", "text_de": "König und Partner, guten Tag!", "text_ar": "كونيغ وشركاه، مساء الخير!"},
                {"speaker": "K", "text_de": "Guten Tag, hier ist Lena Mersa. Ich rufe wegen Ihrer Anzeige an.", "text_ar": "مساء الخير، هنا لينا ميرسا. أتصل بشأن إعلانكم."},
                {"speaker": "F", "text_de": "Ja, die Stelle ist noch nicht besetzt.", "text_ar": "نعم، الوظيفة لم تُشغَل بعد."},
                {"speaker": "K", "text_de": "Ich interessiere mich für die Stelle als Mechatronikerin.", "text_ar": "أنا مهتمة بالوظيفة بوصفي مهندسة ميكاترونيك."},
                {"speaker": "F", "text_de": "Haben Sie denn schon in diesem Bereich gearbeitet?", "text_ar": "هل عملت من قبل في هذا المجال؟"},
                {"speaker": "K", "text_de": "Ja, ich habe drei Jahre Erfahrung als Mechatronikerin.", "text_ar": "نعم، لديّ ثلاث سنوات خبرة كمهندسة ميكاترونيك."},
                {"speaker": "F", "text_de": "Am besten vereinbaren wir einen Termin. Passt Ihnen nächste Woche?", "text_ar": "الأفضل أن نحدد موعداً. هل يناسبك الأسبوع القادم؟"},
                {"speaker": "K", "text_de": "Ja, das passt sehr gut. Ich würde mich über eine Einladung zum Gespräch freuen.", "text_ar": "نعم، هذا مناسب جداً. سأكون سعيدة بالدعوة للمقابلة."},
                {"speaker": "F", "text_de": "Schicken Sie uns bitte Ihre Bewerbungsunterlagen.", "text_ar": "أرسلي لنا من فضلك ملف تقديمك."},
            ]
        },
        {
            "title_de": "Gespräch bei der Arbeit — Wenn etwas schiefgeht",
            "situation_de": "Boris hat versehentlich Kaffee über das Hemd eines Kollegen geschüttet.",
            "lines": [
                {"speaker": "B", "text_de": "Oh, Entschuldigung! Das wollte ich wirklich nicht!", "text_ar": "أوه، عذراً! لم أقصد ذلك أبداً!"},
                {"speaker": "K", "text_de": "Was ist denn passiert?", "text_ar": "ماذا حدث؟"},
                {"speaker": "B", "text_de": "Ich habe aus Versehen Kaffee über Ihr Hemd geschüttet. Das ist mir wirklich peinlich.", "text_ar": "سكبت القهوة على قميصك عن طريق الخطأ. هذا يُحرجني حقاً."},
                {"speaker": "K", "text_de": "Das macht doch nichts. Das kann jedem mal passieren.", "text_ar": "لا يهم. هذا يمكن أن يحدث لأي شخص."},
                {"speaker": "B", "text_de": "Ich übernehme natürlich die Reinigungskosten.", "text_ar": "سأتحمل بالطبع تكاليف التنظيف."},
                {"speaker": "K", "text_de": "Das ist wirklich nicht nötig. Schon gut!", "text_ar": "هذا ليس ضرورياً حقاً. لا بأس!"},
            ]
        },
    ],
    "redemittel": {
        "sich entschuldigen": [
            {"de": "Entschuldigung! / Verzeihung!", "ar": "عفواً! / آسف!"},
            {"de": "Das wollte ich nicht.", "ar": "لم أقصد ذلك."},
            {"de": "Das war keine Absicht.", "ar": "لم يكن مقصوداً."},
            {"de": "Das ist mir wirklich unangenehm / peinlich.", "ar": "هذا يُحرجني حقاً."},
            {"de": "(Es) Tut mir (sehr / schrecklich) leid.", "ar": "أنا آسف جداً."},
        ],
        "auf Entschuldigungen reagieren": [
            {"de": "Bitte. / Schon gut.", "ar": "من فضلك. / لا بأس."},
            {"de": "Kein Problem.", "ar": "لا مشكلة."},
            {"de": "Das macht doch nichts.", "ar": "هذا لا يهم."},
            {"de": "Das kann doch (jedem) mal passieren.", "ar": "هذا يمكن أن يحدث لأي شخص."},
        ],
        "am Telefon — nach Stelle fragen": [
            {"de": "Ich rufe wegen Ihrer Anzeige an.", "ar": "أتصل بشأن إعلانكم."},
            {"de": "Ich interessiere mich für die Stelle als ...", "ar": "أنا مهتم/ة بالوظيفة بوصفي ..."},
            {"de": "Ich hätte da eine Frage zu ...", "ar": "لديّ سؤال بشأن ..."},
            {"de": "Ich würde mich über eine Einladung zum Gespräch freuen.", "ar": "سأكون سعيداً بالدعوة للمقابلة."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 5: Umweltfreundlich?
# ═══════════════════════════════════════════════════════════

KAP_5 = {
    "number": 5,
    "title_de": "Umweltfreundlich?",
    "title_ar": "صديق للبيئة؟",
    "icon": "🌿",
    "description_de": "Umweltschutz, Wetter und Vergleiche",
    "description_ar": "حماية البيئة، الطقس، والمقارنات",
    "grammar_focus": "Komparativ/Superlativ vor Nomen | damit / um…zu",
    "page_start": 48,
    "page_end": 57,
    "themen": [
        {
            "name_de": "Umwelt & Umweltschutz",
            "name_ar": "البيئة وحمايتها",
            "icon": "🌍",
            "order_index": 0,
            "vocab": [
                {"external_id": 501, "de": "die Umwelt", "ar": "البيئة",
                 "ex": "Wir müssen die Umwelt schützen.", "tp": "N"},
                {"external_id": 502, "de": "umweltfreundlich", "ar": "صديق للبيئة",
                 "ex": "Das ist eine umweltfreundliche Alternative.", "tp": "Adj"},
                {"external_id": 503, "de": "der Müll (kein Pl.)", "ar": "القمامة / النفايات",
                 "ex": "Wie viel Abfall produzierst du pro Jahr?", "tp": "N"},
                {"external_id": 504, "de": "die Verpackung (-en)", "ar": "التغليف / العبوة",
                 "ex": "50% des Papiers ist Verpackungsmüll.", "tp": "N"},
                {"external_id": 505, "de": "recyceln", "ar": "يُعيد التدوير",
                 "ex": "Wir recyceln Papier, Glas und Plastik.", "tp": "V"},
                {"external_id": 506, "de": "die Mehrwegflasche (-n)", "ar": "الزجاجة القابلة للإعادة",
                 "ex": "Mehrwegflaschen sind die beste Alternative.", "tp": "N"},
                {"external_id": 507, "de": "der Fleischkonsum", "ar": "استهلاك اللحوم",
                 "ex": "59,6 Kilo Fleisch isst jeder Mensch in Deutschland im Jahr.", "tp": "N"},
                {"external_id": 508, "de": "das Trinkwasser", "ar": "مياه الشرب",
                 "ex": "125 Liter Trinkwasser verbraucht jeder Mensch in Deutschland pro Tag.", "tp": "N"},
                {"external_id": 509, "de": "der Papierverbrauch", "ar": "استهلاك الورق",
                 "ex": "187 Kilo Papier verbraucht jede Person in Deutschland pro Jahr.", "tp": "N"},
                {"external_id": 510, "de": "der ökologische Fußabdruck", "ar": "البصمة البيئية",
                 "ex": "Berechnen Sie Ihren ökologischen Fußabdruck.", "tp": "N"},
                {"external_id": 511, "de": "Energie sparen", "ar": "توفير الطاقة",
                 "ex": "Wir müssen Energie sparen.", "tp": "Ausdruck"},
                {"external_id": 512, "de": "regionale Lebensmittel kaufen", "ar": "شراء المنتجات المحلية",
                 "ex": "Man kann regionale Produkte auf dem Markt kaufen.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Wetter",
            "name_ar": "الطقس",
            "icon": "☀️",
            "order_index": 1,
            "vocab": [
                {"external_id": 513, "de": "der Regen (kein Pl.)", "ar": "المطر",
                 "ex": "In Norddeutschland regnet es oft.", "tp": "N"},
                {"external_id": 514, "de": "der Schnee (kein Pl.)", "ar": "الثلج",
                 "ex": "Im Winter gibt es in Bayern viel Schnee.", "tp": "N"},
                {"external_id": 515, "de": "das Gewitter (-)", "ar": "العاصفة الرعدية",
                 "ex": "Heute Nachmittag gibt es ein Gewitter.", "tp": "N"},
                {"external_id": 516, "de": "der Sturm (Stürme)", "ar": "العاصفة",
                 "ex": "Der Sturm hat viele Bäume umgeworfen.", "tp": "N"},
                {"external_id": 517, "de": "bewölkt / sonnig", "ar": "غائم / مشمس",
                 "ex": "Morgen ist es bewölkt, aber trocken.", "tp": "Adj"},
                {"external_id": 518, "de": "die Temperatur (-en)", "ar": "درجة الحرارة",
                 "ex": "Die Temperaturen erreichen 30 Grad.", "tp": "N"},
                {"external_id": 519, "de": "der Klimawandel", "ar": "التغيّر المناخي",
                 "ex": "Der Klimawandel ist ein globales Problem.", "tp": "N"},
            ]
        },
        {
            "name_de": "Vergleichen",
            "name_ar": "المقارنة",
            "icon": "⚖️",
            "order_index": 2,
            "vocab": [
                {"external_id": 520, "de": "vergleichen", "ar": "يقارن",
                 "ex": "Ich vergleiche immer die Preise.", "tp": "V"},
                {"external_id": 521, "de": "der Geschirrspüler (-)", "ar": "غسالة الأطباق",
                 "ex": "Der Geschirrspüler ist die bessere Wahl.", "tp": "N"},
                {"external_id": 522, "de": "der Vorteil (-e) / der Nachteil (-e)", "ar": "الميزة / العيب",
                 "ex": "Was sind die Vor- und Nachteile?", "tp": "N"},
                {"external_id": 523, "de": "das Bioprodukt (-e)", "ar": "المنتج العضوي",
                 "ex": "Bioprodukte sind teurer, aber gesünder.", "tp": "N"},
                {"external_id": 524, "de": "der Marktanteil (-e)", "ar": "حصة السوق",
                 "ex": "Der Marktanteil von Bio-Fleisch liegt bei nur zwei Prozent.", "tp": "N"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Im Supermarkt — Linda und Juan",
            "situation_de": "Linda und Juan sprechen über umweltfreundliches Einkaufen.",
            "lines": [
                {"speaker": "L", "text_de": "Schau mal, hier sind Tomaten aus Spanien. Die sind viel günstiger!", "text_ar": "انظر، هنا طماطم من إسبانيا. أرخص بكثير!"},
                {"speaker": "J", "text_de": "Ja, aber ich kaufe lieber regionale Produkte, damit ich die Umwelt schütze.", "text_ar": "نعم، لكنني أفضل شراء المنتجات المحلية لكي أحمي البيئة."},
                {"speaker": "L", "text_de": "Stimmt. Lange Transportwege sind schlecht für das Klima.", "text_ar": "صحيح. المسافات الطويلة للنقل تضر بالمناخ."},
                {"speaker": "J", "text_de": "Außerdem kaufe ich keine Produkte mit zu viel Verpackung.", "text_ar": "علاوة على ذلك أنا لا أشتري منتجات بتغليف زائد."},
                {"speaker": "L", "text_de": "Das finde ich auch gut. Ich versuche, Plastikflaschen zu vermeiden.", "text_ar": "أجد هذا جيداً أيضاً. أحاول تجنب زجاجات البلاستيك."},
                {"speaker": "J", "text_de": "Ich nehme immer Mehrwegflaschen. Sie sind die beste Alternative.", "text_ar": "دائماً آخذ زجاجات إعادة الاستخدام. هي الخيار الأفضل."},
            ]
        },
    ],
    "redemittel": {
        "die eigene Meinung äußern": [
            {"de": "Ich bin (nicht) der Meinung, dass ...", "ar": "أنا (لا) أرى أن ..."},
            {"de": "Meiner Meinung nach ...", "ar": "من وجهة نظري ..."},
            {"de": "Ich stehe (nicht) auf dem Standpunkt, dass ...", "ar": "أنا (لا) أتبنى الرأي القائل بأن ..."},
            {"de": "Ich bin (nicht) davon überzeugt, dass ...", "ar": "أنا (غير) مقتنع بأن ..."},
        ],
        "zustimmen": [
            {"de": "Das sehe ich auch so.", "ar": "أرى الأمر بنفس الطريقة."},
            {"de": "Da haben Sie / hast du völlig recht.", "ar": "لديك حق تماماً."},
            {"de": "Ich bin auch der Meinung, dass ...", "ar": "أنا أيضاً أرى أن ..."},
        ],
        "widersprechen": [
            {"de": "Das stimmt meiner Meinung nach nicht, denn ...", "ar": "هذا من وجهة نظري غير صحيح، لأن ..."},
            {"de": "Da muss ich leider widersprechen.", "ar": "يجب عليّ للأسف أن أعارض."},
            {"de": "Ich sehe das etwas anders: ...", "ar": "أرى هذا بشكل مختلف: ..."},
        ],
        "Umwelttipps geben": [
            {"de": "Ich achte darauf, ...", "ar": "أهتم بـ ..."},
            {"de": "Für mich ist extrem wichtig, dass ...", "ar": "بالنسبة لي من الأهمية البالغة أن ..."},
            {"de": "Ich versuche, auf ... zu verzichten.", "ar": "أحاول الامتناع عن ..."},
        ],
    }
}


# ═══════════════════════════════════════════════════════════
# تحديث ALL_KAPITEL
# ═══════════════════════════════════════════════════════════

ALL_KAPITEL = {
    1: KAP_1,
    2: KAP_2,
    3: KAP_3,
    4: KAP_4,
    5: KAP_5,
    # 6-12 ستضاف لاحقاً
}
# ═══════════════════════════════════════════════════════════
# Kapitel 6: Blick nach vorn
# ═══════════════════════════════════════════════════════════

KAP_6 = {
    "number": 6,
    "title_de": "Blick nach vorn",
    "title_ar": "نظرة للأمام",
    "icon": "🔮",
    "description_de": "Zukunftsprognosen, Vorsätze und n-Deklination",
    "description_ar": "تنبؤات المستقبل، النوايا، والأسماء الضعيفة",
    "grammar_focus": "Futur I | n-Deklination | Relativsätze im Dativ",
    "page_start": 58,
    "page_end": 67,
    "themen": [
        {
            "name_de": "Zukunftsprognosen",
            "name_ar": "تنبؤات المستقبل",
            "icon": "🚀",
            "order_index": 0,
            "vocab": [
                {"external_id": 601, "de": "die Prognose (-n)", "ar": "التنبؤ / التوقع",
                 "ex": "Die Zukunftsprognosen sind nicht immer richtig.", "tp": "N"},
                {"external_id": 602, "de": "In der Zukunft werden Menschen auf dem Mars leben.", "ar": "في المستقبل سيعيش البشر على المريخ.",
                 "ex": "Zukunftsprognose.", "tp": "Satz"},
                {"external_id": 603, "de": "die Drohne (-n)", "ar": "الطائرة المسيّرة",
                 "ex": "Wir fliegen als Passagiere in Drohnen zur Arbeit.", "tp": "N"},
                {"external_id": 604, "de": "der medizinische Fortschritt", "ar": "التقدم الطبي",
                 "ex": "Durch den medizinischen Fortschritt werden Menschen 150 Jahre alt.", "tp": "N"},
                {"external_id": 605, "de": "vorhersagen", "ar": "يتنبأ / يتوقع",
                 "ex": "Kann man die Zukunft wirklich vorhersagen?", "tp": "V"},
                {"external_id": 606, "de": "das kann ich mir nicht vorstellen", "ar": "لا أستطيع تصور ذلك",
                 "ex": "Das kann ich mir nicht vorstellen. Das bleibt sicher Fantasie.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Vorsätze & Pläne",
            "name_ar": "النوايا والخطط",
            "icon": "📋",
            "order_index": 1,
            "vocab": [
                {"external_id": 607, "de": "der Vorsatz (Vorsätze)", "ar": "النية / القرار",
                 "ex": "Was sind Ihre Vorsätze für das neue Jahr?", "tp": "N"},
                {"external_id": 608, "de": "vorhaben", "ar": "ينوي",
                 "ex": "Was hast du nächste Woche vor?", "tp": "V"},
                {"external_id": 609, "de": "sich vornehmen", "ar": "يعزم على",
                 "ex": "Ich nehme mir vor, mehr Sport zu machen.", "tp": "V"},
                {"external_id": 610, "de": "aufhören (mit)", "ar": "يتوقف عن",
                 "ex": "Ich möchte aufhören, so viel Fleisch zu essen.", "tp": "V"},
                {"external_id": 611, "de": "abnehmen", "ar": "يخسر وزناً",
                 "ex": "Ich habe vor, nächstes Jahr abzunehmen.", "tp": "V"},
                {"external_id": 612, "de": "die Erwartung (-en)", "ar": "التوقع",
                 "ex": "Meine Erwartungen waren leider zu hoch.", "tp": "N"},
            ]
        },
        {
            "name_de": "n-Deklination",
            "name_ar": "الأسماء الضعيفة",
            "icon": "📝",
            "order_index": 2,
            "vocab": [
                {"external_id": 613, "de": "der Student (-en, -en)", "ar": "الطالب (اسم ضعيف)",
                 "ex": "Ich kenne einen Studenten, der viel reist.", "tp": "n-Dekl"},
                {"external_id": 614, "de": "der Kollege (-n, -n)", "ar": "الزميل (اسم ضعيف)",
                 "ex": "Ich wollte den Kollegen anrufen.", "tp": "n-Dekl"},
                {"external_id": 615, "de": "der Mensch (-en, -en)", "ar": "الإنسان (اسم ضعيف)",
                 "ex": "Viele Menschen haben Zukunftsangst.", "tp": "n-Dekl"},
                {"external_id": 616, "de": "der Nachbar (-n, -n)", "ar": "الجار (اسم ضعيف)",
                 "ex": "Eventuell finden Sie auch einen Nachbarn.", "tp": "n-Dekl"},
                {"external_id": 617, "de": "der Experte (-n, -n)", "ar": "الخبير (اسم ضعيف)",
                 "ex": "Der Experte gibt Ratschläge.", "tp": "n-Dekl"},
                {"external_id": 618, "de": "der Journalist (-en, -en)", "ar": "الصحفي (اسم ضعيف)",
                 "ex": "Der Journalist interviewt den Experten.", "tp": "n-Dekl"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Ratschläge hören — Vorsätze",
            "situation_de": "Ein Experte gibt Ratschläge in einer Radiosendung.",
            "lines": [
                {"speaker": "M", "text_de": "Herzlich willkommen! Heute sprechen wir über Vorsätze. Warum gelingt es oft nicht?", "text_ar": "أهلاً بكم! اليوم نتحدث عن النوايا. لماذا كثيراً ما نفشل؟"},
                {"speaker": "E", "text_de": "Die meisten Menschen nehmen sich zu viel vor.", "text_ar": "معظم الناس يضعون لأنفسهم خططاً كثيرة جداً."},
                {"speaker": "M", "text_de": "Was raten Sie?", "text_ar": "ما الذي تنصح به؟"},
                {"speaker": "E", "text_de": "Erstens: Machen Sie Ihre Vorsätze konkret! Nicht 'Ich möchte mehr Sport machen', sondern 'Ich gehe jeden Montag ins Fitnessstudio'.", "text_ar": "أولاً: اجعل نواياك محددة! ليس 'أريد ممارسة الرياضة أكثر' بل 'أذهب كل اثنين للنادي الرياضي'."},
                {"speaker": "E", "text_de": "Zweitens: Suchen Sie sich Unterstützung — einen Freund, eine Kollegin.", "text_ar": "ثانياً: ابحث عن دعم — صديق، زميلة."},
                {"speaker": "M", "text_de": "Und wenn man doch aufhört?", "text_ar": "وماذا لو توقف المرء؟"},
                {"speaker": "E", "text_de": "Geben Sie nicht auf! Fangen Sie einfach wieder an.", "text_ar": "لا تستسلم! فقط ابدأ من جديد."},
            ]
        },
    ],
    "redemittel": {
        "Pläne und Vorsätze ausdrücken": [
            {"de": "Ich habe vor, ... zu ...", "ar": "أنا أعتزم أن ..."},
            {"de": "Ich nehme mir vor, ...", "ar": "أعقد النية على ..."},
            {"de": "Ich möchte aufhören, ... zu ...", "ar": "أريد أن أتوقف عن ..."},
            {"de": "Ich plane, ... zu ...", "ar": "أخطط لـ ..."},
            {"de": "Mein Ziel ist es, ...", "ar": "هدفي هو ..."},
        ],
        "über Zukunft sprechen": [
            {"de": "In der Zukunft wird / werden ...", "ar": "في المستقبل سـ ..."},
            {"de": "Ich glaube / denke, dass ...", "ar": "أعتقد أن ..."},
            {"de": "Das kann ich mir (nicht) vorstellen.", "ar": "يمكنني (لا يمكنني) تصور ذلك."},
            {"de": "Das bleibt sicher Fantasie.", "ar": "هذا بالتأكيد سيبقى خيالاً."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 7: Zwischenmenschliches
# ═══════════════════════════════════════════════════════════

KAP_7 = {
    "number": 7,
    "title_de": "Zwischenmenschliches",
    "title_ar": "العلاقات الإنسانية",
    "icon": "🤝",
    "description_de": "Beziehungen, Konflikte und Fabeln",
    "description_ar": "العلاقات، النزاعات، والحكايات",
    "grammar_focus": "Plusquamperfekt | bevor/bis/nachdem/seit/während",
    "page_start": 68,
    "page_end": 77,
    "themen": [
        {
            "name_de": "Beziehungen & Freundschaft",
            "name_ar": "العلاقات والصداقة",
            "icon": "❤️",
            "order_index": 0,
            "vocab": [
                {"external_id": 701, "de": "die Freundschaft (-en)", "ar": "الصداقة",
                 "ex": "Freundschaft ist wichtig im Leben.", "tp": "N"},
                {"external_id": 702, "de": "der Konflikt (-e)", "ar": "النزاع / الصراع",
                 "ex": "Jenny und Mark haben einen Konflikt.", "tp": "N"},
                {"external_id": 703, "de": "sich streiten", "ar": "يتشاجر",
                 "ex": "Jenny und Mark streiten sich manchmal.", "tp": "V"},
                {"external_id": 704, "de": "sich vertragen", "ar": "يتوافق / يتصالح",
                 "ex": "Sie haben sich wieder vertragen.", "tp": "V"},
                {"external_id": 705, "de": "sich aus den Augen verlieren", "ar": "يفقدون التواصل",
                 "ex": "Wir haben uns leider aus den Augen verloren.", "tp": "Ausdruck"},
                {"external_id": 706, "de": "beschließen", "ar": "يقرر",
                 "ex": "Wir haben beschlossen, etwas zu ändern.", "tp": "V"},
                {"external_id": 707, "de": "einsam", "ar": "وحيد",
                 "ex": "Sie fühlte sich oft einsam in der neuen Stadt.", "tp": "Adj"},
                {"external_id": 708, "de": "das Mitglied (-er)", "ar": "العضو",
                 "ex": "Matilda wurde Mitglied in einem Netzwerk für Nachbarn.", "tp": "N"},
            ]
        },
        {
            "name_de": "Konflikte",
            "name_ar": "مواقف الخلاف",
            "icon": "⚡",
            "order_index": 1,
            "vocab": [
                {"external_id": 709, "de": "ständig", "ar": "باستمرار / دائماً",
                 "ex": "Du bist ständig erschöpft!", "tp": "Adv"},
                {"external_id": 710, "de": "gleichzeitig", "ar": "في نفس الوقت",
                 "ex": "Kannst du gleichzeitig kochen und putzen?", "tp": "Adv"},
                {"external_id": 711, "de": "erschöpft", "ar": "منهك / مرهق",
                 "ex": "Seitdem du arbeitest, bist du ständig erschöpft.", "tp": "Adj"},
                {"external_id": 712, "de": "nerven", "ar": "يُزعج / يُثير أعصاب",
                 "ex": "Das nervt mich wirklich.", "tp": "V"},
                {"external_id": 713, "de": "diplomatisch", "ar": "دبلوماسي",
                 "ex": "Sei mir nicht böse — das sage ich diplomatisch.", "tp": "Adj"},
            ]
        },
        {
            "name_de": "Fabeln & Sprichwörter",
            "name_ar": "الحكايات والأمثال",
            "icon": "📖",
            "order_index": 2,
            "vocab": [
                {"external_id": 714, "de": "die Fabel (-n)", "ar": "الحكاية / الخرافة",
                 "ex": "Wir lesen die Fabel über den Löwen und den Bären.", "tp": "N"},
                {"external_id": 715, "de": "die Moral (-en)", "ar": "الحكمة / العبرة",
                 "ex": "Die Moral von der Geschichte ist ...", "tp": "N"},
                {"external_id": 716, "de": "Wenn zwei sich streiten, freut sich der Dritte.", "ar": "عندما يتشاجر اثنان يفرح الثالث.",
                 "ex": "Deutsches Sprichwort.", "tp": "Sprichwort"},
                {"external_id": 717, "de": "Wer zuletzt lacht, lacht am besten.", "ar": "من يضحك أخيراً يضحك أطول.",
                 "ex": "Deutsches Sprichwort.", "tp": "Sprichwort"},
                {"external_id": 718, "de": "Der/Die Klügere gibt nach.", "ar": "الأذكى يتنازل.",
                 "ex": "Deutsches Sprichwort.", "tp": "Sprichwort"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Richtig streiten — Konfliktgespräch",
            "situation_de": "Florian und seine Eltern streiten sich.",
            "lines": [
                {"speaker": "M", "text_de": "Florian, seit du Geld verdienst, kaufst du oft Sachen. Das finde ich nicht gut.", "text_ar": "فلوريان، منذ أن بدأت تكسب مالاً تشتري أشياء كثيراً. هذا لا يعجبني."},
                {"speaker": "F", "text_de": "Was? Ich habe doch das Recht, mein eigenes Geld auszugeben!", "text_ar": "ماذا؟ لديّ الحق في إنفاق أموالي الخاصة!"},
                {"speaker": "V", "text_de": "Sei mir nicht böse, bitte. Wir machen uns nur Sorgen.", "text_ar": "لا تكن غاضباً مني. نحن فقط قلقون عليك."},
                {"speaker": "F", "text_de": "Okay, ich verstehe. Aber ich kaufe wirklich nur, was ich brauche.", "text_ar": "حسناً، أفهم. لكنني فعلاً أشتري فقط ما أحتاجه."},
                {"speaker": "M", "text_de": "Ich wünsche mir, dass wir mehr Zeit miteinander verbringen.", "text_ar": "أتمنى أن نقضي وقتاً أكثر معاً."},
                {"speaker": "F", "text_de": "Das wünsche ich mir auch. Was hältst du von einem Familienessen am Wochenende?", "text_ar": "أنا أيضاً أتمنى ذلك. ما رأيك بعشاء عائلي في نهاية الأسبوع؟"},
                {"speaker": "V", "text_de": "Das ist eine sehr gute Idee! Wir finden bestimmt einen Kompromiss.", "text_ar": "هذه فكرة رائعة! بالتأكيد سنجد حلاً وسطاً."},
            ]
        },
    ],
    "redemittel": {
        "etwas hervorheben": [
            {"de": "Im Gegensatz zu ... finde ich ...", "ar": "على عكس ... أجد ..."},
            {"de": "An ... schätze ich vor allem ...", "ar": "أقدّر في ... قبل كل شيء ..."},
            {"de": "Besonders wichtig ist/sind für mich ..., weil ...", "ar": "الأهم بالنسبة لي هو ..., لأن ..."},
        ],
        "Konfliktgespräche führen — diplomatisch": [
            {"de": "Sei mir nicht böse, bitte.", "ar": "لا تكن غاضباً مني."},
            {"de": "Das ist ja nicht so schlimm.", "ar": "الأمر ليس بهذه الخطورة."},
            {"de": "Wir finden bestimmt einen Kompromiss.", "ar": "بالتأكيد سنجد حلاً وسطاً."},
            {"de": "Ich wünsche mir, dass ...", "ar": "أتمنى أن ..."},
        ],
        "undiplomatisch": [
            {"de": "Jetzt übertreibst du aber etwas!", "ar": "الآن تبالغ قليلاً!"},
            {"de": "Das nervt mich wirklich.", "ar": "هذا يُزعجني فعلاً."},
            {"de": "Das kann echt nicht wahr sein!", "ar": "هذا لا يمكن أن يكون حقيقياً!"},
        ],
    }
}


# ═══════════════════════════════════════════════════════════
# تحديث ALL_KAPITEL
# ═══════════════════════════════════════════════════════════

ALL_KAPITEL = {
    1: KAP_1,
    2: KAP_2,
    3: KAP_3,
    4: KAP_4,
    5: KAP_5,
    6: KAP_6,
    7: KAP_7,
    # 8-12 ستضاف لاحقاً
}
# ═══════════════════════════════════════════════════════════
# Kapitel 8: Rund um Körper und Geist
# ═══════════════════════════════════════════════════════════

KAP_8 = {
    "number": 8,
    "title_de": "Rund um Körper und Geist",
    "title_ar": "الجسم والعقل",
    "icon": "💊",
    "description_de": "Gesundheit, Gewohnheiten und Musik",
    "description_ar": "الصحة، العادات، والموسيقى",
    "grammar_focus": "nicht/nur + brauchen+zu | Reflexivpronomen Dativ | zweiteilige Konnektoren",
    "page_start": 78,
    "page_end": 87,
    "themen": [
        {
            "name_de": "Gesundheit & Krankenhaus",
            "name_ar": "الصحة والمستشفى",
            "icon": "🏥",
            "order_index": 0,
            "vocab": [
                {"external_id": 801, "de": "die Besuchszeit (-en)", "ar": "وقت الزيارة",
                 "ex": "Besucher sind prinzipiell jederzeit willkommen.", "tp": "N"},
                {"external_id": 802, "de": "die Wertsachen (Pl.)", "ar": "الأشياء الثمينة",
                 "ex": "Sämtliche Wertsachen im Schließfach aufbewahren.", "tp": "N"},
                {"external_id": 803, "de": "der Notausgang (Notausgänge)", "ar": "مخرج الطوارئ",
                 "ex": "Der Weg zum Notausgang ist beschildert.", "tp": "N"},
                {"external_id": 804, "de": "die Ernährung", "ar": "التغذية",
                 "ex": "Für diätetische Ernährung ist unser Diät-Assistent zuständig.", "tp": "N"},
                {"external_id": 805, "de": "warnen (vor)", "ar": "يُحذّر من",
                 "ex": "Der Arzt warnt vor zu viel Stress.", "tp": "V"},
                {"external_id": 806, "de": "Hilfe anbieten", "ar": "يعرض المساعدة",
                 "ex": "Kann ich Ihnen helfen?", "tp": "Ausdruck"},
                {"external_id": 807, "de": "Hilfe ablehnen", "ar": "يرفض المساعدة",
                 "ex": "Danke, das schaffe ich alleine.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Gewohnheiten",
            "name_ar": "العادات اليومية",
            "icon": "🪥",
            "order_index": 1,
            "vocab": [
                {"external_id": 808, "de": "sich kämmen", "ar": "يُمشّط شعره",
                 "ex": "Kämmst du dich gleich nach dem Aufstehen?", "tp": "V"},
                {"external_id": 809, "de": "sich duschen", "ar": "يستحم",
                 "ex": "Duschst du lieber morgens oder abends?", "tp": "V"},
                {"external_id": 810, "de": "sich die Zähne putzen", "ar": "يغسل أسنانه",
                 "ex": "Ich putze mir die Zähne vor dem Schlafengehen.", "tp": "V"},
                {"external_id": 811, "de": "sich anziehen", "ar": "يرتدي ملابسه",
                 "ex": "Ich ziehe mir den Pullover an.", "tp": "V"},
                {"external_id": 812, "de": "sich die Haare waschen", "ar": "يغسل شعره",
                 "ex": "Wäschst du dir die Haare morgens oder abends?", "tp": "V"},
            ]
        },
        {
            "name_de": "Musik & Gefühle",
            "name_ar": "الموسيقى والمشاعر",
            "icon": "🎵",
            "order_index": 2,
            "vocab": [
                {"external_id": 813, "de": "die Stimmung (-en)", "ar": "المزاج / الحالة",
                 "ex": "Musik beeinflusst unsere Stimmung stark.", "tp": "N"},
                {"external_id": 814, "de": "beruhigend", "ar": "مُهدّئ",
                 "ex": "Langsame Musik wirkt beruhigend.", "tp": "Adj"},
                {"external_id": 815, "de": "fröhlich / traurig", "ar": "مبهج / حزين",
                 "ex": "Schnelle Musik macht uns fröhlich.", "tp": "Adj"},
                {"external_id": 816, "de": "das Gehirn (-e)", "ar": "الدماغ",
                 "ex": "Das Gehirn verarbeitet Musik in zwei Bereichen.", "tp": "N"},
                {"external_id": 817, "de": "die Erinnerung (-en)", "ar": "الذكرى",
                 "ex": "Musik kann uns an Erlebnisse erinnern.", "tp": "N"},
                {"external_id": 818, "de": "sowohl … als auch", "ar": "كلٌّ من ... و...",
                 "ex": "Das Gehirn verarbeitet Musik sowohl im Bereich für Sprache als auch für Gefühle.", "tp": "Konnektor"},
                {"external_id": 819, "de": "weder … noch", "ar": "لا ... ولا ...",
                 "ex": "Er trinkt weder Kaffee noch Tee.", "tp": "Konnektor"},
                {"external_id": 820, "de": "entweder … oder", "ar": "إما ... أو ...",
                 "ex": "Man kann entweder Klassik oder Metal mögen.", "tp": "Konnektor"},
                {"external_id": 821, "de": "nicht nur … sondern auch", "ar": "ليس فقط ... بل أيضاً ...",
                 "ex": "Musik ist nicht nur Unterhaltung, sondern auch Therapie.", "tp": "Konnektor"},
                {"external_id": 822, "de": "zwar … aber", "ar": "صحيح ... لكن ...",
                 "ex": "Musik ist zwar schön, aber zu laut ist ungesund.", "tp": "Konnektor"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Informationen für Ihren Aufenthalt in unserer Klinik",
            "situation_de": "Fein-Klinik Stuttgart — Informationsblatt für Patienten.",
            "lines": [
                {"speaker": "I", "text_de": "Essen und Getränke: Täglich drei Hauptmahlzeiten und Zwischenmahlzeiten.", "text_ar": "الطعام والمشروبات: ثلاث وجبات رئيسية يومياً ووجبات خفيفة."},
                {"speaker": "I", "text_de": "Kleidung: Bitte nehmen Sie bequeme Kleidung und Hausschuhe mit.", "text_ar": "الملابس: يرجى إحضار ملابس مريحة وشباشب."},
                {"speaker": "I", "text_de": "Fernsehen: Das Gerät kostet 2,50 € pro Tag.", "text_ar": "التلفزيون: الجهاز يكلف 2.50 يورو يومياً."},
                {"speaker": "I", "text_de": "Telefon: 2 € pro Tag einschließlich Gespräche ins deutsche Festnetz.", "text_ar": "الهاتف: 2 يورو يومياً شاملاً المكالمات للشبكة الألمانية الثابتة."},
                {"speaker": "I", "text_de": "Besuchszeiten: Besucher sind prinzipiell jederzeit willkommen.", "text_ar": "أوقات الزيارة: الزوار مرحب بهم في أي وقت."},
                {"speaker": "I", "text_de": "Wertsachen: Wir empfehlen Ihnen, Wertsachen im Schließfach aufzubewahren.", "text_ar": "الأشياء الثمينة: ننصحكم بحفظها في الخزانة الآمنة."},
                {"speaker": "I", "text_de": "Notausgang: Bei einem Notfall drücken Sie den Alarmknopf.", "text_ar": "مخرج الطوارئ: في حالة الطوارئ اضغط على زر الإنذار."},
            ]
        },
    ],
    "redemittel": {
        "Hilfe anbieten / annehmen / ablehnen": [
            {"de": "Kann ich Ihnen / dir helfen?", "ar": "هل أستطيع مساعدتك؟"},
            {"de": "Soll ich ... für Sie / dich ...?", "ar": "هل تريد أن أـ ... لك؟"},
            {"de": "Ja, das wäre nett. Danke!", "ar": "نعم، هذا لطيف. شكراً!"},
            {"de": "Danke, das schaffe ich alleine.", "ar": "شكراً، أستطيع ذلك بنفسي."},
        ],
        "warnen": [
            {"de": "Vorsicht! Das ist gefährlich!", "ar": "تنبّه! هذا خطير!"},
            {"de": "Pass auf! Du solltest ...", "ar": "انتبه! يجب أن تـ ..."},
            {"de": "Ich warne Sie / dich vor ...", "ar": "أحذّرك من ..."},
        ],
        "Lerntipps geben": [
            {"de": "Es hilft, wenn man ...", "ar": "يُساعد إذا ..."},
            {"de": "Am besten lernst du, indem du ...", "ar": "الأفضل أن تتعلم من خلال ..."},
            {"de": "Ich empfehle dir, ...", "ar": "أنصحك بـ ..."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 9: Kunststücke
# ═══════════════════════════════════════════════════════════

KAP_9 = {
    "number": 9,
    "title_de": "Kunststücke",
    "title_ar": "الفن",
    "icon": "🎨",
    "description_de": "Kunst, Museum, Musik und Bildungszentrum",
    "description_ar": "الفن، المتحف، الموسيقى، ومركز التعليم",
    "grammar_focus": "Stellung von nicht | Adjektive ohne Artikel",
    "page_start": 88,
    "page_end": 97,
    "themen": [
        {
            "name_de": "Kunst & Museum",
            "name_ar": "الفن والمتحف",
            "icon": "🖼️",
            "order_index": 0,
            "vocab": [
                {"external_id": 901, "de": "das Kunstwerk (-e)", "ar": "العمل الفني",
                 "ex": "Wie gefällt Ihnen dieses Kunstwerk?", "tp": "N"},
                {"external_id": 902, "de": "der Künstler (-) / die Künstlerin", "ar": "الفنان / الفنانة",
                 "ex": "Alice Marosevic ist eine junge Malerin.", "tp": "N"},
                {"external_id": 903, "de": "die Ausstellung (-en)", "ar": "المعرض",
                 "ex": "Es gibt viele Ausstellungen in dieser Stadt.", "tp": "N"},
                {"external_id": 904, "de": "das Bühnenbild (-er)", "ar": "ديكور المسرح",
                 "ex": "Im Theater — Wie entsteht ein Bühnenbild?", "tp": "N"},
                {"external_id": 905, "de": "improvisieren", "ar": "يرتجل",
                 "ex": "In diesem Kurs lernen wir zu improvisieren.", "tp": "V"},
                {"external_id": 906, "de": "begeistert (von)", "ar": "متحمس (لـ)",
                 "ex": "Ich bin von diesem Bild total begeistert.", "tp": "Adj"},
                {"external_id": 907, "de": "Das Bild gefällt mir total gut.", "ar": "اللوحة تعجبني كثيراً.",
                 "ex": "Positiv bewerten.", "tp": "Ausdruck"},
                {"external_id": 908, "de": "Ich finde das eher langweilig.", "ar": "أجد هذا مملاً نوعاً ما.",
                 "ex": "Neutral / negativ bewerten.", "tp": "Ausdruck"},
                {"external_id": 909, "de": "Das spricht mich nicht an.", "ar": "هذا لا يستأثر باهتمامي.",
                 "ex": "Ablehnung ausdrücken.", "tp": "Ausdruck"},
                {"external_id": 910, "de": "Das ist wirklich nichts für mich.", "ar": "هذا ليس من ذوقي أبداً.",
                 "ex": "Ablehnung stark.", "tp": "Ausdruck"},
            ]
        },
        {
            "name_de": "Gesang & Volkslieder",
            "name_ar": "الغناء والأغاني الشعبية",
            "icon": "🎤",
            "order_index": 1,
            "vocab": [
                {"external_id": 911, "de": "das Volkslied (-er)", "ar": "الأغنية الشعبية",
                 "ex": "In Deutschland gibt es viele Volkslieder.", "tp": "N"},
                {"external_id": 912, "de": "der Chor (Chöre)", "ar": "الجوقة",
                 "ex": "Triangel ist bei jedem einzigen Treffen des Chors dabei.", "tp": "N"},
                {"external_id": 913, "de": "singen (sang - gesungen)", "ar": "يغني",
                 "ex": "Wann haben Sie zuletzt gesungen?", "tp": "V"},
                {"external_id": 914, "de": "Die Gedanken sind frei.", "ar": "الأفكار حرة. (أغنية شعبية)",
                 "ex": "Ein Volkslied von 1810.", "tp": "N"},
                {"external_id": 915, "de": "zeitlos", "ar": "خالد / أبدي",
                 "ex": "Volkslieder sind eigentlich zeitlos.", "tp": "Adj"},
                {"external_id": 916, "de": "Mach dir mal keine Gedanken.", "ar": "لا تقلق.",
                 "ex": "Gut gesagt: Redewendungen mit 'Gedanken'.", "tp": "Redewendung"},
            ]
        },
        {
            "name_de": "Bildungszentrum — Kurse",
            "name_ar": "مركز التعليم — الدورات",
            "icon": "📚",
            "order_index": 2,
            "vocab": [
                {"external_id": 917, "de": "der Schwerpunkt (-e)", "ar": "محور التركيز",
                 "ex": "Das Bildungszentrum hat einen neuen Schwerpunkt.", "tp": "N"},
                {"external_id": 918, "de": "das Upcycling", "ar": "إعادة التدوير الإبداعية",
                 "ex": "Aus alt mach neu: Upcycling mit Viktor Mair.", "tp": "N"},
                {"external_id": 919, "de": "kreativ", "ar": "مبدع",
                 "ex": "Sind Sie gern kreativ?", "tp": "Adj"},
                {"external_id": 920, "de": "die Erfahrung (-en)", "ar": "الخبرة / التجربة",
                 "ex": "Sie brauchen keine große Erfahrung mitzubringen.", "tp": "N"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Drei Gespräche über ein Kunstwerk",
            "situation_de": "Drei Personen kommentieren das Bild von Heimrad Prem.",
            "lines": [
                {"speaker": "A", "text_de": "Das Bild gefällt mir total gut. Die Farben sind so lebendig!", "text_ar": "اللوحة تعجبني كثيراً. الألوان حيّة جداً!"},
                {"speaker": "B", "text_de": "Wirklich? Ich finde es ziemlich durcheinander.", "text_ar": "حقاً؟ أجدها فوضوية نوعاً ما."},
                {"speaker": "C", "text_de": "Ich bin begeistert! Der Künstler drückt so viel aus.", "text_ar": "أنا متحمس! الفنان يعبّر عن الكثير."},
                {"speaker": "A", "text_de": "Das sehe ich auch so. Mich spricht es wirklich an.", "text_ar": "أرى هذا أيضاً. إنها تستأثر باهتمامي حقاً."},
                {"speaker": "B", "text_de": "Hmm, ich finde das eher langweilig. Nicht wirklich mein Stil.", "text_ar": "هممم، أجدها مملة نوعاً ما. ليست أسلوبي حقاً."},
                {"speaker": "C", "text_de": "Das ist wirklich Geschmackssache!", "text_ar": "هذا مسألة ذوق حقاً!"},
            ]
        },
    ],
    "redemittel": {
        "Kunstwerke bewerten": [
            {"de": "Das Bild / die Skulptur gefällt mir (total / wirklich) gut.", "ar": "اللوحة / التمثال يعجبني (كثيراً / حقاً)."},
            {"de": "Das finde ich wirklich super / toll.", "ar": "أجد هذا رائعاً حقاً."},
            {"de": "Ich bin (total) begeistert.", "ar": "أنا (كثيراً) متحمس."},
            {"de": "Das finde ich eher langweilig / uninteressant.", "ar": "أجد هذا مملاً / غير مثير للاهتمام."},
            {"de": "Das spricht mich (eigentlich) nicht an.", "ar": "هذا لا يستأثر باهتمامي (في الواقع)."},
            {"de": "Das ist (wirklich) nichts für mich.", "ar": "هذا (حقاً) ليس من ذوقي."},
        ],
        "nachfragen": [
            {"de": "Was meinen Sie / meinst du mit ...?", "ar": "ماذا تقصد بـ ...؟"},
            {"de": "Können Sie das bitte erklären?", "ar": "هل يمكنك شرح ذلك؟"},
            {"de": "Das habe ich nicht ganz verstanden.", "ar": "لم أفهم ذلك تماماً."},
        ],
    }
}


# ═══════════════════════════════════════════════════════════
# تحديث ALL_KAPITEL
# ═══════════════════════════════════════════════════════════

ALL_KAPITEL = {
    1: KAP_1,
    2: KAP_2,
    3: KAP_3,
    4: KAP_4,
    5: KAP_5,
    6: KAP_6,
    7: KAP_7,
    8: KAP_8,
    9: KAP_9,
    # 10-12 ستضاف لاحقاً
}
# ═══════════════════════════════════════════════════════════
# Kapitel 10: Miteinander
# ═══════════════════════════════════════════════════════════

KAP_10 = {
    "number": 10,
    "title_de": "Miteinander",
    "title_ar": "مع بعضنا",
    "icon": "🤲",
    "description_de": "Soziales Engagement und Mini-München",
    "description_ar": "العمل الاجتماعي التطوعي وميني ميونخ",
    "grammar_focus": "Passiv Präsens/Präteritum/Perfekt | Passiv mit Modalverb",
    "page_start": 98,
    "page_end": 107,
    "themen": [
        {
            "name_de": "Soziales Engagement",
            "name_ar": "العمل الاجتماعي التطوعي",
            "icon": "❤️",
            "order_index": 0,
            "vocab": [
                {"external_id": 1001, "de": "die Tafel (-n)", "ar": "جمعية توزيع الغذاء",
                 "ex": "Die erste deutsche Tafel wurde 1993 in Berlin gegründet.", "tp": "N"},
                {"external_id": 1002, "de": "die Lebensmittel (Pl.)", "ar": "المواد الغذائية",
                 "ex": "Die Tafel verteilt Lebensmittel an Bedürftige.", "tp": "N"},
                {"external_id": 1003, "de": "spenden", "ar": "يتبرع",
                 "ex": "Firmen spenden viele Lebensmittel.", "tp": "V"},
                {"external_id": 1004, "de": "verteilen", "ar": "يوزع",
                 "ex": "Die Lebensmittel werden verteilt.", "tp": "V"},
                {"external_id": 1005, "de": "gründen", "ar": "يُؤسّس",
                 "ex": "Das Konzept wurde aus den USA übernommen.", "tp": "V"},
                {"external_id": 1006, "de": "unterstützen", "ar": "يدعم / يساند",
                 "ex": "60.000 Helfer/innen unterstützen die Organisation.", "tp": "V"},
                {"external_id": 1007, "de": "freiwillig", "ar": "طوعي / تطوعي",
                 "ex": "Ich engagiere mich freiwillig.", "tp": "Adj"},
            ]
        },
        {
            "name_de": "Mini-München — Stadt",
            "name_ar": "ميني ميونخ — المدينة",
            "icon": "🏙️",
            "order_index": 1,
            "vocab": [
                {"external_id": 1008, "de": "die Müllabfuhr", "ar": "خدمة جمع القمامة",
                 "ex": "Die Müllabfuhr leert die Mülltonnen.", "tp": "N"},
                {"external_id": 1009, "de": "das Einwohnermeldeamt", "ar": "مكتب تسجيل السكان",
                 "ex": "Wer teilnehmen möchte, meldet sich beim Einwohnermeldeamt an.", "tp": "N"},
                {"external_id": 1010, "de": "der Bürgermeister (-)", "ar": "رئيس البلدية",
                 "ex": "Die Bürger wählen den Bürgermeister.", "tp": "N"},
                {"external_id": 1011, "de": "die Behörde (-n)", "ar": "الجهة الحكومية",
                 "ex": "Die Behörde ist für die Genehmigungen zuständig.", "tp": "N"},
                {"external_id": 1012, "de": "zuständig sein für", "ar": "مسؤول عن",
                 "ex": "Wer ist für das Reinigen der Straßen zuständig?", "tp": "Ausdruck"},
                {"external_id": 1013, "de": "sich anmelden", "ar": "يُسجّل نفسه",
                 "ex": "Man meldet sich beim Einwohnermeldeamt an.", "tp": "V"},
            ]
        },
        {
            "name_de": "Europa & Politik",
            "name_ar": "أوروبا والسياسة",
            "icon": "🇪🇺",
            "order_index": 2,
            "vocab": [
                {"external_id": 1014, "de": "die EU / Europäische Union", "ar": "الاتحاد الأوروبي",
                 "ex": "Deutschland ist Mitglied der EU.", "tp": "N"},
                {"external_id": 1015, "de": "die Institution (-en)", "ar": "المؤسسة",
                 "ex": "Über Institutionen in der Stadt sprechen.", "tp": "N"},
                {"external_id": 1016, "de": "die Präsentation (-en)", "ar": "العرض / التقديم",
                 "ex": "Tipps für eine gute Präsentation.", "tp": "N"},
                {"external_id": 1017, "de": "das Projekt (-e)", "ar": "المشروع",
                 "ex": "Das Projekt 'Mini-München' ist sehr erfolgreich.", "tp": "N"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Über ein soziales Projekt berichten",
            "situation_de": "Schüler/innen präsentieren das Projekt 'Mini-München'.",
            "lines": [
                {"speaker": "S", "text_de": "Guten Tag! Wir möchten Ihnen heute das Projekt 'Mini-München' vorstellen.", "text_ar": "مساء الخير! نريد اليوم تقديم مشروع 'ميني ميونخ' لكم."},
                {"speaker": "S", "text_de": "Mini-München ist eine Spielstadt für Kinder zwischen 7 und 15 Jahren.", "text_ar": "ميني ميونخ مدينة لعب للأطفال بين 7 و15 سنة."},
                {"speaker": "S", "text_de": "Die Kinder organisieren ihre Stadt selbst: Es gibt Polizei, Bäckerei, Bank, Rathaus...", "text_ar": "يُنظّم الأطفال مدينتهم بأنفسهم: يوجد شرطة، مخبز، بنك، بلدية..."},
                {"speaker": "Z", "text_de": "Das klingt interessant! Wie wird das Projekt finanziert?", "text_ar": "يبدو هذا مثيراً! كيف يُموّل المشروع؟"},
                {"speaker": "S", "text_de": "Das Projekt wird von der Stadt München finanziert.", "text_ar": "يُموّل المشروع من مدينة ميونخ."},
                {"speaker": "Z", "text_de": "Seit wann gibt es Mini-München?", "text_ar": "منذ متى يوجد ميني ميونخ؟"},
                {"speaker": "S", "text_de": "Das Projekt wurde vor 30 Jahren gegründet und ist sehr erfolgreich.", "text_ar": "أُسّس المشروع منذ 30 عاماً وهو ناجح جداً."},
            ]
        },
    ],
    "redemittel": {
        "eine Präsentation halten": [
            {"de": "Ich möchte Ihnen / euch heute ... vorstellen.", "ar": "أودّ تقديم ... لكم اليوم."},
            {"de": "Mein Thema ist ...", "ar": "موضوعي هو ..."},
            {"de": "Erstens ... / Zweitens ... / Schließlich ...", "ar": "أولاً ... / ثانياً ... / وأخيراً ..."},
            {"de": "Ich komme jetzt zu meinem nächsten Punkt.", "ar": "أنتقل الآن إلى نقطتي التالية."},
            {"de": "Zusammenfassend kann man sagen, dass ...", "ar": "باختصار يمكن القول أن ..."},
            {"de": "Haben Sie noch Fragen?", "ar": "هل لديكم أسئلة؟"},
        ],
        "über Institutionen sprechen": [
            {"de": "Wer ist für ... zuständig?", "ar": "من المسؤول عن ...؟"},
            {"de": "Die ... kümmert sich um ...", "ar": "الـ ... تُعنى بـ ..."},
            {"de": "Man kann sich bei ... anmelden.", "ar": "يمكن التسجيل في ..."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 11: Stadt, Land, Fluss
# ═══════════════════════════════════════════════════════════

KAP_11 = {
    "number": 11,
    "title_de": "Stadt, Land, Fluss",
    "title_ar": "مدينة ريف نهر",
    "icon": "🏙️",
    "description_de": "Stadt, Verkehr und Adjektive als Nomen",
    "description_ar": "المدينة، المرور، والصفة كاسم",
    "grammar_focus": "irgendein/-welche | Adjektive als Nomen | Relativsätze was/wo",
    "page_start": 108,
    "page_end": 117,
    "themen": [
        {
            "name_de": "Stadt & Verkehr",
            "name_ar": "المدينة والمرور",
            "icon": "🚦",
            "order_index": 0,
            "vocab": [
                {"external_id": 1101, "de": "der Verkehr (kein Pl.)", "ar": "حركة المرور",
                 "ex": "Der Verkehr in der Stadt ist oft ein Problem.", "tp": "N"},
                {"external_id": 1102, "de": "das Reinigungsfahrzeug (-e)", "ar": "سيارة النظافة",
                 "ex": "Das große Reinigungsfahrzeug macht sich auf den Weg.", "tp": "N"},
                {"external_id": 1103, "de": "die Schicht (-en)", "ar": "الوردية / الدوام",
                 "ex": "Um 7:00 Uhr ist seine Schicht zu Ende.", "tp": "N"},
                {"external_id": 1104, "de": "der Nachtdienst (-e)", "ar": "الوردية الليلية",
                 "ex": "Ferdy hat heute Nachtdienst.", "tp": "N"},
                {"external_id": 1105, "de": "die Bäckerei (-en)", "ar": "المخبز",
                 "ex": "Die Bäckerei beginnt um 2 Uhr.", "tp": "N"},
                {"external_id": 1106, "de": "liefern", "ar": "يوصّل",
                 "ex": "Die Fahrerin lädt das Brot und liefert es.", "tp": "V"},
                {"external_id": 1107, "de": "lebenswert", "ar": "يستحق العيش فيه",
                 "ex": "Was macht eine Stadt lebenswert?", "tp": "Adj"},
            ]
        },
        {
            "name_de": "Adjektive als Nomen",
            "name_ar": "الصفة كاسم",
            "icon": "📝",
            "order_index": 1,
            "vocab": [
                {"external_id": 1108, "de": "der/ein Obdachlose (-n)", "ar": "المشرد / مشرد",
                 "ex": "Der Obdachlose schläft im Bauhof.", "tp": "Adj.als.N"},
                {"external_id": 1109, "de": "der/ein Jugendliche (-n)", "ar": "الشاب / شاب",
                 "ex": "Er betreut Jugendliche in seiner Arbeit.", "tp": "Adj.als.N"},
                {"external_id": 1110, "de": "der/ein Angestellte (-n)", "ar": "الموظف / موظف",
                 "ex": "Nick ist Angestellter bei der Stadt.", "tp": "Adj.als.N"},
                {"external_id": 1111, "de": "der/ein Bekannte (-n)", "ar": "المعروف / معروف",
                 "ex": "Nick, ein Bekannter von mir, ist Angestellter.", "tp": "Adj.als.N"},
                {"external_id": 1112, "de": "der/ein Verwandte (-n)", "ar": "القريب / قريب",
                 "ex": "Ich habe mit einer Verwandten gesprochen.", "tp": "Adj.als.N"},
                {"external_id": 1113, "de": "irgendein/-e/-welche", "ar": "بعض / أي (غير محدد)",
                 "ex": "Haben Sie irgendwelche Fragen?", "tp": "Pronomen"},
            ]
        },
        {
            "name_de": "Städte — Leipzig & Zürich",
            "name_ar": "مدن — لايبزيغ وزيوريخ",
            "icon": "🌆",
            "order_index": 2,
            "vocab": [
                {"external_id": 1114, "de": "Leipzig", "ar": "لايبزيغ (مدينة في ألمانيا)",
                 "ex": "Leipzig ist bekannt für seine Musikszene.", "tp": "Eigenname"},
                {"external_id": 1115, "de": "Zürich", "ar": "زيوريخ (مدينة في سويسرا)",
                 "ex": "Zürich ist eine lebenswerte Stadt.", "tp": "Eigenname"},
                {"external_id": 1116, "de": "der Bericht (-e)", "ar": "التقرير",
                 "ex": "Einen Bericht über die Stadt schreiben.", "tp": "N"},
                {"external_id": 1117, "de": "vermitteln", "ar": "يتوسط / ينقل",
                 "ex": "In einer Diskussion vermitteln.", "tp": "V"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Briefe/E-Mails schreiben — Stadtbesuch",
            "situation_de": "Anna schreibt an verschiedene Empfänger über ihren Stadtbesuch.",
            "lines": [
                {"speaker": "A1", "text_de": "Liebe Julia! Ich bin jetzt in Leipzig und es gefällt mir sehr gut. Die Innenstadt ist wunderschön!", "text_ar": "عزيزتي يوليا! أنا الآن في لايبزيغ وأعجبتني كثيراً. وسط المدينة جميل جداً!"},
                {"speaker": "A2", "text_de": "Sehr geehrte Damen und Herren, ich möchte ein Programm für meinen Stadtbesuch erstellen.", "text_ar": "السادة الأفاضل، أودّ إعداد برنامج لزيارتي للمدينة."},
                {"speaker": "A2", "text_de": "Könnten Sie mir bitte Informationen über Sehenswürdigkeiten schicken?", "text_ar": "هل يمكنكم إرسال معلومات عن المعالم السياحية؟"},
                {"speaker": "A1", "text_de": "Gestern war ich in der Nikolaikirche. Die ist so schön! Kommst du mich besuchen?", "text_ar": "كنت أمس في كنيسة نيكولاي. جميلة جداً! هل ستأتي لزيارتي؟"},
            ]
        },
    ],
    "redemittel": {
        "formeller Brief / E-Mail": [
            {"de": "Sehr geehrte Damen und Herren,", "ar": "السادة الأفاضل،"},
            {"de": "Sehr geehrte/r Frau/Herr ...,", "ar": "السيدة/السيد العزيزة/العزيز ...،"},
            {"de": "Ich schreibe Ihnen, weil ...", "ar": "أكتب إليكم لأن ..."},
            {"de": "Mit freundlichen Grüßen", "ar": "مع خالص التحيات"},
        ],
        "informeller Brief": [
            {"de": "Liebe/r ...,", "ar": "عزيزي/عزيزتي ...،"},
            {"de": "Ich schreibe dir, weil ...", "ar": "أكتب إليك لأن ..."},
            {"de": "Viele Grüße / Liebe Grüße", "ar": "مع أطيب التحيات"},
        ],
        "in einer Diskussion vermitteln": [
            {"de": "Ich verstehe beide Seiten.", "ar": "أفهم كلا الجانبين."},
            {"de": "Einerseits ... andererseits ...", "ar": "من جهة ... ومن جهة أخرى ..."},
            {"de": "Ich glaube, wir können einen Kompromiss finden.", "ar": "أعتقد أننا نستطيع إيجاد حل وسط."},
        ],
    }
}
# ═══════════════════════════════════════════════════════════
# Kapitel 12: Geld regiert die Welt?
# ═══════════════════════════════════════════════════════════

KAP_12 = {
    "number": 12,
    "title_de": "Geld regiert die Welt?",
    "title_ar": "المال يحكم العالم؟",
    "icon": "💰",
    "description_de": "Bank, Geld, Globalisierung und Tauschring",
    "description_ar": "البنك، المال، العولمة، ونادي المقايضة",
    "grammar_focus": "je...desto/umso | Partizip II als Adj | Partizip I als Adj",
    "page_start": 118,
    "page_end": 127,
    "themen": [
        {
            "name_de": "Bank & Geld",
            "name_ar": "البنك والمال",
            "icon": "🏦",
            "order_index": 0,
            "vocab": [
                {"external_id": 1201, "de": "die Überweisung (-en)", "ar": "التحويل المصرفي",
                 "ex": "Überweisungen im Inland sind kostenlos.", "tp": "N"},
                {"external_id": 1202, "de": "das Konto (Konten)", "ar": "الحساب البنكي",
                 "ex": "Wie kann ich mein Konto öffnen?", "tp": "N"},
                {"external_id": 1203, "de": "der Dauerauftrag (-aufträge)", "ar": "أمر الدفع الدائم",
                 "ex": "Ich zahle die Miete per Dauerauftrag.", "tp": "N"},
                {"external_id": 1204, "de": "einzahlen", "ar": "يودع / يضع في البنك",
                 "ex": "Sie können Bargeld einzahlen.", "tp": "V"},
                {"external_id": 1205, "de": "überweisen", "ar": "يُحوّل (مبلغاً)",
                 "ex": "Ich überweise das Geld sofort.", "tp": "V"},
                {"external_id": 1206, "de": "sperren", "ar": "يحجب / يوقف",
                 "ex": "Lassen Sie Ihre Karte sofort sperren!", "tp": "V"},
                {"external_id": 1207, "de": "das Formular (-e)", "ar": "الاستمارة / النموذج",
                 "ex": "Füllen Sie das Formular aus und unterschreiben Sie es.", "tp": "N"},
            ]
        },
        {
            "name_de": "Globalisierung",
            "name_ar": "العولمة",
            "icon": "🌐",
            "order_index": 1,
            "vocab": [
                {"external_id": 1208, "de": "die Globalisierung", "ar": "العولمة",
                 "ex": "Ich sehe die Globalisierung eher kritisch.", "tp": "N"},
                {"external_id": 1209, "de": "profitieren (von)", "ar": "يستفيد من",
                 "ex": "Viele Länder profitieren von der Globalisierung.", "tp": "V"},
                {"external_id": 1210, "de": "der Wohlstand", "ar": "الرخاء",
                 "ex": "Durch die Globalisierung gibt es mehr Wohlstand.", "tp": "N"},
                {"external_id": 1211, "de": "sinkende Preise", "ar": "أسعار متراجعة (Partizip I)",
                 "ex": "Sinkende Preise = Preise, die sinken.", "tp": "Part.I"},
                {"external_id": 1212, "de": "steigende Preise", "ar": "أسعار متصاعدة (Partizip I)",
                 "ex": "Steigende Preise = Preise, die steigen.", "tp": "Part.I"},
                {"external_id": 1213, "de": "der überwiesene Betrag", "ar": "المبلغ المحوَّل (Partizip II)",
                 "ex": "Der überwiesene Betrag kommt innerhalb eines Tages an.", "tp": "Part.II"},
                {"external_id": 1214, "de": "die gespeicherte PIN", "ar": "رمز PIN المحفوظ (Partizip II)",
                 "ex": "Eine gespeicherte PIN können Sie jederzeit ändern.", "tp": "Part.II"},
            ]
        },
        {
            "name_de": "Tauschring",
            "name_ar": "نادي المقايضة",
            "icon": "🔄",
            "order_index": 2,
            "vocab": [
                {"external_id": 1215, "de": "der Tauschring (-e)", "ar": "نادي المقايضة",
                 "ex": "Im Tauschring tauscht man Dienste und Fähigkeiten.", "tp": "N"},
                {"external_id": 1216, "de": "tauschen", "ar": "يتبادل",
                 "ex": "Ich tausche Nachhilfe gegen Handwerksarbeit.", "tp": "V"},
                {"external_id": 1217, "de": "berichten (über)", "ar": "يُبلّغ / يروي",
                 "ex": "Über seine Erfahrungen berichten.", "tp": "V"},
                {"external_id": 1218, "de": "je mehr ... desto/umso günstiger", "ar": "كلما زاد ... كلما أصبح أرخص",
                 "ex": "Je mehr Konkurrenz, desto günstiger die Produkte.", "tp": "Konnektor"},
            ]
        },
    ],
    "dialoge": [
        {
            "title_de": "Pro und Contra Globalisierung",
            "situation_de": "Bernd und Sada haben unterschiedliche Meinungen.",
            "lines": [
                {"speaker": "B", "text_de": "Ich finde es gut, dass unser Leben internationaler geworden ist.", "text_ar": "أجد أنه من الجيد أن حياتنا أصبحت أكثر دولية."},
                {"speaker": "S", "text_de": "Ich sehe die Globalisierung eher kritisch. Viele Arbeitsplätze gehen verloren.", "text_ar": "أرى العولمة بعين ناقدة. كثير من الوظائف تُفقد."},
                {"speaker": "B", "text_de": "Aber es gibt auch positive Aspekte: billigere Produkte, mehr Wohlstand.", "text_ar": "لكن هناك أيضاً جوانب إيجابية: منتجات أرخص، رخاء أكبر."},
                {"speaker": "S", "text_de": "Ein Nachteil ist, dass die Unterschiede zwischen Arm und Reich immer größer werden.", "text_ar": "عيب هو أن الفجوة بين الغني والفقير تكبر باستمرار."},
                {"speaker": "B", "text_de": "Das stimmt. Aber je mehr Länder zusammenarbeiten, desto besser können wir Probleme lösen.", "text_ar": "هذا صحيح. لكن كلما تعاونت دول أكثر كلما استطعنا حل المشاكل بشكل أفضل."},
                {"speaker": "S", "text_de": "Pauschal kann man sagen: Es gibt überzeugende Argumente für beide Seiten.", "text_ar": "بشكل عام يمكن القول: هناك حجج مقنعة لكلا الجانبين."},
            ]
        },
        {
            "title_de": "Online-Banking — Fragen und Antworten",
            "situation_de": "Ein Kunde stellt Fragen zum Online-Banking.",
            "lines": [
                {"speaker": "K", "text_de": "Wie kann ich mich einloggen?", "text_ar": "كيف يمكنني تسجيل الدخول؟"},
                {"speaker": "A", "text_de": "Sie haben gesicherten Zugang über unsere Webseite oder App mit Benutzernamen und Passwort.", "text_ar": "لديك وصول آمن عبر موقعنا أو التطبيق باسم المستخدم وكلمة المرور."},
                {"speaker": "K", "text_de": "Wie kann ich meine PIN ändern?", "text_ar": "كيف يمكنني تغيير رمز PIN؟"},
                {"speaker": "A", "text_de": "Eine gespeicherte PIN können Sie jederzeit ändern, wenn Sie eingeloggt sind.", "text_ar": "يمكنك تغيير رمز PIN المحفوظ في أي وقت عند تسجيل الدخول."},
                {"speaker": "K", "text_de": "Was passiert, wenn ich meine Karte verliere?", "text_ar": "ماذا يحدث إذا فقدت بطاقتي؟"},
                {"speaker": "A", "text_de": "Lassen Sie Ihre Karte sofort sperren und melden Sie uns den Verlust.", "text_ar": "أوقف بطاقتك فوراً وأبلغنا بالخسارة."},
            ]
        },
    ],
    "redemittel": {
        "Argumente äußern": [
            {"de": "Ein Vorteil ist, dass ...", "ar": "ميزة هي أن ..."},
            {"de": "Ein Nachteil ist, dass ...", "ar": "عيب هو أن ..."},
            {"de": "Einerseits ... andererseits ...", "ar": "من جهة ... ومن جهة أخرى ..."},
            {"de": "Je mehr ... desto / umso ...", "ar": "كلما زاد ... كلما ..."},
            {"de": "Pauschal kann man sagen, dass ...", "ar": "بشكل عام يمكن القول أن ..."},
        ],
        "in Diskussionen zu Wort kommen": [
            {"de": "Darf ich kurz etwas sagen?", "ar": "هل يمكنني قول شيء باختصار؟"},
            {"de": "Ich möchte noch etwas hinzufügen.", "ar": "أريد إضافة شيء."},
            {"de": "Entschuldigung, ich bin noch nicht fertig.", "ar": "عذراً، لم أنتهِ بعد."},
            {"de": "Was meinen Sie dazu?", "ar": "ما رأيك في ذلك؟"},
        ],
    }
}


# ═══════════════════════════════════════════════════════════
# 🎉 ALL_KAPITEL الكامل - 12 Kapitel
# ═══════════════════════════════════════════════════════════

ALL_KAPITEL = {
    1: KAP_1,
    2: KAP_2,
    3: KAP_3,
    4: KAP_4,
    5: KAP_5,
    6: KAP_6,
    7: KAP_7,
    8: KAP_8,
    9: KAP_9,
    10: KAP_10,
    11: KAP_11,
    12: KAP_12,
}