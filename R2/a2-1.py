from flask import Flask, render_template

# flaskモジュールからFlaskクラスとrender_templateメソッドをインポートする

app = Flask(__name__)
# Flaskインスタンスを生成する．


@app.route("/")
# ルート"/"にアクセスされた場合にsampleが呼び出されることを指定する．メソッドの名前は任意である．
def R2():
    message = "Hello World!"

    return render_template("a2-1.html")
    # templateフォルダに入っているsample2-1.htmlを表示する．


if __name__ == "__main__":
    # このプログラムが直接起動されたものであれば以下を実行する．
    app.debug = True
    # デバッグ機能をONにする．
    app.run(host="localhost", port=8000)
    # ホスト名をlocalhostにして，ポート番号を8000に設定してWebアプリケーションを起動する．
