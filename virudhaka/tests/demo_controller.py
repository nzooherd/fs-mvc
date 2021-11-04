# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 8:42 PM
# @Author  : nzooherd
# @File    : demo_controller.py
# @Software: PyCharm
from virudhaka.router.mapper import mapping
from virudhaka.router.controller import Controller


class DemoController(Controller):

    @mapping(path=[""])
    async def day_todo(self):
        pass

    @mapping(path=[""])
    async def update_blog(self):
        pass
