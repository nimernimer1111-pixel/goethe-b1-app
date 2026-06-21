"""الصفحات الرئيسية: الرئيسية + لوحة التحكم + عرض الفصول."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import Chapter, Progress, db

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """الصفحة الرئيسية - عرض تعريفي."""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    """لوحة تحكم الطالب."""
    chapters = Chapter.query.order_by(Chapter.number).all()
    progress_map = {p.chapter_id: p for p in
                    Progress.query.filter_by(user_id=current_user.id).all()}

    stats = {
        'total_chapters': len(chapters),
        'completed': sum(1 for p in progress_map.values() if p.status == 'completed'),
        'in_progress': sum(1 for p in progress_map.values() if p.status == 'in_progress'),
        'xp': current_user.xp,
        'streak': current_user.streak_days,
    }
    return render_template('dashboard.html',
                           chapters=chapters,
                           progress=progress_map,
                           stats=stats)


@main_bp.route('/chapters')
@login_required
def chapter_list():
    """قائمة جميع الفصول."""
    chapters = Chapter.query.order_by(Chapter.number).all()
    return render_template('chapters.html', chapters=chapters)
