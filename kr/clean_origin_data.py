#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import index
from collections import OrderedDict
from util import handle,crawl,io,constant
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
            lineDic = json.loads(line)
            # 初始化记录字典
            initDic = getInitDic()
            # 这里将初始化部分提前
            initDic['title'] = lineDic['title']
            initDic['url'] = lineDic['posturl']
            initDic['author'] = lineDic['name']
            # 提取时间信息
            postTime = getTimeFromJson(lineDic['gtime'],timeStamp)
            initDic['time'] = postTime
            # 提取内容content中的url链接
            urlList = getUrlListFromContentHtml(lineDic['contenthtml'])
            initDic['content_url'] = urlList
            # 提取内容
            content = crawl.extractContentFromHtmlString(lineDic['contenthtml'])
            initDic['content'] = content
            # 提取标签
            # --这里还有标签的提取步骤--

            jsonRecord = json.dumps(initDic, ensure_ascii=False)
            fw.write(jsonRecord + '\n')
            print(i,jsonRecord)
            i += 1
        else:
            break
    fw.close()
    fr.close()
