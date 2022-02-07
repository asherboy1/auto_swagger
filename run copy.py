import HTMLTestRunnerNew
import HTMLTestRunner
import os
import unittest
from datetime import datetime

from setting.constant import p_path

# from test_case.test_equip import TestLogin
# from Case.testcase_alarm.test_Alarm_Management import Test_Alarm_Management
# from Case.testcase_alarm.test_Check_Realtag import Test_Check_Realtag
# from Case.testcase_alarm.test_Alarm_RealtimeCheck import Test_RealtimeCheck
# from Case.testcase_auth.test_Authorization_Update import Test_Authorization_Update
# from Case.testcase_equip.test_Addbpq import Test_New_bpq


# from test_case.test_auth import TestLogin2
# from test_case.test_addbpq import TestLogin3


# from Case.testcase_alarm.AlarmDefine.test_FindAlarmType import Test_FindAlarmType
# from Case.testcase_alarm.AlarmHistoryCheck.test_FindPageByName import Test_FindPageByName
# from Case.testcase_alarm.AlarmProccess.test_Update import Test_Update
# from Case.testcase_alarm.AlarmProccess.test_ImportAlarmDeal import Test_ImportAlarmDeal
# from Case.testcase_alarm.AlarmRealTimeCheck.test_RealTimeCheck import Test_RealTimeCheck

from Case.testcase_auth.AuthCheck.test_AuthLog import Test_AuthLog

import json
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite() #初始化suite
loader = unittest.TestLoader() #初始化loader

# suite.addTest(loader.loadTestsFromTestCase(Test_Alarm_Management))
# suite.addTest(loader.loadTestsFromTestCase(Test_Check_Realtag))
# suite.addTest(loader.loadTestsFromTestCase(Test_RealtimeCheck))

# suite.addTest(loader.loadTestsFromTestCase(Test_New_bpq))
# suite.addTest(loader.loadTestsFromTestCase(Test_Alarm_Management))
# suite = loader.discover(p_path.CASE_PATH)
# suite1 = loader.discover(tmptest[1])

# suite = loader.discover("E:\\python\\swagger-auto\\Case\\testcase_alarm\\AlarmDefine")

# suite.addTest(loader.loadTestsFromTestCase(Test_FindPageByName))
# suite = loader.discover('E:\\python\\swagger-auto\Case\\testcase_alarm\\AlarmInfo')

suite.addTest(loader.loadTestsFromTestCase(Test_AuthLog))

# suite = loader.discover('E:\\python\\swagger-auto\\Case\\testcase_alarm')



print(f"######共执行了{suite.countTestCases()}条测试用例######")
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
