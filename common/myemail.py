from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
from .log import atp_log
from .setting import bases  #引入Setting的实例化对象

class MailSend():
    def send_mail(self,smtp_dict, report):
        """
        用于将测试报告发送到邮箱
        :param
        smtp_dict = {
            "smtp_server": "发送邮件的smtp ex:smtp.126.com",
            "send_user": "发送邮件的邮箱 ex:am1122@126.com",
            "send_pwd": "发送邮件的邮箱密码 ex:mima",
            "sender": "发件人邮箱用于显示收到邮件中的发件人 ex:am1122@126.com",
            "receiver": "收件人邮箱 ",多个收件人可以写成list
            "subject": "邮件主题 ex:自动化测试报告"
            "from":"邮件发送方 ex:smartpig自动化平台"
        }
        """
        # 邮件正文内容
        content = bases.CONTENT  # 获取Setting对象属性（正文内容）
        textApart = MIMEText(content)

        # 组装邮件
        msg = MIMEMultipart()
        # 添加多个附件
        for i in range(len(report)):
            htmlApart = MIMEApplication(open(report[i], 'rb').read())  # 读取附件
            htmlApart.add_header('Content-Disposition', 'attachment', filename=report[i].split('\\')[-1])  # 邮件中展示的附件名称可以自定义
            msg.attach(htmlApart)  # 附件

        msg.attach(textApart)  # 邮件正文
        msg['Subject'] = smtp_dict["subject"]  # 设置邮件主题
        msg['From'] = formataddr([smtp_dict["from"], smtp_dict["send_user"]])  # 设置发件人昵称
        # 发送邮件
        try:
            smtp = smtplib.SMTP_SSL()  # QQ邮箱必须用SSL  其他可以不用
            smtp.connect(smtp_dict["smtp_server"], port=465)  # 其他邮箱端口为25
            smtp.login(smtp_dict["send_user"], smtp_dict["send_pwd"])
            smtp.sendmail(smtp_dict["sender"], smtp_dict["receiver"], msg.as_string())
            atp_log.info("报告邮件已发送")
            smtp.quit()  # 断开链接
        except smtplib.SMTPException as se:
            atp_log.error("邮件发送失败！！%s" % se)
            print("邮件发送失败报错信息为：%s" % se)

mail_send = MailSend()

