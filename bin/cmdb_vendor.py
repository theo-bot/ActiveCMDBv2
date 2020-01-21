#!/usr/bin/env python3

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()
from core.models import contact

for c in contact.objects.all():
    print("Name: {}".format(c.name))