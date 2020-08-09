# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:03:17 2020

@author: admin
"""

#导入正则模块
import re

#字符匹配
rs = re.findall('abc', 'abc')
rs = re.findall('a.c','abc')
rs = re.findall('a.c','a\nc')
rs = re.findall('a\.c','a.c')
rs = re.findall('a\.c','a.c')
rs = re.findall('a[bd]c','abc')

#预定义的字符集
rs = re.findall('\d', '123')#数字
rs = re.findall('\w', 'Az_123中文@#%$')#字母数字下划线中文

#数量词
# * 0或者无限次
# + 1或者无限次
# ? 0或者1次
# {m} m次
rs = re.findall('a\d*', 'a123')#数字
rs = re.findall('a\d*', 'a')#数字
rs = re.findall('a\d+', 'a123')#数字
rs = re.findall('a\d+', 'a')#数字
rs = re.findall('a\d?', 'a2')#数字
rs = re.findall('a\d?', 'a123')#数字
rs = re.findall('a\d{2}', 'a123')#数字
print(rs)