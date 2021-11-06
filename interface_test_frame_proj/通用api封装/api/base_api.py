import requests

class BaseApi:

    def http_requests(self, req):
        return requests.request(**req)