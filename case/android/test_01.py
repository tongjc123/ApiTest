import unittest,time

class Login_case(unittest.TestCase):
    u"""测试用例集合：描述XX"""
    @classmethod
    def setUpClass(cls):
        time.sleep(1)
        print("在每次setUp之前执行")
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_login(self):
        print("正在运行用例")

if __name__ == '__main__':
    unittest.main()
