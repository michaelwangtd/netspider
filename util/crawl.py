# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
"""
    爬取的工具类
"""

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