from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("a1-4in.html", mode="r", encoding="utf-8") as file:
    input = file.read()
with open("a1-4out.html", mode="r", encoding="utf-8") as file:
    output = file.read()

events = [
    {"id": "1", "name": "イベントA", "date": "2022-05-01", "location": "東京"},
    {"id": "2", "name": "イベントB", "date": "2022-06-01", "location": "大阪"},
    {"id": "3", "name": "イベントC", "date": "2022-07-01", "location": "名古屋"},
]


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = input.format(title="入力画面")
        self.wfile.write(html.encode("utf-8"))
        return

    def do_POST(self):
        form = FieldStorage(
            fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}
        )
        message = format(form.getvalue("name"))
        self.send_response(200)
        self.end_headers()
        html = output.format(
            title="選択リストテスト",
            message1="1",
            message2="入学式",
            message3="2022/4",
            message4="上ヶ原キャンパス",
        )
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
