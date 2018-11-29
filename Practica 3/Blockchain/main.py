from rsa_key import rsa_key
from transaction import transaction
from block_chain import block_chain
import hashlib
import time
import random



##JACOBO
def execute_blockchains():
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

    print("Verificando blockchain de 100 bloques de Jacobo Moral...")
    if myBlockchain.verify():
        print("Verificada correctament la primera blockchain de Jacobo")
    else:
        print("Blockchain no valida")
    myBlockchain.writeFile("blockchain_100_jacobo")


    #__________________________________________________________


    myMessage = str(random.randrange(0,2**256))
    myPrivateKey = rsa_key()
    myTransaction = transaction(myMessage, myPrivateKey)
    xx = 92 #Jacobo Moral. Dni: xxxx7092

    #es crea una nova blockchain amb un bloc, el genesis
    myBlockchain = block_chain(myTransaction)

    for i in range(xx):
         myMessage = str(random.randrange(0,2**256))
         myPrivateKey = rsa_key()
         myTransaction = transaction(myMessage, myPrivateKey)
         myBlockchain.add_block(myTransaction)


    for i in range(99-xx):
        myMessage = str(random.randrange(0,2**256))
        myPrivateKey = rsa_key()
        myTransaction = transaction(myMessage, myPrivateKey)
        myBlockchain.add_block_invalid(myTransaction)


    print("Verificando blockchain de 100 - xx bloques de Jacobo Moral...")
    if myBlockchain.verify():
        print("Verificada correctament la segunda blockchain de Jacobo")
    else:
        print("Blockchain no valida")
    myBlockchain.writeFile("blockchain_100_xx_jacobo")


    #__________________________________________________________
    #__________________________________________________________


    ##ALBERT

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

    print("Verificando blockchain de 100 bloques de Albert Figuera...")
    if myBlockchain.verify():
        print("Verificada correctament la primera blockchain de Albert")
    else:
        print("Blockchain no valida")
    myBlockchain.writeFile("blockchain_100_albert")


    #__________________________________________________________

    myMessage = str(random.randrange(0,2**256))
    myPrivateKey = rsa_key()
    myTransaction = transaction(myMessage, myPrivateKey)
    xx = 72 #Albert Figuera. Dni: xxxx8272

    #es crea una nova blockchain amb un bloc, el genesis
    myBlockchain = block_chain(myTransaction)

    for i in range(xx):
         myMessage = str(random.randrange(0,2**256))
         myPrivateKey = rsa_key()
         myTransaction = transaction(myMessage, myPrivateKey)
         myBlockchain.add_block(myTransaction)


    for i in range(99-xx):
         myMessage = str(random.randrange(0,2**256))
         myPrivateKey = rsa_key()
         myTransaction = transaction(myMessage, myPrivateKey)
         myBlockchain.add_block_invalid(myTransaction)


    print("Verificando blockchain de 100 - xx bloques de Albert Figuera...")
    if myBlockchain.verify():
        print("Verificada correctament la segunda blockchain de Albert")
    else:
        print("Blockchain no valida")
    myBlockchain.writeFile("blockchain_100_xx_albert")


myMessage = None
messageHash512 = None
myPrivateKey = None

def setupTiming():
    global myMessage
    global myPrivateKey
    global messageHash512

    myMessage = str(random.randrange(0,2**256))
    messageHash512 = int(hashlib.sha512(myMessage.encode('utf-8')).hexdigest(), 16)
    myPrivateKey = rsa_key()

def time_sign():
    print("Comenzado temporizador de metodo Sign")
    for i in range(100):
        setupTiming()
        myPrivateKey.sign_timer(messageHash512)
    print("Terminado temporizador de metodo Sign")

def time_sign_slow():
    print("Comenzado temporizador de metodo Sign_slow")
    for i in range(100):
        setupTiming()
        myPrivateKey.sign_slow_timer(messageHash512)
    print("Terminado temporizador de metodo Sign_slow")

time_sign()
time_sign_slow()
