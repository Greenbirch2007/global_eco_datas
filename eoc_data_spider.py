#! -*- coding:utf-8 -*-

import requests
import re  # 用lxml比正则好太多了
import pandas as pd
import json
from pymongo import MongoClient


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
url = 'http://www.8pu.com/country/USA/'
from lxml import etree
html=requests.get(url).content
selector=etree.HTML(html)



#解析函数  表格数据解析多进行多个空列表处理！ 然后多个列表再拼接 不能一起爬了 还要用到pandas
# def parse_one_page(html):
#     patt = re.compile('<td width="100">(.*?).*?<td>(.*?)</td>.*?</tr>',re.S)
#     items = re.findall(patt,html)
#     for i in items:
#         print(i)











# 事例演示，
date1 = []
date = selector.xpath('//*[@id="contents"]/div[1]/div[3]/table/tbody/tr[1]/th//text()')
for i in date:
    # print(i)
    date1.append(i)

pychasing_power = []
themes = selector.xpath('//*[@id="contents"]/div[1]/div[3]/table/tbody/tr[2]/td//text()')
for i in themes:
    # print(i)
    pychasing_power.append(i)

# data = pd.DataFrame({'年份':date1,'购买力':pychasing_power})
# print(data)
data  ={'年份':date1,'购买力':pychasing_power}
data_json = json.dumps(data)
#  关键是如何讲DataFrame的字典格式转换为json格式，就好存入Mongodb中了



def get_to_Mongodb(item):
    client = MongoClient(host='localhost',port=27017)
    db = client.global_eco_datas
    p = db.USA
    result = p.insert(item)
    print(result)

get_to_Mongodb(data_json)



# 文件，数据库都是一个容器，存入容器必须一个一个遍历存入，不能一次整体存入，所以要是可迭代对象
#  直接使用pandas读取html还是有些问题，但是通过lxml的解析，然后使用DataFrame这个数据结构是可行的
# 存入excel还是可以的，但是


# data = pd.read_html(url)
#
# def get_to_file(content):
#     with open('data2.csv','a',encoding='utf-8') as f:
#         f.write(content)
#         f.close()
# get_to_file(str(data))




# 数据导出为csv文件
# data.to_csv('data2.csv',encoding='utf-8',index=False)

# def insert_to_Mongo(data):
#     client = pymongo.MongoClient()
#     db = client.global_eco_datas
#     p = db.USA
#     result = p.insert(data)
#     print(result)
#


# 相当于表格数据应该如何存储，如何入库和如何导出数据文件  不再是json文件格式了！


# 表格类的数据爬取两种办法 一种是直接使用pandas的pd.read_html(url) 方法，
#第二种是from lxml import etree   selector=etree.HTML(html)
#设立若干空列表，分别解析后，再添加到空列表中 ，用data=pd.DataFrame  拼接成表格数据结构
#两者都要用到padas,只是第一种完全以来pd，第二种用空列表完成主要的清晰内容，pd只是拼接而已！
#具体问题具体分析，如果需要清晰的分类过多，超过10个还是用pd直接处理，两个都要练练！




    # 得到所有单个页面链接
# def parse_all_links(html):
#
#     pattern = re.compile('.*?<td>&nbsp;&nbsp;<a href="(.*?)"><font>(.*?)</font>', re.S)
#     items = re.findall(pattern,html)
#     for item in items:
#         print(item[1],item[0])






