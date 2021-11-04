# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 7:35 PM
# @Author  : nzooherd
# @File    : event.py
# @Software: PyCharm
from enum import Enum


class Event(Enum):

    UPDATE = 0x001
    CREATE = 0x010
    DELETE = 0x100

    @staticmethod
    def all_events() -> int:
        return Event.UPDATE | Event.CREATE | Event.DELETE