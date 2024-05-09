from flask import Flask, render_template

app = Flask(__name__)

name = ["入学式", "ネットワーク実習", "卒業式"]
time = ["2022/4", "2024/4", "2026/3"]
place = ["上ヶ原キャンパス", "三田キャンパス", "上ヶ原キャンパス"]


@app.route("/id<num>")
# ルートがidで始まる場合に呼び出される．idより後の部分は変数numに代入される．
def page(num):
    try:
        message = "これは{}のページです．".format(name[int(num) - 1])
        id = int(num)
        messageName = name[int(num) - 1]
        messageTime = time[int(num) - 1]
        messagePlace = place[int(num) - 1]
    except Exception:
        # numの値が正しくない場合は例外が生じる．
        message = "ページは見つかりませんでした"
    return render_template(
        "a2-3.html",
        title="表示テスト",
        message=message,
        id=num,
        messageName=messageName,
        messageTime=messageTime,
        messagePlace=messagePlace,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
