# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:11:35 2020

@author: admin
"""
#1.导入模块 
import requests

#2.发送请求，获取响应
response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")

#3.从响应中获取数据
# print(response.text)
print(response.content.decode())
