# -*- coding:utf-8 -*-
# Time:2023-04-17 18:11
# Author:Zhangfuqi
# File:base.py
# Desc:
"""
base类：存放所有page页面，公共的操作方法！【首先要分析有哪些公共方法】
"""
from selenium.webdriver.support.wait import WebDriverWait
class Base:
    def __init__(self,driver):
        self.driver=driver
    #大前提：找到元素，查找元素方法
    def base_find(self,loc,timeout=10,poll_frequency=0.5):
        #显示等待的好处，可以找元素，可以等待 loc=(By.id,'#userA')#直接用显示等待，把其余元素都封进来。提取元组
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))
    #loc[0],loc[1]) 实际上就是按顺序提取两个，可以写成*loc，前面已经验证过正确了 *loc=loc[0][1] ** 是对字典解包
    #输入方法
    def base_input(self,loc,value):
        #获取元素
        el=self.base_find(loc)#初始化这个对象
        #清空操作，你不清空，前面可能有存留的内容
        el.clear()
        #输入方法
        el.send_keys(value)
        #没有的方法就网上补，谁用谁传
    #点击方法
    def base_click(self,loc):
        self.base_find(loc).click()
    #获取文本值方法
    def base_get_text(self,loc):
        return self.base_find(loc).text  #为什么是返回，因为后面需要对比是否文本一直。没有的就给我传