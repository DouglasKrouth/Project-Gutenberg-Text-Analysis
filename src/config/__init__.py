import yaml

'''
Config class that we'll use to access yaml config file.

TODO : Add param to check whether the config file is in a different location than specified
TODO : Not robust, could benefit from searching for yaml configs with pathlib
'''
class Config:
    config_params = {}

    def __init__(self, use_yaml=True, **kwargs):
        if use_yaml:
            with open("./config.yaml", "r") as f:
                temp = yaml.load(f, Loader=yaml.FullLoader)
                self.config_params.update(temp)
        self.config_params.update(kwargs)