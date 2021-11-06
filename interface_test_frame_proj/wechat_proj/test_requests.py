


import requests


#
# def test_token():
#     corpid="ww5941e32e55315151"
#     corpsecret="ov0xs7zSCCUK9yWoPC1TK9-mkNK2NMqhtz3sDsD55mY"
#     url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
#     r = requests.get(url)
#     print(r.json())


access_token = "JDRHLUoPQIhQ0AZVS4_i4j3azLGPFECwsNXKj0jqWlYlrW7_2onykKrerzXFR6gGniyFhZxxYz1rTNTFF8GKEdKXvueO3chIojZR8tXRPv1BQShQ0yFduvBJBB3uzL88BsD2OEJqh8ft9DuJnjJSyryM-SDOu_RsR38tUDNcvf35koCNR9raqFqF4fivIWyGiDf_aoSVZcNpUUqra17gtA"

def test_get_number():
    userid="TEST_003"
    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid={userid}")
    print(r.json())


def test_create_number():
    data = {
        "userid": "TEST_003",
        "name": "员工3",
        "mobile": "+86 15000000003",
        "department":[2]
    }
    r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}",
                     json=data)
    print(r.json())