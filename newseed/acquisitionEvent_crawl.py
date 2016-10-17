# -*- coding:utf-8 -*-

from newseed.util import linkList
from util import constant,crawl,handle
import socket
import re
import os
"""
数据源：newseed
数据分类：并购关系信息
"""
socket.setdefaulttimeout(60)
"""
读取acquisitionEvent_linkIndex_new.txt索引到内存形成列表，遍历的抓取这些数据
将新的列表以追加的方式写入acquisitionEvent_linkIndex_old.txt文件
"""


def getRelatedCompany(soup):
    '''
        获取并购公司信息
    '''
    productCompanyInfo = []
    investCompanyInfo = []
    if soup.find('div',class_='info').find('p',class_='keyword'):
        keywordSoup = soup.find('div',class_='info').find('p',class_='keyword')
        # 产品公司信息
        if re.search('企</span>\s*(.*?)\s*<span class="btn blue">投',str(keywordSoup),re.S):
            productCompanyStr = re.search('企</span>\s*(.*?)\s*<span class="btn blue">投', str(keywordSoup), re.S).group(1)
            content,link = crawl.getStringAndHrefByAtag(productCompanyStr)
            productCompanyInfo.append((content,link))
        # 投资公司信息
        if re.search('投</span>\s*(.*?)\s*</p>',str(keywordSoup),re.S):
            investCompanyStr = re.search('投</span>\s*(.*?)\s*</p>',str(keywordSoup),re.S).group(1)
            content,link = crawl.getStringAndHrefByAtag(investCompanyStr)
            investCompanyInfo.append(content,link)
    return productCompanyInfo,investCompanyInfo







if __name__ == '__main__':
    # 主页名
    hostName = 'http://newseed.pedaily.cn'
    # 相关路径
    during = 'data/newseed_data'
    fileNameNew = 'acquisitionEvent_linkIndex_new.txt'
    fileNameOld = 'acquisitionEvent_linkIndex_old.txt'
    # 文件名
    outputFileName = 'acquisition_event_info.xls'

    # 从new.txt文本读取链接索引信息
    # linkIndexList = handle.listReadFromTxt(during ,fileNameNew)
    linkIndexList = handle.listReadFromTxt(during ,'acquisitionEvent_linkIndex_test.txt')

    # 1 将索引信息追加到old.txt文本
    # handle.listAppendWrite2Txt(linkIndexList,fileNameOld,during)
    # 遍历索引,抓取信息
    # 2 生成输出文件字段
    outputFilePath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','newseed_data','resultSet',outputFileName)


    i = 1
    for linkIndex in linkIndexList:
        link = hostName + linkIndex.strip()
        try:
            statusCode = handle.getUrlStatus(link)
            if statusCode == 200:
                ## 获取对应信息
                # 获取浓汤soup
                hooshSoup = crawl.getHooshSoup(link)
                # 初始化变量信息
                investTitle = ''
                investTime = ''
                investType = ''
                investMoney = ''
                productCompanyName = ''
                productCompanyLinkIndex = ''
                investCompanyName = ''
                investCompanyLinkIndex = ''
                investIntroduce = ''
                if hooshSoup.find('div',class_='main').find('div',class_='record invest').find('div',class_='col-md-860'):
                    # 定位到html标记的最小单位
                    soup = hooshSoup.find('div',class_='main').find('div',class_='record invest').find('div',class_='col-md-860')
                    # 获取事件标题
                    investTitle = linkList.getEventTitle(soup)
                    # 获取时间，类型，金额
                    investTime,investType,investMoney = linkList.getTimeTypeAndMoney(soup)
                    # 获取并购相关公司名称，链接（公司信息以列表(name,link)形式返回）
                    productCompanyInfo,investCompanyInfo = getRelatedCompany(soup)
                    if productCompanyInfo:
                        productCompanyName = productCompanyInfo[0]
                        productCompanyLinkIndex = productCompanyInfo[1]
                    if investCompanyInfo:
                        investCompanyName = investCompanyInfo[0]
                        investCompanyLinkIndex = investCompanyInfo[1]
                    # 获取事件介绍
                    investIntroduce = linkList.getInvestIntroduce(soup)
                else:
                   print('这条数据信息已丢失...')
                ## 将字段存入列表

            print('已处理第【',str(i),'】条数据...')
            i += 1
        except Exception as err:
            print(err)



