from apihttp.fee.agreementQueryHttp import AgreementQuery
from common.readdata import read_csv
import unittest
import ddt


csv_data = read_csv("testdata/分页查询合同.csv")


@ddt.ddt
class AgreementQuerytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @ddt.data(*csv_data)  # 传入的为列表内嵌字典
    def test_run(self,dict_csvdata):  # 解析成单个字典，即每条csv用例
        is_run=dict_csvdata.get("is_run")
        casename= dict_csvdata.get("casename")
        if is_run == 'n' or is_run =='N':  # 若用例中is_run字段指定为不执行(为空时则默认执行)，则跳过此条用例，不执行（可用于单条用例调试）
            self.skipTest('case is skipped!!')
        else:
            response=AgreementQuery(test_method='csv',csv_data=dict_csvdata).send()
            print(response.json())







if __name__ == '__main__':
    unittest.main()