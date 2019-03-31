import yaml, os

class GetData:

    def __init__(self):
        pass

    def get_read_yml(self, yaml_name):

        """返回yaml文件数据"""
        # file_path = "./"
        with open("./Data"+os.sep+yaml_name, "r",encoding="utf-8") as f:
            return yaml.safe_load(f)


