# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:12:41 2020

@author: admin
"""

import re

#1. findall方法，返回匹配的结果列表
rs = re.findall('\d+', 'chuan12zhi24')
print(rs)

#2. findall方法，flag函数的作用
# rs = re.findall('a.bc', 'a\nbc')#不能匹配特殊字符
rs = re.findall('a.bc', 'a\nbc', re.DOTALL)#可以匹配结果
rs = re.findall('a.bc', 'a\nbc', re.S)#可以匹配结果
print(rs)

#3. findall方法中分组的使用
#返回整个列表
rs = re.findall('a.+bc', 'a\nbc', re.DOTALL)
print(rs)

#分组
#两边字符用于定位，只返回()匹配的内容列表
rs = re.findall('a(.+)bc', 'a\nbc', re.DOTALL)
print(rs)
