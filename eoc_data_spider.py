#! -*- coding:utf-8 -*-

import requests
import re
import json



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


url = 'http://www.8pu.com/country/USA/'
html = call_page(url)


#重点用正则提出标签，空格即可
# 整体是一个列表，但是for迭代之后就变成了45个字符串  print(a)

# 还是要考虑用表达式整体去匹配，不能割裂然后再去拼接！ 模块处理又变成元组了
# 尝试进行一对多字符串拼接组合
# 11 44 484
def parse_one_page(html):
    patt1 = re.compile(' <td width="100">(.*?)</td>',re.S)   #标题匹配,注意去除换行(没有实现去除空格，但是标签都没了)
    patt2 = re.compile('<td>(.*?)</td>', re.S)
    item1 =  re.findall(patt1,html)
    item2 = re.findall(patt2,html)
    # for k,v in zip(item1,item2[0:484:11]):
    #     print(k,v)



    #往空列表里面两次添加
    # for i1 in item1:
    #     print(i1)
    # for i2 in item2:
    #     print(len(i2))

            # ulist.append(i2)



    a0 = {item1[0]:item2[0:11]}
    # a1 = {item1[1]: item2[12:23]}

    print(a0)
    # print(a1)



#后面整理入mysql，不考虑到MongoDB，暂放 2018.6.21














    # for i in items:
    #     print(i)

    # print(items)
    # print(len(items))

    # for item in items:
    #     print((type(item)))

content = parse_one_page(html)








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




# 存储的部分，先都存到MongoDB中，等到mysql建表思路清楚，甚至数据分析的pandas，R思路清晰之后在存到关系型数据库中（第一轮主要积累爬取，清洗）
#第二轮再到应用层面！



