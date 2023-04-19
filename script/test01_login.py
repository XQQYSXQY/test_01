# -*- coding:utf-8 -*-
# Time:2023-04-17 20:04
# Author:Zhangfuqi
# File:test01_login.py
# Desc:
"""
主要是进行调用
"""
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from page.page_login import PageLogin
from parameterized import  parameterized#参数化用

from util import read_json
from log.log import loggers

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        e = Service(executable_path=r'F:\driver\chromedriver.exe')  # 驱动的路径，驱动也参数化 在config中国
        self.driver = webdriver.Chrome(service=e)  # 这里浏览器是大写，返回对象一般就是driver
        # 输入url
        self.driver.maximize_window()  # 这个是最大化
        self.driver.get('http://localhost/index.php/Home/user/login.html')  # 注意这个就是url的参数化了
        self.login=PageLogin(self.driver)
    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized.expand(read_json("login.json", "login"))  # 顺序一定要一样
    def test01_login(self,phone,password,code,expect_text):
          self.login.page_login(phone,password,code)
          #断言
          nickname=self.login.page_get_nickname()
          print('nickname',nickname)
          self.assertEqual(nickname,expect_text)#做了断言，注意关键字
          # loggers.info('有效的用户名和密码，加载成功')

