import requests
# 在api  package中是代表所有的接口信息的具体的实现。使用一个公共方法代表一个接口
from .base_api import BaseApi
import yaml
from string import Template

class Token(BaseApi):
    _corpid= "ww5941e32e55315151"
    _corpsecret = "ov0xs7zSCCUK9yWoPC1TK9-mkNK2NMqhtz3sDsD55mY"

    def template(self):
        with open("/Users/caiyingying/PycharmProjects/UnitTestPractice/接口测试框架/测试步骤的数据驱动/api/token.yaml") as f:
            re = Template(f.read()).substitute(corpid=self._corpid, corpsecret=self._corpsecret)
            return yaml.safe_load(re)

    def get_token(self):
        req = self.template()
        return self.http_requests(req).json()