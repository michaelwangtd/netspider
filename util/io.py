# -*- coding:utf-8 -*-
import os
from xlutils import copy
import xlrd
import xlwt

def getListFromTxt(filePath):
    if os.path.exists(filePath):
        resultList = []
        fr = open(filePath,'r',encoding='utf-8')
        while True:
            line = fr.readline().strip()
            if line:
                result = line.strip()
                resultList.append(result)
            else:
                break
        fr.close()
        return resultList


def getListFromExcel(prePath,fileName):
    tempList = []
    filePath = os.path.join(prePath,fileName)
    if os.path.exists(filePath):
        xls_r = xlrd.open_workbook(filePath)
        sheet_r = xls_r.sheet_by_index(0)
        rows = sheet_r.nrows
        for i in range(rows):
            oneRecord = sheet_r.row_values(i)
            tempList.append(oneRecord)
    return tempList



def appendContent2Excel(infoList,outputFilePath):
    """
        “追加”的方式写入数据
    """
    # 打开excel文件
    r_xls = xlrd.open_workbook(outputFilePath)
    # 找到excel文件的sheet表
    r_sheet = r_xls.sheet_by_index(0)
    # 获取sheet表的行数
    rows = r_sheet.nrows
    # 将excel文件复制一份
    w_xls = copy.copy(r_xls)
    # 获取复制后文件的sheet表
    sheet_write = w_xls.get_sheet(0)

    # 遍历infoList
    for i in range(len(infoList)):
        for j in range(len(infoList[i])):
            sheet_write.write(rows + i,j,infoList[i][j])
        print('第【' + str(i) + '】条数据已经写入...')
    # 保存文件
    w_xls.save(outputFilePath)



def writeContent2Excel(infoList,outputFilePath):
    """
        “覆盖”的方式写入数据
    """
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('Sheet1')
    for i in range(len(infoList)):
        for j in range(len(infoList[i])):
            sheet.write(i,j,infoList[i][j])
        print('写入第【',str(i),'】条数据...')
    xls.save(outputFilePath)
    print('数据写入完成...')



def writeOrAppendContent2Excel(infoList,outputFilePath):
    """
        判断文件是否存在
        文件存在就用追加的方式写入信息
        文件不存在就新写入信息
    """
    if os.path.exists(outputFilePath):
        # “追加”方式写入文件
        xls_r = xlrd.open_workbook(outputFilePath)
        sheet_r = xls_r.sheet_by_index(0)
        rows = sheet_r.nrows
        xls_w = copy.copy(xls_r)
        sheet_w = xls_w.get_sheet(0)
        for i in range(len(infoList)):
            for j in range(len(infoList[i])):
                sheet_w.write(rows + i,j,infoList[i][j])
                print('第【' + str(i) + '】条数据已经写入...')
    else:
        xls_w = xlwt.Workbook()
        sheet_w = xls_w.add_sheet('Sheet1')
        for i in range(len(infoList)):
            for j in range(len(infoList[i])):
                sheet_w.write(i, j, infoList[i][j])
            print('写入第【', str(i), '】条数据...')
    xls_w.save(outputFilePath)