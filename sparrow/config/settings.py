#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    settings
    ~~~~~~~~~
    settings is useful.

    Created by lemon on 2021/7/14.
"""
import os
import secrets


class Config:
    # 指定加密KEY
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe())

    # 指定数据库
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "sqlite:////" + os.getcwd() + os.path.sep + "test.db",
    )

    # 屏蔽 sql alchemy 的 FSADeprecationWarning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
