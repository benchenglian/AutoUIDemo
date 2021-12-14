#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/13  10:43 上午
@Author  : Frank.lian
@File    : base_page.py
@Description :
'''
import time

from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from framework.logger import Logger

logger = Logger(logger="Base").getlog()


class Base(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_context(self):
        # ct = self.driver.current_context
        ch = self.driver.contexts
        # cu = self.driver.current_url
        logger.info("打印当前支持的{}".format(ch))
        # print('当前所有上下文{}'.format(ch))
        # ct = self.driver.current_window_handle
        # print(ct)

    # 录入
    def enter(self, selector, text):
        el = self.find_element(selector)
        #el.clear()
        try:
            el.send_keys(text)
            logger.info("在文本框录入 \' %s \' 数据" % text)
        except AttributeError as e:
            logger.error("未能在文本框中录入 %s" % e)

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            logger.info("在录入前清除文本框文本")
            el.clear()
        except AttributeError as e:
            logger.error("清除文本框文本失败 %s" % e)

    # 点击元素
    def click_element(self, selector):
        selector_value = selector.split('=>')[1]
        try:
            #el = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, selector_value)))
            el = WebDriverWait(self.driver, 10, 2).until(
                lambda driver: self.driver.find_element(By.XPATH, selector_value))
            logger.info("获取元素 \' %s \' 成功 ""by %s 值为: %s " % (el.text, 'xpath', selector_value))
            logger.info("该元素 \' %s \' 已被点击." % el.text)
            el.click()
        except AttributeError as e:
            logger.error("点击元素失败 %s" % e)

    # 切换上下文
    def switch_context(self, contextname):
        contexts = self.driver.contexts
        try:
            for context in contexts:
                if contextname in context:
                    return context
        except ValueError as e:
            print("没找到对应的上下文{}".format(e))

    # 切换到最新窗口句柄
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    # 获取元素text值
    def get_text(self, selector):
        selector_value = selector.split('=>')[1]
        el = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, selector_value)))
        ts = el.text
        logger.info("获取元素text %s" % ts)
        return ts

    def is_element_displayed(self, selector):
        selector_value = selector.split('=>')[1]
        el = WebDriverWait(self.driver, 10, 2).until(
                lambda driver: self.driver.find_element(By.XPATH, selector_value))
        if len(el) == 0:
            logger.info("元素未找到{}".format(el))
            return False
        elif len(el) == 1:
            return True
        else:
            logger.info("找到{}个元素：{}".format(len(el), el))
            return False

    # 判断元素是否在页面，显示则点击
    def element_displayed(self, selector):
        el = self.find_element(selector)
        for num in range(1, 11):
            if el.is_displayed():
                logger.info("该元素在页面显示，向下执行")
                self.click_element(selector)
                break
            elif num == 10:
                logger.info("循环10次退出循环")
                break
            elif num < 10:
                logger.info("休眠一秒后再判断")
                time.sleep(1)
                continue

    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element(By.ID, selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # id定位
        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element(By.ID, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)

        # name定位
        elif selector_by == "n" or selector_by == 'name':
            try:
                element = self.driver.find_element(By.NAME, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)


        # class_name定位
        elif selector_by == "c" or selector_by == 'class_name':
            try:
                element = self.driver.find_element(By.CLASS_NAME, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)

        # link_text定位
        elif selector_by == "l" or selector_by == 'link_text':
            try:
                element = self.driver.find_element(By.LINK_TEXT, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)


        # partial_link_text定位
        elif selector_by == "p" or selector_by == 'partial_link_text':
            try:
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)

        # tag_name定位
        elif selector_by == "t" or selector_by == 'tag_name':
            try:
                element = self.driver.find_element(By.TAG_NAME, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)

        # xpath定位
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element(By.XPATH, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)

        # selector_selector定位
        elif selector_by == "s" or selector_by == 'selector_selector':
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector_value)
                logger.info("获取元素 \' %s \' 成功 "
                            "by %s 值为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)

        else:
            raise AttributeError("Please enter a valid type of targeting elements.")
        return element
