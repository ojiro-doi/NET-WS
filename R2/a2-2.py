import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template():
    # self.send_response(200)
    # # HTTP応答としてOK(200)を返す．
    # self.end_headers()
    # # ヘッダの終了を示す．
    dt = datetime.datetime.now()
    # 今日の日付を得る．
    if dt.second % 2 == 0:
        message = "現在の時刻は{a}時間{b}分{c}秒です.".format(
            a=dt.hour,
            b=dt.minute,
            c=dt.second,
        )
        color = "blue"
    else:
        message = "現在の時刻は{a}時間{b}分{c}秒です.".format(
            a=dt.hour,
            b=dt.minute,
            c=dt.second,
        )
        color = "red"

    return render_template(
        "a2-2.html", title="表示テスト", message=message, color=color
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
