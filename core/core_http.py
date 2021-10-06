import requests
from common.read_config import readenv_config


class CoreHttp:
    """
    调用方式：
    外部调用send_request方法
    默认host为 https://crm.qiyuesuo.me
    """
    def __init__(self,url,method,data_type='json', headers=None,get_params=None,post_params=None):
        __default_host=readenv_config("host")
        self.cookie = {}
        self.url=__default_host+"/"+url
        self.headers=headers
        self.method=method
        self.data_type=data_type
        self.get_params=get_params
        self.post_params=post_params
        self.timeout = 10  # 接口默认超时时间为10s
        # 传入的appid或customerid不为具体的值，转化为默认值
        if "appId" in self.post_params and self.post_params["appId"] == "appId":
            self.post_params['appId'] = readenv_config("appId")
            if "customerId" in self.post_params and self.post_params["customerId"] == "customerId":
                self.post_params['customerId'] = readenv_config("customerId")

    def __set_headers(self):
        token=readenv_config("token")
        __default_headers = {"x-qys-oss-token": token}
        if self.headers is not None:
            self.headers.update(__default_headers)
            return self.headers
        else:
            return __default_headers

    def send_request(self):
        try:
            if self.method == "POST":
                if self.data_type == "json":
                    ret= requests.post(url=self.url, headers=self.__set_headers(), json=self.post_params,
                                         timeout=self.timeout)
                    if ret.status_code != 200:
                        raise Exception("请求失败:",ret.text)
                    return ret
                else:
                    ret = requests.post(url=self.url, headers=self.__set_headers(), data=self.post_params,
                                         timeout=self.timeout)
                    if ret.status_code != 200:
                        raise Exception("请求失败:",ret.text)
                    return ret
            elif self.method == "GET":
                ret = requests.get(url=self.url, headers=self.__set_headers(), params=self.get_params,
                                    timeout=self.timeout)
                if ret.status_code != 200:
                    raise Exception("请求失败:",ret.text)
                return ret
            else:
                print("invalid method")
        except Exception as e:
            print(e)





# if __name__ == '__main__':
#     body={
#         "appId":"2852377753013452992",
#         "customerId": "2852377752958927039",
#         "orderColumn":"month",
#         "orderStrategy":"desc",
#         "pageNo":1,
#         "pageSize":10}
#
#     he={"Content-Type":"application/json"}
#     url="/api/crm/oss/bill/query/page"
#     a=CoreHttp(url,"POST",post_params=body,headers=he,data_type="json")
#     b=a.send_request()
#     print(b.text)



