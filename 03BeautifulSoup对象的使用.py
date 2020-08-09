# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:22:19 2020

@author: admin
"""

#1.导入模块 
from bs4 import BeautifulSoup

#2.创建BeautifulSoup对象
soup = BeautifulSoup('<html>data</html>','lxml')#指明解析器
print(soup)
