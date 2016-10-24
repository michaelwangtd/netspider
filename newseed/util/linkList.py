# -*- coding:utf-8 -*-

from util import handle,crawl
import socket
import re

# socket.setdefaulttimeout(60)
"""
newseed工具类
"""


def getCompanyNameAndLinkStr(hostName,companyInfoList):
    '''
        companyInfoList = [(name,link),(xxx,xxx),(...,...),...]
        实现类似分类的功能，将名称挑出来形成字符串，同时对应的将链接挑出来形成字符串
    '''
    companyName = ''
    companyLink = ''
    if companyInfoList:
        for companyInfo in companyInfoList:
            companyName = companyName + companyInfo[0] + ','
            companyLink = companyLink + hostName + companyInfo[1] + ','
        # 处理掉最后的“，”
        companyName = companyName[0:len(companyName) - 1]
        companyLink = companyLink[0:len(companyLink) - 1]
    return companyName,companyLink



def createRecordList(hostName,investTitle,investTime,investType,investMoney,productCompanyInfoList,investCompanyInfoList,investIntroduce):
    '''
        1 校验数据，发现不合格的数据，立即返回失败标志 -1
        2 清洗部分数据
        3 将字段组成列表
    '''
    # 校验数据
    if handle.verifyTime(investTime) == False:
        return -1
    if handle.verifyTpye(investType) == False:
        return -1
    if handle.verifyMoney(investMoney) == False:
        return -1
    # 清洗数据
    investTitle = crawl.washData(investTitle)
    investTime = crawl.washTime(investTime)
    investIntroduce = crawl.washData(investIntroduce)
    # 获取公司信息名称，链接字符串
    productCompanyName,productCompanyLink = getCompanyNameAndLinkStr(hostName,productCompanyInfoList)
    investCompanyName,investCompanyLink = getCompanyNameAndLinkStr(hostName,investCompanyInfoList)
    # 返回recordList
    return [investTitle,investTime,investType,investMoney,productCompanyName,productCompanyLink,investCompanyName,investCompanyLink,investIntroduce]



def getInvestIntroduce(soup):
    '''
        获取事件介绍信息
    '''
    introduce = ''
    if soup.find('div',class_='info'):
        infoSoup = soup.find('div',class_='info')
        if re.findall('keyword">\s*.*?\s*</p>\s*(.*?)\s*</div>',str(infoSoup),re.S):
            pTagsStr = re.findall('keyword">\s*.*?\s*</p>\s*(.*?)\s*</div>',str(infoSoup),re.S)[0]
            # 从html标记中获取内容
            contentList = crawl.extractContentFromHtmlString(pTagsStr)
            for item in contentList:
                introduce = introduce + item
            return introduce




def getTimeTypeAndMoney(soup):
    '''
    使用正则表达式来匹配
    '''
    # 筛选的标准库
    timeSet = ['年','月','日']
    typeSet = ['不详', 'E轮', 'F轮', 'IPO上市及以后', 'D轮', 'A+轮', '其他轮', 'Pre-A', 'C轮', '天使', '种子', '并购', '股权投资', 'B轮', 'A轮']
    moneySet = ['万日元', '万韩国元', '万新加坡元', '万人民币', '万港币', '万英镑', '万澳大利亚元', '万欧元', '万美元', '万新台币']
    # 初始化字段
    investTime = ''
    investType = ''
    investMoney = ''
    if soup.find('div',class_='info'):
        infoSoup = soup.find('div',class_='info')
        # 使用正则截取需要的部分
        if re.search('info">\s*(.*?)\s*<p class="keyword">',str(infoSoup),re.S):
            cake = re.search('info">\s*(.*?)\s*<p class="keyword">',str(infoSoup),re.S).group(1)
            contentList = crawl.extractContentFromHtmlString(cake)
            print(str(contentList))
            for content in contentList:
                # 判断是否为time
                for time in timeSet:
                    if time in content:
                        investTime = content
                        break
                # 判断是否为type
                for type in typeSet:
                    if type in content:
                        investType = content
                        break
                # 判断是否为money
                for money in moneySet:
                    if money in content:
                        investMoney = content
                        break
    return investTime,investType,investMoney


def getEventTitle(soup):
    '''
    获取事件标题
    '''
    investTitle = ''
    if soup.find('div',class_='title'):
        titleSoup = soup.find('div',class_='title')
        if re.search('title">\s*(.*?)\s*<a',str(titleSoup),re.S).group(1):
            investTitle = re.search('title">\s*(.*?)\s*<a',str(titleSoup),re.S).group(1)
    return investTitle


def getEventLinkIndexList(pageLinkList,logFileName = ''):
    '''
    获取事件链接索引列表
    '''
    eventLinkIndexList = []
    if pageLinkList:
        i = 1
        for pageLink in pageLinkList:
            if handle.getUrlStatus(pageLink) == 200:
                hooshSoup = crawl.getHooshSoup(pageLink,logFileName)
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