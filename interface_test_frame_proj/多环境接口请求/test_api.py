from .env_demo import Api



class TestApi:
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo1.txt",
        "headers": None,
        "json": {}
    }

    def test_send(self):
        api = Api().send(self.data)
        print(api.content)

