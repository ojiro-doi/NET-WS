from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import datetime

with open("b1-2.html", mode="r", encoding="utf-8") as file:
    template = file.read()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("b1-2.html", "rb") as file:
            self.wfile.write(file.read())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode("utf-8"))
        event_name = data["event-name"][0]
        event_date = data["event-date"][0]

        event_date_obj = datetime.datetime.strptime(event_date, "%Y-%m-%d")
        today = datetime.datetime.today()
        days_diff = (today - event_date_obj).days

        message = "{}[{}]まであと{}日です．".format(event_name, event_date, days_diff)

        self.send_response(200)
        self.end_headers()
        html = template.format(message=message)
        self.wfile.write(html.encode("utf-8"))


server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server started at http://localhost:8000")
httpd.serve_forever()
