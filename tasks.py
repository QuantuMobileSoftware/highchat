from invoke import task
import tornado.ioloop

from settings import PORT
from app import app


@task
def run_dev(ctx):
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()