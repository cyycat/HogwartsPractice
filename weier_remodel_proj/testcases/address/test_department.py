import time

import pytest
import os
from weier_remodel_proj.api.address.department_api import DepartmentApi
from weier_remodel_proj.core.case_yaml_split_by_title import case_api_yaml_split_by_title
from weier_remodel_proj.testcases.BaseCase import BaseCase
import yaml
import allure


path = os.path.abspath(os.path.dirname(__file__)) + '/test_department.yml'
# 根据title切割 —> dict
yaml_dict = case_api_yaml_split_by_title(path)


class TestDepartment(BaseCase):
    def setup(self):
        self.DA = DepartmentApi()

    @pytest.mark.parametrize(["name","parentid","id"],
                             yaml.safe_load(yaml_dict["test_creat_department_success"])["data"])
    def test_creat_department_success(self, name, parentid, id):
        try:
            with allure.step(f"如果已存在部门{name}，则先删除"):
                if id != "" and len(self.DA.get_department(id)["department"]) >= 1:
                    self.DA.delete_department(id)

            with allure.step(f"新增部门{name}"):
                result = self.DA.create_department(name, parentid, id)

            with allure.step(f"判断是否新增成功"):
                assert result["errcode"] == 0
                assert self.DA.get_department(result["id"])["department"][0]["name"] == name

            with allure.step(f"删除部门{name}"):
                self.DA.delete_department(result["id"])
        except AssertionError:
            self.DA.delete_department(id)


if __name__ == '__main__':
    pytest.main(["-v","-s"])



