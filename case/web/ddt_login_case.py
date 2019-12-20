import ddt,json
from case.mybase import MyBase
import unittest,requests
from common.getparam import opexcel
import warnings
from common.log import atp_log

#print(opexcel.get_param("LoginCase_DDT"))
#ddt_data = opexcel.get_param("LoginCase_DDT")

@ddt.ddt
class LoginDdtCase(MyBase):
    u"""ddt数据驱动模式"""
    ddt_data = opexcel.get_param("LoginCase_DDT") #获取LoginCase_DDT这个sheet页的数据
    def setUp(cls):
        cls.s = requests.session()
        warnings.simplefilter("ignore", ResourceWarning)
        atp_log.info("======ddt驱动模式======")
        atp_log.info("======setUp======")


    def login_msg(cls,url,headers,data):
        response = cls.s.post(url=url, headers=headers, json=data)
        return response

    @ddt.data(*ddt_data)
    def test_login_case(cls,data):
        u"""登录成功/失败场景"""
        res = cls.login_msg(data['url'], json.loads(data['headers']), json.loads(data['data'])) #转换为dict
        atp_log.info("接口调用......")
        result = json.loads(res.text)[data['msg']] #获取response的关键信息
        atp_log.info('断言：【%s】？=【%s】'%(result,data['expect_res']))
        cls.assertIn(data['expect_res'], result)  #断言

    def tearDown(cls):
        atp_log.info("======tearDown======")

if __name__ == '__main__':
    MyBase.main()