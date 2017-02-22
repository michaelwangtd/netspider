# -*- coding:utf-8 -*-

import requests
import math
import os
from bs4 import BeautifulSoup
from util import io
import time
import redis
import jieba.analyse


"""
    工具类
"""
def getListFromRedis(keyName,r):
    '''
        从redis获取列表
    '''
    resultList = []
    for item in r.lrange(keyName,0,r.llen(keyName)):
        resultList.append(item.decode('utf-8'))
    return resultList


def getTagbaseDicFromRedis(initDic,tagbaseNameList):
    '''
        从redis获取标签库字典
        需要提供redis库key值列表：redisKeyList
        不需要提供redis配置信息，配置信息直接从config配置文件读取
    '''
    if isinstance(tagbaseNameList,list):
        if tagbaseNameList:
            #initDic = {}
            r = redis.Redis(host='139.129.226.200',port=6379,password='redis_zhizhugraph*ts',db=1)
            # 遍历tagbaseNameList
            for tagbaseName in tagbaseNameList:
                # 获取tagbase列表
                tagbaseList = getListFromRedis(tagbaseName,r)
                if tagbaseName not in initDic.keys():
                    initDic[tagbaseName] = tagbaseList
            return initDic


def dic2list(dic):
    '''
        目前dic字典的value值要求是list
        后续可以继续添加由dic转换到list时dic中value的类型
    '''
    resultList = []
    if isinstance(dic,dict):
        for key,value in dic.items():
            if isinstance(value,list):
                resultList.extend(value)
    # resultList = list(set(resultList))
    return resultList


def splitEquivalentTag(tagList):
    '''
        分解同义标签
        列表中的元素如果是同义标签（'xxx||xxx||xxx'），进行分割
        input:list  output:list
    '''
    resultList = []
    for item in tagList:
        if '||' in item:
            resultList.extend(item.split('||'))
        else:
            resultList.append(item)
    return resultList


def double2one(doubleList):
    '''
        列表去重
    '''
    return list(set(doubleList))


def persistentTagbase(tagbase,filePath):
    '''
        为什么是persistent tagbase，因为持久化的文件生成的格式是特定的
        tagbase可以是字典也可以是列表，如果是字典就转化成列表
        将tagbase的列表以“覆盖”写的方式写入filePath文件
    '''
    tagbaseList = []
    # 准备数据格式
    if isinstance(tagbase,dict):
        tagbaseList = dic2list(tagbase)
    if isinstance(tagbase,list):
        tagbaseList = tagbase
    # 分解标签列表中的同义标签
    tagbaseList = splitEquivalentTag(tagbaseList)
    # 去重
    tagbaseList = double2one(tagbaseList)
    # 数据持久化准备
    fw = open(filePath,'w',encoding='utf-8')
    for tag in tagbaseList:
        fw.write(tag + '\n')
    fw.close()


def extractTheme(tagList,tagbaseFilePath):
    themeList = []
    tagbaseList = io.readListFromTxt(tagbaseFilePath)
    for item in tagList:
            if item in tagbaseList:
                themeList.append(item)
    return themeList


def extractTagsFromContent(content):
    '''
        从内容中提取标签的入口函数
    '''
    # redis标签库key值
    tagbaseNameList = ['industry_tags', 'research_inst_tags', 'invs_cmy_tags', 'university_tags', 'product_cmy_tags',
                       'meeting_tags', 'person_tags', 'product_tags']
    tagbaseDic = {}
    # 标签库路径
    tagbaseFilePath = io.getLibFilePath('topic_tagbase.txt')
    # 从redis读取的标签
    if not os.path.exists(tagbaseFilePath):
        tagbaseDic = getTagbaseDicFromRedis(tagbaseDic, tagbaseNameList)
        persistentTagbase(tagbaseDic, tagbaseFilePath)
    # 加载jieba
    jieba.load_userdict(tagbaseFilePath)

    cutOne = content.replace('&nbsp;', '')
    # 提取关键词
    tagList = jieba.analyse.extract_tags(cutOne)
    themeList = extractTheme(tagList, tagbaseFilePath)

    return ' '.join(themeList)


def getNowTimeAndDate():
    '''
        获取系统当前日期，时间，精确到分钟:yyyymmddHHMM
        每次更新数据时用于命名文件名
    '''
    return time.strftime('%Y%m%d%H%M',time.localtime(time.time()))


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