# -*- coding: utf-8 -*-
# author :nicole
# 计费模块：测试基础计费项 单个账单的生成 是否正确

from common.readdata import read_json
from common.data_init import DataInit
from apihttp.fee.secenarioHttp import FeeApi
import time
import unittest
import ddt


"""记录计费模块所有可能使用的api，用于各个接口用例自定义运行"""
APIS={
        'newdata_insert':'oss/crm/oss/resource/test/insert',
        'olddata_insert':'oss/crm/oss/resource/test/insert/migrate',
        'agreement_create':'api/crm/oss/agreement/create',
        'agreement_query': 'api/crm/oss/agreement/query/page',
        'agreement_update': 'api/crm/oss/agreement/price/update',
        'agreement_status': 'api/crm/oss/agreement/update/status',
        'bill_query': 'api/crm/oss/bill/query/page',
        'bill_detail': 'api/crm/oss/bill/detail'
    }

@ddt.ddt
class FeeScenario(unittest.TestCase):

    jsondata = read_json("testdata/scenario_fee/basefeeitem.json")
    # 运行全部json用例====================================================================================
    # testdata_tuple = jsondata.items()

    # 运行指定case--主要用于调试和查看单个或某几个case=========================================================
    # jsondata = read_json("testdata/scenario_fee/olddata.json")
    # # testdata_tuple = jsondata.items()
    casename = 'case32-企业长期证书CORP_LONG_CERT-按个-cfca，2年期，数据为cfca-新数据'
    testdata_tuple = [(casename,jsondata[casename])]

    def setUp(self) -> None:
        '''清空已有数据'''
        DataInit().del_olddata()
        time.sleep(1)
        DataInit().del_newdata()
        time.sleep(1)

    @ddt.data(*testdata_tuple)
    def test_run(self, testdata):
        casename = testdata[0]
        casedata = testdata[1]
        print("===============开始运行，用例名称：", casename)
        for sub_api in casedata:
            if 'url' in sub_api:
                case_url = sub_api["url"]
                data = sub_api

                if case_url == APIS['newdata_insert']:
                    FeeApi().add_data(data)
                    time.sleep(1)
                elif case_url == APIS['olddata_insert']:
                    FeeApi().add_data(data)
                    time.sleep(1)
                elif case_url == APIS['agreement_create']:
                    FeeApi().createagree(data)
                    time.sleep(1)

                elif case_url == APIS['agreement_query']:  # 查询合同列表，返回字典
                    agreement_list = FeeApi().queryagree(data)
                elif case_url == APIS['agreement_update']:  # 根据合同列表返回，更新合同
                    time.sleep(1)
                    if data["data"]['agreementId'] == 'agreementId':
                        agreementId = list(agreement_list.keys())[0]
                        itemid_list = agreement_list[agreementId]
                    FeeApi().updateagree(data, agreementId=agreementId, itemid=itemid_list)

                elif case_url == APIS['agreement_status']:
                    time.sleep(1)
                    if data["data"]['agreementId'] == 'agreementId':
                        agreementId = list(agreement_list.keys())[0]
                    else:
                        agreementId = data["data"]['agreementId']
                    FeeApi().updatestatus(data, agreementid=agreementId)

                elif case_url == APIS['bill_query']:
                    time.sleep(2)
                    resBill = FeeApi().getbill(data)
                    resbillid = resBill.json()["result"]["result"][0]["id"]

                elif case_url == APIS['bill_detail']:
                    time.sleep(2)
                    if data["data"]["billId"] =="billId":
                        billid = resbillid
                    else:
                        billid = data["data"]["billId"]
                    output = FeeApi().billdetail(data, billid=billid)
                    # 账单实际返回结果
                    message = output.json()["result"]["detailList"][0]["itemList"][0]["moneyNumList"]
                    if "exp_result" in sub_api:
                        exp_message = sub_api["exp_result"]
                        self.assertEqual(exp_message,message)
                        print('预期',exp_message)
                        print('实际',message)
                else:
                    print('不存在此接口，请添加 或 检查数据！')


if __name__ == '__main__':
   unittest.main()


