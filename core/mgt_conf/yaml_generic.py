"""
helps to manage all config files
"""
import yaml

import core.mgt_conf.yaml_config as cmy
settings = cmy.load_yaml_config()


def get_configfile_path():
    """
        get the path where lives config
        :return: the full path of config:
    """
    path = ''
    try:
        with open(settings['etc']['path'] + "mgt_conf.yaml", "r") as f:
            config = yaml.safe_load(f)
            path = config['mgt_conf']['rep_app_conf']
    except yaml.YAMLError as exc:
        print('Error in configuration file:', exc)
    return path


def get_config(module_name):
    """
    load the config file
    :param module_name:  the name of the module as python style x.y.z
    :return: the yaml conf as dict(key,value)
    """
    config = ""
    try:
        with open(settings['etc']['path'] + module_name + ".yaml", "r") as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print('Error in configuration file:', exc)
    return config


def extend_config(module_name, ext_path=None):
    """
    load a module with an ext_path into etc (like etc/cmdb for instance)
    :param module_name: the name of the config file
    :param ext_path: a path with / at end
    :return: the config as a dict(key,value)
    """
    config = ""

    try:
        fullpath = settings['etc']['path']
        if ext_path is not None:
            fullpath = fullpath + ext_path
        with open(fullpath + module_name + ".yaml", "r") as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print("Error in configuration file:", exc)
    return config
