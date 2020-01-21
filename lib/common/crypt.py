import base64
import hashlib
import random
import string
from common.system import cmdbdir
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self):
        key = _readKey()
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self,raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        e = base64.b64encode(iv + cipher.encrypt(raw.encode()))
        return e.decode("utf-8")

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self,s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

def generateKey(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def _readKey():
    try:
      f = open(cmdbdir() + "/etc/cmdb.key", "rt")
      key = f.readline()
      f.close()
    except Exception as e:
        print("Failed to open keyfile:", e)
    else:
        return key
