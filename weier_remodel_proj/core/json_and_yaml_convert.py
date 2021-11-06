import yaml
import json


def json_to_yaml(Jdata:json, path="json_and_yaml_test.yaml"):
    """
    json数据转换为yaml格式，写入yaml文件

    :param Jdata: json格式的数据
    :param path: 文件路径
    :return:
    """
    with open(path, "w") as f:
        print(yaml.safe_dump(Jdata))
        yaml.safe_dump(data=Jdata, stream=f, sort_keys=False)


def yaml_to_json(yaml_path) -> str:
    """
    yamL数据转换为json

    :param yaml_path: yaml文件路径
    :return: 返回json数据
    """
    with open(yaml_path) as f:
        str_data = yaml.safe_load(f)
        print(str_data)
        return str_data



if __name__ == '__main__':
    data = {"TITLE":11,"data":[["创建指定部门id", "产品5", 2, "10"],
                              ["自动生成部门id", "产品6", 1, ""]]}

    json_to_yaml(data)
    yaml_to_json("json_and_yaml_test.yaml")