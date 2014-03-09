from bottle import route, run, template, get, request
from bottle import SimpleTemplate
import bottle
from jinja2 import Environment


@get('/')
def index():
    name = request.query.get('name')
    a = int(request.query.get('a'), 10)
    b = int(request.query.get('b'), 10)
    tpl = SimpleTemplate('Hello {{name}}!<br/>\nsum={{sum}}\n')
    sum = a + b
    return tpl.render(name=name, sum=sum)
    # return "hello %s<br>\n %d" % (name, a + b)
    # return Environment().from_string("Hello {{name}}<br/>\n{{sum}}").render(name=name, sum=a + b)


bottle_app = bottle.default_app()


if __name__ == '__main__':
    import tornado.httpserver
    import tornado.ioloop
    import tornado.wsgi
    bottle_handler = tornado.wsgi.WSGIContainer(bottle_app)
    tornado.httpserver.HTTPServer(bottle_handler).listen(8888)
    tornado.ioloop.IOLoop.instance().start()
