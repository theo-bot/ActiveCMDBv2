from django.db import models
from .Vendor import Vendor

# Create your models here.


class DeviceType(models.Model):
    TEXT = 1
    BINARY = 2
    CONFIG_TYPES = (
        (TEXT, 'Text'),
        (BINARY, 'Binary')
    )
    name = models.CharField(max_length=32)
    descr = models.CharField(max_length=256)
    oid = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    networkType = models.PositiveIntegerField(default=1)
    configType = models.PositiveIntegerField(choices=CONFIG_TYPES, default=TEXT)
    lastUpdate = models.DateTimeField(auto_now=True)


class DeviceTypeFlags(models.Model):
    flag = models.CharField(max_length=16)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)