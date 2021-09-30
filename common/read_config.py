from configparser import ConfigParser
from common.getpath import get_abspath
import os

config_path=os.path.join(get_abspath(),"config/env_conf.ini")


def readenv_config(option):
    '''获取对应环境下的option值'''
    conf = ConfigParser()
    conf.read(config_path, encoding='utf-8')
    version=conf.get("VERSION","Version")
    value=conf.get(version, option)
    return value


# def readconfig_readvalues(section):
#     '''根据section，读取该section下所有value,并返回列表'''
#     conf = ConfigParser()
#     conf.read(config_path, encoding='utf-8')
#     res=conf.items(section)
#     values = []
#     for item in res:
#         values.append(item[1])
#     return values

#
# a=readenv_config('datainit_host')
# print(a)
