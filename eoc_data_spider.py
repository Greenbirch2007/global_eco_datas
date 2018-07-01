#! -*- coding:utf-8 -*-

import requests
import re
import pandas as pd




#请求的函数
# def call_page(url):
#
#     try:
#         response = requests.get(url)
#         response.encoding = 'utf-8'    #响应解码
#         if response.status_code == 200:
#             return response.text
#         else :
#             return None
#     except RequestException:
#         return None


#解析函数  表格数据解析多进行多个空列表处理！ 然后多个列表再拼接 不能一起爬了 还要用到pandas
# def parse_one_page(html):
#     patt = re.compile('<td width="100">(.*?).*?<td>(.*?)</td>.*?</tr>',re.S)
#     items = re.findall(patt,html)
#     for i in items:
#         print(i)




url = 'http://www.8pu.com/country/USA/'
data =pd.read_html(url)[3]
print(data)

# 表格类的数据爬取两种办法 一种是直接使用pandas的pd.read_html(url) 方法，
#第二种是from lxml import etree   selector=etree.HTML(html)
#设立若干空列表，分别解析后，再添加到空列表中 ，用data=pd.DataFrame  拼接成表格数据结构
#两者都要用到padas,只是第一种完全以来pd，第二种用空列表完成主要的清晰内容，pd只是拼接而已！
#具体问题具体分析，如果需要清晰的分类过多，超过10个还是用pd直接处理，两个都要练练！

//*[@id="contents"]/div[1]/div[3]/table/tbody/tr[2]/td[1]

//*[@id="contents"]/div[1]/div[3]/table/tbody/tr[11]/td[1]



    # 得到所有单个页面链接
# def parse_all_links(html):
#
#     pattern = re.compile('.*?<td>&nbsp;&nbsp;<a href="(.*?)"><font>(.*?)</font>', re.S)
#     items = re.findall(pattern,html)
#     for item in items:
#         print(item[1],item[0])






