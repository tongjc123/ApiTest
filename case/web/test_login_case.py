import requests
from case.mybase import MyBase
import json
import warnings




class LoginCase(MyBase):
    u"""测试集合：登录成功及失败场景用例"""
    #def setUp(self):
        #warnings.simplefilter("ignore",ResourceWarning) #忽略ResourceWarning
        #self.s = requests.session()

    def test_login_success(cls):
        r1 = cls.s.post(url = cls.data_dic[1],headers = cls.data_dic[2],json=cls.data_dic[3],verify = False)
        result1 = json.loads(r1.text)["code"]
        #se1 = "SUCCESS"  #登录成功则返回SUCCESS
        cls.assertEqual(cls.data_dic[4],result1)

    def test_login_fail(cls):
        r2 = cls.s.post(url = cls.data_dic[5],headers = cls.data_dic[6],json=cls.data_dic[7],verify = False)
        result2 = json.loads(r2.text)["msg"]
        #se2 = "用户名或密码错误121" #账户或密码错误则返回错误
        cls.assertEqual(cls.data_dic[8],result2)


if __name__ == '__main__':
    MyBase.main()