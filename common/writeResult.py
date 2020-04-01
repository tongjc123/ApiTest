#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : writeResult.py
# Author: TongJC
# Date  : 2020-03-28
import xlrd,os
from xlutils.copy import *
from common.setting import bases

class WriteResult():


    def writeresult(self,row,value):
        print('===========测试结果写入interface.xls========')
        file_path = os.path.join(bases.PARAM_PATH,bases.RESULT_NAME)
        workbook = xlrd.open_workbook(file_path)
       # sheets = workbook.sheet_names()
       # sheet_data = workbook.sheet_by_name(sheets[0])
        new_workbook = copy(workbook)   #复制新的工作表
        new_worksheet = new_workbook.get_sheet(0)
        new_worksheet.write(row,11,value)   #重新写入
        new_workbook.save(file_path)


if __name__ == '__main__':

    WriteResult().writeresult(1,"helloworld111")

