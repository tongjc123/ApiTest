#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_newlogin_case.py
# Author: TongJC
# Date  : 2020-03-30
from common.requestMethod import RunMethod
from common.getparam import OpExcel
from case.mybase import MyBase
from common.writeResult import WriteResult
import requests,json

#停止维护
class newLoginCase(MyBase):

    def test_case(cls):
        cls.request = RunMethod()
        cls.myExcel = OpExcel()
        cls.writeResult = WriteResult()
        cls.s = requests.session()
        list_dict = cls.myExcel.get_param("LoginCase")
        cell = 1

        for i in list_dict:
            url = i['url']
            method = i['method'].lower()
            print(method)
            headers = json.loads(i['headers'])
            data = json.loads(i['data'])
            expect = i['expect']
            result = cls.request.run_main(method,url,data)
            print(result)
            cls.assertIn(expect,result)
            if expect in result:
                cls.writeResult.writeresult(cell,"通过")
            else:
                cls.writeResult.writeresult(cell, "失败")
            cell +=1
if __name__ == '__main__':
   # MyBase.main()
    run = newLoginCase()
    run.test_case()