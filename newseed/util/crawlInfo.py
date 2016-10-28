# -*- coding:utf-8 -*-

from util import crawl,handle,io
from newseed.util import linkList
import re



def createVcCompanyRecordList(vcCompanyName,link,vcCompanyFullName,createTime,vcCompanyPlace,vcCompanyArea,vcCompanyHomepage,vcCompanyIntroduce):
    '''
        1 校验数据，发现不合格的数据，立即返回失败标志 -1
        2 清洗部分数据
        3 将字段组成列表
    '''
    # 校验数据
    if createTime:
        if handle.verifyTime(createTime) == False:
            print('createTime字段不合格:【', str(createTime))
            return -1
    if vcCompanyPlace:
        if handle.verifyArea(vcCompanyPlace) == False:
            print('area字段不合格:【', str(vcCompanyPlace))
            return -1
    if vcCompanyArea:
        if handle.verifyPlace(vcCompanyArea) == False:
            print('area字段不合格:【', str(vcCompanyArea))
            return -1
    # 清洗数据
    if createTime:
        createTime = crawl.extractTime(createTime)
    companyIntroduce = crawl.washData(vcCompanyIntroduce)
    # 返回recordList
    return [vcCompanyName, link, vcCompanyFullName, createTime, vcCompanyPlace,vcCompanyArea, vcCompanyHomepage, companyIntroduce]




def createProductCompanyRecordList(productCompanyName, link, productCompanyFullName, createTime, area,productCompanyHomepage,companyIntroduce):
    '''
        1 校验数据，发现不合格的数据，立即返回失败标志 -1
        2 清洗部分数据
        3 将字段组成列表
    '''
    # 校验数据
    if createTime:
        if handle.verifyTime(createTime) == False:
            print('createTime字段不合格:【', str(createTime))
            return -1
    if area:
        if handle.verifyArea(area) == False:
            print('area字段不合格:【', str(area))
            return -1
    # 清洗数据
    if createTime:
        createTime = crawl.extractTime(createTime)
    companyIntroduce = crawl.washData(companyIntroduce)
    # 返回recordList
    return [productCompanyName, link, productCompanyFullName, createTime, area, productCompanyHomepage, companyIntroduce]


def getHomepage(soup):
    homePage = ''
    if soup.find('div',class_='info').find('p',class_='link'):
        linkSoup = soup.find('div',class_='info').find('p',class_='link')
        if linkSoup.find('a'):
            aSoup = linkSoup.find('a')
            content,url = crawl.getStringAndHrefByAtag(str(aSoup))
            if content:
                homePage = content
    return homePage



def getVcCompanyCreateTimePlaceAndArea(soup):
    timeSet = ['年','月','日']
    placeSet = ['市','省','香港','澳门','台湾','地区','共和国','国','州','巴黎','瑞士','柬埔寨','城','台北','纽约','加拿大']
    areaSet = ['本土','外资','合资','海外']
    createTime = ''
    vcCompanyPlace = ''
    vcCompanyArea = ''

    if soup.find('div',class_='info'):
        infoSoup = soup.find('div',class_='info')
        if re.search('class="info">\s*(.*?)\s*<p class="keyword">',str(infoSoup),re.S):
            timeAndAreaStr = re.search('class="info">\s*(.*?)\s*<p class="keyword">', str(infoSoup), re.S).group(1)
            timeAndAreaList = crawl.extractContentFromHtmlString(timeAndAreaStr)
            # 遍历内容列表
            for content in timeAndAreaList:
                # 查找时间
                for item in timeSet:
                    if item in content:
                        createTime = content
                        break
                # 查找place
                for item in placeSet:
                    if item in content:
                        vcCompanyPlace = content
                        break
                # 查找area
                for item in areaSet:
                    if item in content:
                        vcCompanyArea = content
                        break

    return createTime,vcCompanyPlace,vcCompanyArea



def getProductCompanyCreateTimeAndArea(soup):
    time = ''
    area = ''
    if soup.find('div',class_='info'):
        infoSoup = soup.find('div',class_='info')
        if re.search('class="info">\s*(.*?)\s*<p class="keyword">',str(infoSoup),re.S):
            timeAndAreaStr = re.search('class="info">\s*(.*?)\s*<p class="keyword">', str(infoSoup), re.S).group(1)
            timeAndAreaList = crawl.extractContentFromHtmlString(timeAndAreaStr)
            # 去掉list中的“/”
            cleanedList = []
            for item in timeAndAreaList:
                if item != '/':
                    cleanedList.append(item)
            if cleanedList:
                if len(cleanedList) == 2:
                    time = cleanedList[0]
                    area = cleanedList[1]
                elif len(cleanedList) == 1:
                    temp = cleanedList[0]
                    if '年' in temp or '月' in temp or '日' in temp:
                        time = temp
                    else:
                        area = temp
    return time,area



def getAllCompanyName(string):
    name = ''
    fullName = ''
    if string:
        if re.findall('<span>\s*(.*?)\s*</span>',string,re.S):
            name = re.findall('<span>\s*(.*?)\s*</span>', string, re.S)[0]
        if re.findall('class="title">\s*(.*?)\s*<span>',string,re.S):
            fullName = re.findall('class="title">\s*(.*?)\s*<span>', string, re.S)[0]
    return name.strip(),fullName.strip()


def getProductCompanyName(soup):
    if soup.find('div',class_='title'):
        titleSoup = soup.find('div',class_='title')
        name,fullName = getAllCompanyName(str(titleSoup))
        return name,fullName


def getVcCompanyName(soup):
    if soup.find('h1',class_='title'):
        titleSoup = soup.find('h1',class_='title')
        name,fullName = getAllCompanyName(str(titleSoup))
        return name,fullName