# 🎓 Goethe B1 Prep

تطبيق ويب للتحضير لامتحان Goethe B1 مبني على منهاج **Netzwerk neu B1**.

## ✨ الميزات

- 📚 12 Kapitel من المنهج كاملاً
- 🎯 محاكاة امتحان Goethe B1 (Lesen, Hören, Schreiben, Sprechen)
- 🃏 بطاقات مفردات ذكية (Flashcards)
- 📐 شرح القواعد بالعربي
- 💬 حوارات كاملة مع الترجمة
- 🔥 نظام Streak + XP للتحفيز
- 👤 نظام مستخدمين مع حفظ التقدم

## 🚀 التشغيل على جهازك

### المتطلبات
- Python 3.10 أو أحدث
- pip (يأتي مع Python)

### الخطوات

```bash
# 1) فك ضغط الملف أو ادخل للمجلد
cd goethe_b1

# 2) أنشئ بيئة افتراضية
python3 -m venv venv

# 3) فعّلها
# على Linux/Mac:
source venv/bin/activate
# على Windows:
venv\Scripts\activate

# 4) ثبّت المكتبات
pip install -r requirements.txt

# 5) عبّي قاعدة البيانات
python seed.py

# 6) شغّل التطبيق
python run.py
```

بعدها افتح المتصفح على:
**http://localhost:5000**

### 🔑 حساب تجريبي
- اسم المستخدم: `demo`
- كلمة المرور: `demo1234`

## 📁 هيكل المشروع

```
goethe_b1/
├── app/
│   ├── __init__.py        # تهيئة Flask
│   ├── models.py          # نماذج قاعدة البيانات
│   ├── routes/            # صفحات التطبيق
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── chapter.py
│   │   └── practice.py
│   └── templates/         # قوالب HTML
├── instance/
│   └── goethe_b1.db       # قاعدة البيانات SQLite
├── seed.py                # تعبئة قاعدة البيانات
├── run.py                 # نقطة الدخول
└── requirements.txt
```

## 🌐 النشر على الإنترنت (مجاني)

### الخيار 1: Render.com (أسهل)
1. ارفع المشروع على GitHub
2. ادخل render.com واربط الـ repo
3. اختر "Web Service" + Python
4. Build: `pip install -r requirements.txt`
5. Start: `python seed.py && python run.py`

### الخيار 2: PythonAnywhere
1. سجّل حساب مجاني في pythonanywhere.com
2. ارفع الملفات
3. أنشئ Web App جديد

## 📝 الترخيص

التطبيق للاستخدام التعليمي الشخصي. مبني كمساعد تعليمي لكتاب Netzwerk neu B1 من Klett Sprachen.

---
🤖 مبني بمساعدة Mavis AI
