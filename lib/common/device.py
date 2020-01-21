from object.device import CmdbDevice
django.setup()
from cmdb.models import Device


def GetHostByID(id):
    if id > 0:
        device = CmdbDevice(id=id)
        device.fetch()
        return device


def GetHostByName(name):
    if len(name) > 0:
        obj = Device.objects.get(hostname=name)
        device = CmdbDevice(id=obj.id)
