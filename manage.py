#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 15:34
# @Author  : Ke xing
# @Blog    ：https://blog.csdn.net/weixin_45131345?spm=1000.2123.3001.5113
from flask import Flask
app = Flask(__name__)
app.secret_key = "aaasfdfasdg"

app.debug = True
@app.route("/")
def index():

    return "hello"
if __name__ == '__main__':
    app.run()