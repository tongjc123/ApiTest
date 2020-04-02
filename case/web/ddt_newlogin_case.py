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
    u"""慧养猪接口测试"""
    params = opexcel.convert_data("LoginCase")

    @ddt.data(*params)
    def test_run_case(cls,i):
        result_dict = opexcel.result_dict   #全局字典
        if i['run'].lower() == 'yes':
            atp_log.info("==========参数获取==========")
            print("==========参数获取==========")
            #准备请求参数
            url = i['url']
            method = i['method'].lower()
            data = i['data']
            expect = i['expect']
            row = int(i['id'].split('-')[1])  #当前用例在excel中的行数

            #获取参数依赖
            if i['depend_id'].startswith("smartpig"):
                depend_id_list = opexcel.relation_data(i['depend_id'])
                depend_data_list = opexcel.relation_data(i['depend_data'])
                atp_log.info("=========等待数据依赖处理==========")
                print("=========等待数据依赖处理==========")
                try:
                    for j in range(len(depend_id_list)):
                        depend_data = opexcel.get_response_data(result_dict[depend_id_list[j]],depend_data_list[j])   #获取到依赖接口返回的指定数据

                        if method == 'delete':
                            url = os.path.join(url, depend_data) #将url拼接
                        else:
                            data = json.loads(json.dumps(data).replace('$'+str(j+1),depend_data))  #以此替换json中的$1,$2.......

                    # depend_data = opexcel.get_response_data(result_dict[i['depend_id']],i['depend_data']) #获取依赖的返回数据
                    # if method == 'delete':
                    #     url = os.path.join(url, depend_data) #将url拼接
                    # else:
                    #     data = data.replace('$',depend_data)  #如果是json中的依赖参数，就替换
                except Exception as e:
                    atp_log.error("获取返回依赖数据失败--%s"%e)

            atp_log.info("【%s】--url:%s"%(method,url))
            print("【%s】--url:%s"%(method,url))
            atp_log.info("data == %s"%data)
            print("data == %s"%data)
            result = myRequest.run_main(method, url, data)
            atp_log.info("statusCode = 【%s】"%result.status_code)
            print("statusCode = 【%s】"%result.status_code)
            atp_log.info("result == %s"%result.text)
            print("result == %s"%result.text)
            result_dict[i['id']] = result.text #将返回结果添加到全局字典
            #print(result_dict)
            cls.assertIn(expect, result.text)
            try:
                if expect in result.text:
                    cls.writeResult.writeresult(row, "测试通过")
                else:
                    cls.writeResult.writeresult(row, "测试失败")
            except Exception as e:
                atp_log("测试结果写入失败-----【%s】"%e)


if __name__ == '__main__':

   MyBase.main()



