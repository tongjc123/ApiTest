import unittest
import warnings
import requests
from common.log import atp_log
from common.getparam import opexcel
class MyBase(unittest.TestCase):
    """继承Unittest,处理warning."""
    @classmethod
    def setUpClass(cls):
        atp_log.info('=====测试开始=====')
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略ResourceWarning
        cls.s = requests.session()  #session关联，会话保持
        #cls.data_dic = opexcel.get_test_data(opexcel.get_param()) #从excel获取的参数，用例继承该父类，可直接使用参数

    @classmethod
    def tearDownClass(cls):
        atp_log.info('=====测试结束=====')

