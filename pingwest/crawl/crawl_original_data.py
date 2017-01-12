#!/usr/bin/env python
# -*- coding:utf-8 -*-
import index
import requests
import json
from util import io,handle,crawl,constant


def recursivelyWrite(url,data,fw_origin,fw_ptime,count,ptimeList):
    '''
        这里的精彩之处在于递归的写入
    '''
    try:
        count += 1
        r = requests.post(url=url,data=data)
        # 获取内容
        content = r.text    # 这里是原始编码的json格式
        dicList = json.loads(content)
        # lineDicStr = str(dicList[0])
        # lineDicStr = dicList[0]
        # 获取postid
        postId = data['postid']
        # print(postId)
        # 数据持久化
        fw_origin.write(content + '\n')
        fw_ptime.write(str(postId) + '\n')
        print(count,dicList[0]['title'])
        # 给定递归条件
        if dicList[0]['ptime']:
            if str(dicList[0]['ptime']) not in ptimeList:
                data['postid'] = dicList[0]['ptime']
                print(dicList[0]['ptime'])
                return recursivelyWrite(url,data,fw_origin,fw_ptime,count,ptimeList)
        else:
            return 0
    except Exception as ex:
        fw_origin.close()
        fw_ptime.close()



"""
    直接调用ajax接口
"""
if __name__ == '__main__':
    # 设定初始变量
    # 设定的这个postid一定要保证是最新的
    # postid = '1481627840'
    postid = '1347883547'
    originOutputFilePath = index.rootPath + '/data/pingwest_data/' + 'origin_content_1213.txt'
    ptimeOutputFilePath = index.rootPath + '/data/pingwest_data/' + 'origin_ptime_1213.txt'
    ptimeOriginFilePath = index.rootPath + '/data/pingwest_data/' + 'origin_ptime.txt'

    url = 'http://www.pingwest.com/wp-admin/admin-ajax.php'
    data = {'action': 'my_recommand', 'secutity': 'b17e1ad3ea', 'postid': '', 'type': '1'}
    data['postid'] = postid

    # 获取ptimeList
    ptimeList = io.getListFromTxt(ptimeOriginFilePath)
    print(len(ptimeList),ptimeList)
    # I/O操作
    fw_origin = open(originOutputFilePath,'a')
    fw_ptime = open(ptimeOutputFilePath,'a',encoding='utf-8')
    # 使用回掉函数，在函数内部完成持久化操作
    recursivelyWrite(url,data,fw_origin,fw_ptime,0,ptimeList)
    fw_ptime.close()
    fw_origin.close()
