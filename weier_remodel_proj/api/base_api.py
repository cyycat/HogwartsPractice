import requests
import time
from weier_remodel_proj.core.wework import WeWork
from weier_remodel_proj.core.api_yaml_split_by_title import api_yaml_split_by_title
import logging
logging.basicConfig(level=logging.INFO)

class BaseApi:

    def get_token(self):
        return WeWork().get_token(time.time() // (3 * 60))

    def send_request(self, **data):
        res = requests.request(**data).json()
        logging.info(f"requests data = {data}")
        logging.info(f"response = {res}")
        return res

    def get_yaml_data(self, yam_path):
        return api_yaml_split_by_title(yam_path)

