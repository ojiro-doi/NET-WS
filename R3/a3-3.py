from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

schema = ["ID", "名称", "日時", "場所", "残り日数"]

table = [
    [1, "入学式", "2022/4/1", "上ヶ原キャンパス"],
    [2, "ネットワーク実習", "2024/4/11", "三田キャンパス"],
    [3, "卒業式", "2026/3/1", "上ヶ原キャンパス"],
]


@app.template_filter("daysLeft")
# テンプレートフィルタで定義
def period_filter(event_time):
    some_day1 = datetime.strptime(event_time, "%Y/%m/%d")
    today = datetime.today()
    if some_day1 < today:
        rest = (-1) * (today - some_day1).days
    else:
        rest = (some_day1 - today).days
    return rest


# 　デコレーターを使っているので、下記は不要（どっちでもカスタムフィルターを登録できる）

# app.jinja_env.filters["period"] = period_filter
# テンプレートフィルタperiodをFlaskアプリケーションに登録する．


@app.route("/")
def timetable():
    return render_template(
        "a3-3.html",
        title="イベント詳細",
        schema=schema,
        table=table,
        today=datetime.today(),
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
