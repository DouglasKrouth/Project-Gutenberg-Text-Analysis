# test_config.py
from ..config import Config
import os
import logging as log
import pytest

cfg = Config()

def test_check_YAML_present():
    assert os.path.isfile(cfg.yaml_config_path) == True
    
def test_check_config_file_is_yaml():
    assert cfg.yaml_config_path.endswith(".yaml") or cfg.yaml_config_path.endswith(".yml")

def test_create_Config_object():
    assert Config() is not None