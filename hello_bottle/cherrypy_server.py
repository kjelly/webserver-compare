from cherrypy import wsgiserver
from server import bottle_app

server = wsgiserver.CherryPyWSGIServer(
                      ('0.0.0.0', 8000), bottle_app)
server.start()
