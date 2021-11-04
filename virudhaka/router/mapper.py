# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 7:01 PM
# @Author  : nzooherd
# @File    : mapper.py
# @Software: PyCharm
from typing import List

from virudhaka.gate.event import Event


class Mapper:

    def __init__(self, path: List[str], events: int = Event.all_events()):
        self.path = path
        self.events = events

    def __call__(self, *args, **kwargs):
        pass



mapping = Mapper