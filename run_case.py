#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  10:41 上午
@Author  : Frank.lian
@File    : run_case.py
@Description : 执行测试用例
'''
import os
import subprocess
from framework.logger import Logger

logger = Logger(logger="run_UI_Test").getlog()


def run_UI_Test():
    cmd = "python3 -m pytest -sq --reruns 3 -n 1 testcase --alluredir report/xml"
    subprocess.call(cmd, shell=True)
    logger.info("执行UI自动化测试")


def init_report():
    cmd = "allure generate --clean report/html report/xml -o report/html"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/report/html/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


if __name__ == "__main__":
    run_UI_Test()
    init_report()
