# -*- coding:utf-8 -*-

from util import handle,crawl
from newseed.util import crawlInfo
import socket
import re
from bs4 import BeautifulSoup
# socket.setdefaulttimeout(60)
"""
newseed工具类
"""

def getProductCompanyInfoList(linkIndexList,logFileName):
    hostName = 'http://newseed.pedaily.cn'
    productInfoList = []
    if linkIndexList:
        i = 1
        for linkIndex in linkIndexList:
            link = hostName + linkIndex.strip()
            # statusCode = handle.getUrlStatus(link)
            # if statusCode == 200:
            if link:
                ## 获取对应信息
                # 获取浓汤soup
                hooshSoup = crawl.getHooshSoup(link, logFileName)
                if hooshSoup:
                    # print('获取到hooshSoup')
                    # 初始化变量信息
                    investTitle = ''
                    investTime = ''
                    investType = ''
                    investMoney = ''
                    productCompanyInfoList = ''
                    investCompanyInfoList = ''
                    investIntroduce = ''
                    try:
                        if hooshSoup.find('div', class_='main').find('div', class_='record').find('div',
                                                                                                         class_='col-md-860'):
                            # 定位到html标记的最小单位
                            soup = hooshSoup.find('div', class_='main').find('div', class_='record').find('div',
                                                                                                                 class_='col-md-860')
                            # 获取公司名称和注册名称
                            productCompanyName,productCompanyFullName = crawlInfo.getProductCompanyName(soup)
                            # 获取公司创建时间，地域
                            createTime,area = crawlInfo.getProductCompanyCreateTimeAndArea(soup)
                            # 获取并购相关公司名称，链接（公司信息以列表(name,link)形式返回）
                            productCompanyHomepage = crawlInfo.getHomepage(soup)
                            # 获取事件介绍
                            investIntroduce = getInvestIntroduce(soup)
                            companyIntroduce = getCompanyIntroduce(soup)
                        else:
                            print('这条数据信息已丢失...')
                            ## 处理字段，形成列表
                        recordList = createRecordList(hostName, investTitle, investTime, investType, investMoney,
                                                          productCompanyInfoList, investCompanyInfoList, investIntroduce)
                        if recordList != -1:
                            # 将处理完的一条记录数据加入列表
                            productInfoList.append(recordList)
                            print(recordList)
                    except Exception as ex:
                        print(ex)
            print('已处理第【',str(i),'】条记录')
            i += 1
        return productInfoList



def getEventInfoList(linkIndexList,logFileName):
    hostName = 'http://newseed.pedaily.cn'
    eventInfoList = []
    if linkIndexList:
        i = 1
        for linkIndex in linkIndexList:
            link = hostName + linkIndex.strip()
            # statusCode = handle.getUrlStatus(link)
            # if statusCode == 200:
            if link:
                ## 获取对应信息
                # 获取浓汤soup
                hooshSoup = crawl.getHooshSoup(link, logFileName)
                if hooshSoup:
                    # print('获取到hooshSoup')
                    # 初始化变量信息
                    investTitle = ''
                    investTime = ''
                    investType = ''
                    investMoney = ''
                    productCompanyInfoList = ''
                    investCompanyInfoList = ''
                    investIntroduce = ''
                    try:
                        if hooshSoup.find('div', class_='main').find('div', class_='record invest').find('div',
                                                                                                         class_='col-md-860'):
                            # 定位到html标记的最小单位
                            soup = hooshSoup.find('div', class_='main').find('div', class_='record invest').find('div',
                                                                                                                 class_='col-md-860')
                            # 获取事件标题
                            investTitle = getEventTitle(soup)
                            # 获取时间，类型，金额
                            investTime, investType, investMoney = getTimeTypeAndMoney(soup)
                            # 获取并购相关公司名称，链接（公司信息以列表(name,link)形式返回）
                            productCompanyInfoList, investCompanyInfoList = getInvestRelatedCompany(soup)
                            # 获取事件介绍
                            investIntroduce = getInvestIntroduce(soup)
                        else:
                            print('这条数据信息已丢失...')
                            ## 处理字段，形成列表
                        # print('到达数据校验这一步了')
                        recordList = createRecordList(hostName, investTitle, investTime, investType, investMoney,
                                                          productCompanyInfoList, investCompanyInfoList, investIntroduce)
                        if recordList != -1:
                            # 将处理完的一条记录数据加入列表
                            eventInfoList.append(recordList)
                            print(recordList)
                    except Exception as ex:
                        print(ex)
            print('已处理第【',str(i),'】条记录')
            i += 1
        return eventInfoList


def getInvestRelatedCompany(soup):
    '''
        获取并购公司信息
    '''
    productCompanyInfoList = []
    investCompanyInfoList = []
    if soup.find('div',class_='info').find('p',class_='keyword'):
        keywordSoup = soup.find('div',class_='info').find('p',class_='keyword')
        # 产品公司信息
        if re.search('企</span>\s*(.*?)\s*<span class="btn blue">投',str(keywordSoup),re.S):
            productCompanyStr = re.search('企</span>\s*(.*?)\s*<span class="btn blue">投', str(keywordSoup), re.S).group(1)
            content,link = crawl.getStringAndHrefByAtag(productCompanyStr)
            if content:
                productCompanyInfoList.append((content,link))
        # 投资公司信息
        if re.search('投</span>\s*(.*?)\s*</p>',str(keywordSoup),re.S):
            investCompanyStr = re.search('投</span>\s*(.*?)\s*</p>',str(keywordSoup),re.S).group(1)
            investCompanySoup = BeautifulSoup(investCompanyStr)
            # 找出所有a标签
            resultSetAtag = investCompanySoup.find_all('a')
            if resultSetAtag:
                for aTag in resultSetAtag:
                    content,link = crawl.getStringAndHrefByAtag(str(aTag))
                    if content:
                        investCompanyInfoList.append((content,link))
            # 找出所有span标签
            resultSetSpantag = investCompanySoup.find_all('span')
            if resultSetSpantag:
                for spanTag in resultSetSpantag:
                    content = crawl.getStringBySpantag(str(spanTag))
                    if content:
                        investCompanyInfoList.append((content,'/'))

    return productCompanyInfoList,investCompanyInfoList




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
    if investTime:
        if handle.verifyTime(investTime) == False:
            print('investTime字段不合格:【',str(investTime))
            return -1
    if investType:
        if handle.verifyTpye(investType) == False:
            print('investType字段不合格:【',str(investType))
            return -1
    if investMoney:
        if handle.verifyMoney(investMoney) == False:
            print('investMoney字段不合格:【',str(investMoney))
            return -1
    # 清洗数据
    investTitle = crawl.washData(investTitle)
    if investTime:
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


def getCompanyLinkIndexList(pageLinkList,logFileName = ''):
    '''
    获取公司链接索引列表
    '''
    companyLinkIndexList = []
    if pageLinkList:
        i = 1
        for pageLink in pageLinkList:
            if handle.getUrlStatus(pageLink) == 200:
                hooshSoup = crawl.getHooshSoup(pageLink,logFileName)
                if hooshSoup:
                    ulSoup = hooshSoup.find('ul',id='newslist')
                    for trTag in ulSoup.find_all('li'):
                        linkIndex = trTag.find_all('div',class_='user-pic')[0].a.get('href')
                        companyLinkIndexList.append(linkIndex)
                        print('获取索引数目：',str(i),linkIndex)
                        i += 1
    print('companyLinkIndexList长度为：',str(len(companyLinkIndexList)))
    return companyLinkIndexList



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