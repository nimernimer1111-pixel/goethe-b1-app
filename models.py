"""نماذج قاعدة البيانات - Goethe B1 Ultimate."""
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """المستخدم / الطالب."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120))
    target_exam_date = db.Column(db.Date)
    level = db.Column(db.String(20), default='B1')
    daily_goal_minutes = db.Column(db.Integer, default=30)
    xp = db.Column(db.Integer, default=0)
    streak_days = db.Column(db.Integer, default=0)
    last_active = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    progress = db.relationship('Progress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    vocab_progress = db.relationship('VocabProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    exercise_attempts = db.relationship('ExerciseAttempt', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    achievements = db.relationship('UserAchievement', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    schreiben_submissions = db.relationship('SchreibenSubmission', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def add_xp(self, amount):
        self.xp += amount
        db.session.commit()
    
    def update_streak(self):
        today = datetime.utcnow().date()
        if self.last_active == today:
            return  # نفس اليوم
        elif self.last_active == today - timedelta(days=1):
            self.streak_days += 1
        else:
            self.streak_days = 1
        self.last_active = today
        db.session.commit()


class Chapter(db.Model):
    """الفصل (Kapitel)."""
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    title_de = db.Column(db.String(120), nullable=False)
    title_ar = db.Column(db.String(200), nullable=False)
    icon = db.Column(db.String(10))
    description_de = db.Column(db.Text)
    description_ar = db.Column(db.Text)
    grammar_focus = db.Column(db.String(300))  # 🆕 gr من JS
    page_start = db.Column(db.Integer)
    page_end = db.Column(db.Integer)

    topics = db.relationship('Topic', backref='chapter', lazy='dynamic',
                             order_by='Topic.order_index',
                             cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'title_de': self.title_de,
            'title_ar': self.title_ar,
            'icon': self.icon,
            'description_ar': self.description_ar,
            'grammar_focus': self.grammar_focus,
        }


class Topic(db.Model):
    """موضوع داخل الفصل."""
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    name_de = db.Column(db.String(120), nullable=False)
    name_ar = db.Column(db.String(200), nullable=False)
    icon = db.Column(db.String(10))
    order_index = db.Column(db.Integer, default=0)

    vocab = db.relationship('Vocabulary', backref='topic', lazy='dynamic',
                            cascade='all, delete-orphan')
    dialogues = db.relationship('Dialogue', backref='topic', lazy='dynamic',
                                cascade='all, delete-orphan')


class Vocabulary(db.Model):
    """كلمة أو عبارة مع ترجمتها ومثالها."""
    __tablename__ = 'vocabulary'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    # 🆕 external_id من JS
    external_id = db.Column(db.Integer, index=True)  
    word_de = db.Column(db.String(200), nullable=False)
    translation_ar = db.Column(db.String(300), nullable=False)
    example_de = db.Column(db.Text)
    word_type = db.Column(db.String(50))  # N, V, Adj, Ausdruck...
    audio_url = db.Column(db.String(300))
    difficulty = db.Column(db.Integer, default=1)
    
    def to_dict(self):
        return {
            'id': self.external_id or self.id,
            'de': self.word_de,
            'ar': self.translation_ar,
            'ex': self.example_de,
            'tp': self.word_type or 'N',
        }


class Dialogue(db.Model):
    """حوار."""
    __tablename__ = 'dialogues'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    title_de = db.Column(db.String(200))
    title_ar = db.Column(db.String(300))
    situation_de = db.Column(db.Text)
    situation_ar = db.Column(db.Text)

    lines = db.relationship('DialogueLine', backref='dialogue', lazy='dynamic',
                            order_by='DialogueLine.line_index',
                            cascade='all, delete-orphan')


class DialogueLine(db.Model):
    """سطر واحد في الحوار."""
    __tablename__ = 'dialogue_lines'
    id = db.Column(db.Integer, primary_key=True)
    dialogue_id = db.Column(db.Integer, db.ForeignKey('dialogues.id'), nullable=False)
    line_index = db.Column(db.Integer, nullable=False)
    speaker = db.Column(db.String(50))
    text_de = db.Column(db.Text, nullable=False)
    text_ar = db.Column(db.Text, nullable=False)
    audio_url = db.Column(db.String(300))


class Grammar(db.Model):
    """قاعدة نحوية."""
    __tablename__ = 'grammar'
    id = db.Column(db.String(20), primary_key=True)  # 🆕 g1, g2... من JS
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    title_de = db.Column(db.String(200), nullable=False)
    title_ar = db.Column(db.String(300), nullable=False)
    explanation = db.Column(db.Text)  # 🆕 من JS
    table_json = db.Column(db.Text)  # 🆕 JSON من JS
    examples_json = db.Column(db.Text)  # JSON
    tip = db.Column(db.Text)
    order_index = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        import json
        return {
            'id': self.id,
            'k': self.chapter_id,
            'title': self.title_de,
            'sub': self.title_ar,
            'explain': self.explanation,
            'table': json.loads(self.table_json) if self.table_json else None,
            'examples': json.loads(self.examples_json) if self.examples_json else [],
            'tip': self.tip,
        }


class UsefulPhrase(db.Model):
    """تعبير مفيد (Redemittel)."""
    __tablename__ = 'useful_phrases'
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    category = db.Column(db.String(100))
    phrase_de = db.Column(db.String(300), nullable=False)
    phrase_ar = db.Column(db.String(400), nullable=False)


class Exercise(db.Model):
    """تمرين (Quiz)."""
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    skill = db.Column(db.String(50))  # grammatik, wortschatz
    question_type = db.Column(db.String(50))  # multiple_choice, fill_blank
    question_de = db.Column(db.Text, nullable=False)
    options_json = db.Column(db.Text, nullable=False)  # JSON list
    correct_index = db.Column(db.Integer, nullable=False)
    explanation = db.Column(db.Text)
    difficulty = db.Column(db.Integer, default=1)
    
    def to_dict(self):
        import json
        return {
            'id': self.id,
            'k': self.chapter_id,
            'q': self.question_de,
            'opts': json.loads(self.options_json),
            'cor': self.correct_index,
            'exp': self.explanation,
        }


class SchreibenTask(db.Model):
    """مهمة كتابة."""
    __tablename__ = 'schreiben_tasks'
    id = db.Column(db.String(20), primary_key=True)  # 🆕 s1, s2... من JS
    title = db.Column(db.String(200), nullable=False)
    typ = db.Column(db.String(100))  # Formell | K1
    situation = db.Column(db.Text)
    min_words = db.Column(db.Integer, default=80)
    tips_json = db.Column(db.Text)  # JSON
    criteria_json = db.Column(db.Text)  # JSON
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))
    
    def to_dict(self):
        import json
        return {
            'id': self.id,
            'title': self.title,
            'typ': self.typ,
            'sit': self.situation,
            'min': self.min_words,
            'tips': json.loads(self.tips_json) if self.tips_json else [],
            'crit': json.loads(self.criteria_json) if self.criteria_json else [],
        }


class Progress(db.Model):
    """تقدم الطالب في الفصول."""
    __tablename__ = 'progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    status = db.Column(db.String(20), default='locked')
    completion_percent = db.Column(db.Integer, default=0)
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'chapter_id'),)


class VocabProgress(db.Model):
    """تقدم حفظ المفردات (Spaced Repetition - SM-2)."""
    __tablename__ = 'vocab_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    vocab_id = db.Column(db.Integer, db.ForeignKey('vocabulary.id'), nullable=False)
    times_seen = db.Column(db.Integer, default=0)
    times_correct = db.Column(db.Integer, default=0)
    times_wrong = db.Column(db.Integer, default=0)
    mastery_level = db.Column(db.Integer, default=0)  # 0..5
    interval_days = db.Column(db.Integer, default=0)
    next_review = db.Column(db.DateTime, default=datetime.utcnow)
    last_reviewed = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='new')  # new, known, review, hard
    
    __table_args__ = (db.UniqueConstraint('user_id', 'vocab_id'),)


class ExerciseAttempt(db.Model):
    """محاولة حل تمرين."""
    __tablename__ = 'exercise_attempts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    user_answer = db.Column(db.Integer)
    attempted_at = db.Column(db.DateTime, default=datetime.utcnow)


class SchreibenSubmission(db.Model):
    """تسليم مهمة كتابة."""
    __tablename__ = 'schreiben_submissions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task_id = db.Column(db.String(20), db.ForeignKey('schreiben_tasks.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    word_count = db.Column(db.Integer)
    criteria_met = db.Column(db.Text)  # JSON
    ai_feedback = db.Column(db.Text)  # 🆕 ملاحظات AI
    score = db.Column(db.Integer)  # 0-100
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)


class Achievement(db.Model):
    """الإنجازات."""
    __tablename__ = 'achievements'
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300))
    icon = db.Column(db.String(10))
    xp_reward = db.Column(db.Integer, default=50)
    condition_type = db.Column(db.String(50))  # words_count, streak, kapitel_done
    condition_value = db.Column(db.Integer)


class UserAchievement(db.Model):
    """الإنجازات المحققة."""
    __tablename__ = 'user_achievements'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    achievement_id = db.Column(db.String(50), db.ForeignKey('achievements.id'), nullable=False)
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'achievement_id'),)