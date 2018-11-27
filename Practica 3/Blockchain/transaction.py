from rsa_public_key import rsa_public_key
from rsa_key import rsa_key
import hashlib


class transaction:
    def __init__(self, message, RSAkey):
        # genera una transaccio signant "message" amb la clau "RSAkey"

        # self.message = int(hashlib.sha512(message.encode('utf-8')).hexdigest(), 16) #el missatge l'hem calculat el hash-512 i despres l'hem convertit a numero
        # self.public_key = rsa_public_key(RSAkey)
        # self.signature = self.signature(self.message, RSAkey)


        self.message = message
        messageHash = int(hashlib.sha512(message.encode('utf-8')).hexdigest(), 16) #el missatge l'hem calculat el hash-512 i despres l'hem convertit a numero
        self.public_key = rsa_public_key(RSAkey)
        self.signature = self.signature(messageHash, RSAkey)


    def verify(self):
        # retorna el boolea True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau publica "public_key".
        # En qualsevol altre cas retorma el boolea False

        messageHash = int(hashlib.sha512(self.message.encode('utf-8')).hexdigest(), 16) #el missatge l'hem calculat el hash-512 i despres l'hem convertit a numero
        return self.public_key.verify(messageHash, self.signature)

    def signature(self, message, RSAkey):
        return RSAkey.sign(message)
        #return RSAkey.sign_slow(message)
