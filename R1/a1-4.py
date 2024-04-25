from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer


def read_html_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return file.read()


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = read_html_file("a1-4in.html").format(title="入力画面")
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        form = FieldStorage(
            fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}
        )
        try:
            event_id = int(form["id"].value)
        except (KeyError, ValueError):
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = read_html_file("a1-4out.html").format(
                title="ERROR", message="Invalid or missing ID."
            )
            self.wfile.write(html.encode("utf-8"))
            return

        events = {
            1: {
                "ID": "1",
                "Name": "入学式",
                "Time": "2022/4",
                "Place": "上ヶ原キャンパス",
                "color": "black",
            },
            2: {
                "ID": "2",
                "Name": "ネットワーク実習",
                "Time": "2024/4",
                "Place": "三田キャンパス",
                "color": "black",
            },
            3: {
                "ID": "3",
                "Name": "卒業式",
                "Time": "2026/3",
                "Place": "三田キャンパス",
                "color": "red",
            },
        }

        event = events.get(event_id)
        if event:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = read_html_file("a1-4out.html").format(**event)
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = read_html_file("a1-4out.html").format(
                title="ERROR", message="指定されたIDのイベントは存在しません。"
            )
            self.wfile.write(html.encode("utf-8"))


HTTPServer(("", 8000), MyServerHandler).serve_forever()
