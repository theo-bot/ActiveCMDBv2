#!/usr/bin/env python3

import sys
import argparse
sys.path.append('../lib')

from common.crypt import AESCipher

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--encode", default=None, type=str, help="String to be encoded")
group.add_argument("--decode", default=None, type=str, help="String to be decoded")

args = parser.parse_args()
if args.encode:
    coder = AESCipher()
    print(coder.encrypt(args.encode))
if args.decode:
    coder = AESCipher()
    print(coder.decrypt(args.decode))