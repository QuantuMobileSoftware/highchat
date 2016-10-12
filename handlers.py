import re
import json
import tornado.web

from urllib.request import urlopen
from bs4 import BeautifulSoup


class AnalyzeHandler(tornado.web.RequestHandler):
    RE_FIND_URLS = re.compile(r'https?://[^\s]+')

    def post(self):
        content = self.request.body.decode()
        urls = self.RE_FIND_URLS.findall(content)

        response = {'links': []}

        for url in urls:
            body_data = urlopen(url).read()
            soup = BeautifulSoup(body_data, 'html.parser')
            response['links'].append({
                'url': url,
                'title': soup.find('title').contents[0],
            })
        self.write(json.dumps(response))
