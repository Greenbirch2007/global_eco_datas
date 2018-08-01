#! -*- coding:utf-8 -*-








import requests
import re
import pandas as pd
import json
import pymongo
from bs4 import BeautifulSoup

headers = {
    'useragent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
}

#请求的函数
def call_page(url):

    try:
        response = requests.get(url,headers=headers)
        response.encoding = 'utf-8'    #响应解码
        if response.status_code == 200:
            return response.text
        else :
            return None
    except RequestException:
        return None


# tr --> th
# tr  --> td


# 单一页面数据解析！
def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        tds = []
        for td in tr:
            tds.append(td.string)
        yield {
            'themes':tds[1],
            '2017':tds[3],
            '2016':tds[5],
            '2015':tds[7],
            '2014':tds[9],
            '2013':tds[11],
            '2012':tds[13],
            '2011':tds[15],
            '2010':tds[17],
            '2009':tds[19],
            '2008':tds[21],

        }

# db = client.test
# 调用client的test属性即可返回test数据库，当然也可以这样来指定：
# db = client['test']
#　两种方式是等价的。
def insertDB(content):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.Table_DB
    collection = db['JPN']
    collection.insert(content)



# 字符串切割之后就变成了列表
# def parse_all_links(html):
#     pattern = re.compile('<tr id="US_" style="">' +
#                          '.*?<td>&nbsp;&nbsp;<a href="http://www.8pu.com/country/(.*?)/"><font>(.*?)</font></a></td>', re.S)
#     items = re.findall(pattern,html)
#     for item in items:
#         print(item)
        # cut_str = item.split('/')
        # Cname.append(cut_str)








if __name__ == '__main__':
    url = 'http://www.8pu.com/country/JPN/'
    html = call_page(url)
    content = parse_one_page(html)
    insertDB(content)


    # all_countrys = []
    # for one_country in iter(Cname):
    #     one_link = 'http://www.8pu.com/country/%s/' % one_country
    #     all_countrys.append(one_link)
    # for ite in iter(all_countrys):
    #     html = call_page(ite)
    #     content =parse_one_page(html)
    #     insertDB(content)
    #     print(ite)

# 连接存储
# def insertDB(content):
#     client = pymongo.MongoClient('localhost', 27017)
#     db = client.Table_DB
#     collection = db.links
#     collection.insert(content)
#



# 文件，数据库都是一个容器，存入容器必须一个一个遍历存入，不能一次整体存入，所以要是可迭代对象
#  直接使用pandas读取html还是有些问题，但是通过lxml的解析，然后使用DataFrame这个数据结构是可行的
# 存入excel还是可以的，但是


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







