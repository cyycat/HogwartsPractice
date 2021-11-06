from weier_remodel_proj.api.base_api import BaseApi
from weier_remodel_proj.core.api_yaml_template_replace_variables import template



class EmployeeApi(BaseApi):

    def __init__(self, yam_path = "employee.yml"):
        self.yaml_dict = self.get_yaml_data(yam_path)

    # 查询员工信息
    def get_employee(self, user_id):
        # 业务方调用时，参入参数即可，不需要关系内部变量名称；如果变量名发生变化，修改yaml文件一处即可
        variable = {
            "access_token": self.get_token(),
            "userid": user_id
        }
        # 替换变量
        data = template(self.yaml_dict["get_employee"], **variable)
        # 发送请求
        return self.send_request(**data)


    # 创建员工
    def create_employee(self, department, userid, name, mobile):
        variable = {
            "access_token": self.get_token(),
            "department": department,
            "mobile": mobile,
            "name": name,
            "userid": userid
        }
        data = template(self.yaml_dict["create_employee"], **variable)
        return self.send_request(**data)


    def update_employee(self):
        pass

    def delete_employee(self):
        pass

    def batch_delete_employee(self):
        pass

    def get_employee_by_department(self):
        pass


if __name__ == '__main__':
    x = EmployeeApi()
    print(x.get_employee("TEST_001"))
    print(x.create_employee([2], "III", "TEST111", "15000000233"))