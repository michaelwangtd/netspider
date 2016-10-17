# -*- coding:utf-8 -*-

import requests
import math
import os
from bs4 import BeautifulSoup


"""
    工具类
"""

def str2soup(str):
    if type(str) == str:
        soup = BeautifulSoup(str)
        return soup


def listReadFromTxt(during ,fileName):
    """
        从txt文本中读取内容形成列表
    """
    # 列表数据
    dataList = []
    # 根目录
    rootPath = os.path.dirname(os.path.dirname(__file__))
    fullFilePath = os.path.join(rootPath,during,fileName)
    try:
        fr = open(fullFilePath,'r',encoding='utf-8')
        i = 1
        while True:
            line = fr.readline().strip()
            if line:
                dataList.append(line)
                print(str(i),'/',line)
                i += 1
            else:
                break
        fr.close()
    except Exception as err:
        print('文件读取错误：',err)
    if dataList:
        return dataList



def listAppendWrite2Txt(dataList,fileName,during = ''):
    """
        将列表内容追加写入txt文本
    """
    # 获取项目跟目录
    rootPath = os.path.dirname(os.path.dirname(__file__))
    # 组成全路径
    fullFilePath = os.path.join(rootPath,during,fileName)
    # 追加方式写入文本
    fw = open(fullFilePath,'a',encoding='utf-8')
    for item in dataList:
        fw.writelines(item + '\n')
    fw.close()
    print('文件写入完成...')



def getUrlStatus(url):
    """
        获取url链接状态码
    """
    try:
        r = requests.get(url)
        return r.status_code
    except Exception as err:
        print('该链接' + str(url) + '不可用:',err)



def getPageLinkIndexList(totalRecordNum):
    """
        通过总的记录数计算页面链接索引
        以列表形式返回
    """
    if totalRecordNum:
        if int(totalRecordNum) % 10 == 0:
            endNum = int(totalRecordNum) / 10
        else:
            endNum = math.ceil(int(totalRecordNum) /10)
        # 形成字符串索引列表
        return [str(i+1) for i in range(int(endNum))]