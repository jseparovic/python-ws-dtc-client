import logging
import os
import sys

PROTOCOL_VERSION = 8

LOG_LEVEL = logging.INFO
LOG_DIR = '/var/log/dtc'
PROGRAM_NAME = os.path.basename(sys.argv[0]).replace(".py", "")
LOG_FILE = LOG_DIR + '/' + PROGRAM_NAME + ".log"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

FILE_NAME_DATE_PREFIX = "%Y-%m-%d_%H_%M_%S"

CONSOLE_LOGGING = True
