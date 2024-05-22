from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

schema = ["ID", "名称", "日時", "場所", "残り日数"]

table = [
    [1, "入学式", "2022/4/1", "上ヶ原キャンパス"],
    [2, "ネットワーク実習", "2024/4/11", "三田キャンパス"],
    [3, "卒業式", "2026/3/1", "上ヶ原キャンパス"],
]


@app.context_processor
def utility_processor():
    def days_left(event_time):
        some_day1 = datetime.strptime(event_time, "%Y/%m/%d")
        today = datetime.today()
        rest = (some_day1 - today).days
        return rest

    return dict(days_left=days_left)


@app.route("/")
def render_table():
    return render_template(
        "a3-4.html",
        title="イベント詳細",
        schema=schema,
        table=table,
        today=datetime.today(),
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
