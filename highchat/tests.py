import json
import tornado.httpclient as client

from tornado.testing import AsyncTestCase, gen_test
from settings import PORT


class TestHighChat(AsyncTestCase):
    request_timeout = 1000
    connections_count = 1000
    urls = [
        'http://info.cern.ch/hypertext/WWW/TheProject.html',
    ]
    expected_response = {
        "links": [
            {
                "url": "http://info.cern.ch/hypertext/WWW/TheProject.html",
                "title": "The World Wide Web project"
            }
        ]
    }

    def setUp(self):
        super().setUp()
        self.app_address = 'http://localhost:{}'.format(PORT)
        self.request_payload = ' '.join(self.urls)

    @gen_test(timeout=request_timeout)
    def test_high_load(self):
        self.client = client.AsyncHTTPClient(self.io_loop)

        request = client.HTTPRequest(
            self.app_address + '/analyze', method='POST', body=self.request_payload,
            request_timeout=self.request_timeout, connect_timeout=self.request_timeout)

        response_futures = [self.client.fetch(request) for _ in range(self.connections_count)]
        responses = yield response_futures

        for response in responses:
            self.assertEqual(json.loads(response.body.decode()), self.expected_response)
