import json
import sys

from os.path import dirname,abspath
from os import listdir

rootpath = dirname(dirname(abspath(__file__)))
datapath = rootpath + '\\' + 'data'
# print(datapath)

# print(listdir(datapath))

tmp = listdir(datapath)
tmp2 = []
dict1 = {}

for i in tmp:
    if i.startswith('cases') and not i.endswith('xlsx'):
        des = datapath + '\\' + i
        tmp = listdir(des)
        dict1[i] = tmp

for q in dict1.keys():
    for k in dict1[q]:
        tmp2.append(k[6:-5])
    dict1[q] = tmp2
    tmp2 = []

for h in dict1.keys():
    for u in dict1[h]:
        print(f"{h + '_' + u} = cases_{u}.xlsx")




