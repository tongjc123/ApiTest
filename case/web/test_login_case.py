import requests
from case.mybase import MyBase
import json
from common.getparam import opexcel
from common.log import atp_log

class LoginCase(MyBase):
    u"""登录成功及失败场景用例"""
    #def setUp(self):
        #warnings.simplefilter("ignore",ResourceWarning) #忽略ResourceWarning
        #self.s = requests.session()

    def test_login_success(cls):

        test_login_success_data = opexcel.get_test_data(opexcel.get_param("LoginCase"),
                                                        "test_login_success")  # 类名与sheet页名一致,用例方法名与excel中case_name一致
        if not test_login_success_data:
            atp_log.warning("未获取到用例数据")
        url = test_login_success_data.get('url')
        headers = test_login_success_data.get('headers')
        data = test_login_success_data.get('data')
        expect_res = test_login_success_data.get('expect_res')
        res = cls.s.post(url = url,
                        headers = json.loads(headers),
                        json=json.loads(data),
                        verify = False)
        result = json.loads(res.text)["code"] #从请求返回中获取关键字
        #se1 = "SUCCESS"  #登录成功则返回SUCCESS
        cls.assertEqual(expect_res,result)

    def test_login_fail(cls):
        test_login_fail_data = opexcel.get_test_data(opexcel.get_param("LoginCase"),
                                                     "test_login_fail")  #
        if not test_login_fail_data:
            atp_log.warning("未获取到用例数据")
        url = test_login_fail_data.get('url')
        headers = test_login_fail_data.get('headers')
        data = test_login_fail_data.get('data')
        expect_res = test_login_fail_data.get('expect_res')
        res = cls.s.post(url =url,
                        headers = json.loads(headers),
                        json=json.loads(data),
                        verify = False)
        result = json.loads(res.text)["msg"]
        #se2 = "用户名或密码错误121" #账户或密码错误则返回错误data
        cls.assertEqual(expect_res,result)


if __name__ == '__main__':
    MyBase.main()