import django
django.setup()
from cmdb.models import Device

class CmdbDevice(Device):

    def __init__(self, id=0):
        if id > 0:
            self.objects.get(pk=id)

    def fetch(self):
        pass

    def create(self):
        pass


    def update(self):
        pass

    def delete(self):
        pass

    def exists(self):
        pass
