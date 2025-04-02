from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game/top")
def game_top():
    return render_template("game/top.html")


if __name__ == "__main__":
    app.run(debug=True)
