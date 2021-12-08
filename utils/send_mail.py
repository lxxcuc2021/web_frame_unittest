#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import smtplib   # 连接邮箱
from email import encoders
from email.mime.text import MIMEText   # 处理邮件文本信息
from email.mime.multipart import MIMEMultipart  # 处理邮件附件信息
from email.header import Header  # 处理邮件标题
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import os.path
from web_frame_unittest.utils.log import Logger

logger = Logger(logger='sendEmail').getlog()

def sendmail(filename):
    # 第三方SMTP服务
    mail_server = 'smtp.163.com'
    mail_user = 'lxxcuc@163.com'
    mail_pwd = 'ELLFZDKRYRZLJDFY'

    from_address = 'lxxcuc@163.com'
    to_address = ['lxxcuc@163.com', 'lixinxin0806@163.com']

    # 创建一个带附件的实例
    email = MIMEMultipart()
    email['Subject'] = Header('TYNAM后台管理系统测试报告', 'utf-8')
    email['From'] = from_address
    email['To'] = ','.join(to_address)

    # 邮件正文内容
    content = MIMEText('请大家查收自动化测试报告', 'plain', 'utf-8')
    email.attach(content)

    # 添加非图片附件
    att1 = MIMEText(open(filename, encoding='utf-8').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=test.html'
    basename = os.path.basename(filename)
    att1.add_header('Content-Disposition', 'attachment', filename=basename)  # 设置附件头
    email.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(mail_server, port=465)
        smtp.login(mail_user, mail_pwd)
        smtp.sendmail(from_address, to_address, email.as_string())
        logger.info('邮件发送成功')
        smtp.quit()
    except smtplib.SMTPException:
        logger.error('error；无法发送邮件')

# if __name__ == '__main__':
#     sendmail('../report/20211202 1027.html')