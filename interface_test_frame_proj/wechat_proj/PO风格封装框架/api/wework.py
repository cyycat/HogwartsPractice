from wechat_proj.PO风格封装框架.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self, secrete):
        corpid = "ww5941e32e55315151"
        corpsecret = secrete
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }

        return self.send(**data)["access_token"]
    

