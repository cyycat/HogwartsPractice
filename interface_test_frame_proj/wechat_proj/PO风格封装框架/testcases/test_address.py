from wechat_proj.PO风格封装框架.api.address import Address

class TestAddress:
    def setup(self):
        self.address = Address()

    def test_token(self):
        print(self.address.get_token())

    def test_create(self):
        print(self.address.create("zhangsan", "张三", "15000000005"))

    def test_update(self):
        print(self.address.update("zhangsan", "张三update1", "15000000033"))

    def test_delete(self):
        print(self.address.delete("zhangsan"))