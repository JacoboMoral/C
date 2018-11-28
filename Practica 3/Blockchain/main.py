import random
from rsa_key import rsa_key
from transaction import transaction
from block_chain import block_chain


myMessage = str(random.randrange(0,2**256))
myPrivateKey = rsa_key()
myTransaction = transaction(myMessage, myPrivateKey)

#es crea una nova blockchain amb un bloc, el genesis
myBlockchain = block_chain(myTransaction)

for i in range(99):
     myMessage = str(random.randrange(0,2**256))
     myPrivateKey = rsa_key()
     myTransaction = transaction(myMessage, myPrivateKey)
     myBlockchain.add_block(myTransaction)


print("Verificando blockchain...")
if myBlockchain.verify():
    print("Verificada correctament")
else:
    print("Blockchain no valida")
myBlockchain.writeFile("blockchain.txt")
