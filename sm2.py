"""خوارزمية SM-2 للمراجعة المتباعدة."""
from datetime import datetime, timedelta


def sm2_update(progress, quality):
    """
    تحديث تقدم الكلمة بناءً على خوارزمية SM-2.
    
    Args:
        progress: VocabProgress object
        quality: int (0-5)
            0 = نسيت تماماً
            1 = خطأ، لكن تذكرت بعد رؤيتها
            2 = خطأ، لكن سهل التذكر
            3 = صحيح بصعوبة
            4 = صحيح بعد تفكير
            5 = صحيح بسهولة
    
    Returns:
        Updated progress object
    """
    if quality < 3:
        # إعادة من الصفر
        progress.mastery_level = 0
        progress.interval_days = 1
        progress.status = 'hard' if quality < 2 else 'review'
    else:
        # زيادة المستوى
        if progress.mastery_level == 0:
            progress.interval_days = 1
        elif progress.mastery_level == 1:
            progress.interval_days = 6
        else:
            # الضرب في 2.5
            progress.interval_days = int(progress.interval_days * 2.5)
        progress.mastery_level += 1
        progress.status = 'known' if progress.mastery_level >= 3 else 'review'
    
    # تحديث الإحصائيات
    progress.times_seen += 1
    if quality >= 3:
        progress.times_correct += 1
    else:
        progress.times_wrong += 1
    
    # حساب موعد المراجعة القادم
    progress.last_reviewed = datetime.utcnow()
    progress.next_review = datetime.utcnow() + timedelta(days=progress.interval_days)
    
    return progress


def get_due_vocabulary(user_id, db_session, limit=20):
    """الحصول على الكلمات المستحقة للمراجعة."""
    from app.models import VocabProgress, Vocabulary
    
    now = datetime.utcnow()
    due = db_session.query(VocabProgress).join(Vocabulary).filter(
        VocabProgress.user_id == user_id,
        VocabProgress.next_review <= now
    ).order_by(VocabProgress.next_review).limit(limit).all()
    
    return [vp.vocab for vp in due]