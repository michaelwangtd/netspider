# -*- coding:utf-8 -*-

from newseed.util import linkList
"""
数据源：newseed
数据分类：并购关系信息
"""

if __name__ == '__main__':
    # 初始链接地址
    initUrl = 'http://newseed.pedaily.cn/invest/r115-p1'


    # 获取总记录条数
    totalRecordNum = linkList.getTotalRecordNum(initUrl)
