
from common.snmp import snmpget, snmpoidconv

def DiscoverSystem(device):
    oids = {
        "sysName" : ".1.3.6.1.2.1.1.5.0",
        "sysObjectID" : ".1.3.6.1.2.1.1.2.0",
        "sysDescr" : ".1.3.6.1.2.1.1.1.0",
    }

    oidlist = snmpoidconv(oids)
    credentials = snmpcreds(device)
    result = snmpget(device.mgtaddress, oidlist, credentials)


    return result