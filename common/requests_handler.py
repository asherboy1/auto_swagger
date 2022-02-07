import requests
import json
class HttpRequest:
    def __init__(self,url,param):
        self.url = url
        self.param = param

    def http_request(self,method,cookies=None):
        if method.upper() == "GET":
            try:
                res = requests.get(self.url,self.param,cookies=cookies)
            except Exception as e:
                print("执行get请求报错了，错误是:{0}".format(e))
                res = 'Error:get请求报错{0}'.format(e)
        elif method.upper() == "POST":
            try:
                res = requests.post(self.url, self.param,cookies=cookies)
            except Exception as e:
                print("执行post请求报错了，错误是:{0}".format(e))
                res = 'Error:post请求报错{0}'.format(e)
        else:
            print("你的请求方式不对！")
            res = 'Error:请求方式不对报错{0}'.format(method)
        return res

if __name__ == "__main__":
    url1 = 'http://10.88.11.45:8080/mainpages/index.html#/login'  #类似于功能测试 而非只调用其接口进行测试
    param1 = {'account' : 'admin','password' : 'ky123456'}
    headers = {'Conten-Type':'application/json'}
    res = requests.post(url1,json=param1,headers=headers)
    print(res)

    test = HttpRequest(url1, param1)
    print(test.http_request('post'))