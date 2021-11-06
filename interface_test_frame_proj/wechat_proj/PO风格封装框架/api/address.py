import requests

from wechat_proj.PO风格封装框架.api.wework import WeWork
from .base_api import BaseApi


class Address(BaseApi):
    def __init__(self):
        secrete = "ov0xs7zSCCUK9yWoPC1TK9-mkNK2NMqhtz3sDsD55mY"
        self.token = WeWork().send(secrete)
        
    def create(self, userid, name, mobile):
        # 创建员工
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token":self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [2]
            }
        }
        return self.send(**data)

    # def get(self, userid, access_token):
    #     # 查询员工
    #     res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid={userid}")
    #     return res.json()

    def update(self, userid, name, mobile):
        # 更新成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile
            }
        }
        return self.send(**data)


    def delete(self, userid):
        # 删除员工
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid":userid
            },

        }
        return self.send(**data)








