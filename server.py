# -*- coding: utf-8 -*-
import os
from log import Log
from time import sleep

log = Log()

class Server():
    def startServer(self):
        os.system("appium &")
        log.sgLog('开启Appium服务')
        sleep(15)

    def stopServer(self):
        os.system("pkill node")
        log.sgLog('关闭Appium服务')