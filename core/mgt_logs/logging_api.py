"""
Install a logging api with log rotation
"""

import logging as lg
import logging.handlers as rf

import core.mgt_conf.yaml_generic as gen


def generate_logging_filename():
    """
    generate the logging filename (full path)
    :return: the full logging filename (with path)
   """
    # Define the variables
    path = template = ""

    configf = gen.get_config("mgt_logs")

    # Get the logging directory path
    try:
        path = configf["mgt_logs"]["logfile_output_path"]
    except KeyError as e:
        print("generate_logging_filename : The [%s] key is invalid in %s%s.yaml " % (
            e, gen.get_configfile_path(), "gestion_files"))

    # Get the logging template name
    try:
        template = configf["mgt_logs"]["logfile_name"]
    except KeyError as e:
        print("generate_logging_filename : The [%s] key is invalid in %s%s.yaml " % (
            e, gen.get_configfile_path(), "ad_hno"))
    fullname = path + template
    print("logging on" + fullname)
    return fullname


def get_logfile_max_length():
    """
    Get the logfile max length from the configuration file before rotate
    return : the max length
            the max length
            :return: the logfile max length
            :rtype: object
    """

    configf = gen.get_config("mgt_logs")
    length = None

    # Get the logging file max length
    try:
        length = configf["mgt_logs"]["logfile_max_length"]
    except KeyError as e:
        print(
            "get_logfile_max_length : The [%s] key is invalid in %s%s.yaml " % (e, gen.get_configfile_path(), "ad_hno"))
    return length


def get_logger(module_name, logging_level):
    """
    Set a logger and return it
    :param module_name: name of the calling module
    :param logging_level: log level (can be 'DEBUG', 'INFO', 'WARNING', 'ERROR' or 'CRITICAL')
    :return: the logger object
    """
    # get the log file fullname
    log_file = generate_logging_filename()
    print(log_file)

    # create logger
    lg.basicConfig()
    logger = lg.getLogger(module_name)
    logger.setLevel(logging_level)
    #     fh = lg.FileHandler(log_file)
    #
    #     logger.addHandler(fh)

    # create console handler and set level to debug
    ch = rf.RotatingFileHandler(log_file, mode="a", maxBytes=get_logfile_max_length(), backupCount=1, encoding="utf-8")
    ch.setLevel(lg.DEBUG)

    # create formatter
    formatter = lg.Formatter('%(asctime)s - Ticket - Module : %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # return the logger
    return logger
