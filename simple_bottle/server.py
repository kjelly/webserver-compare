from bottle import route, run, template, get
import bottle

@get('/')
def index():
    return '123'


if __name__ == '__main__':
    bottle_app = bottle.default_app()
    import tornado.httpserver
    import tornado.ioloop
    import tornado.wsgi
    bottle_handler = tornado.wsgi.WSGIContainer(bottle_app)
    tornado.httpserver.HTTPServer(bottle_handler).listen(8888)
    tornado.ioloop.IOLoop.instance().start()
