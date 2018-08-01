from bs4 import BeautifulSoup
import requests
import csv
import pymongo

# 检查url地址
def check_link(url):
    try:

        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法链接服务器！！！')

    # 爬取资源

# 用 .string 属性来提取标签里的内容时，该标签应该是只有单个节点的。比如上面的 <td>1</td> 标签那样。


# tr --> td
# 先遍历最外层，整个列表块只能查找，不能提取元素，只能到下一级标签，用string属性 提取。如何存入数据库！
def get_contents(rurl):
    soup = BeautifulSoup(rurl,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        yield {
            'rank':ui[1],
            'name':ui[3],
            'income':ui[5]
        }


# 讲结构话数据存储到MongnDB中很容易！
def insertDB(content):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.Table_DB
    collection = db.example1
    collection.insert(content)



if __name__ == '__main__':
    url = "http://www.maigoo.com/news/463071.html"
    html = check_link(url)
    content = get_contents(html)
    insertDB(content)

# def save_contents(urlist):
#     with open("/home/karson/2016年中国企业500强排行榜.csv", 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(['2016年中国企业500强排行榜'])
#         for i in range(len(urlist)):
#             writer.writerow([urlist[i][1], urlist[i][3], urlist[i][5]])


# def main():
#     urli = []
#     url = "http://www.maigoo.com/news/463071.html"
#     rs = check_link(url)
#     get_contents(urli, rs)
    # print(content)
    # save_contents(urli)


