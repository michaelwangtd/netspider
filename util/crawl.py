# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
"""
    爬取的工具类
"""

def extractContentFromHtmlString(cake):
    """
        从html混合文本字符串中提取属于标记语言之间的内容形成列表
    """
    if cake:
        pattern = re.compile('>\s*(.*?)\s*<',re.S)
        contentList = pattern.findall(cake)
        return contentList



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