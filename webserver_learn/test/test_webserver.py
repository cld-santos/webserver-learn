import pytest
import requests
from threading import Thread
from http.server import HTTPServer
from ..server import HelloWorld


@pytest.fixture
def webserver():
    def start_webserver():
        httpd = HTTPServer(('', 8000), HelloWorld)
        httpd.serve_forever()
    t = Thread(target=start_webserver, daemon=True)
    t.start()


def test_hello_world(webserver):
    g = requests.get('http://localhost:8000/hello-world')
    assert g.text == 'Hello, world!'


def test_fail_hello_world(webserver):
    g = requests.get('http://localhost:8000/helo-rld')
    assert g.status_code == 404
