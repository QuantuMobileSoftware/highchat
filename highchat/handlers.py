import re
import json

import tornado.web
import tornado.httpclient as client

from tornado import gen
from bs4 import BeautifulSoup


class AnalyzeHandler(tornado.web.RequestHandler):
    RE_FIND_URLS = re.compile(r'https?://[^\s]+')

    @gen.coroutine
    def post(self):
        http_client = client.AsyncHTTPClient()

        content = self.request.body.decode()
        urls = self.RE_FIND_URLS.findall(content)

        response_futures = [http_client.fetch(url) for url in urls]
        responses = yield response_futures

        links = []

        for url, response in zip(urls, responses):
            body_data = response.body
            soup = BeautifulSoup(body_data, 'html.parser')
            links.append(
                {
                    'url': url,
                    'title': soup.find('title').contents[0],
                }
            )

        response = {'links': links}
        self.write(json.dumps(response))
