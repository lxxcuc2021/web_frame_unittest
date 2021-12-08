#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/1 
# @Author : lixx
# @File : my_unit.py

import unittest
from selenium import webdriver
from web_frame_unittest.test.pages.login_page import LoginPage


class MyUnitLogin(unittest.TestCase):

	driver = None

	@classmethod
	def setUpClass(cls) -> None:
		cls.driver = webdriver.Chrome()
		cls.driver.get("http://180.76.233.247:8080/#")
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(5)
		cls.lp = LoginPage(cls.driver)
		cls.lp.login('admin@tynam.com', 'tynam123')

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.close()
