import os
import unittest

from libs.ddt import data, ddt
#from libs import ddt
from common.config_handler import config
from common.excel_handler import ExcelHandler
from common.requests_handler import HttpRequest
from setting.constant import p_path

from common.request_mm import RequestModel
from func.choosestatus import ChooseStatus
from func.finddir import FindDir

# 报警管理-报警定义

@ddt
class Test_WriteInSql(unittest.TestCase):
    # 读取配置文件以及测试用例路径信息
    file_name = config.read('excel', 'cases_alarm_proccess')
    tmp = FindDir('alarm', 'proccess')
    tmppath = tmp.finddir()
    file_path = os.path.join(tmppath,file_name)

    # Excel 表格名称
    # sheet_name = config.read('excel', 'code_sheet')

    # url 地址
    url = config.read('http', 'base_url2')

    # Excel 操作
    xls = ExcelHandler(file_path, 'Alarm_WriteInSql')

    #读data表数据
    test_data = xls.read()

    test = ChooseStatus(config.read('accounts', 'user'))
    headers = test.sort_status()


    def setUp(self):
        # choosefunc = ChooseStatus("admin")
        #读header
        # self.headers = choosefunc.sortstatus()
        # self.headers = eval(self.headers)
        # self.headers['Authorization'] = choosefunc.sortstatus()
        pass
        


    @data(*test_data)
    def test_alarm(self, data_item):
        print(f'---------------')
        # print(f'{type(data_item)}')
        # print(f"{type(data_item['url'])}")

        # seesion = requests.Session()
        # res = seesion.post(url=self.url + data_item['url'], json=eval(data_item['params']),headers={'Content':'Application/json'})
        # json.loads(res.content.decode('utf8'))
        
        url = self.url + data_item['url']    #url拼接
        
        # print(url,eval(data_item['params']),self.headers)
        newrequest = RequestModel(data_item['method'], url,data=data_item['params'],headers=self.headers) #传参至方法
        # print(newrequest.headers)
        res = newrequest.sort_requests()

        rownum = int(data_item['case_id'])
        self.xls.write(rownum+1,9, res.status_code)

        if int(data_item['expected']) == res.status_code:
            self.xls.write(rownum+1, 10, 'pass')
        else:
            self.xls.write(rownum+1, 10, 'fail')

        print(f'---------------')
        print(res.content.decode())
        print(f'---------------')
        self.assertEqual(res.status_code, int(data_item['expected']))  
