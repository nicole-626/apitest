from common.HTMLTestRunner import HTMLTestRunner
import unittest
import os
import time


class RunCase:
    def __init__(self):
        self.testcase_path = "./testcase"
        self.report_path = "./report"
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)

    def set_casesuite(self):
        sub_path=os.listdir(self.testcase_path)
        subcase_path=[]
        # 获取所有case的文件夹
        for i in sub_path:
            subcase_path.append(os.path.join(self.testcase_path ,i))
        # 循环获取每个case文件夹下的单独case加入suite中
        suite = unittest.TestSuite()
        for path in subcase_path:
            # discover = unittest.defaultTestLoader.discover(path,pattern="test*.py")
            discover = unittest.defaultTestLoader.discover(path, pattern="test_scenario_serialbill.py")
            suite.addTest(discover)
        return suite

    def run(self):
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        reportname="测试报告"+"-"+now+".html"
        reportfile_path = os.path.join(self.report_path,reportname)
        with open(reportfile_path,mode='wb') as f:
            runner = HTMLTestRunner(stream=f, title='测试报告', description='用例执行情况：')
            runner.run(self.set_casesuite())





RunCase().run()

# if __name__ == '__main__':
#     reportpath="./report"
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename = now + 'result.html'
#     report = os.path.join(reportpath,filename)
#     fp = open(report, 'wb')
#     runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
#     runner.run(set_casesuite())
#     fp.close()





