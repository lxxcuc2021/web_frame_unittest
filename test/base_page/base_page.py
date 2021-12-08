#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import time
from selenium.common.exceptions import NoSuchElementException
import os
from web_frame_unittest.config import globalconfig
from web_frame_unittest.utils.log import Logger

logger = Logger(logger='BasePage').getlog()

class BasePage(object):
	"""
	定义一个基类，封装常用的页面方法
	"""
	def __init__(self, driver):
		"""
		:param driver: 浏览器驱动
		"""
		self.driver = driver

	# 打开页面
	def open_page(self):
		self.driver.maximize_window()
		self.driver.get(self.base_url)
		sleep(1)

	# 定位单个元素
	def locator(self, loc):
		try:
			element = self.driver.find_element(*loc)
			logger.info('find the element successful')
			return element
		except NoSuchElementException as e:
			logger.error('NoSuchElementException:{0}'.format(e))
			self.get_windows_img()

	# 定位多个元素
	def locators(self, loc):
		try:
			element = self.driver.find_elements(*loc)
			logger.info('find the elements successful')
			return element
		except NoSuchElementException as e:
			logger.error('NoSuchElementException:{0}'.format(e))
			self.get_windows_img()

	# 文本框输入
	def input(self, loc, text):
		# self.locator(loc).clear()
		try:
			self.locator(loc).send_keys(text)
			logger.info('type {} in inputbox'.format(text))
		except NameError as e:
			logger.error('fail to type in inputbox with {}'.format(e))
			self.get_windows_img()

	# 点击
	def click(self, loc):
		self.locator(loc).click()

	# 浏览器最大化
	def max_window(self):
		self.driver.maximize_window()

	# 设置浏览器的大小
	def set_window(self, width, height):
		self.driver.set_window_size(width, height)

	# 退出浏览器
	def quit(self):
		self.driver.quit()

	# 浏览器前进
	def forward(self):
		self.driver.forward()

	# 浏览器后退
	def back(self):
		self.driver.back()

	# 隐式等待
	def wait(self, second):
		self.driver.implicitly_wait(second)

	# 关闭当前窗口
	def close(self):
		try:
			self.driver.close()
		except NameError as e:
			print('Fail to close')

	# 保存图片
	def get_windows_img(self):
		img_path = globalconfig.report_path+'/screenpicture'
		img_name_format = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
		image_name = os.path.join(img_path, '{0}.png'.format(img_name_format))
		try:
			self.driver.get_screenshot_as_file(image_name)
			logger.info('take screenshot and save to folder:/screenshots')
		except NameError as e:
			logger.error('fail to take screenpicture!{0}'.format(e))
			self.get_windows_img()

	# 浏览器刷新
	def refresh(self):
		self.driver.refresh()

	# 返回弹框页面
	def switch_alert(self):
		return self.driver.switch_to.alert

	# 进入frame关键字
	def goto_frame(self, frame_ref):
		self.driver.switch_to.frame(frame_ref)

	# 出frame关键字
	def default_frame(self):
		self.driver.switch_to.default_content()

	# 获取元素文本值
	def get_text(self, loc):
		return self.locator(loc).text

	# 获取元素属性值
	def get_attr_value(self, loc, attr):
		return self.locator(loc).get_attribute(attr)
