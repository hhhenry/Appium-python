# -*- coding: utf-8 -*-
import unittest
from suite import CreateSuite
from server import Server
from report import report
from sendEmail import sendEmail

if __name__ == '__main__':

    server = Server()
    server.startServer()

    suite = unittest.TestSuite()
    suite.addTest(CreateSuite().add_sg_case())

    report().sgReport(suite)

    server.stopServer()

    sendEmail().sgEmail()