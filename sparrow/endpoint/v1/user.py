#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    user
    ~~~~~~~~~
    user is useful.

    Created by lemon on 2021/7/13.
"""
from flask import Blueprint
from flask import jsonify

from sparrow.core.logger import Logger

router = Blueprint("user", __name__)


@router.get("/")
@Logger("用户管理", "获取用户详情")
def get_user():
    user = {"username": "张三", "age": 12}
    return jsonify(user)


@router.get("/list/")
@Logger("用户管理", "获取用户列表")
def get_user_list():
    users = [{"username": "张三", "age": 12}, {"username": "李四", "age": 22}]
    return jsonify(users)
