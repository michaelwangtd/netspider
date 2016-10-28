# -*- coding:utf-8 -*-

import os
from util import handle


if __name__ == "__main__":
    '''
        这里的作用主要是合并excel文件
        需要指定：
            1 待合并文件名称列表
            2 新生成excel文件全路径
    '''
    """
        acquisitionEvent 20161017
        investEvent 20161024
        productCompany 20161025
        vcCompany 20161025
    """

    # excelFileNameList = ['invest_event_info_1.xls','invest_event_info_2.xls','invest_event_info_3.xls','invest_event_info_4.xls','invest_event_info_log.xls']
    # excelFileNameList = ['product_company_info_1.xls','product_company_info_2.xls','product_company_info_3.xls','product_company_info_4.xls']
    excelFileNameList = ['vc_company_info_1.xls','vc_company_info_2.xls']

    # outputFileName = 'invest_event_20161024.xls'
    # outputFileName = 'product_company_20161025.xls'
    outputFileName = 'vc_company_20161025.xls'

    # 这里开始重写
    newOutputFilePath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'data','newseed_data','resultSet',outputFileName)

    handle.mergeExcelFromFixedDirNewseed(excelFileNameList,newOutputFilePath)

