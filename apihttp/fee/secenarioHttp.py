
from . import agreementBillDetailHttp
from . import agreementCreateHttp
from . import agreementQueryHttp
from . import agreementUpdateHttp
from . import agreementUpdateStatusHttp
from . import agreenmentGetBillHttp
from common.data_init import DataInit


class FeeApi:
    """
    封装场景测试各接口，以及接口间返回值的前后调用
    """
    def add_data(self,data):
        DataInit().add_data(data)

    def createagree(self,data):
        return agreementCreateHttp.AgreementCreate('json',data).send()

    def queryagree(self,data):
        # 返回合同id 和合同下计费项id，合同id和计费项id可能是多个，为list
        resquery = agreementQueryHttp.AgreementQuery('json', data).send()
        result = resquery.json()["result"]["result"]
        agreement_list = {}
        for l in result:
            priceList = l["priceList"]
            agreement_list[l['id']]=[]
            for i in priceList:
                agreement_list[l['id']].append(i['id'])
        return agreement_list

    def updateagree(self,data,agreementId,itemid):
        return agreementUpdateHttp.AgreementUpdate('json',data,agreementId=agreementId, itemid=itemid).send()

    def updatestatus(self,data, agreementid):
        return agreementUpdateStatusHttp.AgreementUpdateStatus('json', data, agreementId=agreementid).send()

    def getbill(self, data):
        resBill = agreenmentGetBillHttp.AgreementGetBill('json', data).send()
        return resBill

    def billdetail(self,data, billid):
        resMoney = agreementBillDetailHttp.AgreementBillDetail('json', data, billId=billid).send()
        return resMoney