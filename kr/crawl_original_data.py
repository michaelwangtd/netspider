#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import index
import os
from util import io
from util import crawl,handle,io,constant

"""
    1 爬取网页原始数据
    2 原始数据保存到文本
    注意：
        1）每次爬取完成后对origin_html.txt文件标记日期，保存起来，下次更新内容的时候从新建立一个文件
"""

def getRecordPageNum(filePath):
    recordNumList = []
    if os.path.exists(filePath):
        recordNumList = io.getListFromTxt(filePath)
    return recordNumList


if __name__ == '__main__':
    # 初始请求号
    startNum = 5813

    # 获取当前时间
    # currentTime = handle.getNowTimeAndDate()

    # 请求常量参数
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    # 文件输出路径
    pageNumFilePath = index.ROOT_PATH + '/data/kr_data' + '/flag_page_num_record.txt'
    # originHtmlFilePath = index.ROOT_PATH + '/data/kr_data' + '/origin_html_kr_' + currentTime + '.txt'
    originHtmlFilePath = index.ROOT_PATH + '/data/kr_data' + '/origin_html_kr_' + '201702161015' + '.txt'
    # 获取start_num_record.txt中的历史纪录序号
    recordNumList = getRecordPageNum(pageNumFilePath)

    # 建立文件流
    fw_pageNum = open(pageNumFilePath, 'a', encoding='utf-8')
    fw_originHtml = open(originHtmlFilePath, 'a', encoding='utf-8')

    # 初始url
    url = "http://36kr.com/api/post/" + str(startNum) + "/next"
    # 获取内容
    r = requests.get(url=url, headers=header)
    html = r.content.decode('utf-8')
    dic = json.loads(html)

    i = 1
    try:
        while dic['data']['id'] and isinstance(dic['data']['id'],int):
            if str(dic['data']['id']) not in recordNumList:
                # 一 准备数据
                currentPageNum = dic['data']['id']
                # currentUrl
                currentUrl = "www.36kr.com/p/" + str(currentPageNum) + ".html"
                # 新增currentUrl字段
                dic['data']['currentUrl'] = currentUrl
                # 二 写出数据
                outputJson = json.dumps(dic,ensure_ascii=False)
                fw_originHtml.write(outputJson + '\n')
                fw_pageNum.write(str(currentPageNum) + '\n')
                print(i,currentPageNum)
                i += 1
                # 三 更新参数
                startNum = dic['data']['id']
                # 初始url
                url = "http://36kr.com/api/post/" + str(startNum) + "/next"
                # 获取内容
                r = requests.get(url=url, headers=header)
                html = r.content.decode('utf-8')
                dic = json.loads(html)
            else:
                break
    except Exception as ex:
        fw_originHtml.close()
        fw_pageNum.close()
    fw_originHtml.close()
    fw_pageNum.close()