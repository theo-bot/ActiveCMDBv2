import logging
import os
from common.system import cmdbdir

DEFAULT_LOGLEVEL = logging.INFO


def GetFileLogger():
    #
    # Get the filename for the log output
    filename = GetLogFilename()

    #
    # Create a new logger object
    log = logging.getLogger()

    #
    # Set the default loglevel for the logger
    log.setLevel(DEFAULT_LOGLEVEL)

    #
    # Create a handler
    handler = logging.FileHandler(filename)
    handler.setLevel(DEFAULT_LOGLEVEL)

    #
    # Create a formatter for the handler
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(module)s::%(funcName)s) : %(message)s')
    handler.setFormatter(formatter)

    #
    # Connect the handler to the logger
    log.addHandler(handler)

    return log


def GetLogFilename():
    return cmdbdir() + '/var/log/' + os.environ['PROCID'] + '.log'
