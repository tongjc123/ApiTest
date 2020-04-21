import unittest
import warnings
import requests
from common.log import atp_log
from common.getparam import OpExcel
from common.requestMethod import RunMethod
from common.writeResult import WriteResult
import os,xlrd
from xlutils.copy import *
from common.setting import bases

class MyBase(unittest.TestCase):
    """继承Unittest,处理warning."""

    @classmethod
    def setUpClass(cls):
        atp_log.info('=====测试开始=====')
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略ResourceWarning
        #cls.s = requests.session()  #session关联，会话保持
        #cls.data_dic = opexcel.get_test_data(opexcel.get_param()) #从excel获取的参数，用例继承该父类，可直接使用参数

        cls.writeResult = WriteResult()
        cls.cell = 1

        # 初始化结果excel
        cls.file_path = os.path.join(bases.PARAM_PATH,bases.PARAM_NAME)
        cls.workbook = xlrd.open_workbook(cls.file_path)
        cls.new_workbook = copy(cls.workbook)  # 复制新的工作表
        #cls.new_worksheet = cls.new_workbook.get_sheet(0)
        cls.new_workbook.save(os.path.join(bases.REPORT_PATH,bases.RESULT_NAME)) #结果xls文件创建
    @classmethod
    def tearDownClass(cls):
        atp_log.info('=====测试结束=====')

