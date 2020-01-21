#!/usr/bin/env python3

import sys
sys.path.append('../lib')

from common.crypt import generateKey

print(generateKey(32))
