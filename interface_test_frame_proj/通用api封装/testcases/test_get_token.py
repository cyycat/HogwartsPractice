# testcases是以pytest为测试框架，一个method 就是一个case
from interface_test_frame_proj.apiObject模式应用.api.token import Token


class TestToken:

    def setup(self):
        self.gettoken = Token()

    def test_get_token(self):
        assert self.gettoken.get_token()["errcode"] == 0