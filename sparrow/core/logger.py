#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    操作日志记录器
    ~~~~~~~~~
    操作日志记录器用于保存接口访问相关信息.

    Created by lemon on 2021/7/13.
"""
from functools import wraps

import flask
from flask import Response
from flask import request


class Logger:
    """接口操作日志装饰器.

    在需要记录操作日志的路由上打上Logger装饰，即可完成对该路由的请求日志记录.操作日志主
    要记录客户端IP、请求者用户名（角色）、请求地址、请求参数、返回参数、请求方法、请求时
    间、返回状态码、接口耗时等信息.

    Attributes:
        module_name (string): 模块名称，同一个路由分组即为一个模块，模块名称不能重复.
        name (string): 操作名称，同一个模块内名称不能重复.

    Notes:
        视图函数返回必须是Response对象，否则不能获取完整的日志数据.
    """

    def __init__(self, module_name, name):
        self.module_name = module_name
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            current_app = flask.current_app

            current_app.logger.warning(f"Behavior log {self.module_name}:{self.name}")
            current_app.logger.warning(f"client`s ip {request.remote_addr}")
            current_app.logger.warning(f"post data {request.json}")
            current_app.logger.warning(f"method {request.method}")
            current_app.logger.warning(f"headers {request.headers.get('User-Agent')}")
            current_app.logger.warning(f"path {request.path}")

            response: Response = func(*args, **kwargs)

            current_app.logger.warning(f"status_code {response.status_code}")
            current_app.logger.warning(f"response {response.is_json} {response.json}")
            return response

        return wrap
