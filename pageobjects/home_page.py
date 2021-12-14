#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  4:47 下午
@Author  : Frank.lian
@File    : home_page.py
@Description : 首页
'''
from framework.base_page import Base


class HomePage(Base):
    name = "xpath=>//*[@class='user-name']"

    def get_username(self):
        """
        获取用户名称
        :param name: 用户名称
        :return :返回用户名称
        """
        return self.get_text(self.name)

    search_text = "xpath=>//*[@type='text' and @class='input']"

    def enter_search(self, text):
        """
        录入查询条件
        :param text: 查询条件
        """
        self.enter(self.search_text, text)

    search_bt = "xpath=>//*[@class='search-btn']"

    def click_search(self):
        """
        点击查询按钮
        """
        self.click_element(self.search_bt)

    close_bt = "xpath=>//*[@class='close']"

    def click_close(self):
        self.element_displayed(self.close_bt)



