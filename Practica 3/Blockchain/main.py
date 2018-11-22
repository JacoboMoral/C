from rsa_key import rsa_key
from transaction import transaction
from block_chain import block_chain


myMessage = "Mi mensaje 1"
myPrivateKey = rsa_key()
myTransaction = transaction(myMessage, myPrivateKey)

#es crea una nova blockchain amb un blocs, el genesis
myBlockchain = blockchain(myTransaction)

myMessage = "Mi mensaje 2"
myTransaction = transaction(myMessage, myPrivateKey)

#es crea una nova blockchain amb dos blocs, el genesis i un altre
myBlockchain.add_block(myTransaction)