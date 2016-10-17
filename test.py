# -*- coding:utf-8 -*-

from util import constant,handle,crawl
from newseed.util import linkList
import math
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
import os


filePath = os.path.join(os.path.dirname(__file__),'test.xls')
wb = Workbook()
sheet = wb.active
sheet.append(['Title','Time','Type','Money','productCompany','productCompanyLink','investCompany','investCompanyLink','investIntroduce'])
wb.save(filePath)





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