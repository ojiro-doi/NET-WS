from flask import Flask, render_template

app = Flask(__name__)

name = ["北村一輝", "高橋一生", "藤原竜介"]


@app.route("/id<num>")
# ルートがidで始まる場合に呼び出される．idより後の部分は変数numに代入される．
def page(num):
    try:
        message = "これは{}のページです．".format(name[int(num) - 1])
    except Exception:
        # numの値が正しくない場合は例外が生じる．
        message = "ページは見つかりませんでした"
    return render_template("sample2-2.html", title="表示テスト", message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
