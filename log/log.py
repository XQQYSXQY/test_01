# -*- coding:utf-8 -*-
# Time:2023-04-18 10:08
# Author:Zhangfuqi
# File:log.py.py
# Desc:
import logging
loggers=logging.getLogger()
loggers.setLevel(logging.INFO)#设置文件的级别

format=logging.Formatter('%(asctime)s %(filename)s %[line:%(lineno)d] %(levelname)s %(message)s')#显示格式 显示时间、文件名、显示行
f=logging.FileHandler(r'D:\PO\log\log.py',mode='a',encoding='utf-8')#就是打开那个文件,一定要到文件，不到目录
f.setLevel(logging.INFO)#处理器也要设置级别
f.setFormatter(format)
#处理器要加载到日志器
#添加到日志器
loggers.addHandler(f)#接下来就是调用