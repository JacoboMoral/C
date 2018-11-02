from Crypto.Cipher import AES

key = open("albert.key", 'rb').read()
enc = open("albert.enc", 'rb').read()

iv = enc[:AES.block_size]

#Albert Figuera Pérez
cipher = AES.new(key, AES.MODE_CFB, iv)

#Jacobo Moral Buendía
cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = cipher.decrypt(enc[AES.block_size:])
open('soluciones/albert.jpeg', 'wb').write(plaintext)
open('soluciones/albert.html', 'wb').write(plaintext)
