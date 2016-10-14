# -*- coding:utf-8 -*-

from newseed.util import linkList
from util import handle
import socket
import re
"""
数据源：newseed
数据分类：并购关系信息
"""
socket.setdefaulttimeout(60)
"""
数据更新时要重新运行程序，重写acquisitionEvent_linkIndex_new.txt
更新策略：
    最新的索引列表与acquisitionEvent_linkIndex_old.txt索引对比，找出更新的索引
    更新的索引写入acquisitionEvent_linkIndex_new.txt
    acquisitionEvent_linkIndex_old.txt不改动
"""
if __name__ == '__main__':
    # 初始链接地址
    initUrl = 'http://newseed.pedaily.cn/invest/r115-p1'
    during = 'data/newseed_data'
    fileNameNew = 'acquisitionEvent_linkIndex_new.txt'

    # 获取总记录条数
    totalRecordNum = linkList.getTotalRecordNum(initUrl)
    # 获取页面链接索引列表
    if totalRecordNum:
        # 计算页面链接索引列表
        pageLinkIndexList = handle.getPageLinkIndexList(totalRecordNum)
        # 获取页面链接列表
        pageLinkList = [re.sub('/r115-p\d+','/r115-p%s' % index,initUrl,re.S) for index in pageLinkIndexList]
        # 获取并购事件链接索引列表（最新的）
        eventLinkIndexList = linkList.getEventLinkIndexList(pageLinkList)
        ## 初次爬取，将索引写入旧表（old）
        handle.listAppendWrite2Txt(eventLinkIndexList ,during=during ,fileName = fileNameNew)
        # 读取索引列表（old）

        # 找到更新的索引

        # 更新索引写入新表（new）

