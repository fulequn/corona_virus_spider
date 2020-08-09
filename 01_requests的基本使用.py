# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:04:09 2020

@author: admin
"""

#1. 导入模块
import requests

#2. 发送请求，获取相应
response = requests.get('https://www.baidu.com/')
# print(response)
#3. 获取响应数据
# print(response.encoding)#二进制转换字符使用的编码
# print(response.text)#响应体str类型
# print(response.content)#响应体bytes类型
print(response.content.decode())#根据对应的编码进行解析