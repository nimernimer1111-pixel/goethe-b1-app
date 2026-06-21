"""مسارات الفصول - Chapters API."""
from flask import Blueprint, jsonify
from flask_login import login_required
from ..models import db, Chapter, Topic, Vocabulary, Dialogue, DialogueLine, Grammar, UsefulPhrase
from data.kapitel import ALL_KAPITEL

chapters_bp = Blueprint('chapters', __name__)


@chapters_bp.route('', methods=['GET'])
@login_required
def get_all_chapters():
    chapters = Chapter.query.order_by(Chapter.number).all()
    return jsonify([{
        'id': ch.id,
        'number': ch.number,
        'title_de': ch.title_de,
        'title_ar': ch.title_ar,
        'icon': ch.icon,
        'description_ar': ch.description_ar,
        'grammar_focus': ch.grammar_focus,
    } for ch in chapters]), 200


@chapters_bp.route('/<int:number>', methods=['GET'])
@login_required
def get_chapter(number):
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    
    return jsonify({
        'id': chapter.id,
        'number': chapter.number,
        'title_de': chapter.title_de,
        'title_ar': chapter.title_ar,
        'icon': chapter.icon,
        'description_de': chapter.description_de,
        'description_ar': chapter.description_ar,
        'grammar_focus': chapter.grammar_focus,
        'topics_count': chapter.topics.count(),
    }), 200


@chapters_bp.route('/<int:number>/topics', methods=['GET'])
@login_required
def get_chapter_topics(number):
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    topics = chapter.topics.order_by(Topic.order_index).all()
    
    return jsonify([{
        'id': t.id,
        'name_de': t.name_de,
        'name_ar': t.name_ar,
        'icon': t.icon,
        'vocab_count': t.vocab.count(),
    } for t in topics]), 200


@chapters_bp.route('/<int:number>/vocabulary', methods=['GET'])
@login_required
def get_chapter_vocabulary(number):
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    topics = chapter.topics.order_by(Topic.order_index).all()
    
    result = []
    for topic in topics:
        vocab_list = [{
            'id': v.external_id or v.id,
            'de': v.word_de,
            'ar': v.translation_ar,
            'ex': v.example_de,
            'tp': v.word_type,
        } for v in topic.vocab.order_by(Vocabulary.id).all()]
        
        result.append({
            'topic': {'id': topic.id, 'name_de': topic.name_de, 'name_ar': topic.name_ar},
            'vocab': vocab_list
        })
    
    return jsonify(result), 200


@chapters_bp.route('/<int:number>/dialogues', methods=['GET'])
@login_required
def get_chapter_dialogues(number):
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    topics = chapter.topics.order_by(Topic.order_index).all()
    
    result = []
    for topic in topics:
        for dialogue in topic.dialogues.all():
            lines = [{
                'speaker': l.speaker,
                'de': l.text_de,
                'ar': l.text_ar,
            } for l in dialogue.lines.order_by(DialogueLine.line_index).all()]
            
            result.append({
                'id': dialogue.id,
                'title_de': dialogue.title_de,
                'title_ar': dialogue.title_ar,
                'situation_de': dialogue.situation_de,
                'situation_ar': dialogue.situation_ar,
                'lines': lines,
            })
    
    return jsonify(result), 200


@chapters_bp.route('/<int:number>/grammar', methods=['GET'])
@login_required
def get_chapter_grammar(number):
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    grammar_list = Grammar.query.filter_by(chapter_id=chapter.id).order_by(Grammar.order_index).all()
    
    return jsonify([g.to_dict() for g in grammar_list]), 200


@chapters_bp.route('/<int:number>/redemittel', methods=['GET'])
@login_required
def get_chapter_redemittel(number):
    chapter = Chapter.query.filter_by(number=number).first_or_404()
    phrases = UsefulPhrase.query.filter_by(chapter_id=chapter.id).all()
    
    # تجميع حسب الفئة
    result = {}
    for p in phrases:
        if p.category not in result:
            result[p.category] = []
        result[p.category].append({
            'de': p.phrase_de,
            'ar': p.phrase_ar,
        })
    
    return jsonify(result), 200