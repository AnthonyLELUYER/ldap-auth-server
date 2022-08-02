"""
return the high level configuration as a yaml configuration
"""


import os
import yaml
import inspect


def load_yaml_config():
    # [:-33] corresponds to "core/mgt_conf/yaml_config.py"
    # path = os.path.abspath(inspect.getfile(load_yaml_config))[:-33]

    # Retrieve full path of the current function
    full_path = os.path.abspath(inspect.getfile(load_yaml_config))
    # "yaml_config.py" should always be two folders away from the project root directory
    folder_array = full_path.split(os.sep)[:-3]
    # We join the folders with either / or \ depending on the OS
    path = os.sep.join(folder_array) + os.sep

    with open(path + "config.yaml", "r") as f:
        settings = yaml.safe_load(f)
    return settings


# Old way


"""
global settings

with open("/var/www/config.yaml", "r") as f:
    settings = yaml.safe_load(f)
"""
