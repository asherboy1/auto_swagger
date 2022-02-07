from os.path import abspath,dirname
from os import listdir
import sys

dirpath = dirname(dirname(abspath(__file__)))
sys.path.append(dirpath)
from setting.constant import p_path

Datapath = p_path.DATA_PATH

class FindDir:
    def __init__(self,name1,name2):     #name1 一个模块整体 name2 细分  如：name1 = 'alarm' name2 = 'define'
        # print(p_path.DATA_PATH)
        self.name1 = name1.lower()
        self.name2 = name2.lower()

    def finddir(self):
        tmpdir = self.listdirname(Datapath)
        for i in tmpdir:
            if i.endswith(self.name1):
                des = Datapath + '\\' + i
                break
        
        return des

    def listdirname(self,dest):
        tmp = listdir(dest)
        return tmp



if __name__ == '__main__':
    test = FindDir('alarm', 'define')
    # print(listdir(CasePath))
    print(test.finddir())