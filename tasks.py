import tornado.ioloop

from invoke import task
from highchat.app import app

from settings import PORT


@task
def run_dev(ctx):
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()