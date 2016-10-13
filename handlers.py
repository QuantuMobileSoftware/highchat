import re
import json

import tornado.web
import tornado.httpclient

from tornado import gen
from bs4 import BeautifulSoup


class AnalyzeHandler(tornado.web.RequestHandler):
    RE_FIND_URLS = re.compile(r'https?://[^\s]+')

    @gen.coroutine
    def post(self):
        http_client = tornado.httpclient.AsyncHTTPClient()

        content = self.request.body.decode()
        urls = self.RE_FIND_URLS.findall(content)

        links = []

        for url in urls:
            response = yield http_client.fetch(url)
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
