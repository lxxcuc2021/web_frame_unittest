#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/1 
# @Author : lixx
# @File : test_student.py
from web_frame_unittest.test.pages.student_page import StudentPage
from ddt import ddt, data, unpack
from web_frame_unittest.test.testcase.my_unit_login import MyUnitLogin


@ddt
class TestStudent(MyUnitLogin):
	"""
	测试学生信息页
	"""

	@data(['1001', 'lily', 'Female', '一年级二班'])
	@unpack
	def test_01_add(self, sid, name, sex, grade):
		sp = StudentPage(TestStudent.driver)
		sp.add_student(sid, name, sex, grade)

