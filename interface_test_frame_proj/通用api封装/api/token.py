import requests
# 在api  package中是代表所有的接口信息的具体的实现。使用一个公共方法代表一个接口
from .base_api import BaseApi

class Token(BaseApi):

    def get_token(self):
        corpid = "ww5941e32e55315151"
        corpsecret = "ov0xs7zSCCUK9yWoPC1TK9-mkNK2NMqhtz3sDsD55mY"

        # 把请求信息转化为一个规范的字典结构体（就是对请求的一次描述）
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }

        return self.http_requests(data).json