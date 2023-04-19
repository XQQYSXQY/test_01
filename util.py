# -*- coding:utf-8 -*-
# Time:2023-04-17 21:06
# Author:Zhangfuqi
# File:util.py
# Desc:
import json
import os


def read_json(filename,key):
    filepath=os.path.dirname(__file__)+ os.sep + "data" + os.sep +filename#绝对路径
    zuzhuang=[ ]
    with open(filepath,'r',encoding='utf-8') as f:
        for data in json.load(f).get(key):
            zuzhuang.append(tuple(data.values())[1:])#我们需要的是参数值,但是格式不对，我们需要重新组织。在列表中的增加进去.tuple转换元组
            #后面那个是切片，因为登录成功没有用
        return zuzhuang
# if __name__ == '__main__':
#     print(read_json("login.json","login"))