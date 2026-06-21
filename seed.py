"""سكربت تعبئة قاعدة البيانات - Goethe B1 Ultimate."""
import json
import sys
import os

# إضافة المسار الرئيسي
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app.models import (
    db, User, Chapter, Topic, Vocabulary, Dialogue, DialogueLine,
    Grammar, UsefulPhrase, Exercise, SchreibenTask, Achievement
)
from data.kapitel import ALL_KAPITEL
from data.grammar import GRAMMAR
from data.quiz import QUIZ
from data.schreiben import SW_TASKS


def seed():
    app = create_app()
    with app.app_context():
        print("🗑️  تنظيف قاعدة البيانات...")
        db.drop_all()
        db.create_all()

        # ==================== المستخدم التجريبي ====================
        print("👤 إنشاء مستخدم تجريبي...")
        demo = User(
            username='demo',
            email='demo@goethe-b1.app',
            full_name='طالب تجريبي',
            xp=120,
            streak_days=3
        )
        demo.set_password('demo1234')
        db.session.add(demo)
        db.session.flush()

        # ==================== الفصول (Chapters) ====================
        print("📚 إنشاء الفصول الـ 12...")
        chapters_map = {}
        
        for k_num, k_data in ALL_KAPITEL.items():
            chapter = Chapter(
                number=k_num,
                title_de=k_data['title_de'],
                title_ar=k_data['title_ar'],
                icon=k_data['icon'],
                description_de=k_data.get('description_de', ''),
                description_ar=k_data.get('description_ar', ''),
                grammar_focus=k_data.get('grammar_focus', ''),
                page_start=k_data.get('page_start'),
                page_end=k_data.get('page_end'),
            )
            db.session.add(chapter)
            db.session.flush()
            chapters_map[k_num] = chapter
            print(f"   ✓ Kapitel {k_num}: {k_data['title_de']}")

        # ==================== المواضيع والمفردات ====================
        print("📖 إنشاء المواضيع والمفردات...")
        total_vocab = 0
        
        for k_num, k_data in ALL_KAPITEL.items():
            chapter = chapters_map[k_num]
            
            for t_idx, thema in enumerate(k_data['themen']):
                topic = Topic(
                    chapter_id=chapter.id,
                    name_de=thema['name_de'],
                    name_ar=thema['name_ar'],
                    icon=thema.get('icon', '📁'),
                    order_index=t_idx,
                )
                db.session.add(topic)
                db.session.flush()

                # المفردات
                for vocab_data in thema['vocab']:
                    vocab = Vocabulary(
                        topic_id=topic.id,
                        external_id=vocab_data['external_id'],
                        word_de=vocab_data['de'],
                        translation_ar=vocab_data['ar'],
                        example_de=vocab_data.get('ex', ''),
                        word_type=vocab_data.get('tp', 'N'),
                        difficulty=1,
                    )
                    db.session.add(vocab)
                    total_vocab += 1

        # ==================== الحوارات ====================
        print("💬 إنشاء الحوارات...")
        total_dialogs = 0
        total_lines = 0
        
        for k_num, k_data in ALL_KAPITEL.items():
            chapter = chapters_map[k_num]
            topics = Topic.query.filter_by(chapter_id=chapter.id).order_by(Topic.order_index).all()
            
            for d_idx, dialog_data in enumerate(k_data['dialoge']):
                topic = topics[d_idx % len(topics)] if topics else None
                
                dialogue = Dialogue(
                    topic_id=topic.id if topic else None,
                    title_de=dialog_data['title_de'],
                    title_ar=dialog_data.get('title_ar', ''),
                    situation_de=dialog_data.get('situation_de', ''),
                    situation_ar=dialog_data.get('situation_ar', ''),
                )
                db.session.add(dialogue)
                db.session.flush()
                total_dialogs += 1

                # سطور الحوار
                for l_idx, line_data in enumerate(dialog_data['lines']):
                    line = DialogueLine(
                        dialogue_id=dialogue.id,
                        line_index=l_idx,
                        speaker=line_data['speaker'],
                        text_de=line_data['text_de'],
                        text_ar=line_data['text_ar'],
                    )
                    db.session.add(line)
                    total_lines += 1

        # ==================== Redemittel ====================
        print("💡 إنشاء Redemittel...")
        total_phrases = 0
        
        for k_num, k_data in ALL_KAPITEL.items():
            chapter = chapters_map[k_num]
            
            for category, phrases in k_data.get('redemittel', {}).items():
                for phrase_data in phrases:
                    phrase = UsefulPhrase(
                        chapter_id=chapter.id,
                        category=category,
                        phrase_de=phrase_data['de'],
                        phrase_ar=phrase_data['ar'],
                    )
                    db.session.add(phrase)
                    total_phrases += 1

        # ==================== القواعد (Grammar) ====================
        print("📐 إنشاء القواعد النحوية...")
        
        for g_data in GRAMMAR:
            chapter = chapters_map.get(g_data['k'])
            if not chapter:
                continue
                
            grammar = Grammar(
                id=g_data['id'],
                chapter_id=chapter.id,
                title_de=g_data['title_de'],
                title_ar=g_data['title_ar'],
                explanation=g_data.get('explanation', ''),
                table_json=json.dumps(g_data.get('table')),
                examples_json=json.dumps(g_data.get('examples', [])),
                tip=g_data.get('tip'),
                order_index=g_data.get('order_index', 0),
            )
            db.session.add(grammar)

        # ==================== الكويز (Quiz) ====================
        print("📝 إنشاء أسئلة الكويز...")
        
        for q_data in QUIZ:
            chapter = chapters_map.get(q_data['k'])
            if not chapter:
                continue
            
            exercise = Exercise(
                chapter_id=chapter.id,
                skill='grammatik',
                question_type='multiple_choice',
                question_de=q_data['q'],
                options_json=json.dumps(q_data['opts']),
                correct_index=q_data['cor'],
                explanation=q_data.get('exp', ''),
                difficulty=q_data.get('difficulty', 1),
            )
            db.session.add(exercise)

        # ==================== مهام الكتابة ====================
        print("✍️ إنشاء مهام الكتابة...")
        
        for sw_data in SW_TASKS:
            chapter = chapters_map.get(sw_data.get('chapter_id', 1))
            
            task = SchreibenTask(
                id=sw_data['id'],
                title=sw_data['title_de'],
                typ=sw_data.get('typ', ''),
                situation=sw_data.get('situation_de', ''),
                min_words=sw_data.get('min_words', 80),
                tips_json=json.dumps(sw_data.get('tips', [])),
                criteria_json=json.dumps(sw_data.get('criteria', [])),
                chapter_id=chapter.id if chapter else None,
            )
            db.session.add(task)

        # ==================== الإنجازات (Achievements) ====================
        print("🏆 إنشاء نظام الإنجازات...")
        
        achievements = [
            {"id": "first_word", "title": "أول كلمة", "description": "حفظ أول كلمة", "icon": "🌱", "xp_reward": 10, "condition_type": "words_count", "condition_value": 1},
            {"id": "first_kapitel", "title": "أول فصل", "description": "إكمال أول فصل", "icon": "📘", "xp_reward": 50, "condition_type": "kapitel_done", "condition_value": 1},
            {"id": "streak_7", "title": "أسبوع متواصل", "description": "7 أيام متتالية", "icon": "🔥", "xp_reward": 100, "condition_type": "streak", "condition_value": 7},
            {"id": "words_100", "title": "100 كلمة", "description": "حفظ 100 كلمة", "icon": "💯", "xp_reward": 200, "condition_type": "words_count", "condition_value": 100},
            {"id": "words_500", "title": "500 كلمة", "description": "حفظ 500 كلمة", "icon": "🏆", "xp_reward": 500, "condition_type": "words_count", "condition_value": 500},
            {"id": "all_kapitel", "title": "كل الفصول", "description": "إكمال كل الفصول", "icon": "🎓", "xp_reward": 1000, "condition_type": "kapitel_done", "condition_value": 12},
            {"id": "perfect_quiz", "title": "كويز مثالي", "description": "20 إجابة صحيحة متتالية", "icon": "⭐", "xp_reward": 150, "condition_type": "quiz_streak", "condition_value": 20},
            {"id": "writing_master", "title": "كاتب ماهر", "description": "إكمال 4 مهام كتابة", "icon": "✍️", "xp_reward": 200, "condition_type": "writing_done", "condition_value": 4},
        ]
        
        for ach_data in achievements:
            achievement = Achievement(
                id=ach_data['id'],
                title=ach_data['title'],
                description=ach_data.get('description', ''),
                icon=ach_data.get('icon', '🏆'),
                xp_reward=ach_data.get('xp_reward', 50),
                condition_type=ach_data.get('condition_type', ''),
                condition_value=ach_data.get('condition_value', 0),
            )
            db.session.add(achievement)

        # ==================== الحفظ النهائي ====================
        print("💾 حفظ البيانات...")
        db.session.commit()

        # ==================== الإحصائيات ====================
        print("\n" + "="*60)
        print("✅ تم بنجاح!")
        print("="*60)
        print(f"📊 الإحصائيات النهائية:")
        print(f"   • الفصول: {Chapter.query.count()}")
        print(f"   • المواضيع: {Topic.query.count()}")
        print(f"   • المفردات: {Vocabulary.query.count()}")
        print(f"   • الحوارات: {Dialogue.query.count()}")
        print(f"   • سطور الحوار: {DialogueLine.query.count()}")
        print(f"   • Redemittel: {UsefulPhrase.query.count()}")
        print(f"   • القواعد: {Grammar.query.count()}")
        print(f"   • أسئلة الكويز: {Exercise.query.count()}")
        print(f"   • مهام الكتابة: {SchreibenTask.query.count()}")
        print(f"   • الإنجازات: {Achievement.query.count()}")
        print(f"   • المستخدمين: {User.query.count()}")
        print("="*60)


if __name__ == '__main__':
    seed()