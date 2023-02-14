# test_config.py
import src.config as config
import os
import logging as log

cfg = config.Config()

def test_check_YAML_present():
    assert os.path.isfile(cfg.yaml_config_path) == True
    
def test_check_config_file_is_yaml():
    assert cfg.yaml_config_path.endswith(".yaml") or cfg.yaml_config_path.endswith(".yml")