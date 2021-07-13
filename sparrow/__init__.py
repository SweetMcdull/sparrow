#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    __init__
    ~~~~~~~~~
    __init__ is useful.

    Created by lemon on 2021/7/13.
"""
from flask import Flask


def create_app() -> Flask:
    """创建Flask核心对象并完成初始化工作"""
    app = Flask(__name__)

    return app
