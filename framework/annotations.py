#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  10:43 上午
@Author  : Frank.lian
@File    : annotations.py
@Description : case 断言失败截图装饰器
'''
from functools import wraps
import allure
import time
import os

def get_ErrImage(func):
    # 保持传入的case的名称不被装饰器所改变
    @wraps(func)
    def get_screenshot_about_case(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            # 截屏的路径
            file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/screenshots/error/'
            # 获得现在的时间戳
            rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            # 组装图片名称
            screen_name = file_path + rq + '.PNG'
            # 截图并保存到相应的名称的路径
            self.driver.get_screenshot_as_file(screen_name)
            allure.attach(rq, self.driver.get_screenshot_as_png(), allure.attachment_type.PNG)
            raise e
    return get_screenshot_about_case