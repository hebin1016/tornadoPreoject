#-*-coding:utf-8-*-
__author__ = 'hebin'

from application import app
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


from tornado.options import define,options

define("port",default=8001,help="the fucking world",type=int)


def main():
    tornado.options.parse_command_line();
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':
    main()




