from string import Template
import yaml
import logging
logging.basicConfig(level=logging.INFO)

def api_yaml_template_replace_variables(source:str, **variable):
    """
    解析字符串，替换变量($标识)
    :param source: 被解析对象，字符串格式
    :param variable: 替换的变量参数，变量名称必须一致
    :return:

    eg:
    source = {
        "a" : $a
        "b": $b
    }
    variable = {"a":1, "b":2}

    :return = {
        "a" : 1
        "b": 2
    }
    """
    template_str_data = Template(source).substitute(**variable)
    result = yaml.safe_load(template_str_data)
    logging.info(f"变量替换后：{template_str_data}")
    logging.info(f"yaml.safe_load为字典格式：{result}")

    return yaml.safe_load(template_str_data)


