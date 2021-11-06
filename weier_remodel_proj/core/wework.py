import time
import requests
from functools import lru_cache

class WeWork:

    @lru_cache(1)
    def get_token(self, _):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww5941e32e55315151",
                "corpsecret": "ov0xs7zSCCUK9yWoPC1TK9-mkNK2NMqhtz3sDsD55mY"
            }
        }
        return requests.request(**data).json()["access_token"]

if __name__ == '__main__':
    print(WeWork().get_token(time.time()//(3*60)))

