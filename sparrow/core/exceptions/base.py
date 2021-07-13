#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    base
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
    code = 500
    message = "Internal Server Error"
    message_code = 10001


class Forbidden(APIException):
    code = 401
    message = "Forbidden"
    message_code = 10070


class MethodNotAllowed(APIException):
    code = 401
    message = "Method Not Allowed"
    message_code = 10080
