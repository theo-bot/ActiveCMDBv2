from django.db import models

# Create your models here.
class Vendor (models.Model):
    name = models.CharField(max_length=128)
    pen = models.PositiveIntegerField()

    def MyTest(self):
        print("{}: {}".format(self.name, self.pen))


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=16)
    phone = models.CharField(max_length=32)
    mobile = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(
            self.name, self.email
        )