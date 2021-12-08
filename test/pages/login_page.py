#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


from web_frame_unittest.test.base_page.base_page import BasePage
from web_frame_unittest.utils.read_excel import ReadExcel


# 定义TestData类，处理excel数据，得到测试所需数据
class TestData(object):

    def get_data(self):
        # 获取excel文件数据
        excel = ReadExcel(sheet_name='Login')
        file_data = excel.excel_reader()
        # 得到所需数据的索引，根据索引获取相应顺序的数据
        user_index = file_data[0].index('用户名')
        pwd_index = file_data[0].index('密码')
        type_index = file_data[0].index('类型')
        assert_index = file_data[0].index('预期结果')

        row_num = len(file_data)
        print(row_num)
        all_data = []
        for i in range(1, row_num):
            row_data = []
            row_data.append(file_data[i][user_index])
            row_data.append(file_data[i][pwd_index])
            row_data.append(file_data[i][type_index])
            row_data.append(file_data[i][assert_index])
            all_data.append(row_data)
        return all_data

class LoginPage(BasePage, unittest.TestCase):
    """
    登录页面
    """

    #
    username_loc = (By.XPATH, "//input[@class='email']")
    passwd_loc = (By.XPATH, "//input[@class='password']")
    button_loc = (By.XPATH, '//input[@type="button"]')
    title_loc = (By.XPATH, "//h1[text()='TYNAM后台管理系统']")
    email_error_loc = (By.XPATH, "//div[contains(text(),'邮箱')]")
    passwd_error_loc = (By.XPATH, "//div[contains(text(),'密码')]")

    def login(self, name, pwd):
        """
        登录
        """
        if name is not None:
            self.input(self.username_loc, name)
        if pwd is not None:
            self.input(self.passwd_loc, pwd)
        self.click(self.button_loc)

    def get_assert_msg(self, result_type):
        if result_type == 'login success':
            assert_msg = self.get_text(self.title_loc)
        elif result_type == 'email error':
            assert_msg = self.get_text(self.email_error_loc)
        elif result_type == 'password error':
            assert_msg = self.get_text(self.passwd_error_loc)
        else:
            assert_msg = self.switch_alert().text
            self.switch_alert().accept()
        return assert_msg





# if __name__ == '__main__':
#     data1 = TestData().get_data()
#     print(data1)

