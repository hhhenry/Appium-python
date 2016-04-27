# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from report import report
from log import Log

log = Log()

class sendEmail():

    def sgEmail(self):
        log.sgLog('发送三国测试结果\n')
        testDate = report().testDate()
        filename = report().fileName()

        msg = MIMEMultipart()
        html = open(filename,'rb').read()
        part1 = MIMEText(html,'html','utf-8')
        msg.attach(part1)

        msg['to'] = 'haoran.li@redatoms.com'
        msg['from'] = 'haoran.li@redatoms.com'
        msg['subject'] = '三国前台自动化测试报告' + testDate

        try:
            server = smtplib.SMTP()
            server.connect('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('haoran.li@redatoms.com','Confuse0210')
            server.sendmail(msg['from'], msg['to'],msg.as_string())
            server.quit()
            print '发送成功'
        except Exception, e:
            print str(e)