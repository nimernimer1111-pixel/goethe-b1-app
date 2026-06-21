"""مسارات الذكاء الاصطناعي - AI Routes (Claude)."""
import os
import json
import requests
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

ai_bp = Blueprint('ai', __name__)

# مفتاح API من متغيرات البيئة
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
CLAUDE_MODEL = "claude-sonnet-4-6"
CLAUDE_URL = "https://api.anthropic.com/v1/messages"


SYSTEM_PROMPT = """أنت معلم لغة ألمانية متخصص في إعداد طلاب B1 لامتحان Goethe B1.
- تجيب بالعربية (مفاهيم) والألمانية (مصطلحات وأمثلة)
- تستخدم منهاج Netzwerk neu B1
- تساعد في القواعد والمفردات والكتابة والمحادثة
- ردودك واضحة ومختصرة مع أمثلة عملية"""


def call_claude(user_message, context=""):
    """استدعاء Claude API."""
    if not ANTHROPIC_API_KEY:
        return "⚠️ مفتاح API غير متوفر. أضف ANTHROPIC_API_KEY في البيئة."
    
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    full_message = f"{context}\n\n{user_message}" if context else user_message
    
    payload = {
        "model": CLAUDE_MODEL,
        "max_tokens": 1000,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": full_message}]
    }
    
    try:
        response = requests.post(CLAUDE_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data['content'][0]['text']
    except Exception as e:
        return f"⚠️ خطأ في الاتصال: {str(e)}"


@ai_bp.route('/ask', methods=['POST'])
@login_required
def ask_ai():
    """سؤال عام للـ AI."""
    data = request.get_json()
    question = data.get('question', '').strip()
    
    if not question:
        return jsonify({'error': 'السؤال فارغ'}), 400
    
    answer = call_claude(question)
    current_user.add_xp(5)  # مكافأة على الاستخدام
    
    from ..models import db
    db.session.commit()
    
    return jsonify({
        'question': question,
        'answer': answer,
        'xp_gained': 5
    }), 200


@ai_bp.route('/grammar', methods=['POST'])
@login_required
def explain_grammar():
    """شرح قاعدة نحوية."""
    data = request.get_json()
    topic = data.get('topic', '').strip()
    
    if not topic:
        return jsonify({'error': 'الموضوع فارغ'}), 400
    
    prompt = f"""اشرح القاعدة النحوية التالية لمستوى B1:
الموضوع: {topic}

قدم:
1. شرح بسيط بالعربية
2. القاعدة الأساسية بالألمانية
3. 3 أمثلة مع الترجمة العربية
4. نصيحة للحفظ
5. أخطاء شائعة يجب تجنبها"""
    
    answer = call_claude(prompt)
    current_user.add_xp(10)
    
    from ..models import db
    db.session.commit()
    
    return jsonify({
        'topic': topic,
        'explanation': answer,
        'xp_gained': 10
    }), 200


@ai_bp.route('/writing-feedback', methods=['POST'])
@login_required
def writing_feedback():
    """ملاحظات على نص ألماني."""
    data = request.get_json()
    text = data.get('text', '').strip()
    level = data.get('level', 'B1')
    
    if not text or len(text) < 20:
        return jsonify({'error': 'النص قصير جداً'}), 400
    
    prompt = f"""راجع النص الألماني التالي لطالب مستوى {level}:

النص: "{text}"

قدم:
1. ✅ ما هو جيد
2. ⚠️ أخطاء نحوية أو إملائية (صححها)
3. 💡 اقتراحات لتحسين الأسلوب
4. 📊 تقييم من 10
5. 🎯 نصيحة للتطوير"""
    
    answer = call_claude(prompt)
    current_user.add_xp(15)
    
    from ..models import db
    db.session.commit()
    
    return jsonify({
        'feedback': answer,
        'xp_gained': 15
    }), 200


@ai_bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    """ترجمة مع شرح."""
    data = request.get_json()
    text = data.get('text', '').strip()
    direction = data.get('direction', 'de-ar')  # de-ar or ar-de
    
    if not text:
        return jsonify({'error': 'النص فارغ'}), 400
    
    if direction == 'de-ar':
        prompt = f"""ترجم الجملة الألمانية التالية إلى العربية:
"{text}"

قدم:
- الترجمة الطبيعية
- شرح الكلمات الصعبة
- ملاحظات نحوية إن وجدت"""
    else:
        prompt = f"""ترجم الجملة العربية التالية إلى الألمانية (مستوى B1):
"{text}"

قدم:
- الترجمة الألمانية
- النطق التقريبي بالعربية
- شرح القواعد المستخدمة"""
    
    answer = call_claude(prompt)
    current_user.add_xp(5)
    
    from ..models import db
    db.session.commit()
    
    return jsonify({
        'text': text,
        'direction': direction,
        'result': answer
    }), 200