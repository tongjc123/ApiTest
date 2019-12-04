import ddt,json
from case.mybase import MyBase
import unittest,requests
from common.getparam import opexcel
import warnings

#print(opexcel.get_param("LoginCase_DDT"))
#ddt_data = opexcel.get_param("LoginCase_DDT")

@ddt.ddt
class LoginDdtCase(MyBase):
    u"""ddt数据驱动模式"""
    ddt_data = opexcel.get_param("LoginCase_DDT") #获取LoginCase_DDT这个sheet页的数据
    def setUp(cls):
        cls.s = requests.session()
        warnings.simplefilter("ignore", ResourceWarning)
        print("start!!")

    def login_msg(cls,url,headers,data):
        response = cls.s.post(url=url, headers=headers, json=data)
        return response

    @ddt.data(*ddt_data)
    def test_login_case(cls,data):  #使用可变参数
        u"""登录成功/失败场景"""
        res = cls.login_msg(data['url'], json.loads(data['headers']), json.loads(data['data'])) #转换为dict
        result = json.loads(res.text)[data['msg']] #获取response的关键信息
        print(result)
        print(data['expect_res'])
        cls.assertIn(data['expect_res'], result)  #断言

    def tearDown(cls):
        print("end!!")

if __name__ == '__main__':
    MyBase.main()