# -*- coding:utf-8 -*-
# Time:2023-04-17 18:45
# Author:Zhangfuqi
# File:page_login.py
# Desc:
"""
模块名：page_模块名
类名：大驼峰
方法：当前页面要操作哪些元素，就封装哪些方法
"""
from selenium.webdriver.common.by import By

from base.base import Base
#用户名
username=By.CSS_SELECTOR,'#username'#实际上是元组元组类型。搜易
#密码
pwd=By.CSS_SELECTOR,'#password'
#验证码
verify_code=By.CSS_SELECTOR,'#verify_code'
#登录按钮
login_btn=By.CSS_SELECTOR,'.J-login-submit'
#获取昵称
nick_name=By.CSS_SELECTOR,'.userinfo'
class PageLogin(Base):#这里需要继承，因为继承之后，啥都能用了#继承方便
    #输入用户名
    def __page_username(self,value):  #__变成私有的，防止干扰我们。因为后面也基本不会用到
        self.base_input(username,value)
    #输入密码
    def __pase_pwd(self,value):
        self.base_input(pwd,value)
    #输入验证码
    def __page_verify_code(self,value):
        self.base_input(verify_code,value)

    #点击登录
    def page_click_login_btn(self):
        self.base_click(login_btn)
    #获取昵称
    def page_get_nickname(self):#获取就给return
        return self.base_get_text(nick_name)
    #组合业务（这个是最好写，给测试用的，先强调这个方法，便捷）
    def page_login(self,phone,password,code):#这些就传入到相应的value中
        self.__page_username(phone)
        self.__pase_pwd(password)
        self.__page_verify_code(code)
        self.page_click_login_btn()
