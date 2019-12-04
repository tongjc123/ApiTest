import os.path
import time

class Setting():
    """存放所有基础信息，方便管理"""
    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.SMTP_DICT = {
        "smtp_server": "smtp.exmail.qq.com",  # 发送邮件服务器
        "send_user": "tongjc@newhope.cn",  # 发送邮件的邮箱账号
        #"send_pwd": "lqtfbacgzwwkhjbg",  # 发送邮件的账号密码
        "send_pwd" : "Tt1140720529",
        "sender": "tongjc@newhope.cn",  # 显示在邮件中的发件人
        "receiver": ["1162856094@qq.com"],  # 收件邮箱地址
        "subject": "smartpig自动化测试报告",  # 邮件主题
        "from": "smartpig自动化平台"  #邮件发送方
    }
        # 项目名称(自定义)
        self.PROJECT_NAME = 'Smartpig'
        # 存放用例的路径
        self.CASE_PATH = os.path.join(self.BASE_PATH,'case')
        # 存放报告的路径
        self.REPORT_PATH = os.path.join(self.BASE_PATH,'report')
        # 报告的文件名
        times = time.strftime("%Y%m%d%H%M%S")
        self.REPORT_NAME = self.PROJECT_NAME+times+'report.html'
        #邮件中正文内容
        self.CONTENT = 'Hi all,\n    本次测试结果已生成，请查阅附件(本邮件是自动化测试邮件，请勿回复！)。为了更好的报告展示，请您使用chrome打开报告。谢谢！'
        #邮件中展示自定义附件名
        self.File_NAME = 'smartpig_report.html'
        # 日志的文件名
        self.LOG_NAME='atp.log'
        # 存放日志的路径
        self.LOG_PATH = os.path.join(self.BASE_PATH, 'logs')
        # 默认日志级别
        self.LEVEL = 'info'
        # 用例参数文件路径
        self.PARAM_PATH = os.path.join(self.BASE_PATH,'params')
        # 用例参数文件名
        self.PARAM_NAME = 'interface.xlsx'

bases = Setting()   #实例化Setting
