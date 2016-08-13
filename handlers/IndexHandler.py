#-*-coding:utf-8-*-
__author__ = 'hebin'

import tornado.web
import jsonpickle
import tornado.httpclient
import urllib
import json
import datetime
import time
import tornado.gen

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        list=[]
        i=10
        while(i>0):
            wather = Weather("20", "热")
            list.append(wather)
            i-=1

        self.write(jsonpickle.encode(list,"utf-8"));


class Weather():
    temperature = ""
    weather = ""

    def __init__(self, temperature, weather):
        self.temperature= temperature
        self.size = weather


class TestAsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        client=tornado.httpclient.AsyncHTTPClient();
        response = yield tornado.gen.Task(client.fetch,"http://www.weather.com.cn/data/sk/101010100.html")
        res=json.loads(response.body.decode())
        self.write(res)
        self.finish()











