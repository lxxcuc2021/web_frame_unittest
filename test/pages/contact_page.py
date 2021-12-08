# -*- coding:utf-8 -*-
# @Time : 2021/11/25 
# @Author : lixx
# @File : contact_page.py
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from web_frame.BasePage.base_page import BasePage


class ContactPage(BasePage):
	"""
	新建联系人
	"""
	# 页面元素
	contact_tab_loc = (By.XPATH, '//li[@id="_mail_tabitem_1_134"]')
	add_button_loc = (By.XPATH, "//span[text()='新建联系人']/..")
	name_loc = (By.ID, 'input_N')
	email_loc = (By.XPATH, "//div[@id='iaddress_MAIL_wrap']/dl/dd/div/input")
	commit_loc = (By.XPATH, "//span[text()='确 定']")
	close_button = (By.XPATH, "//span[text()='关 闭']")

	search_loc = (By.XPATH, "//input[contains(@id,'_searchInput_inputId')]")
	search_result_loc = (By.XPATH, "//div[@title='联系人列表区']/section/div[2]/table/tbody/tr/td[4]")

	check_box_loc = (By.XPATH, "//div[@title='联系人列表区']/section/div[2]/table/tbody/tr/td[2]")
	write_button_loc = (By.XPATH, "//div[contains(@id,'mail_toolbar')]/div[2]/div")
	subject_loc = (By.XPATH, "//input[contains(@id,'subjectInput')]")
	attachment_loc = (By.XPATH, "//input[@type='file']")
	send_button_loc = (By.XPATH, "//span[text()='发送']")
	send_email_tab_loc = (By.XPATH, "//li[contains(@title,subject)]")
	send_result_loc = (By.XPATH, "//h1[contains(@id,'succInfo')]")
	tabs_loc = (By.XPATH, "//div[@id='dvMultiTab']/ul/li")



	# 页面动作
	def add_contact(self, username, email):
		"""
		添加联系人
		"""
		self.click(ContactPage.contact_tab_loc)
		self.click(ContactPage.add_button_loc)
		self.input(ContactPage.name_loc, username)
		self.input(ContactPage.email_loc, email)
		self.click(ContactPage.commit_loc)
		self.click(ContactPage.close_button)

	def search_contact(self, name):
		"""
		搜索联系人
		"""
		self.input(ContactPage.search_loc, name)
		time.sleep(3)
		return self.get_text(ContactPage.search_result_loc)

	def send_email(self, subject, attachment):
		"""
		选择联系人发送email
		"""
		self.click(ContactPage.check_box_loc)
		self.click(ContactPage.write_button_loc)
		time.sleep(3)
		self.input(ContactPage.subject_loc, subject)
		self.input(ContactPage.attachment_loc, attachment)
		self.click(ContactPage.send_button_loc)
		time.sleep(3)
		# print(self.locators(ContactPage.tabs_loc))
		self.locators(ContactPage.tabs_loc)[-2].click()
		time.sleep(3)
		print(self.get_text(ContactPage.send_result_loc))
		return self.get_text(ContactPage.send_result_loc)



