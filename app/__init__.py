from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # メインのBlueprintを登録
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    # ゲーム機能のBlueprintを登録
    from app.routes.game import game_bp
    app.register_blueprint(game_bp)

    # Jinja2学習のBlueprintを登録
    from app.routes.jinja_s import jinja_s_bp
    app.register_blueprint(jinja_s_bp)
    return app