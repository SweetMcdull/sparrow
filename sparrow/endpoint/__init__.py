#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~
    __init__.py is useful.

    Created by lemon on 2021/7/13.
"""
from flask import Blueprint
from .v1 import user


def create_blueprint_v1() -> Blueprint:
    bp_v1 = Blueprint('v1', __name__)

    # 向v1蓝图注册子蓝图
    bp_v1.register_blueprint(user.router, url_prefix="/user")
    return bp_v1
