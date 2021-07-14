#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    user
    ~~~~~~~~~
    user is useful.

    Created by lemon on 2021/7/14.
"""
from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy import String

from .base import InfoCrud as Base


class UserInterface(Base):
    __tablename__ = "lin_user"
    __table_args__ = (
        Index("username_del", "username", "delete_time", unique=True),
        Index("email_del", "email", "delete_time", unique=True),
    )

    id = Column(Integer(), primary_key=True)
    username = Column(String(24), nullable=False, comment="用户名，唯一")
    nickname = Column(String(24), comment="用户昵称")
    _avatar = Column("avatar", String(500), comment="头像url")
    email = Column(String(100), comment="邮箱")


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default="未名")
    summary = Column(String(1000))
    image = Column(String(100))
