import HTMLTestRunnerNew
import HTMLTestRunner
import os
import unittest
from datetime import datetime

from setting.constant import p_path

# from test_case.test_equip import TestLogin
from test_case.test_alarm import TestLogin1
# from test_case.test_auth import TestLogin2
# from test_case.test_addbpq import TestLogin3

import json
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite() #初始化suite
loader = unittest.TestLoader() #初始化loader

suite.addTest(loader.loadTestsFromTestCase(TestLogin))
suite.addTest(loader.loadTestsFromTestCase(TestLogin1))
suite.addTest(loader.loadTestsFromTestCase(TestLogin2))
suite.addTest(loader.loadTestsFromTestCase(TestLogin3))

print(suite.countTestCases())
# REPORT_PATH + 时间戳字符串 + 后缀名 .html
report_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
report_file = os.path.join(p_path.REPORT_PATH, report_name+'.html')

if __name__ == '__main__':
    with open(report_file,'wb') as file:
        runner = HTMLTestRunnerNew.HTMLTestRunner(file,verbosity=2,title='施工升降机接口测试',tester='tiger')
        runner.run(suite)

    # runner = BeautifulReport(suite)
    # runner.report(
    #     description='信息',
    #     filename='report'
    # )
