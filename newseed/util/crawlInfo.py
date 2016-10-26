# -*- coding:utf-8 -*-

from util import crawl,handle,io
from newseed.util import linkList
import re


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




def getProductCompanyCreateTimeAndArea(soup):
    time = ''
    area = ''
    if soup.find('div',class_='info'):
        infoSoup = soup.find('div',class_='info')
        if re.search('class="info">\s*(.*?)\s*<p class="keyword">',str(infoSoup),re.S):
            timeAndAreaStr = re.search('class="info">\s*(.*?)\s*<p class="keyword">', str(infoSoup), re.S)
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