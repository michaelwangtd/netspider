# -*- coding:utf-8 -*-

from newseed.util import linkList
from util import handle
import socket
import re
"""
数据源：newseed
数据分类：产品公司信息
"""
# socket.setdefaulttimeout(60)
"""
数据更新时要重新运行程序，重写acquisitionEvent_linkIndex_new.txt
更新策略：
    最新的索引列表与acquisitionEvent_linkIndex_old.txt索引对比，找出更新的索引
    更新的索引写入acquisitionEvent_linkIndex_new.txt
    acquisitionEvent_linkIndex_old.txt不改动
"""
if __name__ == '__main__':
    # 初始链接地址
    initUrl = 'http://newseed.pedaily.cn/company/p1'
    during = 'data/newseed_data'
    fileNameNew = 'productCompany_linkIndex_new.txt'
    fileNameOld = 'productCompany_linkIndex_old.txt'
    logFileName = 'log_product_company_link_newseed.txt'


    """
    初次获取事件链接
    """
    # 获取总记录条数
    totalRecordNum = linkList.getTotalRecordNum(initUrl)
    # 计算页面链接索引列表
    pageLinkIndexList = handle.getPageLinkIndexList(totalRecordNum)
    # 获取页面链接列表
    pageLinkList = [re.sub('/company/p\d+','/company/p%s' % index,initUrl,re.S) for index in pageLinkIndexList]

    # 将pageLinkList分成4份，分别写入文件
    middleNum = int(len(pageLinkList) / 2)
    earlierNum = int(middleNum / 2)
    laterNum = int((middleNum + len(pageLinkList)) / 2)
    pageLinkGroupList = [pageLinkList[:earlierNum],pageLinkList[earlierNum:middleNum],pageLinkList[middleNum:laterNum],pageLinkList[laterNum:]]

    for i in range(len(pageLinkGroupList)):
        fileName = 'productCompany_linkIndex_old_'
        during = 'data\\newseed_data'
        handle.listAppendWrite2Txt(pageLinkGroupList[i],fileName + str(i) + '.txt',during)




    """
    读取日志文件获取事件链接
    """

    # 从日志列表读取页面链接
    pageLinkList = handle.listReadFromTxt('log', 'log_product_company_link_4_2.txt')
    eventLinkIndexList = linkList.getCompanyLinkIndexList(pageLinkList, 'log_product_company_link_4_3.txt')
    handle.listAppendWrite2Txt(eventLinkIndexList, during=during, fileName='productCompany_linkIndex_old_4.txt')

