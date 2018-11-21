class block:
    def __init__(self):
        # crea un bloc (no neces`ariamnet v`alid)
        self.block_hash
        self.previous_block_hash
        self.transaction
        self.seed

    def genesis(self,transaction):
        # genera el primer bloc d’una cadena amb la transacco "transaction" que es caracteritza per:
        # - previous_block_hash=0
        # - ser valid
        a = 5

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
