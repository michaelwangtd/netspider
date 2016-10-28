# -*- coding:utf-8 -*-

import requests
import math
import os
from bs4 import BeautifulSoup
from util import io



"""
    工具类
"""

def mergeExcelFromFixedDirNewseed(fileNameList,newOutputFilePath):
    '''
        所有excel内容读取到内存中，重新写入到新文件中
    '''
    prePath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','newseed_data','resultSet')
    if fileNameList:
        # 将所有excel信息读取到列表
        cacheList = []
        for i in range(len(fileNameList)):
            tempList = io.getListFromExcel(prePath,fileNameList[i])
            cacheList.extend(tempList)
        # 重新生成一个excel文件
        io.writeContent2Excel(cacheList,newOutputFilePath)








def verifyArea(area):
    """
        校验地域
    """
    areaSet = ['市','省','香港','澳门','台湾','地区','共和国','国','州','巴黎','瑞士','柬埔寨','城','台北','纽约','加拿大']
    if area:
        for item in areaSet:
            if item in area:
                return True
    return False


def verifyPlace(place):
    """
        校验地域
    """
    areaSet = ['本土','外资','合资','海外']
    if place:
        for item in areaSet:
            if item in place:
                return True
    return False



def verifyMoney(investMoney):
    """
        校验金额
    """
    moneySet = ['万日元', '万韩国元', '万新加坡元', '万人民币', '万港币', '万英镑', '万澳大利亚元', '万欧元', '万美元', '万新台币']
    if investMoney:
        for item in moneySet:
            if item in investMoney:
                return True
    return False



def verifyTpye(investType):
    """
        校验类型
    """
    typeSet = ['不详', 'E轮', 'F轮', 'IPO上市及以后', 'D轮', 'A+轮', '其他轮', 'Pre-A', 'C轮', '天使', '种子', '并购', '股权投资', 'B轮', 'A轮']
    if investType:
        for item in typeSet:
            if item in investType:
                return True
    return False



def verifyTime(investTime):
    """
        校验时间
    """
    timeSet = ['年','月','日']
    if investTime:
        for item in timeSet:
            if item in investTime:
                return True
    return False



def str2soup(str):
    """
        将字符串转换成Beautiful元素
    """
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
                print(str(i),'    ',line)
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