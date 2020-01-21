import os
import json

def cmdbdir():
    return os.environ['CMDB_HOME']

def readconfig(rname):
    filename = cmdbdir() + '/etc/' + rname
    with open(filename, 'r') as cfgfile:
        data = cfgfile.read()

    # Parse json data
    cfg = json.loads(data)

    return cfg
