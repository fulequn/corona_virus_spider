# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:25:12 2020

@author: admin
"""

#思路
# 1. 发送请求,获取疫情首页
# 2. 从疫情首页中提取最近一日各国疫情字符串
# 3. 从最近一日各国疫情字符串中,提取json格式字符串
# 4. 把json格式字符串，转换为Python类型
# 5. 把Python类型的数据,以json格式存入文件中


# 》重构原来代码,以提高扩展性
#   把功能封装到一个类中
#   每一个小功能变成一个方法
#   通过run方法启动爬虫
# 》实现采集从01月23日以来的世界各国疫情数据
#   》加载最近一日各国疫情数据
#   》遍历各国疫情数据，获取从01月23日以来的各个国家疫情的URL
#   》发送请求,获取获取从01月23日以来的各个国家疫情的json字符串
#   》解析各个国家疫情的json字符串,添加到列表
#   》以json格式保存从01月23日以来的各个国家疫情数据

import requests
from bs4 import BeautifulSoup
import re
import json
from  tqdm import tqdm


class CoronaVirusSpider(object):
    
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        '''
        根据URL,获取响应内容的字符串数据
        :param url: 请求的URL
        :return: 响应内容的字符串
        '''
        response = response = requests.get(url)
        home_page = response.content.decode()
        return home_page

    def parse_home_page(self, home_page):
        '''
        解析首页内容，获取解析后的Python数据
        :param home_page: 首页的内容
        :return: 解析后的python数据
        '''
        # 2. 从疫情首页中提取最近一日各国疫情字符串
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id='getListByCountryTypeService2true')
        text = script.string
        # print(text)
        
        # 3. 从最近一日各国疫情字符串中,提取json格式字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)
        
        # 4. 把json格式字符串，转换为Python类型
        data = json.loads(json_str)
        return data
    
    def save(self, data, path):
        # 5. 把Python类型的数据,以json格式存入文件中
        with open(path, 'w', encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False)
            
    def crawl_last_day_corona_virus(self):
        '''
        采集最近一天的各国疫情信息
        '''
        # 1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析首页内容，获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page)
        # 3.保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')
    
    def crawl_corona_virus(self):
        '''
        采集从1月23日以来的各国疫情数据
        '''
        #   》加载最近一日各国疫情数据
        with open('data/last_day_corona_virus.json', encoding="utf-8") as fp:
            last_day_corona_virus = json.load(fp)
        # print(last_day_corona_virus)
        #   》遍历各国疫情数据，获取从01月23日以来的各个国家疫情的URL
        corona_virus = []
        for country in tqdm(last_day_corona_virus, '采集1月23日以来各国疫情信息'):
            #   》发送请求,获取获取从01月23日以来的各个国家疫情的json字符串
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            #   》解析各个国家疫情的json字符串,添加到列表
            statistics_data = json.loads(statistics_data_json_str)['data']
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            #append整体放列表，extend元素放列表
            corona_virus.extend(statistics_data)
        #   》以json格式保存从01月23日以来的各个国家疫情数据
        self.save(corona_virus, 'data/corona_virus.json')
        
        
    def run(self):
        self.crawl_last_day_corona_virus()
        
if __name__ == '__main__':
    spider = CoronaVirusSpider()
    # spider.run()
    spider.crawl_corona_virus()

