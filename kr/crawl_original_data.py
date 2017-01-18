#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import index
import os
from util import io

"""
    1 爬取网页原始数据
    2 原始数据保存到文本
    注意：
        1）每次爬取完成后对origin_html.txt文件标记日期，保存起来，下次更新内容的时候从新建立一个文件
"""

def getRecordStartNum(filePath):
    recordNumList = []
    if os.path.exists(filePath):
        recordNumList = io.getListFromTxt(filePath)
    return recordNumList


if __name__ == '__main__':
    # 初始请求号
    startNum = 5062069

    # 初始url
    url = "http://36kr.com/api/post/" + str(startNum) + "/next"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    # 获取内容
    r = requests.get(url=url, headers=header)
    # 原始网页字符串
    html = r.content.decode('utf-8')
    dic = json.loads(html)

    # 文件输出路径
    startNumFilePath = index.ROOT_PATH + '/data/kr_data' + '/start_num_record.txt'
    originHtmlFilePath = index.ROOT_PATH + '/data/kr_data' + '/origin_html.txt'
    # originHtmlFilePath = index.ROOT_PATH + '/data/kr_data' + '/origin_html_up_1.txt'

    # 获取start_num_record.txt中的历史纪录序号
    recordNumList = getRecordStartNum(startNumFilePath)

    # 建立文件流
    fw_startNum = open(startNumFilePath,'a',encoding='utf-8')
    fw_originHtml = open(originHtmlFilePath,'a',encoding='utf-8')
    # 写入初始数据
    fw_startNum.write(str(startNum) + '\n')
    fw_originHtml.write(html + '\n')

    i = 1
    try:
        while dic['data']['id']:
            if str(dic['data']['id']) not in recordNumList:
                startNum = dic['data']['id']
                # 更新请求地址
                url = "http://36kr.com/api/post/" + str(startNum) + "/next"
                r = requests.get(url=url, headers=header)
                # 原始html数据
                html = r.content.decode('utf-8')
                dic = json.loads(html)
                fw_startNum.write(str(startNum) + '\n')
                fw_originHtml.write(html + '\n')
                print(i,'已写入文件的序号：',startNum)
                if dic['data']['id']:
                    print(i,'获取的最新的序号：',dic['data']['id'])
                i += 1
            else:
                break
    except Exception as ex:
        fw_startNum.close()
        fw_originHtml.close()
    # 关闭文件
    fw_startNum.close()
    fw_originHtml.close()
