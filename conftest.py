#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/12/13  10:40 上午
@Author  : Frank.lian
@File    : conftest.py
@Description :
"""

import pytest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
from pageobjects.home_page import HomePage


@pytest.fixture()
def driver_setup(request):
    # addfinalizer 无论fixture中setup代码是否引发异常,都将始终调用teardown代码。
    browser = BrowserEngine(request)
    request.instance.driver = browser.open_brower(request)

    def driver_teardown():
        request.instance.driver.quit()

    request.addfinalizer(driver_teardown)


@pytest.fixture()
def geekbang_login(request):
    """
    testcase对登录有依赖fixture调用此方法
    """
    browser = BrowserEngine(request)
    request.instance.driver = browser.open_brower(request)
    login_page = LoginPage(request.instance.driver)
    login_page.login_account_password("username", "password")# 录入正确账号/密码。
    home_page = HomePage(request.instance.driver)
    home_page.click_close()
    def driver_teardown():
        request.instance.driver.quit()

    request.addfinalizer(driver_teardown)
