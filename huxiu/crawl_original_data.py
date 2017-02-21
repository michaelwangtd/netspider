#!/usr/bin python
# -*- coding:utf-8 -*-

from util import handle
import index

if __name__ == '__main__':
    # 设定初始序号
    indexNum = 19

    # 获取当前时间
    currentTime = handle.getNowTimeAndDate()

    # 存储已经爬取的索引号
    indexNumFilePath = index.ROOT_PATH + '/data/xiu_data' + '/index_num_record.txt'
    # 存储结果
    originHtmlFilePath = index.ROOT_PATH + '/data/xiu_data' + '/result_set_xiu_' + currentTime + '.csv'

    flag = True
    resultDataList = []

    # 设置控制变量
    datasItemNum = 10
    cycleNum = 0

