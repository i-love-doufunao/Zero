# -*- coding: utf-8 -*-
import random
import requests
import socket
import time
from bs4 import BeautifulSoup
from queue import Queue #LILO队列



def getIndustryCode(industry):
    ""


def getEntryPageContent(url, headers, ):
    """
    获取城市编码信息，该请求单独放到一个Python应用中实现，将查询结果写入文件即可。
    当前只需从文件中读出结果
    :param url:需要爬取的页面
    :return:dict：城市-编码
    """
    timeout = random.choice(range(80, 180))
    req_city_url = url
    while True:
        try:
            req = requests.get(req_city_url, headers=headers, timeout=timeout)
            req.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))
        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

    # 查找ul
    soup = BeautifulSoup(req.text, 'lxml')
    return soup


"""
需要支持的需求包括：
1、支持输入成都、关键字、行业进行爬取，爬取公司以及该公司职位
--->确定有几页，构造地址循环。从第二页开始，格式为：https://www.zhipin.com/i100020-c101270100/h_101270100/?query=技术&page=2&ka=page-2
--->最后一页，再次获取翻页页码，继续进行，知道无页码为止。
--->获取公司、职位名，构造好数据
--->数据批量入库
2、支持输入除成都为其他城市、关键字、行业进行爬取，爬取公司以及该公司在成都的技术职位
3、支持输入成都、行业进行爬取，通过公司名字和公司介绍，爬取和感兴趣关键字相关公司（医药、健康、教育、k12）以及该公司的职位

"""

if __name__ == '__main__':
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'upgrade - insecure - requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'cookie': 'lastCity=101270100; JSESSIONID=""; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1533388366; __c=1533388382; __l=r=https%3A%2F%2Fwww.zhipin.com%2F&l=%2Fwww.zhipin.com%2Fgongsi%2Fc70e5cfe3e8e2ae63nF6.html%3Fka%3Dindex_rcmd_companylogo_2_custompage; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%26scity%3D101270100%26industry%3D%26position%3D100509; __a=33591570.1533388364.1533388364.1533388382.39.2.38.39; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1533542204'
    }

    # 解析输入参数，格式：query:大数据,industry:医疗...
    query = ""
    industry = ""

    # 根据输入参数对应的key，获取相应的编码
    industry = getIndustryCode(industry)

    # 构造请求url
    mainUrl = "https://www.zhipin.com/job_detail/?query=%s&scity=101270100&industry=%s&position=" % (query, industry)

    # 构造1个队列，队列内容就是url
    spiderJobQueue = Queue()
    spiderJobQueue.put()
    # spiderJobQueue.

    # 爬取入口页内容
    # exceptionTimes = 0
    beginSleepIndex = 80
    endSleepIndex = 180
    while True:
        entryPageContent = getEntryPageContent(mainUrl, headers)
        if (entryPageContent is None):
            if (exceptionTimes == 5):
                print("重试5次失败，退出")
                break
            exceptionTimes = exceptionTimes + 1
            timeout = random.choice(range(beginSleepIndex * exceptionTimes, endSleepIndex * exceptionTimes))
        else:
            break

    if (entryPageContent is None):
        exit(1)

    # 获取分页链接
