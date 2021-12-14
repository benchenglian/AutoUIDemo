#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  10:49 上午
@Author  : Frank.lian
@File    : test_home_page.py
@Description : 首页
'''
import time

import allure
import pytest
from framework.annotations import get_ErrImage
from pageobjects.home_page import HomePage
from pageobjects.search_list_page import SearchListPage


@allure.feature("首页")
@pytest.mark.usefixtures('geekbang_login')
class TestLoginPage(object):


    @pytest.mark.parametrize("search_value",["自动化测试", "接口自动化"])
    @allure.story("查询功能")
    @get_ErrImage
    def test_search(self, search_value):
        '''
        正常登录验证
        '''
        homepage = HomePage(self.driver)
        slpage = SearchListPage(self.driver)

        homepage.enter_search(search_value)
        homepage.click_search()
        slpage.switch_window()
        course_name = slpage.get_search_course_value(3)
        assert search_value in course_name


