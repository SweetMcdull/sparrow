#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    settings
    ~~~~~~~~~
    settings is useful.

    Created by lemon on 2021/7/14.
"""
import secrets

from pydantic import BaseSettings


class Config(BaseSettings):
    # 指定加密KEY
    SECRET_KEY: str = secrets.token_urlsafe()

    # 指定数据库
    SQLALCHEMY_DATABASE_URI: str = "sqlite://///test.db"

    # 屏蔽 sqlalchemy 的 FSADeprecationWarning
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    SQLALCHEMY_ECHO: bool = False

    # class Config:
    #     case_sensitive = False
    #     env_prefix = ''
    #     env_file = '.env'
    #     env_file_encoding = 'utf-8'
