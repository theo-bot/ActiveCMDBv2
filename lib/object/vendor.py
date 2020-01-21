import django
django.setup()
from cmdb.models import Vendor

class CmdbVendor(Vendor):
    def __init__(self, id=0):
        if id > 0:
            self.objects.get(pk=id)
