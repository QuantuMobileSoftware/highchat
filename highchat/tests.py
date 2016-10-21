import os
import tornado.ioloop
import tornado.httpclient as client

from tornado.testing import AsyncTestCase, gen_test, main


URLS = [
    'http://info.cern.ch/hypertext/WWW/TheProject.html',
]

RESP = '{"links": [{"url": "http://info.cern.ch/hypertext/WWW/TheProject.html", "title": "The World Wide Web project"}]}'


class TestHighChat(AsyncTestCase):
    def setUp(self):
        super().setUp()
        self.app_address = 'http://localhost:{}'.format(os.environ.get('APPLICATION_PORT', '9000'))
        self.request_payload = ' '.join(URLS)

    @gen_test(timeout=1000)
    def test_1k_requests(self):
        self.client = client.AsyncHTTPClient(self.io_loop)

        request = client.HTTPRequest(self.app_address + '/analyze', method='POST', body=self.request_payload)
        response_futures = [self.client.fetch(request) for _ in range(1000)]
        responses = yield response_futures

        for response in responses:
            self.assertEqual(response.body.decode(), RESP)
