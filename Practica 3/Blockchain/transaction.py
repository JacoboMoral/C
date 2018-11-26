from rsa_public_key import rsa_public_key
from rsa_key import rsa_key
import hashlib


class transaction:
    def __init__(self, message, RSAkey):
        # genera una transaccio signant "message" amb la clau "RSAkey"
        print(message)
        self.message = int(hashlib.sha512(message.encode('utf-8')).hexdigest(), 16) #el missatge l'hem calculat el hash-512 i despres l'hem convertit a numero
        print(self.message)
        self.public_key = rsa_public_key(RSAkey)
        self.signature = self.signature(self.message, RSAkey)

    def verify(self):
        # retorna el boolea True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau publica "public_key".
        # En qualsevol altre cas retorma el boolea False

        return self.public_key.verify(self.message, self.signature)

    def signature(self, message, RSAkey):
        return RSAkey.sign(message)
        #return RSAkey.sign_slow(message)
