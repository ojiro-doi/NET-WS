from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

events = {
    "1": {
        "message1": "1",
        "message2": "入学式",
        "message3": "2022/4",
        "message4": "上ヶ原キャンパス",
    },
    "2": {
        "message1": "2",
        "message2": "ネットワーク実習",
        "message3": "2024/4",
        "message4": "三田キャンパス",
    },
    "3": {
        "message1": '<font color="red">3</font>',
        "message2": '<font color="red">卒業式</font>',
        "message3": '<font color="red">2026/3</font>',
        "message4": '<font color="red">上ヶ原キャンパス</font>',
    },
}

with open("b1-3in.html", mode="r", encoding="utf-8") as file:
    input_template = file.read()

with open("b1-3out.html", mode="r", encoding="utf-8") as file:
    output_template = file.read()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(input_template.encode("utf-8"))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode("utf-8"))
            event_id = data.get("event", [""])[0]

            if event_id in events:
                event = events[event_id]
                message = "{}の情報".format(event["message2"])
                html = output_template.format(
                    title="イベント情報",
                    message=message,
                    message1=event["message1"],
                    message2=event["message2"],
                    message3=event["message3"],
                    message4=event["message4"],
                )
            else:
                html = output_template.format(
                    title="エラー",
                    message="選択したイベントは見つかりませんでした。",
                    message1="",
                    message2="",
                    message3="",
                    message4="",
                )

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404)


HTTPServer(("", 8000), SimpleHTTPRequestHandler).serve_forever()
