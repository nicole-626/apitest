# -*- coding: utf-8 -*-
# author :nicole
# 计费模块 基础计费项 正向单个账单测试；不包含异常场景，例如不生成账单；不包含多账单测试，例如生成2个月的账单

from common.readdata import read_json
from common.data_init import DataInit
from apihttp.fee import agreementUpdateStatusHttp,agreementBillDetailHttp,agreementQueryHttp,agreementCreateHttp,agreementUpdateHttp,agreenmentGetBillHttp
import time
import unittest
import ddt

@ddt.ddt
class BaseFeeItem(unittest.TestCase):
    jsondata = read_json("testdata/scenario/basefeeitem_old.json")
    '''运行全部json用例'''
    # testdata_tuple = jsondata.items()

    '''运行指定case--主要用于调试和查看单个或某几个case'''
    casename = 'case03-短信MESSAGE-按次-套餐包不在时间范围内-新数据'
    testdata_tuple = [(casename,jsondata[casename])]

    def setUp(self) -> None:
        '''清空已有数据'''
        DataInit().del_olddata()
        time.sleep(1)
        DataInit().del_newdata()
        time.sleep(2)

    def adddata(self,data):
        DataInit().add_data(data[0]["data"])

    def createagree(self,data):
        agreementCreateHttp.AgreementCreate('json',data).send()

    def queryagree(self,data):
        resquery = agreementQueryHttp.AgreementQuery('json', data).send()
        agreementId = resquery.json()["result"]["result"][0]["id"]
        itemid = resquery.json()["result"]["result"][0]["priceList"][0]["id"]
        return agreementId, itemid

    def updateagree(self,data,agreementId,itemid):
        agreementUpdateHttp.AgreementUpdate('json',data,agreementId=agreementId, itemid=itemid).send()

    def updatestatus(self,data,agreementId,status):
        agreementUpdateStatusHttp.AgreementUpdateStatus('json', data, agreementId=agreementId, status=status).send()

    def getbill(self, data):
        resBill = agreenmentGetBillHttp.AgreementGetBill('json', data).send()
        billId = resBill.json()["result"]["result"][0]["id"]
        return billId

    def billdetail(self,data, billId):
        resMoney = agreementBillDetailHttp.AgreementBillDetail('json', data, billId=billId).send()
        return resMoney

    @ddt.data(*testdata_tuple)
    def test_run(self,testdata):
        case=testdata[0]
        data=testdata[1]
        print("===============开始运行，用例名称：", case)
        # 添加数据并创建合同
        self.adddata(data)
        self.createagree(data)
        # 查询合同id
        res = self.queryagree(data)
        time.sleep(2)
        # 更新并启用合同
        self.updateagree(data, agreementId=res[0], itemid=res[1])
        time.sleep(2)
        self.updatestatus(data, agreementId=res[0], status='enable')
        time.sleep(3)
        # 获取账单
        billid = self.getbill(data)
        time.sleep(1)
        output = self.billdetail(data, billId=billid)
        message = output.json()["result"]["detailList"][0]["itemList"][0]["moneyNumList"]
        # 禁用合同
        self.updatestatus(data, agreementId=res[0], status='disable')
        time.sleep(2)
        # 断言返回结果
        exp_message = data[8]['exp_result']
        self.assertEqual(message, exp_message)


if __name__ == '__main__':
   unittest.main()


