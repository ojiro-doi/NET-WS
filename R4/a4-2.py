from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "abc"
# セッション変数を利用するためには秘密鍵(secret_key)の登録が必要


@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される
def input():

    return render_template("a4-2.html", title="セッション変数", number=0)


@app.route("/", methods=["POST"])
def count_session():
    if "count" in session:
        # "count"という名前のセッション変数を探す．
        count = session["count"]
        # あれば変数countに代入する
    else:
        # なければ変数countを1に初期化する．
        count = 1

    message_cookies = "あなたはこのサイトに{}回アクセスしました．".format(count)
    session["count"] = count + 1
    # セッション変数を1増やして，更新する．
    return render_template(
        "a4-2.html",
        title="セッション変数",
        message_cookies=message_cookies,
    )


def number_session():
    if "number" in session:
        num = session["number"]
    else:
        num = 0

    session["number"] = num + 1
    return render_template("a4-2.html", number=num)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
