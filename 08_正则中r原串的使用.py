# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:19:56 2020

@author: admin
"""

import re

#1. 在不使用r原串的情况下，遇到转义符
rs = re.findall('a\nbc', 'a\\nbc')
print(rs)

rs = re.findall('a\\nbc', 'a\\nbc')
print(rs)

rs = re.findall('a\\\nbc', 'a\\nbc')
print(rs)

rs = re.findall('a\\\\nbc', 'a\\nbc')
print(rs)

#r原串在正则中可以消除转义符带来的影响
rs = re.findall(r'a\\nbc', 'a\\nbc')
print(rs)

rs = re.findall(r'a\nbc', 'a\nbc')
print(rs)

#拓展：可以解决写正则的时候，不符合PEP8规范的问题
rs = re.findall(r'\d', 'a123')
print(rs)