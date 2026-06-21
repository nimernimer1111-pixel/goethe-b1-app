"""مسارات التدريب - Practice API."""
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
import json

from ..models import (
    db, User, Chapter, Vocabulary, VocabProgress, 
    Exercise, ExerciseAttempt, SchreibenTask, 
    SchreibenSubmission, Progress
)
from ..services.sm2 import sm2_update, get_due_vocabulary

practice_bp = Blueprint('practice', __name__)


# ═══════════════════════════════════════════════════════════
# FLASHCARDS - نظام المراجعة المتباعدة (SM-2)
# ═══════════════════════════════════════════════════════════

@practice_bp.route('/flashcard/due', methods=['GET'])
@login_required
def get_due_flashcards():
    """الحصول على الكلمات المستحقة للمراجعة."""
    chapter_id = request.args.get('chapter_id', type=int)
    limit = request.args.get('limit', 20, type=int)
    
    query = VocabProgress.query.join(Vocabulary).join(Topic).filter(
        VocabProgress.user_id == current_user.id,
        VocabProgress.next_review <= datetime.utcnow()
    )
    
    if chapter_id:
        query = query.filter(Topic.chapter_id == chapter_id)
    
    due_progress = query.order_by(VocabProgress.next_review).limit(limit).all()
    
    words = []
    for vp in due_progress:
        word_data = vp.vocab.to_dict()
        word_data['status'] = vp.status
        word_data['mastery_level'] = vp.mastery_level
        words.append(word_data)
    
    return jsonify({
        'count': len(words),
        'words': words
    }), 200


@practice_bp.route('/flashcard/answer', methods=['POST'])
@login_required
def answer_flashcard():
    """تسجيل إجابة البطاقة وتطبيق خوارزمية SM-2."""
    data = request.get_json()
    
    vocab_id = data.get('vocab_id')  # external_id من JS
    quality = data.get('quality', 0)  # 0-5
    
    if not vocab_id:
        return jsonify({'error': 'vocab_id مطلوب'}), 400
    
    # البحث عن الكلمة
    vocab = Vocabulary.query.filter_by(external_id=vocab_id).first()
    if not vocab:
        return jsonify({'error': 'الكلمة غير موجودة'}), 404
    
    # البحث عن التقدم أو إنشاؤه
    progress = VocabProgress.query.filter_by(
        user_id=current_user.id,
        vocab_id=vocab.id
    ).first()
    
    if not progress:
        progress = VocabProgress(
            user_id=current_user.id,
            vocab_id=vocab.id
        )
        db.session.add(progress)
    
    # تطبيق خوارزمية SM-2
    progress = sm2_update(progress, quality)
    
    # إضافة XP
    xp_gain = {0: 0, 1: 1, 2: 2, 3: 5, 4: 7, 5: 10}.get(quality, 0)
    current_user.add_xp(xp_gain)
    
    db.session.commit()
    
    return jsonify({
        'message': 'تم التحديث',
        'progress': {
            'mastery_level': progress.mastery_level,
            'status': progress.status,
            'next_review': progress.next_review.isoformat(),
            'interval_days': progress.interval_days,
        },
        'xp_gained': xp_gain,
        'total_xp': current_user.xp
    }), 200


@practice_bp.route('/flashcard/stats', methods=['GET'])
@login_required
def flashcard_stats():
    """إحصائيات البطاقات."""
    user_id = current_user.id
    
    total = VocabProgress.query.filter_by(user_id=user_id).count()
    known = VocabProgress.query.filter_by(user_id=user_id, status='known').count()
    review = VocabProgress.query.filter_by(user_id=user_id, status='review').count()
    hard = VocabProgress.query.filter_by(user_id=user_id, status='hard').count()
    due_now = VocabProgress.query.filter(
        user_id=user_id,
        next_review <= datetime.utcnow()
    ).count()
    
    return jsonify({
        'total_seen': total,
        'known': known,
        'review': review,
        'hard': hard,
        'due_now': due_now,
        'accuracy': (known / total * 100) if total > 0 else 0
    }), 200


# ═══════════════════════════════════════════════════════════
# QUIZ - الكويز
# ═══════════════════════════════════════════════════════════

@practice_bp.route('/quiz/questions', methods=['GET'])
@login_required
def get_quiz_questions():
    """الحصول على أسئلة الكويز."""
    chapter_id = request.args.get('chapter_id', type=int)
    limit = request.args.get('limit', 10, type=int)
    
    query = Exercise.query.filter_by(skill='grammatik')
    
    if chapter_id:
        query = query.filter_by(chapter_id=chapter_id)
    
    exercises = query.order_by(db.func.random()).limit(limit).all()
    
    return jsonify([{
        'id': ex.id,
        'k': ex.chapter_id,
        'q': ex.question_de,
        'opts': json.loads(ex.options_json),
        'difficulty': ex.difficulty,
    } for ex in exercises]), 200


@practice_bp.route('/quiz/submit', methods=['POST'])
@login_required
def submit_quiz():
    """تسليم إجابات الكويز."""
    data = request.get_json()
    answers = data.get('answers', [])  # [{exercise_id, user_choice}]
    
    if not answers:
        return jsonify({'error': 'لا توجد إجابات'}), 400
    
    results = []
    correct_count = 0
    xp_total = 0
    
    for ans in answers:
        ex_id = ans.get('exercise_id')
        user_choice = ans.get('user_choice')
        
        exercise = Exercise.query.get(ex_id)
        if not exercise:
            continue
        
        is_correct = (user_choice == exercise.correct_index)
        if is_correct:
            correct_count += 1
            xp_total += 10
        
        # حفظ المحاولة
        attempt = ExerciseAttempt(
            user_id=current_user.id,
            exercise_id=ex_id,
            is_correct=is_correct,
            user_answer=user_choice
        )
        db.session.add(attempt)
        
        results.append({
            'exercise_id': ex_id,
            'is_correct': is_correct,
            'correct_index': exercise.correct_index,
            'explanation': exercise.explanation,
        })
    
    current_user.add_xp(xp_total)
    db.session.commit()
    
    total = len(answers)
    accuracy = (correct_count / total * 100) if total > 0 else 0
    
    return jsonify({
        'total': total,
        'correct': correct_count,
        'accuracy': round(accuracy, 1),
        'xp_gained': xp_total,
        'total_xp': current_user.xp,
        'results': results
    }), 200


# ═══════════════════════════════════════════════════════════
# SCHREIBEN - الكتابة
# ═══════════════════════════════════════════════════════════

@practice_bp.route('/schreiben/tasks', methods=['GET'])
@login_required
def get_schreiben_tasks():
    """الحصول على مهام الكتابة."""
    tasks = SchreibenTask.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200


@practice_bp.route('/schreiben/task/<task_id>', methods=['GET'])
@login_required
def get_schreiben_task(task_id):
    """الحصول على مهمة كتابة محددة."""
    task = SchreibenTask.query.get_or_404(task_id)
    return jsonify(task.to_dict()), 200


@practice_bp.route('/schreiben/submit', methods=['POST'])
@login_required
def submit_schreiben():
    """تسليم مهمة كتابة."""
    data = request.get_json()
    
    task_id = data.get('task_id')
    text = data.get('text', '').strip()
    criteria = data.get('criteria', {})  # {0: true, 1: false, ...}
    
    if not task_id or not text:
        return jsonify({'error': 'بيانات ناقصة'}), 400
    
    task = SchreibenTask.query.get_or_404(task_id)
    
    # حساب عدد الكلمات
    word_count = len(text.split())
    min_words = task.min_words
    words_ok = word_count >= min_words
    
    # حساب النقاط من المعايير
    criteria_met = sum(1 for v in criteria.values() if v)
    total_criteria = len(criteria)
    criteria_score = (criteria_met / total_criteria * 100) if total_criteria > 0 else 0
    
    # النقاط النهائية
    score = round((criteria_score * 0.7) + (100 if words_ok else (word_count/min_words)*100 * 0.3), 1)
    score = min(score, 100)
    
    # إضافة XP
    xp_gained = int(score / 5)  # 20 نقطة لكل 100%
    current_user.add_xp(xp_gained)
    
    # حفظ التسليم
    submission = SchreibenSubmission(
        user_id=current_user.id,
        task_id=task_id,
        text=text,
        word_count=word_count,
        criteria_met=json.dumps(criteria),
        score=score,
    )
    db.session.add(submission)
    db.session.commit()
    
    return jsonify({
        'message': 'تم التسليم بنجاح!',
        'word_count': word_count,
        'min_words': min_words,
        'words_ok': words_ok,
        'score': score,
        'criteria_met': criteria_met,
        'total_criteria': total_criteria,
        'xp_gained': xp_gained,
        'total_xp': current_user.xp,
    }), 200


@practice_bp.route('/schreiben/history', methods=['GET'])
@login_required
def schreiben_history():
    """سجل التسليمات."""
    submissions = SchreibenSubmission.query.filter_by(
        user_id=current_user.id
    ).order_by(SchreibenSubmission.submitted_at.desc()).limit(20).all()
    
    return jsonify([{
        'id': s.id,
        'task_id': s.task_id,
        'word_count': s.word_count,
        'score': s.score,
        'submitted_at': s.submitted_at.isoformat(),
    } for s in submissions]), 200


# ═══════════════════════════════════════════════════════════
# PROGRESS - التقدم
# ═══════════════════════════════════════════════════════════

@practice_bp.route('/progress/overview', methods=['GET'])
@login_required
def progress_overview():
    """نظرة عامة على التقدم."""
    # إحصائيات المفردات
    vocab_total = Vocabulary.query.count()
    vocab_known = VocabProgress.query.filter_by(
        user_id=current_user.id, status='known'
    ).count()
    
    # إحصائيات الفصول
    chapters_total = Chapter.query.count()
    chapters_done = Progress.query.filter_by(
        user_id=current_user.id, status='completed'
    ).count()
    
    # إحصائيات الكويز
    quiz_attempts = ExerciseAttempt.query.filter_by(user_id=current_user.id).count()
    quiz_correct = ExerciseAttempt.query.filter_by(
        user_id=current_user.id, is_correct=True
    ).count()
    
    return jsonify({
        'user': {
            'username': current_user.username,
            'full_name': current_user.full_name,
            'xp': current_user.xp,
            'streak_days': current_user.streak_days,
            'level': current_user.level,
        },
        'vocabulary': {
            'total': vocab_total,
            'known': vocab_known,
            'progress_pct': round((vocab_known / vocab_total * 100), 1) if vocab_total else 0
        },
        'chapters': {
            'total': chapters_total,
            'completed': chapters_done,
            'progress_pct': round((chapters_done / chapters_total * 100), 1) if chapters_total else 0
        },
        'quiz': {
            'attempts': quiz_attempts,
            'correct': quiz_correct,
            'accuracy': round((quiz_correct / quiz_attempts * 100), 1) if quiz_attempts else 0
        }
    }), 200


@practice_bp.route('/progress/chapter/<int:number>/complete', methods=['POST'])
@login_required
def complete_chapter(number):
    """تحديد الفصل كمكتمل."""
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    
    progress = Progress.query.filter_by(
        user_id=current_user.id,
        chapter_id=chapter.id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            chapter_id=chapter.id,
            status='completed',
            completion_percent=100
        )
        db.session.add(progress)
    else:
        progress.status = 'completed'
        progress.completion_percent = 100
        progress.last_accessed = datetime.utcnow()
    
    # مكافأة XP
    current_user.add_xp(50)
    db.session.commit()
    
    return jsonify({
        'message': f'🎉 تهانينا! أكملت Kapitel {number}',
        'xp_gained': 50,
        'total_xp': current_user.xp,
    }), 200