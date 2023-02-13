import yaml
import os

'''
Config class that we'll use to access yaml config file.

TODO : Add param to check whether the config file is in a different location than specified
TODO : Not robust, could benefit from searching for yaml configs with pathlib
'''
class Config:
    config_params = {}
    yaml_config_path = os.path.abspath("./src/config/config.yaml")

    def __init__(self, use_yaml=True, **kwargs):
        if use_yaml:
            with open(self.yaml_config_path, "r") as f:
                temp = yaml.load(f, Loader=yaml.FullLoader)
                self.config_params.update(temp)
        self.config_params.update(kwargs)