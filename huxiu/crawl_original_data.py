#!/usr/bin python
# -*- coding:utf-8 -*-

from util import handle
import index
import socket
import os
from util import io,handle,crawl,constant
import requests
from bs4 import BeautifulSoup

socket.setdefaulttimeout(60)


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
    return '|'.join(urlList)


def getInfoFromHtml(url):
    '''
        爬虫主体程序
    '''
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    r = requests.get(url=url,headers=header)
    html = r.content.decode('utf-8')
    soup = BeautifulSoup(html)
    if soup.find('div',id='log-send-article'):
        oneSoup = soup.find('div',id='log-send-article')
        if oneSoup.find('div',id='related-article-wrap'):
            bodySoup = oneSoup.find('div',id='related-article-wrap')
            # 初始化数据存储数据
            # lineData = []   # 顺序：
            title = ''
            author = ''
            articleTime = ''
            contentUrlList = ''
            content = ''
            tags = ''
            originTags = ''
            # 标题
            if bodySoup.find('h1',class_='t-h1'):
                title = bodySoup.find('h1',class_='t-h1').string.replace(',','')
            # 作者
            if bodySoup.find('span',class_='author-name'):
                author = bodySoup.find('span', class_='author-name').find('a').string.replace(',','')
            # 时间
            if bodySoup.find('span',class_='article-time'):
                articleTime = bodySoup.find('span',class_='article-time').string.replace(',','')
            # url
            if bodySoup.find('div',id='article_content'):
                contentSoup = bodySoup.find('div', id='article_content')
                contentHtml = str(contentSoup)
                if contentHtml:
                    # 内容中的url链接
                    contentUrlList = getUrlListFromContentHtml(contentHtml)
                    # 内容
                    content = crawl.extractContentFromHtmlString(contentHtml).replace(',','')
                    # 提取的标签
                    if content:
                        tags = handle.extractTagsFromContent(content)
            return [title,articleTime,url,originTags,tags,author,contentUrlList,content]
    return -1







def getLatestIndexNum(indexNumFilePath):
    fr = open(indexNumFilePath,'r',encoding='utf-8')
    indexNum = fr.readline().strip()
    fr.close()
    return indexNum


def recordIndexNum2Txt(indexNum,filePath):
    fw = open(filePath,'w',encoding='utf-8')
    fw.write(str(indexNum))
    fw.close()



if __name__ == '__main__':
    # 设定初始序号
    indexNum = 6968

    # 获取当前时间
    currentTime = handle.getNowTimeAndDate()

    # 存储已经爬取的索引号
    indexNumFilePath = index.ROOT_PATH + '/data/xiu_data' + '/index_num_record.txt'
    # 存储结果
    originHtmlFilePath = index.ROOT_PATH + '/data/xiu_data' + '/result_set_xiu_' + currentTime + '.csv'
    fw = open(originHtmlFilePath,'a',encoding='utf-8')

    if os.path.exists(indexNumFilePath):
        # 获取文本中存储的最新索引号
        latestIndexNum = getLatestIndexNum(indexNumFilePath)
        if latestIndexNum:
            indexNum = int(latestIndexNum)

    flag = True
    resultDataList = []

    # 设置控制变量
    datasItemNum = 100
    cycleNum = 0
    flagNum = 0
    indexNumRecord = 0
    while flag:
        cycleNum += 1
        try:
            indexNum += 1
            # 构建原始网页
            url = 'https://www.huxiu.com/article/' + str(indexNum) + '.html'
            # 获取原始网页
            lineData = getInfoFromHtml(url)
            print(lineData)
            if lineData == -1:
                flagNum += 1
            else:
                indexNumRecord = indexNum
                outputLine = ','.join(lineData)
                fw.write(outputLine + '\n')
                # resultDataList.append(lineData)

            if flagNum == datasItemNum:
                flag = False
            if cycleNum == datasItemNum:
                cycleNum = 0
                flagNum = 0
        except Exception as ex:
            continue
    # 数据写入
    # io.writeContent2Excel(resultDataList,originHtmlFilePath)
    # 记录当前结束时的爬取记录号
    recordIndexNum2Txt(indexNum,indexNumFilePath)
    fw.close()




