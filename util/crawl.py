# -*- coding:utf-8 -*-

import requests
from util import constant
import json
"""
    爬取的工具类
"""

def getHooshSoup(url):
    """
        根据url链接获取html文本，以BeautifulSoup形式返回
    """
    # try:
    header = json.load(constant.HEADER)
    r = requests.get(url,headers = header)
    r.encoding = 'utf-8'
    html = r.text
    print(html)
    # except Exception as err:
    #     print('requests获取html失败：',err)