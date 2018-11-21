class block:
    def __init__(self):
        self.block_hash
        self.previous_block_hash
        self.transaction
        self.seed

class transaction:
    def __init__(self, message, RSAkey):
        self.public_key
        self.message
        self.signature

class rsa_key:
    def __init__(self,bits_modulo=2048,e=2**16+1):
        self.publicExponent
        self.privateExponent
        self.modulus
        self.primeP
        self.primeQ
        self.privateExponentModulusPhiP
        self.privateExponentModulusPhiQ
        self.inverseQModulusP

class rsa_public_key:
    def __init__(self, rsa_key):
        # • publicExponent ´es l’exponent p´ublic de la clau rsa key,
        # • modulus ´es el m`odul de la clau rsa key.
        # Un bloc ´es v`alid si el seu hash h satisf`a la condici´o h < 2
        # 256−d on d ´es un par`ametre que indica el proof of work
        # necessari per generar un bloc v`alid. Per aquesta pr`actica d=8.

        self.publicExponent
        self.modulus

class rsa_key:
    def __init__(self,bits_modulo=2048,e=2**16+1):
        # genera una clau RSA (de 2048 bits i amb exponent p´ublic 2**16+1 per defecte)    self.publicExponent

        self.privateExponent
        self.modulus
        self.primeP
        self.primeQ
        self.privateExponentModulusPhiP
        self.privateExponentModulusPhiQ
        self.inverseQModulusP
    def sign(self,message):
        # retorma un enter que ´es la signatura de "message" feta amb la clau RSA fent servir el TXR

    def sign_slow(self,message):
        # retorma un enter que ´es la signatura de "message" feta amb la clau RSA sense fer servir el TXR

class rsa_public_key:
    def __init__(self, rsa_key):
        # genera la clau p´ublica RSA asociada a la clau RSA "rsa_key"

        self.publicExponent
        self.modulus

    def verify(self, message, signature):
        # retorna el boole`a True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau RSA associada a la clau
        # p´ublica RSA.
        # En qualsevol altre cas retorma el boole`a False
        a

class transaction:
    def __init__(self, message, RSAkey):
        # genera una transacci´o signant "message" amb la clau "RSAkey"

        self.public_key
        self.message
        self.signature

    def verify(self):
        # retorna el boole`a True si "signature" es correspon amb una
        # signatura de "message" feta amb la clau p´ublica "public_key".
        # En qualsevol altre cas retorma el boole`a False


class block:
def __init__(self):
    # crea un bloc (no neces`ariamnet v`alid)

    self.block_hash
    self.previous_block_hash
    self.transaction
    self.seed

def genesis(self,transaction):
    # genera el primer bloc d’una cadena amb la transacci´o "transaction" que es caracteritza per:
    # - previous_block_hash=0
    # - ser v`alid
    a

def next_block(self, transaction):
    # genera el seg¨uent block v`alid amb la transacci´o "transaction"
    a

def verify_block(self):
    # Verifica si un bloc ´es v`alid:
    # -Comprova que el hash del bloc anterior cumpleix las condicions exigides
    # -Comprova la transacci´o del bloc ´es v`alida
    # -Comprova que el hash del bloc cumpleix las condicions exigides
    # Si totes les comprovacions s´on correctes retorna el boole`a True.
    # En qualsevol altre cas retorma el boole`a False
    a

class block_chain:

    def __init__(self,transaction):
        # genera una cadena de blocs que ´es una llista de blocs,
        # el primer bloc ´es un bloc "genesis" generat amb la transacci´o "transaction"
        self.list_of_blocks

    def add_block(self,transaction):
        #afegeix a la llista de blocs un nou bloc v`alid generat amb la transacci´o "transaction"
        a


    def verify(self):
        # verifica si la cadena de blocs ´es v`alida:
        # - Comprova que tots el blocs s´on v`alids
        # - Comprova que el primer bloc ´es un bloc "genesis"
        # - Comprova que per cada bloc de la cadena el seg¨uent ´es el correcte
        # Si totes les comprovacions s´on correctes retorna el boole`a True.
        # En qualsevol altre cas retorma el boole`a False i fins a quin bloc la cadena ´es v´alida
