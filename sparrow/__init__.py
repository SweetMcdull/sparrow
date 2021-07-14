#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    sparrow入口
    ~~~~~~~~~
    sparrow完成Flask核心对象的创建入口.

    Created by lemon on 2021/7/13.
"""
from dotenv import load_dotenv
from flask import Flask

from sparrow.endpoint import create_blueprint_v1
from sparrow.extention.sqlalchemy import db


def register_blueprints(app: Flask) -> None:
    """蓝图向Flask核心对象注册"""

    blueprint_v1 = create_blueprint_v1()
    app.register_blueprint(blueprint_v1, url_prefix="/v1")


def apply_cors(app, **kwargs):
    """处理跨域"""
    from flask_cors import CORS

    CORS(app, **kwargs)


def load_app_config(app: Flask):
    # 读取 .env
    load_dotenv(".env")
    # 读取配置类
    app.config.from_object("sparrow.config.settings.Config")


def create_app() -> Flask:
    """创建Flask核心对象并完成初始化工作"""
    app = Flask(__name__)
    load_app_config(app)

    apply_cors(app)
    register_blueprints(app)
    db.init_app(app)
    return app
