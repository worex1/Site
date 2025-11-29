import os
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

print("Sunucu başladı!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Merhaba! Kodum Render'da calisiyor</h1>")

HTTPServer(("", 8080), Handler).serve_forever()
