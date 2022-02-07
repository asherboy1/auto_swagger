import json
import requests
#分GET与POST请求

class RequestModel:
    def __init__(self,method,url,data,headers,file=None):
        self.url = url
        self.data = data
        self.method = method
        self.headers = headers
        self.file = file

    def sort_requests(self):
        res = None
        null = None #json中 null字段无法识别
        
        if self.data is not None:
            self.data = eval(self.data)

        if self.method.upper() == 'GET':
            res = requests.get(self.url,params=self.data,headers=self.headers)
        elif self.method.upper() == 'POST':
            res = requests.post(self.url,json=self.data,headers=self.headers,files=self.file)
        elif self.method.upper() == 'PUT':
            res = requests.put(self.url,json=self.data,headers=self.headers,files=self.file)
        else:
            print('method not exist!')
        return res