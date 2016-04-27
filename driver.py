import os
from appium import webdriver

class Driver():

    def sgDriver(self):
        app = os.path.join(os.path.dirname(__file__),'/Users/henry/test/sgll/','ST92.app')
        app = os.path.abspath(app)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.2'
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['app'] = app
#        desired_caps['appPackage'] = 'com.android.dialer'
#        desired_caps['appActivity'] = '.DialtactsActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        return driver
