#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 17:19
# @Author  : Ke xing
# @Blog    ：https://blog.csdn.net/weixin_45131345?spm=1000.2123.3001.5113
from flask import current_app

from .import indexblue
@indexblue.route("/index")
def index():
    current_app.logger.info('我来了')
    return "index"

@indexblue.route("/password")
def pa():

    return "password"