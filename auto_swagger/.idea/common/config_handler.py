
import os
from configparser import ConfigParser, NoSectionError, NoOptionError

from os.path import abspath,dirname
##rom setting.constant import p_path


class ConfigHandler:

    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        config = ConfigParser()
        config.read(filename, encoding=encoding)
        self.config = config

    def read(self, section, option):
        """读取配置文件某一项"""
        try:
            return self.config.get(section, option)
        except NoSectionError:
            print('没有这个 section')
        except NoOptionError:
            print("没有这个 option")

    def read_2(self, section, option):
        try:
            return self.config[section][option]
        except NoSectionError:
            print('没有这个 section')
        except NoOptionError:
            print("没有这个 option")

    def write(self, section, option, value, mode='w'):
        """写操作"""
        if self.config.has_section(section):
            self.config.set(section, option, value)
            with open(self.filename, mode=mode, encoding=self.encoding) as f:
                self.config.write(f)
                # f.write(config)

    def get_list(self, section, option):
        option_str =  self.read(section, option)
        # list 转化
        if isinstance(eval(option_str), list):
            return eval(option_str)
        return None

    def get_dict(self):
        pass


filenameini = dirname(dirname(abspath(__file__)))
filenameini = filenameini + '\setting\config.ini'
# print(filenameini)

# config = ConfigHandler(os.path.join(p_path.CONFIG_PATH, 'config.ini'))
# print(config.read(section,option))

config = ConfigHandler(filenameini)
print(type(config.read('db','host')))

# print(config.get_list('db','host'))
