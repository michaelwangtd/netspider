#!/usr/bin/env python
# -*- coding:utf-8 -*-

import index
import json
from util import crawl,handle,constant,io
import copy
import re
from collections import OrderedDict


def scanTitle(title):
    if 'PW晨报' in title or '今日乐见' in title or '晨间阅读' in title or 'PW晚报' in title\
        or '晨报' in title or '今日bu乐见' in title or '今日 bu 乐见' in title or\
        'PW 晨报' in title or 'PW晚报' in title:
        return False
    else:
        return True


def selectProcessArticle(title):
    if 'PW晨报' in title or 'PW晚报' in title or '晨报' in title:
    # if 'PW晨报' in title:
        return True
    else:
        return False


def getInitDic():
    initDic = OrderedDict()
    initDic['title'] = '',
    initDic['time'] = '',
    initDic['url'] = '',
    initDic['originTag'] = '',
    initDic['tag'] = '',
    initDic['content'] = '',
    initDic['author'] = '',
    initDic['content_url'] = []
    return initDic


def getTitleAndContentList(strline):
    # 正则表达式
    pattern = re.compile('(>[0-9][.):：、,，])|(>[【|\[][0-9][\]|】])', re.S)
    # 初始变量
    articleList = []
    boatList = []
    finalArticleList = []
    # 分段落算法
    for item in strline.split('\n'):
        if pattern.findall(item):
            if boatList:
                articleList.append(boatList)
                boatList = []
            boatList.append(item)
        else:
            boatList.append(item)
    # 格式化
    for item in articleList:
        if item[0]:
            title = crawl.extractContentFromHtmlString(item[0])
        else:
            title = ''
        contentList = item[1:]
        content = crawl.extractContentFromHtmlString(''.join(contentList))
        finalArticleList.append([title,content])
    return finalArticleList


def getTimeStampFromTxt(originHtmlTxtName):
    '''
        正则提取字符串中的时间信息
    '''
    cake = originHtmlTxtName
    if isinstance(str,cake):
        if '.' in cake:
            part1 = cake.split('.')[0]
            if '_' in part1:
                if part1.count('_') == 3:
                    timeStamp = part1.split('_')[len(part1.split('_')) - 1]
                    return timeStamp


def isValid(title):
    '''
        剔除诸如“今日乐见”等较难处理的标题
    '''
    blackList = index.TITLE_BLACK_LIST_PINGWEST
    for item in blackList:
        if item in title:
            print('当前记录不处理...')
            return False
    return True


def getTimeFromJson(timeString,timeStamp):
    '''
        timeStamp为格式化的时间信息，精确到分 eg：201702141536
        timeString待提取的时间信息
    '''
    if timeString:
        #
        if '秒前' in timeString or '分前' in timeString or '小时前' in timeStamp:
            return timeStamp[0:4] + '-' + timeStamp[4:6] + '-' + timeStamp[6:8]
        elif '天前' in timeStamp:
            if re.findall('([0-9]+)', timeStamp, re.S):
                dayNum = int(re.findall('([0-9]+)', timeStamp, re.S)[0])
                # 获取时间戳毫秒数
                currentNum = int(time.mktime(time.strptime(timeStamp, '%Y%m%d%H%M')))
                beforeNum = currentNum - int(dayNum) * 24 * 60 * 60
                return time.strftime('%Y-%m-%d', time.localtime(beforeNum))
        else:
            return timeString


def getUrlListFromContentHtml(contentHtml):
    '''

    '''






if __name__ == '__main__':
    # 指定待处理文件的文件名
    originHtmlTxtName = 'origin_html_pingwest_201701181122.txt'


    # 获取文件名中的时间信息
    timeStamp = getTimeStampFromTxt(originHtmlTxtName)

    # 构建路径
    inputFilePath = index.ROOT_PATH + '/data/pingwest_data/' + originHtmlTxtName
    outputFilePath = index.ROOT_PATH + '/data/pingwest_data/resultSet/' + 'shaped_pingwest_' + timeStamp + '.txt'
    #
    fr = open(inputFilePath,'r')
    fw = open(outputFilePath,'w',encoding='utf-8')
    i = 1
    while True:
        line = fr.readline().strip()
        if line:
            lineDic = json.loads(line)[0]
            if isValid(lineDic['title']):
                # 初始化记录字典
                initDic = getInitDic()
                # 这里将初始化部分提前
                initDic['title'] = lineDic['title']
                initDic['url'] = lineDic['posturl']
                initDic['author'] = lineDic['name']
                # 提取时间信息
                time = getTimeFromJson(lineDic['gtime'],timeStamp)
                initDic['time'] = time
                # 提取内容content中的url链接
                getUrlListFromContentHtml(lineDic['contenthtml'])
                # 提取内容
                getContentFromJson(lineDic['contenthtml'])
                # 提取标签


                # print(i,type(lineDic),lineDic['title'])
                # 挑选出不需要处理的记录
                # if scanTitle(lineDic['title']):
                #     # 处理文章内容
                #     content = ''.join(crawl.extractContentFromHtmlString(lineDic['contenthtml']))
                #     # 构建记录字典
                #     initDic['content'] = content
                #     initDic['title'] = lineDic['title']
                #     jsonRecord = json.dumps(initDic,ensure_ascii=False)
                #     fw.write(jsonRecord + '\n')
                # if selectProcessArticle(lineDic['title']):
                #     # print(i,lineDic['title'])
                #     titleAndContentList = getTitleAndContentList(lineDic['contenthtml'])
                #     for item in titleAndContentList:
                #
                #         newInitDic = copy.deepcopy(initDic)
                #         newInitDic['title'] = item[0]
                #         newInitDic['content'] = item[1]
                #         jsonRecord = json.dumps(newInitDic,ensure_ascii=False)
                #         fw.write(jsonRecord + '\n')
                #         print(i,item[0])
                #         i += 1
                # # i += 1

                jsonRecord = json.dumps(initDic, ensure_ascii=False)
                fw.write(jsonRecord + '\n')
                print(i,jsonRecord)
                i += 1
        else:
            break
    fw.close()
    fr.close()





