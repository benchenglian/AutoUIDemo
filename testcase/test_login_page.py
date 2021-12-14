#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/12/13  10:48 上午
@Author  : Frank.lian
@File    : test_login_page.py
@Description :
"""
import allure, pytest
from framework.annotations import get_ErrImage
from pageobjects.login_page import LoginPage
from pageobjects.home_page import HomePage


@allure.feature("登录页面")
@pytest.mark.usefixtures('driver_setup')
class TestLoginPage(object):

    @allure.story("合法登录")
    @get_ErrImage
    def test_legal_login(self):
        '''
        正常登录验证
        '''
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.login_account_password("username", "password")
        assert homepage.get_username() == '阿廉'  # 断言用户名称

    search_value = [("13269000012", "adfjkoiosd", "该账号不存在"), ("18510601975", "adfjkoiosd", "密码错误")]

    @pytest.mark.parametrize("username,password,expected", search_value)
    @allure.story("非法登录")
    @get_ErrImage
    def test_illegality_login(self, username, password, expected):
        '''
        非法登录验证
        '''
        loginpage = LoginPage(self.driver)
        loginpage.login_account_password(username, password)
        assert loginpage.get_error() == expected
