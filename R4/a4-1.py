from flask import Flask, make_response, render_template, request
import datetime

app = Flask(__name__)
app.secret_key = "abc"
# セッション変数を利用するためには秘密鍵(secret_key)の登録が必要

name = ["入学式", "ネットワーク実習", "卒業式"]
time = ["2022/4", "2024/4", "2026/3"]
place = ["上ヶ原キャンパス", "三田キャンパス", "上ヶ原キャンパス"]


@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される
def input():
    id_cookies = request.cookies.get("count")
    # クッキー変数"count"を読み出し，countに代入する．
    if id_cookies is None:
        # クッキー変数"count"が存在しない場合は，countに"1"を代入する．
        id_cookies = ""
    max_age = 60 * 60 * 24 * 120
    # クッキーの賞味期限を120日にする
    response = make_response(render_template("a4-1in.html", title="フォームの利用"))
    response.set_cookie("id_cookies", value=str(id_cookies), max_age=max_age)
    return response


@app.route("/", methods=["POST"])
def cookie():
    count = request.cookies.get("count")
    dt = datetime.datetime.now()

    try:
        num = request.form["id"]
        # フォームからnameデータを取得する．
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

    # クッキー変数"count"を読み出し，countに代入する．
    if count is None:
        # クッキー変数"count"が存在しない場合は，countに"1"を代入する．
        count = "1"
    message_cookies = "あなたはこのサイトに{}回アクセスしました．".format(count)
    max_age = 60 * 60 * 24 * 120
    # クッキーの賞味期限を120日にする
    response = make_response(
        render_template(
            "a4-1out.html",
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
    # クッキー変数"count"にcountに1加えたものを代入する．
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
