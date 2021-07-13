#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    sparrow入口
    ~~~~~~~~~
    sparrow完成Flask核心对象的创建入口.

    Created by lemon on 2021/7/13.
"""
from flask import Flask

from sparrow.endpoint import create_blueprint_v1


def register_blueprints(app: Flask) -> None:
    """蓝图向Flask核心对象注册"""

    blueprint_v1 = create_blueprint_v1()
    app.register_blueprint(blueprint_v1, url_prefix="/v1")


def apply_cors(app, **kwargs):
    """处理跨域"""
    from flask_cors import CORS

    CORS(app, **kwargs)


def create_app() -> Flask:
    """创建Flask核心对象并完成初始化工作"""
    app = Flask(__name__)

    apply_cors(app)
    register_blueprints(app)
    return app
