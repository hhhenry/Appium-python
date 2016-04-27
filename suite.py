# -*- coding: utf-8 -*-
import unittest
from case import TestCase
from log import Log

log = Log()

class CreateSuite():

    def add_sg_case(self):
        log.sgLog('添加测试用例')

        suite = unittest.TestSuite()
        suite.addTest(TestCase("test_sg_register"))
        suite.addTest(TestCase("test_sg_logout"))
        suite.addTest(TestCase("test_sg_login"))
        suite.addTest(TestCase("test_sg_chat"))
        suite.addTest(TestCase("test_sg_mission"))
        suite.addTest(TestCase("test_sg_fight"))
        suite.addTest(TestCase("test_sg_battle"))
        suite.addTest(TestCase("test_sg_rob"))
        suite.addTest(TestCase("test_sg_army"))
        suite.addTest(TestCase("test_sg_mall"))
        suite.addTest(TestCase("test_sg_home"))
        suite.addTest(TestCase("test_sg_force"))
        suite.addTest(TestCase("test_sg_bg"))
        suite.addTest(TestCase("test_sg_teamFb"))
        suite.addTest(TestCase("test_sg_rank"))
        suite.addTest(TestCase("test_sg_entity"))
        suite.addTest(TestCase("test_sg_illustration"))
        suite.addTest(TestCase("test_sg_message"))
        suite.addTest(TestCase("test_sg_intensify"))
        suite.addTest(TestCase("test_sg_profile"))
        suite.addTest(TestCase("test_sg_announcement"))
        suite.addTest(TestCase("test_sg_activity"))
        suite.addTest(TestCase("test_sg_demon"))
        suite.addTest(TestCase("test_sg_unrebirth"))
        suite.addTest(TestCase("test_sg_friend"))

        return suite
