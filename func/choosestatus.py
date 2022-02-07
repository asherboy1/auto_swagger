#选择admin用户 或者 OEM用户  返回其headers

import requests,json

class ChooseStatus:
    def __init__(self,status):
        self.status = status
        self.url = 'http://10.88.11.62:8888/empoworx-admin/api/sys/login'
        self.headers = {"Content-Type" : "application/json"}
        self.res = None

    def sort_status(self):
        if self.status.upper() == 'ADMIN':

            data = {
                "account" : "admin",
                "password" : "ky123456",
                "captcha" : ""
            }

            self.res = requests.post(self.url,json=data,headers=self.headers)
            token = self.choosetoken(self.res)

            self.headers['Authorization'] = token
            return self.headers

        elif self.status.upper() == 'OEM':

            data = {
                "account" : "sdjh",
                "password" : "admin",
                "captcha" : ""
            }

            self.res = requests.post(self.url,json=data,headers=self.headers)
            token = self.choosetoken(self.res)

            self.headers['Authorization'] = token
            return self.headers
            
        else:
            print('status not exist!')
        
    def choosetoken(self,res):
        data = json.loads(self.res.content.decode('utf8'))
        token = data['data']['tokenHead'] + data['data']['token']
        return token 

if __name__ == '__main__':
    test = ChooseStatus('oem')
    mm = test.sortstatus()
    print(mm)
