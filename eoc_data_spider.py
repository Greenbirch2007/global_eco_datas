#! -*- coding:utf-8 -*-

import requests
import re




# 正则解析吧，bs4还是比较烂！ 正则绝对不会失效，但是bs4文档的例子都是错的！

#请求的函数
def call_page(url):

    try:
        response = requests.get(url)
        response.encoding = 'utf-8'    #响应解码
        if response.status_code == 200:
            return response.text
        else :
            return None
    except RequestException:
        return None

#
# def parse_all_links(html):
#
#     pattern = re.compile('.*?&nbsp;<a href="(.*?)"><font>', re.S)
#     items = re.findall(pattern,html)
#     for item in items:
#         print(item)
#
#
#
# url = 'http://www.8pu.com/gdp/ranking_2017.html'
# html = call_page(url)
#
# print(parse_all_links(html))


# def parse_one_country(html):
#     patt = re.compile()
#     item1s =



url = 'http://www.8pu.com/country/USA/'

print(call_page(url))




