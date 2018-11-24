class rsa_public_key:
    def __init__(self, rsa_key):
        # genera la clau publica RSA asociada a la clau RSA "rsa_key"

        self.publicExponent = 10
        self.modulus = 10

    def verify(self, message, signature):
        # retorna el boolea True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau RSA associada a la clau
        # publica RSA.
        # En qualsevol altre cas retorma el boolea False
        return False;
