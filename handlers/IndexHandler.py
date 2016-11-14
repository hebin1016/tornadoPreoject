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
from uuid import uuid4
from tornado.template import Template

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


class Shoppingcart(object):
    totalInventory=10
    callbacks=[]
    carts={}

    def register(self,callback):
        self.callbacks.append(callback)

    def moveItemToCart(self,session):
        if session in self.carts:
            return

        self.carts[session]=True;
        self.notifyCallbacks()

    def removeItemFromCart(self,session):
        if session not in self.carts:
            return

        del(self.carts[session])
        self.notifyCallbacks()


    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)

        self.callbacks=[]

    def callbackHelper(self,callback):
        callback(self.getInventoryCount())

    def getInventoryCount(self):
        return self.totalInventory-len(self.carts)



class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        session=uuid4()
        count=self.application.shoppingCart.getInventoryCount()
        self.write('{"count":"%s","session":"%s"}'% (count,session))


class CartHandler(tornado.web.RequestHandler):
    def post(self):
        action=self.get_argument("action")
        session=self.get_argument("session")

        # 如果session是null
        if not session:
            self.set_status(400)
            return

        if action =="add":
            self.application.shoppingCart.moveItemToCart(session)
        elif action=="remove":
            self.application.shoppingCart.removeItemFromCart(session)
        else:
            self.set_status(400)

class StatusHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.application.shoppingCart.register(self.async_callback(self.on_message))

    def on_message(self,count):
        self.write('{"inventoryCount":"%d"}' % count)
        self.finish()










