from django.db import models


class Domain(models.Model):
    SHA = 'sha'
    MD5 = 'md5'
    DES = 'des'
    AES = 'aes'
    AUTHPROTO = (
        (SHA , 'SHA'),
        (MD5, 'MD5')
    )
    PRIVPROTO = (
        (DES, 'DES'),
        (AES, 'AES')
    )
    name = models.CharField(max_length=32)
    telnet_user = models.CharField(max_length=32)
    telnet_pass = models.CharField(max_length=64)
    snmp_ro = models.CharField(max_length=64)
    snmp_rw = models.CharField(max_length=64)
    securityName = models.CharField(max_length=64)
    authProtocol = models.CharField(choices=AUTHPROTO, default=MD5, max_length=3)
    authKey = models.CharField(max_length=64)
    privProtocol = models.CharField(choices=PRIVPROTO, default=AES, max_length=3)
    privKey = models.CharField(max_length=64)
    lastUpdate = models.DateTimeField(auto_now=True)

