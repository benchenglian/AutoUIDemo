#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  10:48 上午
@Author  : Frank.lian
@File    : login_page.py
@Description : 登录页
'''
from framework.base_page import Base


class LoginPage(Base):

    username = "xpath=>//*[@placeholder='手机号']"
    password = "xpath=>//*[@placeholder='密码']"
    login_bt = "xpath=>//*[@gkbtn-color='login']"
    agree = "xpath=>//*[@id='agree']"
    def login_account_password(self, username, password):
        """
        账号和密码登录
        :param username:用户名
        :param password:密码
        """
        self.enter(self.username,username)
        self.enter(self.password,password)
        self.click_element(self.agree)
        self.click_element(self.login_bt)

    error_value = "xpath=>//*[@class='gkui-form-error']"

    def get_error(self):
        """
        获取错误提示
        :return: 返回错误值
        """
        return self.get_text(self.error_value)