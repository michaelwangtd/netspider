#!/usr/bin/env python
# -*- coding:utf-8 -*-

import index
import requests
import json
from util import io,handle,crawl,constant
import os
import time

"""
    通过接口直接获取json数据
"""

# def recursivelyWrite(url,data,fw_origin,fw_ptime,count,ptimeList):
#     '''
#         这里的精彩之处在于递归的写入
#     '''
#     try:
#         count += 1
#         r = requests.post(url=url,data=data)
#         # 获取内容
#         content = r.text    # 这里是原始编码的json格式
#         dicList = json.loads(content)
#         # lineDicStr = str(dicList[0])
#         # lineDicStr = dicList[0]
#         # 获取postid
#         postId = data['postid']
#         # print(postId)
#         # 数据持久化
#         fw_origin.write(content + '\n')
#         fw_ptime.write(str(postId) + '\n')
#         print(count,dicList[0]['title'])
#         # 给定递归条件
#         if dicList[0]['ptime']:
#             if str(dicList[0]['ptime']) not in ptimeList:
#                 data['postid'] = dicList[0]['ptime']
#                 print(dicList[0]['ptime'])
#                 return recursivelyWrite(url,data,fw_origin,fw_ptime,count,ptimeList)
#         else:
#             return 0
#     except Exception as ex:
#         fw_origin.close()
#         fw_ptime.close()



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




    # ptimeList = io.getListFromTxt(ptimeOriginFilePath)
    # print(len(ptimeList),ptimeList)
    # # I/O操作
    # fw_origin = open(originOutputFilePath,'a')
    # fw_ptime = open(ptimeOutputFilePath,'a',encoding='utf-8')
    # # 使用回掉函数，在函数内部完成持久化操作
    # recursivelyWrite(url,data,fw_origin,fw_ptime,0,ptimeList)
    # fw_ptime.close()
    # fw_origin.close()
