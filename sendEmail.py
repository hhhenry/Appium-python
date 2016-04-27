# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from report import report
from log import Log

log = Log()

class sendEmail():

    def sgEmail(self):
        log.sgLog('发送测试结果\n')
        testDate = report().testDate()
        filename = report().fileName()

        msg = MIMEMultipart()
        html = open(filename,'rb').read()
        part1 = MIMEText(html,'html','utf-8')
        msg.attach(part1)

        msg['to'] = 'email address'
        msg['from'] = 'email address'
        msg['subject'] = '前台自动化测试报告' + testDate

        try:
            server = smtplib.SMTP()
            server.connect('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('username','password')
            server.sendmail(msg['from'], msg['to'],msg.as_string())
            server.quit()
            print '发送成功'
        except Exception, e:
            print str(e)
