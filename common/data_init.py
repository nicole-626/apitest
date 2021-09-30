# coding="utf-8"


from common.read_config import readenv_config
import requests


class DataInit:
    '''数据初始化：删除所有旧数据插入新数据'''
    def __init__(self):
        self.host=readenv_config('datainit_host')
        self.headers={
                    "Content-Type":"application/json",
                    "x-qys-oss-token":readenv_config("token")}
        self.default_body = {
            "appId": readenv_config("appId"),
            "customerId": readenv_config("customerId")}

    def del_newdata(self,data=None):
        if data is None:
            body = self.default_body
        else:
            body = data
        url=self.host+"/oss/crm/oss/resource/test/delete"
        responce = requests.post(url,headers=self.headers, json=body)
        if responce.json()["message"] != 'SUCCESS':
            raise Exception("插入数据失败",responce.json())

    def del_olddata(self,data=None):
        if data is None:
            body = self.default_body
        else:
            body = data
        url = self.host + "/oss/crm/oss/resource/test/delete/migrate"
        responce = requests.post(url, headers=self.headers, json=body)
        if responce.json()["message"] != 'SUCCESS':
            raise Exception("插入数据失败",responce.json())

    def add_data(self, testdata):
        url = self.host + "/"+testdata["url"]
        body = testdata["data"]
        if "appId" in body and body["appId"] == "appId":
            body['appId'] = ("CUSTOMER", "appId")
            if "customerId" in body and body["customerId"] == "customerId":
                body['customerId'] = readenv_config("customerId")

        responce = requests.post(url, headers=self.headers, json=body)
        if responce.json()["message"] != 'SUCCESS':
            raise Exception("插入数据失败",responce.json())


if __name__ == '__main__':
    a=DataInit().del_newdata()
    print(a.json())






