#-*-coding:utf-8-*-
__author__ = 'hebin'

from handlers.IndexHandler import WeatherHandler
from handlers.IndexHandler import TestAsyncHandler
from handlers.IndexHandler import CartHandler
from handlers.IndexHandler import StatusHandler
from handlers.IndexHandler import DetailHandler



urls=[(r"/", DetailHandler),
    (r"/test", TestAsyncHandler),
      (r"/cart", CartHandler),
      (r"/cart/status", StatusHandler)

      ]