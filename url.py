#-*-coding:utf-8-*-
__author__ = 'hebin'

from handlers.IndexHandler import WeatherHandler
from handlers.IndexHandler import TestAsyncHandler

urls=[(r"/", WeatherHandler),
    (r"/test", TestAsyncHandler)
      ]