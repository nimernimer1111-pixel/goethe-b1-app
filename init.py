"""تهيئة تطبيق Flask - Goethe B1 Ultimate."""
import os
from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from .models import db, User


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'الرجاء تسجيل الدخول أولاً'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    
    # إعدادات الأمان
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-change-in-prod'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///goethe_b1.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False  # لدعم العربية
    
    # تهيئة الامتدادات
    db.init_app(app)
    login_manager.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})  # للربط مع Frontend
    
    # تسجيل الـ Blueprints
    from .routes.auth import auth_bp
    from .routes.main import main_bp
    from .routes.chapters import chapters_bp
    from .routes.practice import practice_bp
    from .routes.ai import ai_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(chapters_bp, url_prefix='/api/chapters')
    app.register_blueprint(practice_bp, url_prefix='/api/practice')
    app.register_blueprint(ai_bp, url_prefix='/api/ai')
    
    # إنشاء الجداول
    with app.app_context():
        db.create_all()
    
    return app