#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/1 
# @Author : lixx
# @File : student_page.py
import time
import unittest

from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By

from web_frame_unittest.test.base_page.base_page import BasePage

@ddt
class StudentPage(BasePage):
	"""
	学生管理页面
	"""
	add_button_loc = (By.ID, 'add')
	edt_button_loc = (By.ID, 'edt')
	del_button_loc = (By.ID, 'del')
	id_loc = (By.XPATH, "//div[@id='add-dialog']/div[2]/input")
	name_loc = (By.XPATH, "//div[@id='add-dialog']/div[3]/input")
	sex_loc = (By.XPATH, "//div[@id='add-dialog']/div[4]/input")
	grade_loc = (By.XPATH, "//div[@id='add-dialog']/div[5]/input")
	confirm_button_loc = (By.XPATH, "//div[@id='add-dialog']/button[1]")

	def add_student(self, sid, name, sex, grade):
		"""
		添加学生信息
		"""
		self.click(self.add_button_loc)
		time.sleep(1)
		self.input(self.id_loc, sid)
		self.input(self.name_loc, name)
		self.input(self.sex_loc, sex)
		self.input(self.grade_loc, grade)
		time.sleep(3)
		self.click(self.confirm_button_loc)



if __name__ == '__main__':
	StudentPage().add_student('1001', 'lily', 'Female', '一年级二班')
	#
	# @data(['1001', 'lily', 'Female', '一年级二班'])
	# @unpack
