from flask import Blueprint, render_template

# メインのBlueprintを作成
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """トップページのビュー関数"""
    return render_template('index.html')
