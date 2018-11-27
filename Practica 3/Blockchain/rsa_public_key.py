import hashlib

class rsa_public_key:
    def __init__(self, rsa_key):
        # genera la clau publica RSA asociada a la clau RSA "rsa_key"

        self.publicExponent = rsa_key.publicExponent
        self.modulus = rsa_key.modulus

    def verify(self, message, signature):
        # retorna el boolea True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau RSA associada a la clau
        # publica RSA.
        # En qualsevol altre cas retorma el boolea False

        verifyMessage = pow(signature, self.publicExponent, self.modulus)

        if message == verifyMessage:
            return True
        else:
            print("rsa_public_key verify = false")
            return False
