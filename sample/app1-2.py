import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("sample1-2.html", mode="r", encoding="utf-8") as file:
    template = file.read()
    # sample1-2.htmlを読み込みモードで開く．文字コードはutf-8に指定する．HTMLファイルの中身をtemplateに代入する．ファイルをwithでopenすると，自動的にcloseする．


class MyServerHandler(BaseHTTPRequestHandler):
    # BaseHTTPRequestHandlerを継承したMyServerHandlerを定義する．
    def do_GET(self):
        self.send_response(200)
        # HTTP応答としてOK(200)を返す．
        self.end_headers()
        # ヘッダの終了を示す．
        dt = datetime.datetime.now()
        # 今日の日付を得る．
        message = "今日は{a}年{b}月{c}日です．".format(a=dt.year, b=dt.month, c=dt.day)
        # 今日の日付が書かれたメッセージを生成する．{a},{b},{c}の部分がそれぞれ年，月，日に置換される．
        html = template.format(title="表示テスト", message=message)
        # HTMLファイルの内容を変更する．{title}と{message}が置換される．
        self.wfile.write(html.encode("utf-8"))
        # HTMLファイルを文字コートutf-8で書き出す．
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
# HTTPサーバを起動する．
