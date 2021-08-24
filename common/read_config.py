from configparser import ConfigParser
from common.getpath import get_abspath
import os

config_path=os.path.join(get_abspath(),"config/base_conf.ini")


def readconfig(section, option):
    '''获取指定section下的指定option值'''
    conf = ConfigParser()
    conf.read(config_path, encoding='utf-8')
    value=conf.get(section, option)
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
# a=readconfig_readvalues('FeeApi_URL')
