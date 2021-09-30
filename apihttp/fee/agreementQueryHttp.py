from common.readdata import read_csv
from core.core_http import CoreHttp


class AgreementQuery:
    def __init__(self,test_method,jsondata,csv_data=None):
        # 选择csv文件 则运行csv中单接口用例
        if test_method == "CSV":
            test_data = csv_data
            self.url = test_data["url"]
            self.headers = test_data["headers"]
            self.method = test_data["method"]
            self.data_type = test_data["data_type"]
            self.body = test_data["params"]
        # 选择json文件，则运行json中的场景用例
        elif test_method == "json":
            json_data = jsondata
            self.body = json_data["data"]
            self.url = json_data["url"]
            self.data_type = 'json'
            self.method = 'POST'
            self.headers = {"ContentType": "application/json"}

    def send(self):
        responce=CoreHttp(self.url,self.method,self.data_type,self.headers,post_params=self.body).send_request()
        return responce


if __name__ == '__main__':
    a=AgreementQuery()
    a.get_responce()
