"""مسارات المصادقة - Auth Routes."""
from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from ..models import db, User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    full_name = data.get('full_name', '').strip()
    
    if not username or not email or not password:
        return jsonify({'error': 'الرجاء إكمال جميع الحقول'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'اسم المستخدم موجود مسبقاً'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'البريد الإلكتروني مستخدم'}), 400
    
    user = User(username=username, email=email, full_name=full_name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    login_user(user)
    
    return jsonify({
        'message': f'أهلاً بك يا {full_name or username}! 🎉',
        'user': {'id': user.id, 'username': user.username, 'xp': user.xp, 'streak': user.streak_days}
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        login_user(user, remember=True)
        user.update_streak()
        
        return jsonify({
            'message': f'أهلاً بعودتك يا {user.full_name or user.username}! 👋',
            'user': {'id': user.id, 'username': user.username, 'xp': user.xp, 'streak': user.streak_days}
        }), 200
    
    return jsonify({'error': 'اسم المستخدم أو كلمة المرور غير صحيحة'}), 401


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'تم تسجيل خروجك. إلى اللقاء! 👋'}), 200


@auth_bp.route('/me', methods=['GET'])
@login_required
def get_current_user():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'email': current_user.email,
        'full_name': current_user.full_name,
        'xp': current_user.xp,
        'streak_days': current_user.streak_days,
        'level': current_user.level,
        'daily_goal_minutes': current_user.daily_goal_minutes,
    }), 200