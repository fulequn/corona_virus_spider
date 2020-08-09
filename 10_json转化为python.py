# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:30:54 2020

@author: admin
"""
import json

# 1.把JSON字符串转化为PYTHON数据
# 1.1准备JSON字符串
json_str = '''[
    {
        "id": 1, 
        "name": "男士", 
        "productTypeDtos": [
            {
                "id": 23, 
                "name": "上装", 
                "productTypeDtos": [
                    {
                        "id": 33, 
                        "name": "毛衣"
                    }, 
                    {
                        "id": 34, 
                        "name": "T恤"
                    }, 
                    {
                        "id": 35, 
                        "name": "衬衫"
                    }, 
                    {
                        "id": 36, 
                        "name": "卫衣"
                    }, 
                    {
                        "id": 37, 
                        "name": "背心"
                    }, 
                    {
                        "id": 38, 
                        "name": "针织衫"
                    }, 
                    {
                        "id": 39, 
                        "name": "POLO衫"
                    }
                ]
            }, 
            {
                "id": 24, 
                "name": "裤装", 
                "productTypeDtos": [
                    {
                        "id": 40, 
                        "name": "背带裤"
                    }, 
                    {
                        "id": 41, 
                        "name": "休闲裤"
                    }, 
                    {
                        "id": 42, 
                        "name": "短裤"
                    }, 
                    {
                        "id": 43, 
                        "name": "运动裤"
                    }, 
                    {
                        "id": 44, 
                        "name": "哈伦裤"
                    }, 
                    {
                        "id": 45, 
                        "name": "九分裤"
                    }, 
                    {
                        "id": 46, 
                        "name": "七分裤"
                    }, 
                    {
                        "id": 47, 
                        "name": "西裤"
                    }, 
                    {
                        "id": 48, 
                        "name": "牛仔裤"
                    }
                ]
            }, 
            {
                "id": 25, 
                "name": "外套", 
                "productTypeDtos": [
                    {
                        "id": 49, 
                        "name": "皮衣"
                    }, 
                    {
                        "id": 50, 
                        "name": "风衣"
                    }, 
                    {
                        "id": 51, 
                        "name": "夹克"
                    }, 
                    {
                        "id": 52, 
                        "name": "便西"
                    }, 
                    {
                        "id": 53, 
                        "name": "马甲"
                    }, 
                    {
                        "id": 54, 
                        "name": "大衣"
                    }, 
                    {
                        "id": 55, 
                        "name": "羽绒服"
                    }
                ]
            }
        ]
    }, 
    {
        "id": 2, 
        "name": "女士", 
        "productTypeDtos": [
            {
                "id": 26, 
                "name": "上装", 
                "productTypeDtos": [
                    {
                        "id": 56, 
                        "name": "T恤"
                    }, 
                    {
                        "id": 57, 
                        "name": "衬衫"
                    }, 
                    {
                        "id": 58, 
                        "name": "上衣"
                    }, 
                    {
                        "id": 59, 
                        "name": "卫衣"
                    }, 
                    {
                        "id": 60, 
                        "name": "雪纺衫"
                    }, 
                    {
                        "id": 61, 
                        "name": "针织衫"
                    }, 
                    {
                        "id": 62, 
                        "name": "背心"
                    }
                ]
            }, 
            {
                "id": 27, 
                "name": "裤装", 
                "productTypeDtos": [
                    {
                        "id": 63, 
                        "name": "打底裤"
                    }, 
                    {
                        "id": 64, 
                        "name": "休闲裤"
                    }, 
                    {
                        "id": 65, 
                        "name": "牛仔裤"
                    }, 
                    {
                        "id": 66, 
                        "name": "短裤"
                    }, 
                    {
                        "id": 67, 
                        "name": "连体裤"
                    }, 
                    {
                        "id": 68, 
                        "name": "七分裤"
                    }, 
                    {
                        "id": 69, 
                        "name": "九分裤"
                    }, 
                    {
                        "id": 70, 
                        "name": "哈伦裤"
                    }
                ]
            }, 
            {
                "id": 29, 
                "name": "裙装", 
                "productTypeDtos": [
                    {
                        "id": 71, 
                        "name": "连衣裙"
                    }, 
                    {
                        "id": 72, 
                        "name": "半身裙"
                    }, 
                    {
                        "id": 73, 
                        "name": "套裙"
                    }, 
                    {
                        "id": 74, 
                        "name": "迷你短裙"
                    }, 
                    {
                        "id": 75, 
                        "name": "礼服"
                    }
                ]
            }, 
            {
                "id": 28, 
                "name": "外套", 
                "productTypeDtos": [
                    {
                        "id": 76, 
                        "name": "风衣"
                    }, 
                    {
                        "id": 77, 
                        "name": "便西"
                    }, 
                    {
                        "id": 78, 
                        "name": "夹克"
                    }, 
                    {
                        "id": 79, 
                        "name": "马甲"
                    }, 
                    {
                        "id": 80, 
                        "name": "斗篷"
                    }, 
                    {
                        "id": 81, 
                        "name": "大衣"
                    }, 
                    {
                        "id": 82, 
                        "name": "羽绒服"
                    }, 
                    {
                        "id": 83, 
                        "name": "皮草"
                    }
                ]
            }, 
            {
                "id": 30, 
                "name": "内衣", 
                "productTypeDtos": [
                    {
                        "id": 84, 
                        "name": "内衣"
                    }
                ]
            }
        ]
    }, 
    {
        "id": 3, 
        "name": "童装", 
        "productTypeDtos": [
            {
                "id": 31, 
                "name": "男童", 
                "productTypeDtos": [
                    {
                        "id": 85, 
                        "name": "T恤"
                    }, 
                    {
                        "id": 86, 
                        "name": "外套"
                    }, 
                    {
                        "id": 87, 
                        "name": "卫衣"
                    }, 
                    {
                        "id": 88, 
                        "name": "衬衫"
                    }, 
                    {
                        "id": 89, 
                        "name": "裤子"
                    }
                ]
            }, 
            {
                "id": 32, 
                "name": "女童", 
                "productTypeDtos": [
                    {
                        "id": 90, 
                        "name": "连衣裙"
                    }, 
                    {
                        "id": 91, 
                        "name": "T恤"
                    }, 
                    {
                        "id": 92, 
                        "name": "卫衣"
                    }, 
                    {
                        "id": 93, 
                        "name": "背心"
                    }, 
                    {
                        "id": 94, 
                        "name": "礼服"
                    }, 
                    {
                        "id": 95, 
                        "name": "雪纺衫"
                    }, 
                    {
                        "id": 96, 
                        "name": "衬衫"
                    }, 
                    {
                        "id": 97, 
                        "name": "裤子"
                    }, 
                    {
                        "id": 98, 
                        "name": "半身裙"
                    }, 
                    {
                        "id": 99, 
                        "name": "外套"
                    }
                ]
            }
        ]
    }
]
'''
# 1.2把JSON字符串转化为PYTHON
rs = json.loads(json_str)
print(rs)
print(type(rs))#<class 'list'>
print(type(rs[0]))#<class 'dict'>

# 2.把JSON文件转化为PYTHON类型的数据
# 2.1构建指向该文件的文件对象
with open('data/test.json',encoding='UTF-8') as fp:
    #2.2 加载该文件对象，转化为PYTHON类型的数据
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))#<class 'list'>
    print(type(python_list[0]))