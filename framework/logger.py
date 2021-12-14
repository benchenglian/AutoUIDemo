#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/12/13  10:44 上午
@Author  : Frank.lian
@File    : logger.py
@Description :
"""
import logging
import os.path
import time


class Logger(object):
    # __init__相当于构造方法，创建对象后立即调用。
    def __init__(self, logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger，返回一个名称为“logger参数name"的Logger实例。
        self.logger = logging.getLogger(logger)
        # 设置一个log 等级
        self.logger.setLevel(logging.DEBUG)

        # strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间

        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

        '''
         os.path.dirname去掉文件名返回目录。
         os.path.abspath返回绝对路径'.'是返回当前项目路径
         log_path值是当前项目路径+/logs/
        '''

        log_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/logs/'
        # log_name:xxxx(项目路径)/logs/当前时间.log

        log_name = log_path + rq + '.log'

        # 创建一个handler,用于写日志文件，log等级为INFO
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式;
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
