import tornado.web
import tornado
import pytest


class MainHandler(tornado.web.RequestHandler):

    def _initialize(self):
        pass

    def get(self):
        pytest.main(['-v', '-s', '--alluredir=./result'])
        response = {'success': True, 'message': '构建成功'}
        self.write(response)

def make_app():
    return tornado.web.Application([(r"/api/task/start", MainHandler), ], debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
