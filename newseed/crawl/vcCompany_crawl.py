# -*- coding:utf-8 -*-

from newseed.util import linkList
from util import constant,crawl,handle,io
import socket
import re
import os
from bs4 import BeautifulSoup
"""
数据源：newseed
数据分类：投融资关系信息
"""
# socket.setdefaulttimeout(60)
"""
读取investEvent_linkIndex_new.txt索引到内存形成列表，遍历的抓取这些数据
将新的列表以追加的方式写入investEvent_linkIndex_old.txt文件
"""



if __name__ == '__main__':
    # 主页名
    hostName = 'http://newseed.pedaily.cn'
    # 相关路径
    during = 'data/newseed_data'
    fileNameNew = 'investEvent_linkIndex_new.txt'
    fileNameOld = 'investEvent_linkIndex_old.txt'
    # 文件名
    outputFileName = 'invest_event_info.xls'
    # 日志文件
    logFileName = 'log_invest_event_info_newseed.txt'

    # 从new.txt文本读取链接索引信息
    # linkIndexList = handle.listReadFromTxt(during ,fileNameNew)
    linkIndexList = handle.listReadFromTxt(during ,'investEvent_linkIndex_part1_2000.txt')
    print('具体页面链接数量:',len(linkIndexList))
    # 1 将索引信息追加到old.txt文本
    # handle.listAppendWrite2Txt(linkIndexList,fileNameOld,during)

    eventInfoList = linkList.getEventInfoList(linkIndexList,logFileName)

    # 输出文件目录
    outputFilePath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'data','newseed_data','resultSet',outputFileName)
    # 将爬取数据写入excel文件
    if eventInfoList:
        print('开始将数据集合中数据写入excel文档,infoList中记录数为：',str(len(eventInfoList)))

        # 将信息写入excel文本
        io.writeOrAppendContent2Excel(eventInfoList,outputFilePath)

        # “覆盖”写入的方式
        # io.writeContent2Excel(eventInfoList,outputFilePath)
        # “追加”写入的方式
        # io.appendContent2Excel(eventInfoList,outputFilePath)




