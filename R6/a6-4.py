from flask import Flask, make_response, render_template, request
import datetime

app = Flask(__name__)
app.secret_key = "abc"

name = ["入学式", "ネットワーク実習", "卒業式"]
time = ["2022/4", "2024/4", "2026/3"]
place = ["上ヶ原キャンパス", "三田キャンパス", "上ヶ原キャンパス"]


@app.route("/", methods=["GET"])
def input():
    id_cookies = request.cookies.get("count")
    if id_cookies is None:
        id_cookies = ""
    max_age = 60 * 60 * 24 * 120
    response = make_response(render_template("a6-4in.html", title="フォームの利用"))
    response.set_cookie("id_cookies", value=str(id_cookies), max_age=max_age)
    return response


@app.route("/", methods=["POST"])
def cookie():
    count = request.cookies.get("count")
    dt = datetime.datetime.now()

    try:
        num = request.form["id"]
        num = int(num)
        if num < 1 or num > 3:
            raise Exception
        else:
            message = "これは{}のページです．".format(name[num - 1])
            Name = name[num - 1]
            Time = time[num - 1]
            Place = place[num - 1]
    except Exception:
        message = "ページは見つかりませんでした"
        Name = ""
        Time = ""
        Place = ""

    if count is None:
        count = "1"
    message_cookies = "あなたはこのサイトに{}回アクセスしました．".format(count)
    max_age = 60 * 60 * 24 * 120
    response = make_response(
        render_template(
            "a6-4out.html",
            title="クッキーの利用",
            name=name,
            message=message,
            Id=num,
            Name=Name,
            Time=Time,
            Place=Place,
            message_cookies=message_cookies,
        )
    )
    response.set_cookie("count", value=str(int(count) + 1), max_age=max_age)
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
