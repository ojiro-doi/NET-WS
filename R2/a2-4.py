import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

name = ["入学式", "ネットワーク実習", "卒業式"]
time = ["2022/4", "2024/4", "2026/3"]
place = ["上ヶ原キャンパス", "三田キャンパス", "上ヶ原キャンパス"]


@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def input():
    return render_template("a2-4in.html", title="フォームの利用")


@app.route("/", methods=["POST"])
# POSTメソッドでのアクセスは以下が実行される．
def output():
    dt = datetime.datetime.now()
    num = request.form["id"]
    # フォームからnameデータを取得する．

    try:
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
    return render_template(
        "a2-4out.html",
        name=name,
        message=message,
        Id=num,
        Name=Name,
        Time=Time,
        Place=Place,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
