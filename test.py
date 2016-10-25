# -*- coding:utf-8 -*-

from util import constant,handle,crawl,io
from newseed.util import linkList
import math
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
import os
import time

# pageLinkList = ['http://newseed.pedaily.cn/vc/p1','http://newseed.pedaily.cn/vc/p2']
#
# result = linkList.getCompanyLinkIndexList(pageLinkList)
# print(result)


# # 使用python判断文件是否存在
# filePath1 = os.path.join(os.path.dirname(__file__),'data','newseed_data','investEvent_linkIndex_test.txt')
# filePath2 = os.path.join(os.path.dirname(__file__),'data','test.txt')
# if os.path.exists(filePath1):
#     print(filePath1,'1存在')
# if os.path.exists(filePath2):
#     print(filePath2,'2存在')



# html = """<p>
# <p class="keyword">
# <span class="btn red">企</span>
# <a class="btn default" href="/company/43614" target="_blank">乐视汽车(LeSEE乐视超级汽车)</a>
# <span class="btn blue">投</span>
# <a class="default" href="/vc/36904" target="_blank">深创投</a>
# <a class="default" href="/vc/31890" target="_blank">联想控股</a>
# <a class="default" href="/vc/39299" target="_blank">英大资本</a>
# <span id="#" class="default">民生信托</span>
# <a class="default" href="/vc/31186" target="_blank">华夏润石（新华联集团）</a>
# <span id="#" class="default">宏兆基金</span>
# </p>"""
# investCompanyStr = re.search('投</span>\s*(.*?)\s*</p>',str(html),re.S).group(1)
# investCompanySoup = BeautifulSoup(investCompanyStr)
# resultSetSpantag = investCompanySoup.find_all('span')
# if resultSetSpantag:
#     for spanTag in resultSetSpantag:
#         print(str(spanTag))
#         content = crawl.getStringBySpantag(str(spanTag))
#         print(content)




#
# html = """<span class="btn blue">投</span>
# <a class="default" href="/vc/35782" target="_blank">光信资本</a>
# <a class="default" href="/vc/24573" target="_blank">源码资本</a>
# <a class="default" href="/vc/31886" target="_blank">洪泰基金</a>
# <a class="default" href="/vc/8572" target="_blank">创新工场</a>
# <a class="default" href="/vc/533" target="_blank">晨兴创投</a>
# <span id="#" class="default">51信用卡</span>
# </p>"""
#
# investCompanyStr = re.search('投</span>\s*(.*?)\s*</p>',html,re.S).group(1)
# # print(investCompanyStr)
#
# investSoup = BeautifulSoup(investCompanyStr)
# resultA = investSoup.find_all('a')
# print(type(resultA))
# for item in resultA:
#     print(item)
#     print(str(item))
#     print(type(item))
# print(type(result))
# print(result)


# result = re.findall('target="_blank">\s*(.*?)\s*</a>',investCompanyStr,re.S)
# relink = re.findall('class="default" href="(.*?)" target="',investCompanyStr,re.S)
# print(result)
# print(relink)





# infoList = [('妙品','/invest/444'),('大大','/vc/456')]
# name,link = linkList.getCompanyNameAndLinkStr(infoList)
# print(name)
# print(link)




# infoList = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# infoList2 = [[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]]
# # outputFilePath = 'D:\\workstation\\repositories\\netspider\\data\\newseed_data\\result\\test.xls'
# outputFilePath = os.path.join(os.path.dirname(__file__),'data','newseed_data','resultSet','test.xls')
# # io.writeContent2Excel(infoList,outputFilePath)
# # io.appendContent2Excel(infoList2,outputFilePath)
# io.appendContent2Excel_test(infoList,outputFilePath)



# companyName = 'company'
# # companyName = companyName[0:len(companyName) - 1]
# # print(companyName)
# print(companyName[0:1])





# string = """技术的咖啡机啊看<jdskaf>健康收到了就啊大家"""
# print(string)
# result = re.sub('<.*?>','',string)
# print(result)




# newTimeStr = '2016-09-25-15-00'
# structTime = time.strptime(newTimeStr, '%Y-%m-%d-%H-%M')
# timeStamp = int(time.mktime(structTime))
# print(timeStamp)



# filePath = os.path.join(os.path.dirname(__file__),'test.xls')
# wb = Workbook()
# sheet = wb.active
# sheet.append(['Title','Time','Type','Money','productCompany','productCompanyLink','investCompany','investCompanyLink','investIntroduce'])
# wb.save(filePath)


# testList = ['','']
# if testList:
#     print('lll')



# string = """
# <p></p>
# <p>深圳市银桦投资管理有限公司投资雷士光电科技有限公司。</p>
# <p></p>"""
# singleContentList = []
# cleanedContentList = []
# contentList = crawl.extractContentFromHtmlString(string)
# print(contentList)
#
# for item in contentList:
#     if item :
#         singleContentList.append(item)
# print(singleContentList)
#
# for item in singleContentList:
#     temp = item.replace('\s','').replace('\t','').replace('\r','')
#     cleanedContentList.append(temp)
# print(cleanedContentList  )


# string = """<p> TMT </p>
# <p class="keyword">
# <span class="btn red">企</span>
# <a class="btn default" href="/company/2746" target="_blank">雷士光电科技有限公司 </a>
# <span class="btn blue">投</span>
# <a class="default" href="/vc/22210" target="_blank">银桦投资</a>
# </p>
# <p></p>
# <p>深圳市银桦投资管理有限公司投资雷士光电科技有限公司。</p>
# <p></p>"""
# # print(re.findall('keyword">\s*.*?\s*</p>\s*(.*?)\s*$',string,re.S))     #['<p></p>\n<p>深圳市银桦投资管理有限公司投资雷士光电科技有限公司。</p>\n<p></p>']
# print(re.findall('keyword">\s*.*?\s*</p>\s*(.*?)\s*',string,re.S))      #['']


# print(type('sss'))
# if type('sss') == str:
#     print('类型为字符串...')


# html = """<div class="info">
# <p>
# 2016年08月03日
# <i class="slash">/</i>
# 并购
# <i class="slash">/</i>
# 1000万人民币
# <i class="slash">/</i>
# 传统互联网
# </p>
# <p class="keyword">
# <span class="btn red">企</span>"""
# # result = re.search('info">\s*(.*?)\s*<p class="keyword">',str(html),re.S).group(1)
# # print(result)
# # crawl.extractContentFromHtmlString(result)
# html = BeautifulSoup(html)
# print(linkList.getTimeTypeAndMoney(html))


# html = """<div class="title">
# 邮件工具服务Front 获得 Social Capital 领投的1000 万美元 A 轮融资
# <a class="btn font-blue favor-add" data-resid="35391" data-restypeid="6" href="javascript:void(0);">"""
# result = re.search('title">\s*(.*?)\s*<a',str(html),re.S).group(1)
# print(result)



# # 目前来讲一个可行的读取文件的方式
# filePath = 'D:/workstation/repositories/netspider/data/newseed_data/acquisitionEvent_linkIndex_new.txt'
# try:
#     fr = open(filePath, 'r', encoding='utf-8')
#     i = 1
#     while True:
#         line = fr.readline().strip()
#         if line:
#             print(str(i),line)
#             i += 1
#         else:
#             break
#     fr.close()
# except Exception as err:
#     print('文件读取错误：',err)


# handle.listWrite2Txt(['1'],'/ddd','a.txt')


# url = 'http://newseed.pedaily.cn/invest/r225-p2'
# hooshSoup = crawl.getHooshSoup(url)
# tbodySoup = hooshSoup.find('tbody')
# print(tbodySoup)


# list = ['http://newseed.pedaily.cn/invest/r115-p1']
# linkList.getEventLinkIndexList(list)
# re = crawl.getHooshSoup('http://newseed.pedaily.cn/invest/r115-p1')
# print(re)


# initUrl = 'http://newseed.pedaily.cn/invest/r115-p1'
# print(str.replace(initUrl,initUrl[-1],'xxx'))


# print(handle.getPageLinkIndexList(170))

# print(math.ceil(173/10))