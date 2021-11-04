# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 7:02 PM
# @Author  : nzooherd
# @File    : log.py
# @Software: PyCharm

import logging
import sys
from os import makedirs
from os.path import dirname, exists

loggers = {}

LOG_ENABLED = True
LOG_TO_CONSOLE = True
LOG_TO_FILE = True

LOG_PATH = '../log/app'
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - \
%(name)s - %(lineno)d - %(module)s - %(message)s'


def get_logger(name=None):
    """
    get logger by name
    :param name: name of logger
    :return: logger
    """
    global loggers

    if not name:
        name = __name__

    if loggers.get(name):
        return loggers.get(name)

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # log to console
    if LOG_ENABLED and LOG_TO_CONSOLE:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    # log to file
    if LOG_ENABLED and LOG_TO_FILE:
        log_dir = dirname(LOG_PATH)
        if not exists(log_dir):
            makedirs(log_dir)
        file_handler = logging.FileHandler(LOG_PATH, encoding='utf-8')
        file_handler.setLevel(level=LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    loggers[name] = logger
    return logger
