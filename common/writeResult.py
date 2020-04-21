#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : writeResult.py
# Author: TongJC
# Date  : 2020-03-28
import xlrd,os
from openpyxl import *
from xlutils.copy import *
from common.setting import bases

class WriteResult():


    def writeresult(self,row,value):
        print('===========测试结果写入result表格========')
        self.file_path = os.path.join(bases.REPORT_PATH, bases.RESULT_NAME)
        self.workbook = xlrd.open_workbook(self.file_path)
        self.new_workbook = copy(self.workbook)  # 复制新的工作表
        self.new_worksheet = self.new_workbook.get_sheet(0)

        self.new_worksheet = self.new_worksheet.write(row,11,value)    #重新写入
        self.new_workbook.save(self.file_path)




if __name__ == '__main__':
    import time
    write = WriteResult()
    for i in range(1,5):
        time.sleep(2)
        write.writeresult(i,"helloworld"+str(i))




