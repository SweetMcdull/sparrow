#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    自定义HTTPException异常基类
    ~~~~~~~~~
    base is useful.

    Created by lemon on 2021/7/13.
"""
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    message = "Unknown Internal Server Error"
    message_code = 10000
    headers = {"Content-Type": "application/json"}


class InternalServerError(APIException):
    message_code = 10001


class Forbidden(APIException):
    code = 403
    message = "Forbidden"
    message_code = 10002


class MethodNotAllowed(APIException):
    code = 405
    message = "Method Not Allowed"
    message_code = 10003


class NotFound(APIException):
    code = 404
    message = "Not Found"
    message_code = 10004
