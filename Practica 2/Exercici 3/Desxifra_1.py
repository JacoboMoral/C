from Crypto.Cipher import AES

key = open("jacobo.key", 'rb').read()
enc = open("jacobo.enc", 'rb').read()
iv = enc[:AES.block_size]
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(enc[AES.block_size:])
open('soluciones/sol', 'wb').write(plaintext)
