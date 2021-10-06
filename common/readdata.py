import csv
from common.getpath import get_abspath
import json


def read_csv(datapath):
    path=get_abspath()+"/"+datapath
    with open(path,'r') as f:
        reader=csv.reader(f)
        keynames=next(reader)
        csv_reader=csv.DictReader(f,fieldnames=keynames)
        data=[]
        for row in csv_reader:
            d={}
            for k,v in row.items():
                if k == "headers" or k =="params":
                    d[k]=json.loads(v)
                else:
                    d[k]=v
            data.append(d)
        return data


def read_json(jsonpath):
    path = get_abspath() + "/" + jsonpath
    with open(path,mode='r',encoding='utf-8') as f:
        a=json.load(f)
    return a





# a=read_json("testdata/scenario_fee/basefeeitem_old.json")
# print(a["test01-签署计费项==================="][0]["初始化数据"])


# a=read_csv("testdata/创建合同.csv")
# print(a)