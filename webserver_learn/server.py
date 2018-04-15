import re
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus


class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        matched = re.match(self.path_pattern, self.path)
        if matched:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b'Hello, world!')
            self.wfile.flush()
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()


class HelloWorld(HTTPHandler):
    def __init__(self, *args, **kwargs):
        self.path_pattern = r'/hello-world/?'
        HTTPHandler.__init__(self, *args, **kwargs)
