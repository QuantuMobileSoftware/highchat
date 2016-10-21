import tornado.web
from highchat.handlers import AnalyzeHandler


app = tornado.web.Application([
    (r'/analyze', AnalyzeHandler),
])
