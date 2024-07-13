from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import datetime

EVENTS = {
    "1": {
        "id": "1",
        "name": "入学式",
        "date": "2022/4",
        "location": "上ヶ原キャンパス",
    },
    "2": {
        "id": "2",
        "name": "ネットワーク実習",
        "date": "2024/4",
        "location": "神戸三田キャンパス",
    },
    "3": {
        "id": "3",
        "name": "卒業式",
        "date": "2026/3",
        "location": "上ヶ原キャンパス",
    },
}


class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        event_id = query_params.get("id", [""])[0]
        event = EVENTS.get(event_id, None)

        if event:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("b1-1.html", "r", encoding="utf-8") as f:
                html_content = f.read()
                html_content = html_content.replace("{{id}}", event["id"])
                html_content = html_content.replace("{{name}}", event["name"])
                html_content = html_content.replace("{{date}}", event["date"])
                html_content = html_content.replace("{{location}}", event["location"])

                # 日付を比較して未来のイベントかどうかを判定
                event_date = datetime.datetime.strptime(event["date"], "%Y/%m")
                if event_date > datetime.datetime.now():
                    html_content = html_content.replace(
                        '<tr id="event">', '<tr id="event" class="future-event">'
                    )

                self.wfile.write(html_content.encode("utf-8"))


server_address = ("", 8000)
handler_class = CustomRequestHandler

server = HTTPServer(server_address, handler_class)
server.serve_forever()
