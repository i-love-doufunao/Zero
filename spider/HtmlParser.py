# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from spider import Job, MysqlUtils
from spider import Company
import time

f = open('data/test.xml', 'r', encoding='utf-8')
soup = BeautifulSoup(f.read(), 'lxml')

def getPageList(htmlContent, headerUrl, ):
    """
    根据HTML内容，获取分页链接
    :param htmlContent:
    :param headerUrl:
    :return:
    """
    nextPageUrlList = []
    pages = soup.find(class_='page')

    # 只有1页，无翻页
    if (pages is None):
        return nextPageUrlList

    aList = pages.find_all('a')
    for a in aList:
        clz = a.get('class')
        if clz is not None:
            continue
        else:  # a['page']
            nextPageUrlList.append("%s%s&%s" % (headerUrl, a.get('page'), a.get('ka')))
    return nextPageUrlList


def getJobListInfo(htmlContent, ):
    """
    获取公司和职位信息
    :param htmlContent:
    :return:jobList[Job1,Job2...]
    """
    jobList = []
    jobInfosInHtml = htmlContent.find_all(class_='job-primary')
    for jobInfo in jobInfosInHtml:

        # 职位名称
        jobTitle = jobInfo.find(class_='job-title').string
        print(jobTitle)

        # 所在城市
        locateContent = jobInfo.find('p').text
        locate = ''

        # 遇到数字停止，作为endIndex
        for i in range(len(locateContent)):
            if (locateContent[i].isdigit()):
                locate = locateContent[:i].strip()
                break
        print("locate:", locate)

        # 薪酬
        salary = jobInfo.find('span').string
        print(salary)

        # 链接
        url = jobInfo.find(class_='info-primary').find('a').get('href')

        # 发布时间，原始数据为'发布于08月13日'
        publishTime = jobInfo.find(class_='info-publis').find('p').string
        publishTime = publishTime.replace('发布于', '').replace('月', '-').replace('日', '')
        publishTime = time.strftime("%Y", time.localtime()) + '-' + publishTime

        # 时间只有月-日，需要补齐
        print(publishTime)

        # 公司
        companyName = jobInfo.find(class_='company-text').find('a').string
        job = Job.Job(_name=jobTitle, _publishTime=publishTime,
                      _locate=locate, _url=url, _company=companyName, _salary=salary)
        jobList.append(job)
    return jobList


jobList = getJobListInfo(soup)
print(len(jobList))
MysqlUtils.insertJobInfo(jobList)
