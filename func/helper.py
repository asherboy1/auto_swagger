
import random
import re

# from common.config_handler import config
# from middler_ware.db_handler import MyDBHandler


def mk_phone():
    """随机生成手机号码.
    1[35789]()
    """
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        # 取 9 次
        num = str(random.randint(0, 9))
        phone += num
    return phone


#
# def md5_phone(phone):
#     return md5(phone)


# def login():
#     """登录，获取 token, member_id"""
#     req = RequestsHandler()
#     # 登录， 测试账号来登录
#     res = req.json('post',
#                    # 也可以读取Excel测试数据
#                    config.read('http', 'base_url') + config.read('http', 'login_url'),
#                    json={"mobile_phone": config.read('accounts', 'mobile_phone'), "pwd": config.read('accounts', 'password')},
#                    headers=eval(config.read('http', 'headers')))
#     data = {"token":res['data']['token_info']['token'], "member_id": res['data']['id']}
#     return data

def random_ip():
    ip = '{}.{}.{}.{}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
                              random.randint(0, 255))
    return ip


def random_phone():
    """随机生成手机号"""
    while True:
        item = ''
        for i in range(5):
            i = random.randint(0, 9)
            item += str(i)
        mobile = '137' + item + '716'
        # a = random.randint()
        # b = random.randint()
        # c = random.randint()

        # 查询数据库该号码是否存在
        # count = MyDBHandler().query(
        #     'SELECT * FROM sms_db_{}.t_mvcode_info_7 WHERE Fmobile_no={};'.format(mobile))
        # if not count:
        #     break
    return mobile


class Context:
    """保存临时替换的数据"""
    # phone = '777'  #仅能写入str类型
    # pwd = 10086
    phone =None
    pwd = None

    # pass

    # @property
    # def ip(self):
    #     return random_ip()
    #
    #
    # @property
    def mobile(self):
        self.phone = mk_phone()


def replace_label(target):  # 字符串:replace.
    """用 data 替换 target 里的标签。
    {"mobile_phone":"#phone#", "pwd": "#pwd#"} ==> {"mobile_phone":"137"}
    """
    pattern = r"#(.*?)#"
    ctx = Context()

    ctx.mobile()
    # 判断是否有符合条件的字符串
    while re.search(pattern, target):
        # 匹配  phone , pwd
        key = re.search(pattern, target).group(1)
        # print(key)
        value = getattr(ctx, key, '')
        # "phone"
        # Context.phone def make_str
        # eval("Context." + make_str(param), )
        target = re.sub(pattern, value, target, 1)
    return target


if __name__ == '__main__':
    # print(login())
    # setattr(object, name, value)
    dict1 = {"mobile_phone":"#phone#", "pwd": "#pwd#"}
    dict1['mobile_phone'] = replace_label(dict1["mobile_phone"])
    print(dict1)