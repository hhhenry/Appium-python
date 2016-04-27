# -*- coding: utf-8 -*-
import HTMLTestRunner
import time
from log import Log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

log = Log()

class report():

    def testDate(self):
        timestr = time.strftime('%Y%m%d',time.localtime(time.time()))

        return timestr

    def fileName(self):
        filename = "/Users/haoran.li/test/autoTest/result" + self.testDate() + ".html"

        return filename

    def sgReport(self,suite):
        fp = open(self.fileName(), 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='三国测试结果',
                description='三国测试报告'
                )
        runner.run(suite)

        log.sgLog('开始测试三国')

        fp.close()
