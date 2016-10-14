# -*- coding:utf-8 -*-

from newseed.util import linkList
from util import constant,crawl,handle
import socket
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
    if soup.find('div',class_='info').find('p',class_='keyword'):
        keywordSoup = soup.find('div',class_='info').find('p',class_='keyword')
        # 这里处理的是并购信息，情况相对简单一些




if __name__ == '__main__':
    # 主页名
    hostName = 'http://newseed.pedaily.cn'
    # 相关路径
    during = 'data/newseed_data'
    fileNameNew = 'acquisitionEvent_linkIndex_new.txt'
    fileNameOld = 'acquisitionEvent_linkIndex_old.txt'

    # 从new.txt文本读取链接索引信息
    # linkIndexList = handle.listReadFromTxt(during ,fileNameNew)
    linkIndexList = handle.listReadFromTxt(during ,'acquisitionEvent_linkIndex_test.txt')
    # 将索引信息追加到old.txt文本
    # handle.listAppendWrite2Txt(linkIndexList,fileNameOld,during)
    # 遍历索引,抓取信息
    i = 1
    for linkIndex in linkIndexList:
        link = hostName + linkIndex.strip()
        try:
            statusCode = handle.getUrlStatus(link)
            if statusCode == 200:
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
                    # 获取事件介绍
                    investIntroduce = linkList.getInvestIntroduce(soup)
                else:
                   print('这条数据信息已丢失...')
        except Exception as err:
            print()



