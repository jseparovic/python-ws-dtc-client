#!/usr/bin/python

import argparse
import subprocess
from datetime import datetime

from lib.constants import *


class Util:
    @staticmethod
    def set_promiscuous_mode(interface):
        import os
        ret = os.system("ifconfig %s promisc" % interface)

    @staticmethod
    def get_timestamp_string(datetime_now=None):
        if not datetime_now:
            datetime_now = datetime.now()
        return datetime_now.strftime(FILE_NAME_DATE_PREFIX)

    @staticmethod
    def setup_logging(logger_name, console=True, log_to_file=False):
        root_logger = logging.getLogger()
        root_logger.name = logger_name
        log_formatter = logging.Formatter(LOG_FORMAT)

        # log to file
        if log_to_file:
            log_dir = os.path.dirname(LOG_FILE)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            file_handler = logging.FileHandler(LOG_FILE)
            file_handler.setFormatter(log_formatter)
            root_logger.addHandler(file_handler)

        if console:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(log_formatter)
            root_logger.addHandler(stream_handler)

        log_level = os.getenv(LOG_LEVEL) if os.getenv(LOG_LEVEL) else DEFAULT_LOG_LEVEL
        root_logger.setLevel(logging.getLevelName(log_level))
        return root_logger

    @staticmethod
    def call(argv):
        proc = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = proc.wait()
        logging.info("returned status=%s stdout=\"%s\" stderr=\"%s\""
                     % (res, proc.stdout.read().rstrip(), proc.stderr.read().rstrip()))
        return res, proc

    @staticmethod
    def call_ls():
        res, proc = Util.call(['ls'])

    @staticmethod
    def today_serial_date_part():
        return datetime.utcnow().strftime('%Y%m%d')


class AgentError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        super(AgentError, self).__init__(message)


class InvalidArgumentsError(AgentError):
    def __init__(self, message="Invalid Arguments Error"):
        super(AgentError, self).__init__(message)


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        logging.error(message)
        self.print_help()
        sys.exit(2)

    def _print_message(self, message, file=None):
        logging.error(message)

