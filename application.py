#-*-coding:utf-8-*-
__author__ = 'hebin'

from url import urls
import tornado.web
import os

setting=dict(
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"statics")
)

app=tornado.web.Application(handlers=urls,**setting)



