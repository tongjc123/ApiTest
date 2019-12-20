import os
import unittest
from common import HTMLTestRunner_cn
from common.setting import bases  #引入Setting的实例化对象
from common.myemail import mail_send  #引入MailSend的实例化对象
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(curPath)


def add_case(rule = "*case.py"):
    """第一步，获取setting的CASE_PATH,组装case,返回case列表"""
    discover = unittest.defaultTestLoader.discover(bases.CASE_PATH,pattern=rule)
    #print(discover)
    return discover


def run_case():
    """第二步，运行所有case,生成测试报告，返回报告的绝对路径"""
    reportFilePath = os.path.join(bases.REPORT_PATH,bases.REPORT_NAME) #组装完整的报告绝对路径
    with open(reportFilePath,"wb") as file:

        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file,
                                                  verbosity=2,
                                                  title="自动化测试报告",
                                                  description="这是测试报告描述内容",
                                                  retry=2,
                                                  save_last_try=False
                                                  )
        runner.run(add_case())
    return reportFilePath

if __name__ == '__main__':

    #smtp_dict = bases.SMTP_DICT #获取参数
    #mail_send.send_mail(smtp_dict, run_case())  #直接调用邮件发送即可运行所有用例
    run_case()






