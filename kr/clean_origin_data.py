#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import index
from collections import OrderedDict
from util import handle,crawl,io,constant
from bs4 import BeautifulSoup
"""
    36kr原始网页数据清理代码
"""

def getTimeStampFromTxt(originHtmlTxtName):
    '''
        正则提取字符串中的时间信息
    '''
    cake = originHtmlTxtName
    if isinstance(cake,str):
        if '.' in cake:
            part1 = cake.split('.')[0]
            if '_' in part1:
                if part1.count('_') == 3:
                    timeStamp = part1.split('_')[len(part1.split('_')) - 1]
                    return timeStamp


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


def getPostTime(timeStamp):
    if isinstance(timeStamp,str):
        return timeStamp.split(' ')[0]


def getUrlListFromContentHtml(contentHtml):
    '''

    '''
    urlList = []
    soup = BeautifulSoup(contentHtml)
    aTagList = soup.find_all('a')
    for item in aTagList:
        if item.string != None:
            url = item.get('href')
            urlList.append(url)
    return urlList


def getOriginTag(cake):
    '''
        从字符串中提取出原始标签，以字符串方式再返回
    '''
    resultList = []
    if isinstance(cake,str):
        breadList = json.loads(cake)
        if breadList:
            for item in breadList:
                resultList.append(item[0])
    return ' '.join(resultList)


if __name__ == '__main__':
    # 指定待处理文件的文件名
    originHtmlTxtName = 'origin_html_kr_201702171539.txt'


    # 获取文件名中的时间信息
    timeStamp = getTimeStampFromTxt(originHtmlTxtName)

    # 构建路径
    inputFilePath = index.ROOT_PATH + '/data/kr_data/' + originHtmlTxtName
    outputFilePath = index.ROOT_PATH + '/data/kr_data/resultSet/' + 'shaped_kr_' + timeStamp + '.txt'
    #
    fr = open(inputFilePath,'r',encoding='utf-8')
    fw = open(outputFilePath,'w',encoding='utf-8')
    i = 1
    while True:
        line = fr.readline().strip().replace('\ufeff','')
        if line:
            print(i)
            try:
                lineDic = json.loads(line)
                # 初始化记录字典
                initDic = getInitDic()
                # 这里将初始化部分提前
                initDic['title'] = lineDic['data']['title']
                initDic['url'] = lineDic['data']['currentUrl']
                if lineDic['data']['user']:
                    initDic['author'] = lineDic['data']['user']['name']
                else:
                    initDic['author'] = ''
                # 提取时间信息
                postTime = getPostTime(lineDic['data']['published_at'])
                initDic['time'] = postTime
                # 提取内容content中的url链接
                urlList = getUrlListFromContentHtml(lineDic['data']['content'])
                initDic['content_url'] = urlList
                # 提取内容
                content = crawl.extractContentFromHtmlString(lineDic['data']['content'])
                initDic['content'] = content
                # 提取原始标签
                originTags = getOriginTag(lineDic['data']['extraction_tags'])
                initDic['originTag'] = originTags
                # 提取标签
                tags = handle.extractTagsFromContent(content)
                initDic['tag'] = tags

                jsonRecord = json.dumps(initDic, ensure_ascii=False)
                fw.write(jsonRecord + '\n')
                # print(i,jsonRecord)
                # i += 1
            except Exception as ex:
                print('这条记录数据有问题...')
            i +=1
        else:
            break
    fw.close()
    fr.close()
