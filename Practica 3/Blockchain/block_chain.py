from block import block

class block_chain:

    def __init__(self,transaction):
        # genera una cadena de blocs que es una llista de blocs,
        # el primer bloc es un bloc "genesis" generat amb la transaccio "transaction"
        self.list_of_blocks = []

        #crear bloque genesis
        self.add_genesis_block(transaction)

    def add_block(self,transaction):
        #afegeix a la llista de blocs un nou bloc valid generat amb la transaccio "transaction"
        bloc = block()
        last_block_hash = self.getLastBlock().getBlockHash()
        bloc.next_block(transaction, last_block_hash)
        self.list_of_blocks.append(bloc)

    def add_block_invalid(self, transaction):
        #afegeix a la llista de blocs un nou bloc NO VALID generat amb la transaccio "transaction"
        a = 5

    def add_genesis_block(self,transaction):
        #afegeix a la llista de blocs un nou bloc gensis generat amb la transaccio "transaction"
        bloc = block()
        bloc.genesis(transaction)
        self.list_of_blocks.append(bloc)

    def getLastBlock(self):
        return self.list_of_blocks[-1]

    def verify(self):
        # verifica si la cadena de blocs es valida:
        # - Comprova que tots el blocs son valids
        # - Comprova que el primer bloc es un bloc "genesis"
        # - Comprova que per cada bloc de la cadena el seguent es el correcte
        # Si totes les comprovacions son correctes retorna el boolea True.
        # En qualsevol altre cas retorma el boolea False i fins a quin bloc la cadena es valida
        return True;
