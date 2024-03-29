import hashlib
from random import random
import json
from transaction import transaction



class block:
    def __init__(self):
        # crea un bloc (no necessariamnet valid)
        self.block_hash = None
        self.previous_block_hash = None
        self.transaction = None
        self.seed = None
        self.d = 8

    def genesis(self,transaction):
        # genera el primer bloc d’una cadena amb la transaccio "transaction" que es caracteritza per:
        # - previous_block_hash=0
        # - ser valid

        self.previous_block_hash = 0
        self.transaction = transaction
        self.generateValidSeed()
        #self.block_hash = self.calculateHash256()

    def next_block(self, transaction, previous_block_hash):
        # genera el seguent block valid amb la transaccio "transaction"
        self.previous_block_hash = previous_block_hash
        self.transaction = transaction
        self.generateValidSeed()

    def verify_block(self):
        # Verifica si un bloc es valid:
        # -Comprova que el hash del bloc anterior cumpleix las condicions exigides
        # -Comprova la transaccio del bloc es valida
        # -Comprova que el hash del bloc cumpleix las condicions exigides
        # Si totes les comprovacions son correctes retorna el boolea True.
        # En qualsevol altre cas retorma el boolea False

        if not self.verifyBlockHash(self.block_hash):
            return False
        if not self.verifyBlockHash(self.previous_block_hash):
            return False
        if not self.verifyTransaction(self.transaction):
            return False
        return True

    def verifyBlockHash(self, block_hash):
        # Un bloc es valid si el seu hash h satisfa la condicio
        # h < 2^(256−d) on d es un parametre que indica el proof of work
        # necessari per generar un bloc valid.

        llindar = pow(2,256-self.d)
        return block_hash < llindar

    def verifyTransaction(self, transaction):
        return self.transaction.verify()

    def calculateHash256(self):
        entrada=str(self.previous_block_hash)
        entrada=entrada+str(self.transaction.public_key.publicExponent)
        entrada=entrada+str(self.transaction.public_key.modulus)
        entrada=entrada+str(self.transaction.message)
        entrada=entrada+str(self.transaction.signature)
        entrada=entrada+str(self.seed)
        h=int(hashlib.sha256(entrada.encode()).hexdigest(),16)
        return h

    def generateValidSeed(self):
        generated = False
        while not generated:
            self.seed = int(random()*pow(10,17))
            h=self.calculateHash256()
            if (self.verifyBlockHash(h)):
                generated = True
                self.block_hash = h
