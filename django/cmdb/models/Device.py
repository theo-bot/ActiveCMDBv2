from django.db import models
from .DeviceType import DeviceType
from .Domain import Domain


class Device(models.Model):
    hostname = models.CharField(max_length=128)
    mgtaddress = models.GenericIPAddressField
    status = models.PositiveIntegerField,
    deviceType = models.ForeignKey(DeviceType, on_delete=models.PROTECT)
    dateAdded = models.TimeField
    sysUptime = models.BigIntegerField
    sysDescr = models.CharField(max_length=256, default='')
    sysObjectID = models.CharField(max_length=128, default='')
    EngineID = models.CharField(max_length=128, default='')
    critical = models.BooleanField(default=False)
    lastUpdate = models.DateTimeField(auto_now=True)
    snmpPort = models.PositiveIntegerField(default=161)
    lastDiscovery = models.DateTimeField
    lastConfigfetch = models.DateTimeField
    doesSsh = models.BooleanField(default=False)
    doesTelnet = models.BooleanField(default=False)
    sysLocation = models.CharField(max_length=256, default='')
    osType = models.CharField(max_length=32, default='', null=True)
    osVersion = models.CharField(max_length=32, default='', null=True)


class DeviceError(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    icmpError = models.BooleanField(default=False)
    icmpFirstAlert = models.DateTimeField
    icmpLastAlert = models.DateTimeField
    snmpError = models.BooleanField(default=False)
    snmpFirstAlert = models.DateTimeField
    snmpLastAlert = models.DateTimeField
    configError = models.BooleanField(default=False)
    configFirstAlert = models.DateTimeField
    configLastAlert = models.DateTimeField


class DeviceSecurity(models.Model):
    SHA = 'sha'
    MD5 = 'md5'
    DES = 'des'
    AES = 'aes'
    COM = 'com'
    USM = 'usm'
    AUTHPROTO = (
        (SHA, 'SHA'),
        (MD5, 'MD5')
    )
    PRIVPROTO = (
        (DES, 'DES'),
        (AES, 'AES')
    )
    AUTHMODEL = (
        (COM, 'Community'),
        (USM, 'User Security Model')
    )
    device = models.ForeignKey(Device, related_name='security', on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT)
    telnet_user = models.CharField(max_length=32)
    telnet_pass = models.CharField(max_length=64)
    snmpAuthModel = models.CharField(choices=AUTHMODEL, default=USM, max_length=3)
    snmp_ro = models.CharField(max_length=64)
    snmp_rw = models.CharField(max_length=64)
    securityName = models.CharField(max_length=64)
    authProtocol = models.CharField(choices=AUTHPROTO, default=MD5, max_length=3)
    authKey = models.CharField(max_length=64)
    privProtocol = models.CharField(choices=PRIVPROTO, default=AES, max_length=3)
    privKey = models.CharField(max_length=64)
    lastUpdate = models.DateTimeField(auto_now=True)



