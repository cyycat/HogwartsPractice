
import re
import logging
logging.basicConfig(level=logging.INFO)

def api_yaml_split_by_title(yaml_path) -> dict:
    """
    根据TITLE，切割请求步骤（api的yaml数据）
    :param yam_path:
    :return:

    eg:
    :return {"TITLE1":"对应请求步骤数据"，"TITLE2":"对应请求步骤数据"}
    """
    yaml_dict = {}

    with open(yaml_path) as f:
        # 切割文件 —> list
        files = f.read().split("---")
        # 过滤掉列表中的''
        results = list(filter(lambda x: x != '', files))
        # 组装字典，key为TITLE
        for i in results:
            # 获取TITLE
            k = re.findall(r'TITLE.*', i)[0].split()[1]
            yaml_dict[k] = re.sub(r'TITLE.*', '\n', i)
    logging.info(f"根据TITLE，切割请求步骤: {yaml_dict}")
    return yaml_dict