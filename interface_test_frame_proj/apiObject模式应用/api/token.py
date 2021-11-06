import requests
# 在api  package中是代表所有的接口信息的具体的实现。使用一个公共方法代表一个接口


class Token:

    def get_token(self):
        corpid = "ww5941e32e55315151"
        corpsecret = "ov0xs7zSCCUK9yWoPC1TK9-mkNK2NMqhtz3sDsD55mY"
        params = {
                "corpid": corpid,
                "corpsecret": corpsecret
            }

        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params).json()