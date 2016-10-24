# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os
"""
    爬取的工具类
"""

def washTime(investTime):
    if investTime:
        temp = ''
        if '年' in investTime and '月' in investTime and '日' in investTime:
            temp = investTime.replace('年','.').replace('月','.').replace('日','')
        if '年' in investTime and '月' in investTime and '日' not in investTime:
            temp = investTime.replace('年','.').replace('月','')
        if '年' in investTime and '月' not in investTime and '日' not in investTime:
            temp = investTime.replace('年','')
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


def getStringBySpantag(string):
    """
        通过正则匹配a标签内的内容和链接
    """
    content = ''
    if re.search('class="default">\s*(.*?)\s*</span>',string,re.S):
        content = re.search('class="default">\s*(.*?)\s*</span>',string,re.S).group(1)
    return content



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



def getHooshSoup(url,logFileName = ''):
    """
        获取hooshSoup
        根据url链接获取html文本，以BeautifulSoup形式返回
        logFileName作用是将未抓取到的url写入到指定文件中，日志目录指定在netspider根目录下
    """
    try:
        header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' }
        r = requests.get(url,headers = header,timeout = 5)
        r.encoding = 'utf-8'
        html = r.text
        hooshSoup = BeautifulSoup(html).find('body')
        return hooshSoup
    except Exception as err:
        print('requests获取html失败：',err)
        # 将未获取到的url写入文件
        if logFileName:
            logFilePath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'log',logFileName)
            fw = open(logFilePath,'a',encoding='utf-8')
            fw.writelines(url.strip() + '\n')
            fw.close()