from Crypto.Cipher import DES3
from Crypto import Random
import base64


class DESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.key = self._pad(key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        return self._unpad(cipher.decrypt(enc))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]



a = '{"course_id": "course-v1:test2+test2+test2", "username": "admin", "email": "xahgmah@yandex.ru"}'
key = "123456789012346"
print "ROW -  " + a
dc = DESCipher(key)
encoded = dc.encrypt(a)
print "KEY -  " + dc.key
print "ENCODED -  " + encoded
decoded = dc.decrypt(encoded)
print "DECODE -  " + decoded