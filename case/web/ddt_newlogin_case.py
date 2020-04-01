#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ddt_newlogin_case.py
# Author: TongJC
# Date  : 2020-03-31

import ddt,json,os
from case.mybase import MyBase
from common.getparam import opexcel
from common.requestMethod import myRequest
from common.log import atp_log

@ddt.ddt
class NewLoginCase(MyBase):
    params = opexcel.convert_data("LoginCase")

    @ddt.data(*params)
    def test_run_case(cls,i):

        result_dict = opexcel.result_dict   #全局字典
        if i['run'].lower() == 'yes':
            #准备请求参数
            url = i['url']
            method = i['method'].lower()
            data = i['data']
            expect = i['expect']
            row = int(i['id'].split('-')[1])  #当前用例在excel中的行数
            #获取参数依赖
            if i['depend_id'].startswith("smartpig"):
                try:
                    depend_data = opexcel.get_response_data(result_dict[i['depend_id']],i['depend_data']) #获取依赖的返回数据
                    if method == 'delete':
                        url = os.path.join(url, depend_data) #将url拼接
                    else:
                        data = data.replace('$',depend_data)  #如果是json中的依赖参数，就替换
                except Exception as e:
                    atp_log.error("获取返回依赖数据失败--%s"%e)

            result = myRequest.run_main(method, url, data)
            result_dict[i['id']] = result #将返回结果添加到全局字典
            print(result_dict)
            cls.assertIn(expect, result)
            try:
                if expect in result:
                    cls.writeResult.writeresult(row, "测试通过")
                else:
                    cls.writeResult.writeresult(row, "测试失败")
            except Exception as e:
                atp_log("测试结果写入失败！！")


    def tearDown(self):

        pass

if __name__ == '__main__':
   MyBase.main()



