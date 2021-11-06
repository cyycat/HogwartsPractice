import yaml

def test_yaml():
    env = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid": "ww5941e32e55315151",
                "corpsecret": "ov0xs7zSCCUK9yWoPC1TK9"
            }
        }

    with open("get_token.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)




