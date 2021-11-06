import requests


class BaseApi:

    def send(slef, **data):
        return requests.request(**data).json()
