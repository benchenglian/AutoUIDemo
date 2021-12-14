#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/14  10:40 上午
@Author  : Frank.lian
@File    : search_list_page.py
@Description : 查询列表页
'''
from framework.base_page import Base


class SearchListPage(Base):

    course_list = "xpath=>//*[@class='SearchPc_result_1n5du']/div"

    def get_search_course_value(self, num):
        """
        获取查询后课程名称
        :param num: 获取查询后列表的第几个元素
        :return:
        """
        course_value = "{}{}".format(self.course_list, [num], "/div/div[2]/div/h3")
        return self.get_text(course_value)
