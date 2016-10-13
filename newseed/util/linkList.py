# -*- coding:utf-8 -*-

from util import handle,crawl
import socket
socket.setdefaulttimeout(60)
"""
newseed工具类
"""

def getEventLinkIndexList(pageLinkList):
    '''
    获取事件链接索引列表
    '''
    eventLinkIndexList = []
    if pageLinkList:
        i = 1
        for pageLink in pageLinkList:
            if handle.getUrlStatus(pageLink) == 200:
                hooshSoup = crawl.getHooshSoup(pageLink)
                if hooshSoup:
                    tbodySoup = hooshSoup.find('tbody')
                    for trTag in tbodySoup.find_all('tr'):
                        linkIndex = trTag.find_all('td',class_='td6')[0].a.get('href')
                        eventLinkIndexList.append(linkIndex)
                        print('获取索引数目：',str(i),linkIndex)
                        i += 1
    print('eventLinkIndexList长度为：',str(len(eventLinkIndexList)))
    return eventLinkIndexList


def getTotalRecordNum(initUrl):
    '''
    获取页面总记录数
    '''
    recordNum = ''
    # 检验url链接
    statusCode = handle.getUrlStatus(initUrl)
    if statusCode == 200:
        # 获取初始的浓汤
        hooshSoup = crawl.getHooshSoup(initUrl)
        # 获取总记录数
        if hooshSoup.find('span',id='total'):
            recordNum = hooshSoup.find('span',id='total').string
    return recordNum