from hashlib import sha256
import json



class block:
    def __init__(self):
        # crea un bloc (no necessariamnet valid)
        h = 5

    def genesis(self,transaction):
        # genera el primer bloc d’una cadena amb la transaccio "transaction" que es caracteritza per:
        # - previous_block_hash=0
        # - ser valid
        self.previous_block_hash = 0
        self.transaction = transaction
        self.seed = 5
        self.block_hash = self.getHash256()

    def next_block(self, transaction):
        # genera el seguent block valid amb la transaccio "transaction"
        a = 5

    def verify_block(self):
        # Verifica si un bloc es valid:
        # -Comprova que el hash del bloc anterior cumpleix las condicions exigides
        # -Comprova la transaccio del bloc es valida
        # -Comprova que el hash del bloc cumpleix las condicions exigides
        # Si totes les comprovacions son correctes retorna el boolea True.
        # En qualsevol altre cas retorma el boolea False

        return True

    def getHash256(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
