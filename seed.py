"""سكربت تعبئة قاعدة البيانات بالبيانات الأولية.

يشمل:
- Kapitel 1 بالكامل (من JSON النموذجي اللي بعثه المستخدم)
- عناوين Kapitel 2-12 (المستخرجة من الـ OCR)
- مستخدم تجريبي للاختبار
"""
import json
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app.models import (
    db, User, Chapter, Topic, Vocabulary, Dialogue, DialogueLine,
    Grammar, UsefulPhrase
)

# ============================================================
# Kapitel 1 - "Gute Reise!" (محتوى كامل من نموذج المستخدم)
# ============================================================

KAPITEL_1_DATA = {
    "kapitel": 1,
    "title_de": "Gute Reise!",
    "title_ar": "رحلة سعيدة!",
    "icon": "✈️",
    "themen": [
        {
            "thema_de": "Urlaubsarten",
            "thema_ar": "أنواع الإجازات",
            "icon": "🏖️",
            "vocab": [
                {"de": "der Pauschalurlaub", "ar": "إجازة شاملة (كل شيء مدفوع)", "ex": "Im letzten Sommer haben wir einen Pauschalurlaub in der Türkei gemacht.", "type": "Nomen", "plural": "die Pauschalurlaube"},
                {"de": "die Pauschalreise", "ar": "رحلة شاملة", "ex": "Eine Pauschalreise ist oft günstiger als Einzelbuchungen.", "type": "Nomen", "plural": "die Pauschalreisen"},
                {"de": "der Aktivurlaub", "ar": "إجازة النشاط والحركة", "ex": "Ich mache gern Aktivurlaub in den Bergen.", "type": "Nomen", "plural": "die Aktivurlaube"},
                {"de": "der Bildungsurlaub", "ar": "إجازة تعليمية", "ex": "Mein Chef gibt mir Bildungsurlaub für einen Sprachkurs.", "type": "Nomen", "plural": "die Bildungsurlaube"},
                {"de": "der Kultururlaub", "ar": "إجازة ثقافية", "ex": "Ein Kultururlaub in Italien wäre toll!", "type": "Nomen", "plural": "die Kultururlaube"},
                {"de": "der Strandurlaub", "ar": "إجازة شاطئية", "ex": "Strandurlaub ist sehr entspannend.", "type": "Nomen", "plural": "die Strandurlaube"},
                {"de": "der Familienurlaub", "ar": "إجازة عائلية", "ex": "Wir planen einen Familienurlaub in Spanien.", "type": "Nomen", "plural": "die Familienurlaube"},
                {"de": "der Kurzurlaub", "ar": "إجازة قصيرة (ويك إند)", "ex": "Nächste Woche fahren wir für einen Kurzurlaub nach München.", "type": "Nomen", "plural": "die Kurzurlaube"},
            ],
        },
        {
            "thema_de": "Reiseplanung",
            "thema_ar": "التخطيط للرحلة",
            "icon": "🗺️",
            "vocab": [
                {"de": "buchen (bucht - buchte - gebucht)", "ar": "يحجز", "ex": "Ich möchte ein Zimmer im Hotel buchen.", "type": "Verb", "conjugation": "buchen - bucht - buchte - hat gebucht"},
                {"de": "reservieren", "ar": "يحجز مسبقاً", "ex": "Haben Sie einen Tisch für zwei Personen reserviert?", "type": "Verb", "conjugation": "reservieren - reserviert - reservierte - hat reserviert"},
                {"de": "vorbestellen", "ar": "يطلب مسبقاً", "ex": "Kann ich die Tickets vorbestellen?", "type": "Verb", "conjugation": "vorbestellen - bestellt vor - bestellte vor - hat vorbestellt"},
                {"de": "die Buchung (-en)", "ar": "الحجز", "ex": "Die Buchung des Fluges war einfach.", "type": "Nomen", "plural": "die Buchungen"},
                {"de": "die Reservierung", "ar": "الحجز المسبق", "ex": "Ich möchte eine Reservierung für morgen.", "type": "Nomen", "plural": "die Reservierungen"},
                {"de": "der Vorschlag (Vorschläge)", "ar": "الاقتراح", "ex": "Hast du einen guten Vorschlag für den Urlaub?", "type": "Nomen", "plural": "die Vorschläge"},
                {"de": "die Reisebegleitung", "ar": "مرافق الرحلة", "ex": "Mein Bruder ist meine Reisebegleitung.", "type": "Nomen", "plural": "die Reisebegleitungen"},
                {"de": "der Reiseführer (-)", "ar": "دليل السفر / المرشد السياحي", "ex": "Der Reiseführer hat uns viel erzählt.", "type": "Nomen", "plural": "die Reiseführer"},
                {"de": "die Sehenswürdigkeit (-en)", "ar": "معلم سياحي", "ex": "Das Brandenburger Tor ist eine berühmte Sehenswürdigkeit.", "type": "Nomen", "plural": "die Sehenswürdigkeiten"},
                {"de": "die Besichtigung (-en)", "ar": "الزيارة / المعاينة", "ex": "Die Besichtigung des Museums dauert zwei Stunden.", "type": "Nomen", "plural": "die Besichtigungen"},
                {"de": "die Stadtrundfahrt", "ar": "جولة في المدينة", "ex": "Wir machen eine Stadtrundfahrt mit dem Bus.", "type": "Nomen", "plural": "die Stadtrundfahrten"},
                {"de": "die Wanderung (-en)", "ar": "رحلة مشي / تنزه", "ex": "Am Sonntag machen wir eine Wanderung im Wald.", "type": "Nomen", "plural": "die Wanderungen"},
            ],
        },
        {
            "thema_de": "Transport",
            "thema_ar": "وسائل النقل",
            "icon": "🚆",
            "vocab": [
                {"de": "der Flug (Flüge)", "ar": "رحلة الطيران", "ex": "Der Flug von Berlin nach Madrid dauert drei Stunden.", "type": "Nomen", "plural": "die Flüge"},
                {"de": "der Linienflug", "ar": "رحلة مجدولة (خط منتظم)", "ex": "Ich nehme einen Linienflug nach Wien.", "type": "Nomen", "plural": "die Linienflüge"},
                {"de": "der Charterflug", "ar": "رحلة مستأجرة", "ex": "Charterflüge sind oft günstiger als Linienflüge.", "type": "Nomen", "plural": "die Charterflüge"},
                {"de": "die Abfahrt", "ar": "المغادرة", "ex": "Die Abfahrt des Zuges ist um 8 Uhr.", "type": "Nomen", "plural": "die Abfahrten"},
                {"de": "die Ankunft", "ar": "الوصول", "ex": "Die Ankunft in Hamburg war pünktlich.", "type": "Nomen", "plural": "die Ankünfte"},
                {"de": "die Verspätung", "ar": "التأخير", "ex": "Der Zug hat leider 30 Minuten Verspätung.", "type": "Nomen", "plural": "die Verspätungen"},
                {"de": "verpassen", "ar": "يفوّت", "ex": "Ich habe meinen Bus verpasst.", "type": "Verb", "conjugation": "verpassen - verpasst - verpasste - hat verpasst"},
                {"de": "umsteigen", "ar": "يغيّر وسيلة النقل", "ex": "In Frankfurt müssen wir umsteigen.", "type": "Verb", "conjugation": "umsteigen - steigt um - stieg um - ist umgestiegen"},
                {"de": "der Anschluss (Anschlüsse)", "ar": "الربط / الوسيلة التالية", "ex": "Ich habe meinen Anschluss verpasst.", "type": "Nomen", "plural": "die Anschlüsse"},
                {"de": "die Fahrkarte (-n)", "ar": "تذكرة السفر", "ex": "Haben Sie schon eine Fahrkarte gekauft?", "type": "Nomen", "plural": "die Fahrkarten"},
                {"de": "das Ticket (-s)", "ar": "التذكرة", "ex": "Das Ticket kostet 25 Euro.", "type": "Nomen", "plural": "die Tickets"},
                {"de": "die Hin- und Rückfahrt", "ar": "الذهاب والعودة", "ex": "Eine Hin- und Rückfahrt kostet 60 Euro.", "type": "Nomen", "plural": "die Hin- und Rückfahrten"},
                {"de": "der Aufenthalt", "ar": "الإقامة", "ex": "Der Aufenthalt in Paris war wunderschön.", "type": "Nomen", "plural": "die Aufenthalte"},
            ],
        },
        {
            "thema_de": "Unterkunft",
            "thema_ar": "الإقامة",
            "icon": "🏨",
            "vocab": [
                {"de": "das Hotel (-s)", "ar": "الفندق", "ex": "Das Hotel liegt direkt am Strand.", "type": "Nomen", "plural": "die Hotels"},
                {"de": "die Pension (-en)", "ar": "بيت الضيافة", "ex": "Wir übernachten in einer kleinen Pension.", "type": "Nomen", "plural": "die Pensionen"},
                {"de": "die Jugendherberge (-n)", "ar": "بيت الشباب", "ex": "Die Jugendherberge ist sehr günstig.", "type": "Nomen", "plural": "die Jugendherbergen"},
                {"de": "die Ferienwohnung (-en)", "ar": "شقة العطلة", "ex": "Wir haben eine Ferienwohnung in Italien gemietet.", "type": "Nomen", "plural": "die Ferienwohnungen"},
                {"de": "das Gästezimmer (-)", "ar": "غرفة الضيوف", "ex": "Kann ich ein Gästezimmer haben?", "type": "Nomen", "plural": "die Gästezimmer"},
                {"de": "das Einzelzimmer", "ar": "غرفة فردية", "ex": "Ich hätte gern ein Einzelzimmer mit Frühstück.", "type": "Nomen", "plural": "die Einzelzimmer"},
                {"de": "das Doppelzimmer", "ar": "غرفة مزدوجة", "ex": "Ein Doppelzimmer bitte, mit Blick auf das Meer.", "type": "Nomen", "plural": "die Doppelzimmer"},
                {"de": "das Mehrbettzimmer", "ar": "غرفة متعددة الأسرّة", "ex": "Das Mehrbettzimmer ist günstiger.", "type": "Nomen", "plural": "die Mehrbettzimmer"},
                {"de": "das Frühstück", "ar": "الإفطار", "ex": "Das Frühstück ist im Preis inklusive.", "type": "Nomen", "plural": "die Frühstücke"},
                {"de": "die Halbpension", "ar": "نصف إقامة (إفطار + عشاء)", "ex": "Ich habe Halbpension gebucht.", "type": "Nomen", "plural": "die Halbpensionen"},
                {"de": "die Vollpension", "ar": "إقامة كاملة (3 وجبات)", "ex": "Vollpension ist sehr bequem im Urlaub.", "type": "Nomen", "plural": "die Vollpensionen"},
                {"de": "die Übernachtung (-en)", "ar": "المبيت / ليلة", "ex": "Die Übernachtung kostet 80 Euro.", "type": "Nomen", "plural": "die Übernachtungen"},
                {"de": "die Rezeption", "ar": "الاستقبال", "ex": "An der Rezeption können Sie einchecken.", "type": "Nomen", "plural": "die Rezeptionen"},
            ],
        },
    ],
    "dialoge": [
        {
            "title_de": "Dialog 1: Im Reisebüro",
            "title_ar": "في مكتب السفر",
            "situation_de": "Anna geht zum Reisebüro, um einen Urlaub zu buchen.",
            "situation_ar": "Anna تروح لمكتب السفر لتحجز إجازة.",
            "lines": [
                {"sprecher": "R", "text_de": "Guten Tag! Was kann ich für Sie tun?", "text_ar": "مساء الخير! ماذا أستطيع أن أفعل لك؟"},
                {"sprecher": "K", "text_de": "Hallo! Ich möchte gern einen Urlaub buchen.", "text_ar": "مرحباً! أودّ حجز إجازة."},
                {"sprecher": "R", "text_de": "Wohin möchten Sie denn reisen? Und wann?", "text_ar": "إلى أين تريد السفر؟ ومتى؟"},
                {"sprecher": "K", "text_de": "Ich würde gern im August nach Spanien fahren. Für zwei Wochen.", "text_ar": "أودّ السفر إلى إسبانيا في أغسطس. لمدة أسبوعين."},
                {"sprecher": "R", "text_de": "Haben Sie eine bestimmte Region im Sinn?", "text_ar": "هل لديك منطقة معينة في ذهنك؟"},
                {"sprecher": "K", "text_de": "Ja, am liebsten an die Costa del Sol. Ich mag Strandurlaub.", "text_ar": "نعم، أفضل ساحل الشمس. أحب الإجازات الشاطئية."},
                {"sprecher": "R", "text_de": "Gut. Möchten Sie ein Hotel oder eine Ferienwohnung?", "text_ar": "حسناً. هل تريد فندقاً أم شقة؟"},
                {"sprecher": "K", "text_de": "Ein Hotel mit Halbpension wäre schön. Und nicht zu teuer, bitte.", "text_ar": "فندق مع نصف إقامة (إفطار + عشاء) سيكون جميلاً. وغير مكلف من فضلك."},
                {"sprecher": "R", "text_de": "Ich habe hier ein tolles Angebot: 7 Nächte im Drei-Sterne-Hotel mit Frühstück für 850 Euro pro Person.", "text_ar": "لدي هنا عرض رائع: 7 ليالٍ في فندق 3 نجوم مع إفطار بـ 850 يورو للشخص."},
                {"sprecher": "K", "text_de": "Gibt es auch ein günstigeres Angebot?", "text_ar": "هل هناك عرض أرخص؟"},
                {"sprecher": "R", "text_de": "Ja, eine Pension in Strandnähe. 7 Nächte mit Frühstück für 550 Euro.", "text_ar": "نعم، بيت ضيافة قريب من الشاطئ. 7 ليالٍ مع إفطار بـ 550 يورو."},
                {"sprecher": "K", "text_de": "Das klingt gut! Kann ich es buchen?", "text_ar": "هذا يبدو جيداً! هل يمكنني حجزه؟"},
                {"sprecher": "R", "text_de": "Natürlich. Darf ich Ihren Ausweis sehen, bitte?", "text_ar": "بالتأكيد. هل يمكنني رؤية هويتك من فضلك؟"},
                {"sprecher": "K", "text_de": "Hier bitte.", "text_ar": "تفضل."},
                {"sprecher": "R", "text_de": "Danke. Hier ist Ihre Buchungsbestätigung. Gute Reise!", "text_ar": "شكراً. إليك تأكيد الحجز. رحلة سعيدة!"},
            ],
        },
        {
            "title_de": "Dialog 2: Am Bahnhof",
            "title_ar": "في محطة القطار",
            "situation_de": "Markus möchte eine Fahrkarte nach München kaufen.",
            "situation_ar": "Markus يريد شراء تذكرة قطار إلى ميونخ.",
            "lines": [
                {"sprecher": "K", "text_de": "Entschuldigung, ich möchte gern eine Fahrkarte nach München.", "text_ar": "عذراً، أود شراء تذكرة إلى ميونخ."},
                {"sprecher": "S", "text_de": "Einfache Fahrt oder Hin und Rückfahrt?", "text_ar": "ذهاب فقط أم ذهاب وعودة؟"},
                {"sprecher": "K", "text_de": "Hin und Rückfahrt, bitte. Für übermorgen.", "text_ar": "ذهاب وعودة، من فضلك. ليوم بعد غد."},
                {"sprecher": "S", "text_de": "Welche Klasse? Erste oder zweite?", "text_ar": "أي درجة؟ الأولى أم الثانية؟"},
                {"sprecher": "K", "text_de": "Zweite Klasse, bitte. Was kostet das?", "text_ar": "الدرجة الثانية، من فضلك. كم سعرها؟"},
                {"sprecher": "S", "text_de": "98 Euro. Möchten Sie auch eine Platzreservierung?", "text_ar": "98 يورو. هل تريد أيضاً حجز مقعد؟"},
                {"sprecher": "K", "text_de": "Ja, bitte. Am Fenster, wenn möglich.", "text_ar": "نعم، من فضلك. بجانب النافذة، إن أمكن."},
                {"sprecher": "S", "text_de": "Gut. Der Zug fährt um 14:30 Uhr von Gleis 7. Sie haben noch 20 Minuten Zeit.", "text_ar": "حسناً. القطار يغادر الساعة 14:30 من الرصيف 7. لديك 20 دقيقة."},
                {"sprecher": "K", "text_de": "Wann komme ich in München an?", "text_ar": "متى أصل إلى ميونخ؟"},
                {"sprecher": "S", "text_de": "Um 18:45 Uhr. Hier ist Ihre Fahrkarte. Gute Fahrt!", "text_ar": "الساعة 18:45. تذكرتك هنا. رحلة سعيدة!"},
                {"sprecher": "K", "text_de": "Danke schön! Auf Wiedersehen!", "text_ar": "شكراً جزيلاً! إلى اللقاء!"},
            ],
        },
        {
            "title_de": "Dialog 3: Im Hotel einchecken",
            "title_ar": "تسجيل الدخول في الفندق",
            "situation_de": "Familie Schmidt kommt im Hotel an.",
            "situation_ar": "عائلة Schmidt تصل إلى الفندق.",
            "lines": [
                {"sprecher": "R", "text_de": "Guten Abend! Haben Sie eine Reservierung?", "text_ar": "مساء الخير! هل لديكم حجز؟"},
                {"sprecher": "F", "text_de": "Ja, auf den Namen Schmidt. Wir haben ein Doppelzimmer und ein Einzelzimmer gebucht.", "text_ar": "نعم، باسم شميت. حجزنا غرفة مزدوجة وغرفة فردية."},
                {"sprecher": "R", "text_de": "Einen Moment bitte... Ja, hier ist es. Drei Nächte mit Frühstück, richtig?", "text_ar": "لحظة من فضلك... نعم، ها هو. ثلاث ليالٍ مع إفطار، صحيح؟"},
                {"sprecher": "F", "text_de": "Genau. Können wir bitte ein Zimmer mit Meerblick bekommen?", "text_ar": "بالضبط. هل يمكننا الحصول على غرفة تطل على البحر؟"},
                {"sprecher": "R", "text_de": "Es tut mir leid, alle Zimmer mit Meerblick sind belegt. Aber ich kann Ihnen ein Zimmer mit Seeblick anbieten.", "text_ar": "آسف، جميع الغرف المطلة على البحر محجوزة. لكن يمكنني تقديم غرفة تطل على البحيرة."},
                {"sprecher": "F", "text_de": "Das ist auch schön. Wann gibt es Frühstück?", "text_ar": "هذا جميل أيضاً. متى يقدم الإفطار؟"},
                {"sprecher": "R", "text_de": "Von 7 bis 10 Uhr im Restaurant im Erdgeschoss. Hier sind Ihre Schlüsselkarten. Zimmer 305 und 307.", "text_ar": "من 7 إلى 10 في المطعم بالطابق الأرضي. ها هي بطاقات المفاتيح. الغرفة 305 و307."},
                {"sprecher": "F", "text_de": "Vielen Dank! Gibt es WLAN im Zimmer?", "text_ar": "شكراً جزيلاً! هل هناك واي فاي في الغرفة؟"},
                {"sprecher": "R", "text_de": "Ja, das Passwort finden Sie auf dem Schreibtisch. Genießen Sie Ihren Aufenthalt!", "text_ar": "نعم، ستجد كلمة المرور على المكتب. استمتع بإقامتك!"},
            ],
        },
    ],
    "redemittel": {
        "im_reisebuero": [
            {"de": "Ich möchte einen Urlaub buchen.", "ar": "أودّ حجز إجازة."},
            {"de": "Haben Sie ein Angebot für...?", "ar": "هل لديكم عرض لـ...؟"},
            {"de": "Was kostet die Reise insgesamt?", "ar": "كم تكلفة الرحلة الإجمالية؟"},
            {"de": "Ist das Frühstück inklusive?", "ar": "هل الإفطار مشمول؟"},
            {"de": "Gibt es auch ein günstigeres Angebot?", "ar": "هل هناك عرض أرخص؟"},
            {"de": "Ich möchte gern stornieren.", "ar": "أودّ الإلغاء."},
            {"de": "Kann ich die Reise umbuchen?", "ar": "هل يمكنني تغيير الحجز؟"},
        ],
        "am_bahnhof": [
            {"de": "Wann fährt der nächste Zug nach...?", "ar": "متى يغادر القطار التالي إلى...؟"},
            {"de": "Von welchem Gleis fährt der Zug?", "ar": "من أي رصيف يغادر القطار؟"},
            {"de": "Wie lange dauert die Fahrt?", "ar": "كم تستغرق الرحلة؟"},
            {"de": "Muss ich umsteigen?", "ar": "هل يجب أن أغير القطار؟"},
            {"de": "Der Zug hat Verspätung.", "ar": "القطار متأخر."},
        ],
        "meinung": [
            {"de": "Ich finde Strandurlaub am besten.", "ar": "أجد الإجازة الشاطئية الأفضل."},
            {"de": "Mir ist es wichtig, dass...", "ar": "من المهم لي أن..."},
            {"de": "Ich reise am liebsten mit der Bahn.", "ar": "أفضل السفر بالقطار."},
            {"de": "Im Urlaub möchte ich mich erholen.", "ar": "في الإجازة أريد أن أرتاح."},
        ],
    },
    "grammatik": [
        {
            "title_de": "Infinitiv mit zu",
            "title_ar": "المصدر مع zu",
            "explanation_ar": "في الألمانية، نستخدم zu + مصدر الفعل بعد أفعال معينة مثل anfangen, aufhören, beginnen, hoffen, sich freuen, vergessen وغيرها. مثل: Ich freue mich, dich zu sehen.",
        },
        {
            "title_de": "Nebensatz mit weil",
            "title_ar": "الجملة السبببية مع weil",
            "explanation_ar": "نستخدم weil (لأن) للربط بين جملتين، والفعل يذهب للنهاية. مثل: Ich bleibe zu Hause, weil ich krank bin.",
        },
        {
            "title_de": "Nebensatz mit obwohl",
            "title_ar": "الجملة التناقضية مع obwohl",
            "explanation_ar": "نستخدم obwohl (بالرغم من) للتعبير عن تناقض. مثل: Obwohl es regnet, gehe ich spazieren.",
        },
        {
            "title_de": "Modalverben",
            "title_ar": "أفعال الحالة (können, müssen, wollen, sollen, dürfen, mögen)",
            "explanation_ar": "أفعال الحالة تعدّل المعنى الأساسي للفعل. الجملة: Ich kann Deutsch sprechen (أستطيع التحدث بالألمانية).",
        },
    ],
}

# ============================================================
# Kapitel 2-12 (عناوين فقط من الـ OCR)
# ============================================================

OTHER_CHAPTERS = [
    {"number": 2, "title_de": "Das ist ja praktisch!", "title_ar": "يا لها من عملية!", "icon": "🔧"},
    {"number": 3, "title_de": "Veränderungen", "title_ar": "التغييرات", "icon": "🔄"},
    {"number": 4, "title_de": "Arbeitswelt", "title_ar": "عالم العمل", "icon": "💼"},
    {"number": 5, "title_de": "Umweltfreundlich?", "title_ar": "صديق للبيئة؟", "icon": "🌱"},
    {"number": 6, "title_de": "Blick nach vorn", "title_ar": "نظرة نحو الأمام", "icon": "🚀"},
    {"number": 7, "title_de": "Beziehungen", "title_ar": "العلاقات", "icon": "❤️"},
    {"number": 8, "title_de": "Alltag und Konsum", "title_ar": "الحياة اليومية والاستهلاك", "icon": "🛒"},
    {"number": 9, "title_de": "Gesundheit und Fitness", "title_ar": "الصحة واللياقة", "icon": "🏃"},
    {"number": 10, "title_de": "Mobilität und Verkehr", "title_ar": "التنقل والمواصلات", "icon": "🚗"},
    {"number": 11, "title_de": "Medien und Technik", "title_ar": "الإعلام والتقنية", "icon": "📱"},
    {"number": 12, "title_de": "Feste und Feiern", "title_ar": "المناسبات والاحتفالات", "icon": "🎉"},
]


def seed():
    app = create_app()
    with app.app_context():
        print("🗑️  تنظيف قاعدة البيانات...")
        db.drop_all()
        db.create_all()

        print("👤 إنشاء مستخدم تجريبي...")
        demo = User(username='demo', email='demo@goethe-b1.app', full_name='طالب تجريبي')
        demo.set_password('demo1234')
        demo.xp = 120
        demo.streak_days = 3
        db.session.add(demo)

        print("📚 إنشاء Kapitel 1 مع المحتوى الكامل...")
        k1 = Chapter(
            number=KAPITEL_1_DATA['kapitel'],
            title_de=KAPITEL_1_DATA['title_de'],
            title_ar=KAPITEL_1_DATA['title_ar'],
            icon=KAPITEL_1_DATA['icon'],
            description_de='Reisen, Urlaubsplanung und Unterkunft',
            description_ar='السفر، تخطيط الإجازات، والإقامة',
            page_start=8,
            page_end=17,
        )
        db.session.add(k1)
        db.session.flush()

        # المواضيع
        for i, thema in enumerate(KAPITEL_1_DATA['themen']):
            topic = Topic(
                chapter_id=k1.id,
                name_de=thema['thema_de'],
                name_ar=thema['thema_ar'],
                icon=thema['icon'],
                order_index=i,
            )
            db.session.add(topic)
            db.session.flush()

            for v in thema['vocab']:
                db.session.add(Vocabulary(
                    topic_id=topic.id,
                    word_de=v['de'],
                    translation_ar=v['ar'],
                    example_de=v['ex'],
                    word_type=v['type'],
                    plural=v.get('plural'),
                    conjugation=v.get('conjugation'),
                    difficulty=1,
                ))

        # الحوارات
        all_topics = Topic.query.filter_by(chapter_id=k1.id).order_by(Topic.id).all()
        for i, dialog in enumerate(KAPITEL_1_DATA['dialoge']):
            topic_for_dialog = all_topics[i % len(all_topics)]
            d = Dialogue(
                topic_id=topic_for_dialog.id,
                title_de=dialog['title_de'],
                title_ar=dialog['title_ar'],
                situation_de=dialog.get('situation_de'),
                situation_ar=dialog.get('situation_ar'),
            )
            db.session.add(d)
            db.session.flush()

            for j, line in enumerate(dialog['lines']):
                db.session.add(DialogueLine(
                    dialogue_id=d.id,
                    line_index=j,
                    speaker=line['sprecher'],
                    text_de=line['text_de'],
                    text_ar=line['text_ar'],
                ))

        # Redemittel
        for cat, items in KAPITEL_1_DATA['redemittel'].items():
            for p in items:
                db.session.add(UsefulPhrase(
                    chapter_id=k1.id,
                    category=cat,
                    phrase_de=p['de'],
                    phrase_ar=p['ar'],
                ))

        # القواعد
        for i, g in enumerate(KAPITEL_1_DATA['grammatik']):
            db.session.add(Grammar(
                chapter_id=k1.id,
                title_de=g['title_de'],
                title_ar=g['title_ar'],
                explanation_ar=g['explanation_ar'],
                order_index=i,
            ))

        print(f"📖 إنشاء Kapitel 2-12 (عناوين فقط)...")
        for ch in OTHER_CHAPTERS:
            db.session.add(Chapter(
                number=ch['number'],
                title_de=ch['title_de'],
                title_ar=ch['title_ar'],
                icon=ch['icon'],
            ))

        db.session.commit()
        print("✅ تم بنجاح!")

        # إحصائيات
        n_chapters = Chapter.query.count()
        n_topics = Topic.query.count()
        n_vocab = Vocabulary.query.count()
        n_dialogues = Dialogue.query.count()
        n_lines = DialogueLine.query.count()
        n_grammar = Grammar.query.count()
        n_phrases = UsefulPhrase.query.count()
        print(f"\n📊 الإحصائيات:")
        print(f"   • Chapters: {n_chapters}")
        print(f"   • Topics: {n_topics}")
        print(f"   • Vocabulary: {n_vocab}")
        print(f"   • Dialogues: {n_dialogues}")
        print(f"   • Dialogue Lines: {n_lines}")
        print(f"   • Grammar Points: {n_grammar}")
        print(f"   • Useful Phrases: {n_phrases}")


if __name__ == '__main__':
    seed()
