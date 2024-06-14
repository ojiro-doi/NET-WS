from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("a4-4.html")


@app.route("/add_event", methods=["POST"])
def add_event():
    date = request.form["date"]
    event = request.form["event"]

    try:
        # 入力された日付の形式を検証する
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "無効な日付", 400

    with open("a4-3.txt", "a", encoding="utf-8") as file:
        file.write(f"{date}, {event}\n")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="localhost")
