# -*- coding:utf-8 -*-

import requests

"""
工具类
"""

def getUrlStatus(url):
    """
        获取url链接状态码
    """
    try:
        r = requests.get(url)
        return r.status_code
    except Exception as err:
        print('该链接不可用:',err)


