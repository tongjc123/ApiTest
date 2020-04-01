import os
import unittest
from common import HTMLTestRunner_cn
from common.setting import bases  #引入Setting的实例化对象
from common.myemail import mail_send  #引入MailSend的实例化对象
import sys
import os
from common.log import atp_log


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(curPath)


def add_case(rule = "ddt_newlogin_case.py"):
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
                                                  title="API自动化测试报告",
                                                  description="本次测试是针对慧养猪API接口串联测试，结果如下：",
                                                  retry=2,
                                                  save_last_try=False
                                                  )
        runner.run(add_case())
    return reportFilePath

if __name__ == '__main__':

    smtp_dict = bases.SMTP_DICT #获取参数
    result = os.path.join(bases.PARAM_PATH,bases.RESULT_NAME) #测试结果
    atp_log.info("获取邮件参数,准备将测试结果写入邮件...")
    mail_send.send_mail(smtp_dict, [run_case(),result])  #直接调用邮件发送即可运行所有用例
    #run_case()






