class rsa_key:
    def __init__(self,bits_modulo=2048,e=2**16+1):
        # genera una clau RSA (de 2048 bits i amb exponent public 2**16+1 per defecte)

        self.publicExponent
        self.privateExponent
        self.modulus
        self.primeP
        self.primeQ
        self.privateExponentModulusPhiP
        self.privateExponentModulusPhiQ
        self.inverseQModulusP

    def sign(self,message):
        # retorma un enter que es la signatura de "message" feta amb la clau RSA fent servir el TXR
        a=5

    def sign_slow(self,message):
        # retorma un enter que ´es la signatura de "message" feta amb la clau RSA sense fer servir el TXR
        a=5