# -*- coding:utf-8 -*-

from util import handle,crawl

"""
newseed工具类
"""

def getTotalRecordNum(initUrl):
    '''
    获取页面总记录数
    '''
    # 检验url链接
    statusCode = handle.getUrlStatus(initUrl)
    if statusCode == 200:
        #
        crawl.getHooshSoup(initUrl)