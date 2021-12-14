#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  10:44 上午
@Author  : Frank.lian
@File    : browser_engine.py
@Description : 浏览器初始化
'''
import configparser
import os.path
import selenium
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

# 运行环境：0.测试服务器 1.本地  2.测试服务器-VNC可视化
runenv = 1


class BrowserEngine(object):
    chrome_options = webdriver.ChromeOptions()
    if runenv == 1:
        # 本地
        chrome_driver_path = "/Users/frank.lian/PycharmProjects/AutoUIDemo/tools/chromedriver"
    elif runenv == 0:
        # 测试服务器
        chrome_options.add_argument("--headless")

    def __init__(self, driver):
        self.driver = driver

    def open_brower(self, driver):
        # 读取配置文件
        config = configparser.ConfigParser()
        proDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        configPath = proDir + '/config/config.ini'
        logger.info("配置文件路径{}".format(configPath))
        path = os.path.abspath(configPath)

        config.read(path, encoding="utf-8")

        # 获取配置文件属性
        browser = config.get('browserType', 'browserName')
        logger.info("你选择{}浏览器.".format(browser))
        url = config.get("testServer", "url")
        logger.info("测试地址是{}".format(url))

        if browser == "Firefox":
            driver = webdriver.Firefox
            logger.info("打开Firefox浏览器")
        elif browser == "chrome":
            if runenv == 1:
                driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
            elif runenv == 2:
                # 可视化
                # 远程链接docker-seleniumhub
                driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://远程hub地址/wd/hub",
                                                                       desired_capabilities=DesiredCapabilities.CHROME)
            else:
                # 无头
                driver = selenium.webdriver.remote.webdriver.WebDriver(
                    command_executor="http://远程hub地址/wd/hub",
                    desired_capabilities=DesiredCapabilities.CHROME, options=self.chrome_options)

            logger.info("打开Chrome浏览器")
        elif browser == "IE":
            driver = webdriver.Ie
            logger.info("打开IE浏览器")

        driver.get(url)
        logger.info("打开URL{}:".format(url))
        driver.maximize_window()
        driver.implicitly_wait(10)
        logger.info("设置隐性等待10秒")
        return driver

    def quit_browser(self):
        logger.info("关闭、退出浏览器")
        self.driver.quit()
