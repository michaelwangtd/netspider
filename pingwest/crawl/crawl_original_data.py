#!/usr/bin/env python
# -*- coding:utf-8 -*-

import index
import requests
import json
from util import io,handle
import os


"""
    通过接口直接获取json数据
"""




def getRecordPostId(filePath):
    recordNumList = []
    if os.path.exists(filePath):
        recordNumList = io.getListFromTxt(filePath)
    return recordNumList


if __name__ == '__main__':
    # 每次更新时只需设定ptime为最新
    ptime = 1487008612

    currentTime = handle.getNowTimeAndDate()

    originHtmlOutputFilePath = index.ROOT_PATH + '/data/pingwest_data/' + 'origin_html_pingwest_' + currentTime + '.txt'
    ptimeFlagOutputFilePath = index.ROOT_PATH + '/data/pingwest_data/' + 'ptime_flag_record_pingwest.txt'

    url = 'http://www.pingwest.com/wp-admin/admin-ajax.php'
    data = {'action': 'my_recommand', 'secutity': 'b17e1ad3ea', 'postid': '', 'type': '1'}
    data['postid'] = ptime

    r = requests.post(url=url, data=data)
    html = r.content.decode('utf-8')
    dicList = json.loads(html)

    # 获取ptimeList
    ptimeList = getRecordPostId(ptimeFlagOutputFilePath)

    # 建立文件流
    fw_ptime = open(ptimeFlagOutputFilePath,'a',encoding='utf-8')
    fw_originHtml = open(originHtmlOutputFilePath,'a',encoding='utf-8')
    # 写入初始数据
    fw_ptime.write(str(ptime) + '\n')
    fw_originHtml.write(html + '\n')

    i = 1
    try:
        while dicList[0]['ptime']:
            if str(dicList[0]['ptime']) not in ptimeList:
                ptime = dicList[0]['ptime']
                # 更新ptime
                data['postid'] = ptime
                r = requests.post(url=url, data=data)
                # 原始html数据
                html = r.content.decode('utf-8')
                dicList = json.loads(html)
                fw_ptime.write(str(ptime) + '\n')
                fw_originHtml.write(html + '\n')
                print(i, '已写入文件的序号：', ptime)
                if dicList[0]['ptime']:
                    print(i, '获取的最新的序号：', dicList[0]['ptime'])
                i += 1
            else:
                break
    except Exception as ex:
        fw_ptime.close()
        fw_originHtml.close()
    # 关闭文件
    fw_ptime.close()
    fw_originHtml.close()





