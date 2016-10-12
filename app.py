import tornado.web
from handlers import AnalyzeHandler


app = tornado.web.Application([
    (r'/analyze', AnalyzeHandler),
])
