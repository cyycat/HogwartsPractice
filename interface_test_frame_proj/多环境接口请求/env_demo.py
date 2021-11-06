import requests
import yaml

class Api:
    env = yaml.safe_load(open("./env.yaml"))

    # data是请求信息
    def send(self, data:dict):
        data["url"] = str(data["url"]).replace("testing-studio", self.env["testing-studio"][self.env["default"]])
        res = requests.request(method=data["method"], url=data["url"], headers=data["headers"],json=data["json"])
        return res