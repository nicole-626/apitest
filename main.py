import unittest
from apihttp import *
from common.data_init import DataInit
from common import read_config
import time


class Run(unittest.TestCase):
    def setUp(self) -> None:
        '''清空已有数据'''
        DataInit().del_olddata()
        time.sleep(1)
        DataInit().del_newdata()
        time.sleep(1)

    def test_scenario(self):
        pass








if __name__ == '__main__':
    Run()





