import logging
import logging.config
import os

import yaml
from qutils import ROOT_DIR


class LoggingMixin:

    __logger_configured = False

    @staticmethod
    def setup_logger_config() -> None:
        if not LoggingMixin.__logger_configured:
            with open(os.path.join(ROOT_DIR, 'resources/logger.yml')) as f:
                config = yaml.safe_load(f)
                logging.config.dictConfig(config)
            LoggingMixin.__logger_configured = True

    @property
    def logger():
        LoggingMixin.setup_logger_config()

        if name is None:
            logger_name = self.__class__.__name__
        else:
            logger_name = name
        return logging.getLogger(logger_name)


def get_logger(name: str):
    LoggingMixin.setup_logger_config()
    return logging.getLogger(name)
