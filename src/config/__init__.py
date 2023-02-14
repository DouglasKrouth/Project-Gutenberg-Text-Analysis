import yaml
from os import path, pardir
from pathlib import Path
import logging


class Config:
    """
    Config class that we'll use to access yaml config file.

    TODO : Add param to check whether the config file is in a different location than specified
    TODO : Not robust, could benefit from searching for yaml configs with pathlib
    """

    config_params = {}
    # yaml_config_path = path.abspath(path.join("config.yaml", pardir))
    yaml_config_path = r"../config.yaml"

    def __init__(self, use_yaml=True, **kwargs):
        if use_yaml:
            try:
                with open(self.yaml_config_path, "r") as f:
                    temp = yaml.load(f, Loader=yaml.FullLoader)
                    self.config_params.update(temp)
            except FileNotFoundError:
                logging.error("Config file not found!")
        self.config_params.update(kwargs)
        # No params passed : throw warning
        if len(self.config_params) == 0:
            logging.warning(
                "No config parameters passed! Is the config file @ {} empty?".format(
                    self.yaml_config_path
                )
            )
