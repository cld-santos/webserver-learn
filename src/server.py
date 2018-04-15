from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus


class CldHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        self.wfile.flush()

if __name__=='__main__':
    httpd = HTTPServer(('', 8000), CldHTTPHandler)
    httpd.serve_forever()

