from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

with open("a1-3.html", mode="r", encoding="utf-8") as file:
    template = file.read()


routes = []
# ルートを保存するグローバル変数を初期化する


def route(path, method):
    routes.append((path, method))
    # ルートのパスとそれに応じた処理（メソッド）をタプルとしてroutesに登録する．


route("/id1", "id1")
route("/id2", "id2")
route("/id3", "id3")
# 2つのルートと処理を登録する．


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)
        # クラス内変数_urlにアクセスパスを代入する.
        for r in routes:
            # routesの要素を順にrに代入する．
            if r[0] == _url.path:
                eval("self." + r[1] + "()")
                # パスに応じたメソッドを実行する．
                break
                # 登録しているパスであった場合は処理を実行し，for文を抜ける．
        else:
            self.error()
            # routesに登録されていない場合は，errorメソッドを実行する．

    def id1(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(
            title="ルーティングテスト",
            message1="1",
            message2="入学式",
            message3="2022/4",
            message4="上ヶ原キャンパス",
        )
        self.wfile.write(html.encode("utf-8"))
        return

    def id2(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(
            title="ルーティングテスト",
            message1="2",
            message2="ネットワーク実習",
            message3="2024/4",
            message4="三田キャンパス",
        )
        self.wfile.write(html.encode("utf-8"))
        return

    def id3(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(
            title="ルーティングテスト",
            message1='<font color="red">3</font>',
            message2='<font color="red">卒業式</font>',
            message3='<font color="red">2026/3</font>',
            message4='<font color="red">上ヶ原キャンパス</font>',
        )
        self.wfile.write(html.encode("utf-8"))
        return

    def error(self):
        self.send_error(404, "CANNOT ACCESS!!")
        # エラーコード(404)とメッセージを表示する．
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
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
