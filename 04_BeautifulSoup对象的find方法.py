# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:56:44 2020

@author: admin
"""
#根据标签名查找
#1.导入模块 
from bs4 import BeautifulSoup

#2.文档内容
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<h1>我的第一个标题</h1>
<p>我的第一个段落。</p>

</body>
</html>
"""
#3.创建BeautifulSoup对象
soup = BeautifulSoup(html, 'lxml')

#4.查找title标签
title = soup.find('title')
print(title)

#5. 查找a标签
a = soup.find('a')
print(a)

#6. 查找所有的a标签
a_s = soup.find_all('a')
print(a_s)

#二、根据属性进行查找
#查找id为link1的标签
#方式1： 通过命名参数进行制定的
a = soup.find(id="link1")
print(a)
#方式2： 通过attrs来指定属性字典，进行查找
a = soup.find(attrs={'id': 'link1'})
print(a)


#三、根据文本内容进行查找
text = soup.find(text = "Elsie")
print(text)

#Tag对象
#对应原始文档的XML和HTML标签
#属性有
# name 姓名
# attrs 属性
# text 文档内容
print(type(a))
print(a.name)
print(a.attrs)
print(a.text)
