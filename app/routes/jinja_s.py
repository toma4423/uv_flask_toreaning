from flask import Blueprint, render_template

# Blueprintの作成（URLの接頭辞として/jinja_sを設定）
jinja_s_bp = Blueprint('jinja_s', __name__, url_prefix='/jinja_s')

@jinja_s_bp.route('/')
def index():
    """Jinja2学習トップページ"""
    context = {
        'title': 'Jinja2学習ページ',
        'items': ['変数の表示', '制御構文', 'フィルター', 'マクロ'],
        'user': {
            'name': 'テストユーザー',
            'role': '学習者'
        }
    }
    return render_template('jinja_s/index.html', **context)

@jinja_s_bp.route('/control')
def control():
    """制御構文の学習ページ"""
    context = {
        'numbers': range(1, 6),
        'users': [
            {'name': 'Alice', 'age': 20},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ],
        'show_message': True
    }
    return render_template('jinja_s/control.html', **context)

@jinja_s_bp.route('/filters')
def filters():
    """フィルターの学習ページ"""
    context = {
        'text': 'hello, world',
        'html_text': '<script>alert("危険!")</script>',
        'numbers': [1, 2, 3, 4, 5],
        'date': '2024-04-04'
    }
    return render_template('jinja_s/filters.html', **context)
