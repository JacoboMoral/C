from rsa_public_key import rsa_public_key
from rsa_key import rsa_key
import hashlib
import time
from timeit import Timer

class transaction:
    def __init__(self, message, RSAkey):
        # genera una transaccio signant "message" amb la clau "RSAkey"

        # self.message = int(hashlib.sha512(message.encode('utf-8')).hexdigest(), 16) #el missatge l'hem calculat el hash-512 i despres l'hem convertit a numero
        # self.public_key = rsa_public_key(RSAkey)
        # self.signature = self.signature(self.message, RSAkey)


        self.message = message
        self.messageHash512 = int(hashlib.sha512(message.encode('utf-8')).hexdigest(), 16) #el missatge l'hem calculat el hash-512 i despres l'hem convertit a numero
        self.public_key = rsa_public_key(RSAkey)
        self.signature = self.signature(self.messageHash512, RSAkey)


    def verify(self):
        # retorna el boolea True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau publica "public_key".
        # En qualsevol altre cas retorma el boolea False

        return self.public_key.verify(self.messageHash512, self.signature)

    def signature(self, message, RSAkey):
        #per calcular el temps:
        time, signature = self.my_timeit(RSAkey.sign(message))
        print(time)
        return signature

        #si no volem calcular el temps:
        return RSAkey.sign(message)
        #return RSAkey.sign_slow(message)

    def my_timeit(self, func, *args, **kwargs):
        output_container = []
        def wrapper():
            output_container.append(func(*args, **kwargs))
        timer = Timer(wrapper)
        delta = timer.timeit(1)
        return delta, output_container.pop()
