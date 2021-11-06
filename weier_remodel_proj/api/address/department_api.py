from weier_remodel_proj.api.base_api import BaseApi
from weier_remodel_proj.core.api_yaml_template_replace_variables import api_yaml_template_replace_variables
import os


path = os.path.abspath(os.path.dirname(__file__))

class DepartmentApi(BaseApi):
    def __init__(self, yam_path = path+"/department.yml"):
        # 根据title切割 —> dict
        self.yaml_data = self.get_yaml_data(yam_path)


    def get_department(self, id):
        variable = {
            "access_token": self.get_token(),
            "id": id
        }
        data = api_yaml_template_replace_variables(self.yaml_data["get_department"], **variable)
        return self.send_request(**data)


    def create_department(self, name, parentid, id):
        variable = {
            "access_token": self.get_token(),
            "name": name,
            "parentid": parentid,
            "id": id
        }
        data = api_yaml_template_replace_variables(self.yaml_data["create_department"], **variable)
        return self.send_request(**data)


    def delete_department(self, id):
        variable = {
            "access_token": self.get_token(),
            "id": id
        }
        data = api_yaml_template_replace_variables(self.yaml_data["delete_department"], **variable)
        return self.send_request(**data)

if __name__ == '__main__':
    x = DepartmentApi()
    # create = x.create_department("产品5", 2, "")
    # print(create)
    print(x.get_department(6))
    # print(x.delete_department(create['id']))
    # print(os.path.abspath(os.path.dirname(__file__)))

