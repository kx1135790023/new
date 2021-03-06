#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 16:29
# @Author  : Ke xing
# @Blog    ：https://blog.csdn.net/weixin_45131345?spm=1000.2123.3001.5113
import logging

import redis


class  Config():
    SECRET_KEY = "AAAAA"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/flask_27"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始语句
    SQLALCHEMY_ECHO = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT =6379
    #Z增加flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是s

class DevelopementConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG



class ProductionConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.ERROR

config = {
    "development": DevelopementConfig,
    "production": ProductionConfig
}