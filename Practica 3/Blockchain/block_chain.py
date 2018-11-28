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
        last_block_hash = self.getLastBlock().block_hash
        bloc.next_block(transaction, last_block_hash)
        self.list_of_blocks.append(bloc)

    def add_block_invalid(self, transaction):
        #afegeix a la llista de blocs un nou bloc NO VALID generat amb la transaccio "transaction"
        bloc = block()
        last_block_hash = 2**256 #un block b no es valid si el seu previous_block_hash no es valid (previous_block_hash de b < 2^(256-d)
        bloc.next_block(transaction, last_block_hash)
        self.list_of_blocks.append(bloc)


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

        if not self.verifyBlocks():
            return False
        if not self.verifyGenesis():
            return False
        if not self.verifyBlockChain():
            return False
        return True

    def verifyBlocks(self):
        # Comprova que tots el blocs son valids

        for b in self.list_of_blocks:
            if not b.verify_block():
                return False
        return True

    def verifyGenesis(self):
        # Comprova que el primer bloc es un bloc "genesis"
        # comprova que el primer block de la llista de blocks sigui genesis. Per aixo comprova
        # que el seu previous_block_hash sigui 0 i que a mes sigui valid

        if self.list_of_blocks[0].previous_block_hash != 0:
            return False
        if not self.list_of_blocks[0].verify_block():
            return False
        return True

    def verifyBlockChain(self):
        # Comprova que per cada bloc de la cadena el seguent es el correcte
        # comprova que per tot block b de la llista de blocks block_hash de b == previous_block_hash de b+1

        for i in range(len(self.list_of_blocks)-1):
            if (self.list_of_blocks[i].block_hash != self.list_of_blocks[i+1].previous_block_hash):
                return False
        return True

    def writeFile(self, filename):

        import pickle
        with open(filename, "wb") as file:
            pickle.dump(self.list_of_blocks, file)

        file = open(filename+"_readable","w")
        for b in self.list_of_blocks:
            file.write("Block:\n")
            file.write("  previous_block_hash: ")
            file.write(str(b.previous_block_hash)+"\n")
            file.write("  block_hash: ")
            file.write(str(b.block_hash)+"\n")
            file.write("  seed: ")
            file.write(str(b.seed)+"\n")
            file.write("  transaction:\n")
            file.write("  ...........................................................\n")
            file.write("\n      ________________________________________________________\n")
            file.write("                  PUBLIC KEY: \n")
            file.write("       publicExponent: ")
            file.write(str(b.transaction.public_key.publicExponent))
            file.write("\n")
            file.write("       modulus: ")
            file.write(str(b.transaction.public_key.modulus))
            file.write("\n      ________________________________________________________\n\n")
            file.write("       message: ")
            file.write(str(b.transaction.message))
            file.write("\n")
            file.write("       signature: ")
            file.write(str(b.transaction.signature))
            file.write("\n\n  ........................................................... \n,\n\n")
            file.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

        file.close()
