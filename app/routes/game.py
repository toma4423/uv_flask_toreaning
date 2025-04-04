from flask import Blueprint, render_template

# Blueprintの作成（URLの接頭辞として/gameを設定）
game_bp = Blueprint('game', __name__, url_prefix='/game')

@game_bp.route('/top')
def top():
    """ゲームトップページ"""
    games = [
        {'id': 1, 'title': 'アクションゲーム', 'description': '爽快アクション！'},
        {'id': 2, 'title': 'パズルゲーム', 'description': '頭を使って解こう！'},
        {'id': 3, 'title': 'RPGゲーム', 'description': '壮大な冒険の世界へ！'}
    ]
    return render_template('game/top.html', games=games)

@game_bp.route('/play/<int:game_id>')
def play(game_id):
    """ゲームプレイページ"""
    # 仮のゲームデータ
    game = {
        'id': game_id,
        'title': 'サンプルゲーム' + str(game_id),
        'description': 'ゲームの説明文がここに入ります'
    }
    return render_template('game/play.html', game=game)

@game_bp.route('/ranking')
def ranking():
    """ランキングページ"""
    # 仮のランキングデータ
    rankings = [
        {'rank': 1, 'name': 'プレイヤー1', 'score': 1000},
        {'rank': 2, 'name': 'プレイヤー2', 'score': 850},
        {'rank': 3, 'name': 'プレイヤー3', 'score': 750}
    ]
    return render_template('game/ranking.html', rankings=rankings)
