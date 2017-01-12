#!/usr/bin/env python
# -*- coding:utf-8 -*-

import index
import json
from util import crawl,handle,constant,io
import copy
import re


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
    initDic = {}
    initDic['url'] = '',
    initDic['content'] = '',
    initDic['ptime'] = '',
    initDic['gtime'] = '',
    initDic['date'] = '',
    initDic['cat'] = '',
    initDic['title'] = '',
    initDic['tag'] = []
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


if __name__ == '__main__':
    # 构建路径
    inputFilePath = index.rootPath + '/data/pingwest_data/' + 'origin_content_1213.txt'
    outputFilePath = index.rootPath + '/data/pingwest_data/resultSet/' + 'shaped_pingwest.txt'
    #
    fr = open(inputFilePath,'r')
    fw = open(outputFilePath,'w',encoding='utf-8')
    i = 1
    while True:
        line = fr.readline().strip()
        if line:
            # 初始化记录字典
            initDic = getInitDic()
            lineDic = json.loads(line)[0]
            # 这里将初始化部分提前
            initDic['url'] = lineDic['posturl']
            initDic['ptime'] = lineDic['ptime']
            initDic['gtime'] = lineDic['gtime']
            initDic['cat'] = lineDic['cat']
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
            if selectProcessArticle(lineDic['title']):
                # print(i,lineDic['title'])
                titleAndContentList = getTitleAndContentList(lineDic['contenthtml'])
                for item in titleAndContentList:

                    newInitDic = copy.deepcopy(initDic)
                    newInitDic['title'] = item[0]
                    newInitDic['content'] = item[1]
                    jsonRecord = json.dumps(newInitDic,ensure_ascii=False)
                    fw.write(jsonRecord + '\n')
                    print(i,item[0])
                    i += 1
            # i += 1
        else:
            break
    fw.close()
    fr.close()





