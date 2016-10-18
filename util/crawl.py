# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
"""
    爬取的工具类
"""

def washTime(investTime):
    if investTime:
        temp = investTime.replace('年','.').replace('月','.').replace('日','')
        return temp



def washData(string):
    """
        1 去除“<>”内容
        2 去除空格
    """
    if string:
        temp = re.sub('<.*?>','',string)
        string = temp.replace('\r','').replace('\n','').replace('\t','')
        return string



def getStringAndHrefByAtag(string):
    """
        通过正则匹配a标签内的内容和链接
    """
    content = ''
    link = ''
    if re.search('target="_blank">(.*?)</a>',string,re.S):
        content = re.search('target="_blank">(.*?)</a>',string,re.S).group(1)
    if re.search('href="(.*?)" target',string,re.S):
        link = re.search('href="(.*?)" target',string,re.S).group(1)
    return content,link



def extractContentFromHtmlString(cake):
    """
        从html混合文本字符串中提取属于标记语言之间的内容形成列表
    """
    singleContentList = []
    cleanedContentList = []
    if cake:
        pattern = re.compile('>\s*(.*?)\s*<',re.S)
        contentList = pattern.findall(cake)
        # 去掉列表中“空”元素
        for item in contentList:
            if item:
                singleContentList.append(item)
        # 去掉字符串中的空格
        for item in singleContentList:
            temp = item.replace('\s', '').replace('\t', '').replace('\r', '')
            cleanedContentList.append(temp)
        return cleanedContentList



def getHooshSoup(url):
    """
        获取hooshSoup
        根据url链接获取html文本，以BeautifulSoup形式返回
    """
    try:
        header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' }
        r = requests.get(url,headers = header)
        r.encoding = 'utf-8'
        html = r.text
        hooshSoup = BeautifulSoup(html).find('body')
        return hooshSoup
    except Exception as err:
        print('requests获取html失败：',err)