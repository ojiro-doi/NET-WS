import datetime

from flask import Flask, render_template

app = Flask(__name__)


schedule = [
    # 授業スケジュールのリスト
    [datetime.time(9, 0, 0), datetime.time(10, 40, 0)],
    # 1限は9時に始まり，10時40分に終わる．
    [datetime.time(11, 10, 0), datetime.time(12, 50, 0)],
    # 2限は11時10分に始まり，12時50分に終わる．
    [datetime.time(13, 30, 0), datetime.time(15, 10, 0)],
    # 3限は13時30分に始まり，15時10分に終わる．
    [datetime.time(15, 20, 0), datetime.time(17, 0, 0)],
    # 4限は15時20分に始まり，17時に終わる．
    [datetime.time(17, 5, 0), datetime.time(18, 45, 0)],
    # 5限は17時5分に始まり，18時45分に終わる．
]


@app.template_filter("daysLeft")
# テンプレートフィルタで定義
def period_filter(event_time):
    some_day1 = datetime.datetime.fromisoformat(event_time)
    print(some_day1)
    today = datetime.datetime.now().day
    return event_time - today


# 　デコレーターを使っているので、下記は不要（どっちでもカスタムフィルターを登録できる）

# app.jinja_env.filters["period"] = period_filter
# テンプレートフィルタperiodをFlaskアプリケーションに登録する．


# @app.context_processor
# # コンテキストプロセッサの定義
# # 登録用の関数としてcountdown_processorを定義する．関数名は任意．
# def countdown_processor():
#     # 組み込み関数としてcountdownを定義する．
#     def countdown(period):
#         now = datetime.datetime.now()
#         rest = datetime.datetime.combine(now.date(), schedule[period - 1][1]) - now
#         # 今日のperiod時限の終了時刻から現在時刻を引くことで授業の残り時間を計算する．
#         return rest.seconds
#         # 残り時間の秒数を返す．

#     return dict(countdown=countdown)
#     # countdownをコンテキストプロセッサとして登録する．


@app.route("/")
def timetable():
    schema = ["ID", "名称", "日時", "場所"]
    # 表の属性名のリスト
    table = [
        [1, "入学式", "2022/4/1", "上ヶ原キャンパス"],
        [2, "ネットワーク実習", "2024/4/11", "三田キャンパス"],
        [3, "卒業式", "2026/3/1", "上ヶ原キャンパス"],
    ]
    return render_template(
        "a3-2.html",
        title="イベント詳細",
        schema=schema,
        table=table,
        time=datetime.datetime.now().time(),
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
