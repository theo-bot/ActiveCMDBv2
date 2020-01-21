import sys
import os
import time
import daemon
from daemon import pidfile
from common.messagebus import broker
from common.logger import GetFileLogger
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

class DiscoveryServer():

    def __init__(self):
        self.log = GetFileLogger()

    def Discover(self, hostname='', id=0):
        if id > 0:
            device = GetHostByID(id)
        elif ( hostname.length > 0 ):
            device = GetHostByName(hostname)
        else:
            self.log.warn("Unable to fetch device")




