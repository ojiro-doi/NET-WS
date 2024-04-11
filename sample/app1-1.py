from http.server import HTTPServer, SimpleHTTPRequestHandler
# http.serverモジュールからHTTPServer, SimpleHTTPRequestHandlerクラスをインポートする．

server_address = ("", 8000)
# サーバーの名前(未設定)とポート番号(8000)を設定する．
handler_class = SimpleHTTPRequestHandler
# ハンドラーをHTTP要求に対応するクラスをSimpleHTTPRequestHandlerに設定する．
server = HTTPServer(server_address, handler_class)
# Webサーバーのインスタンスを作成する．
server.serve_forever()
# Webサーバーを起動する．
