import os
import tornado.ioloop
import tornado.httpclient as client

from unittest import TestCase


URLS = [
    'https://www.google.com.ua',
    'http://www.tornadoweb.org/',
    'https://www.python.org/'
]


class TestHighChat(TestCase):
    def setUp(self):
        self.app_address = 'http://localhost:{}'.format(os.environ.get('APPLICATION_PORT', '9000'))
        self.request_payload = ' '.join(URLS)

        tornado.ioloop.IOLoop.current().start()
        self.client = client.AsyncHTTPClient()

    def test_1k_requests(self):
        request_url = os.path.join(self.app_address, '/analyze')
        response_futures = [self.client.fetch(request_url) for _ in range(1000)]
        responses = yield response_futures

