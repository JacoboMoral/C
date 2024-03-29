# source:  https://github.com/boppreh/aes/blob/master/aes.py
from random import randint
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]


#no fa res, deixa el bloc s tal qual estava
def shift_rows(s):
    return


def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j] ^= k[i][j]


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])



r_con = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)


def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

def xor_bytes(a, b):
    """ Returns a new byte array with the elements xor'ed. """
    return bytes(i^j for i, j in zip(a, b))

def pad(plaintext):
    """
    Pads the given plaintext with PKCS#7 padding to a multiple of 16 bytes.
    Note that if the plaintext size is a multiple of 16,
    a whole block will be added.
    """
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding



class AES(object):
    """
    Class for AES-128 encryption with CBC mode and PKCS#7.
    This is a raw implementation of AES, without key stretching or IV
    management. Unless you need that, please use `encrypt` and `decrypt`.
    """
    rounds_by_key_size = {16: 10, 24: 12, 32: 14}
    def __init__(self, master_key):
        """
        Initializes the object with a given key.
        """
        assert len(master_key) in AES.rounds_by_key_size
        self.n_rounds = AES.rounds_by_key_size[len(master_key)]
        self._key_matrices = self._expand_key(master_key)

    def _expand_key(self, master_key):
        """
        Expands and returns a list of key matrices for the given master_key.
        """
        # Initialize round keys with raw key material.
        key_columns = bytes2matrix(master_key)
        iteration_size = len(master_key) // 4

        # Each iteration has exactly as many columns as the key material.
        columns_per_iteration = len(key_columns)
        i = 1
        while len(key_columns) < (self.n_rounds + 1) * 4:
            # Copy previous word.
            word = list(key_columns[-1])

            # Perform schedule_core once every "row".
            if len(key_columns) % iteration_size == 0:
                # Circular shift.
                word.append(word.pop(0))
                # Map to S-BOX.
                word = [s_box[b] for b in word]
                # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
                word[0] ^= r_con[i]
                i += 1
            elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
                # Run word through S-box in the fourth iteration when using a
                # 256-bit key.
                word = [s_box[b] for b in word]

            # XOR with equivalent word from previous iteration.
            word = xor_bytes(word, key_columns[-iteration_size])
            key_columns.append(word)

        # Group key words in 4x4 byte matrices.
        return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]

    def encrypt_block(self, plaintext):
        """
        Encrypts a single block of 16 byte long plaintext.
        """
        assert len(plaintext) == 16

        plain_state = bytes2matrix(plaintext)
        add_round_key(plain_state, self._key_matrices[0])

        #el codi original nomes feia 1 iteracio en aquest bucle i una altra fora, en comptes de
        #9 iteracions + 1 fora en el cas de AES-128
        for i in range(0, self.n_rounds-1, 1):
            sub_bytes(plain_state)
            shift_rows(plain_state)
            escriuBloc(-1,(plaintext))
            plaintext = [[138, 138, 138, 138],[138, 138, 138, 138],[138, 138, 138, 138],[138, 138, 138, 138]]
            plaintext = matrix2bytes(plaintext)
            mix_columns(plain_state)
            escriuBloc(-1,(plaintext))
            add_round_key(plain_state, self._key_matrices[i])

        sub_bytes(plain_state)
        shift_rows(plain_state)
        add_round_key(plain_state, self._key_matrices[-1])

        return matrix2bytes(plain_state)

    def encrypt_cbc(self, plaintext, iv):
        """
        Encrypts `plaintext` using CBC mode and PKCS#7 padding, with the given
        initialization vector (iv).
        """
        assert len(iv) == 16

        plaintext = pad(plaintext)
        blocks = []
        previous = iv
        plaintext_block = plaintext[0:16]
        # CBC mode encrypt: encrypt(plaintext_block XOR previous)
        block = self.encrypt_block(xor_bytes(plaintext_block, previous))
        blocks.append(block)
        previous = block
        return b''.join(blocks)

import os
from hashlib import pbkdf2_hmac
from hmac import new as new_hmac, compare_digest

AES_KEY_SIZE = 16
HMAC_KEY_SIZE = 16
IV_SIZE = 16

SALT_SIZE = 16
HMAC_SIZE = 32

def get_key_iv(password, salt, workload=100000):
    """
    Stretches the password and extracts an AES key, an HMAC key and an AES
    initialization vector.
    """
    stretched = pbkdf2_hmac('sha256', password, salt, workload, AES_KEY_SIZE + IV_SIZE + HMAC_KEY_SIZE)
    aes_key, rest = stretched[:AES_KEY_SIZE], stretched[AES_KEY_SIZE:]
    hmac_key, rest = stretched[:HMAC_KEY_SIZE], stretched[HMAC_KEY_SIZE:]
    iv = stretched[:IV_SIZE]
    return aes_key, hmac_key, iv


def encrypt(key, plaintext, workload=100000):
    """
    Encrypts `plaintext` with `key` using AES-128, an HMAC to verify integrity,
    and PBKDF2 to stretch the given key.
    The exact algorithm is specified in the module docstring.
    """
    if isinstance(key, str):
        key = key.encode('utf-8')
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
        print("vaya")
    salt = os.urandom(SALT_SIZE)
    key, hmac_key, iv = get_key_iv(key, salt, workload)
    ciphertext = AES(key).encrypt_cbc(plaintext, iv)
    hmac = new_hmac(hmac_key, salt + ciphertext, 'sha256').digest()
    assert len(hmac) == HMAC_SIZE

    #return hmac + salt + ciphertext
    return ciphertext


def escriuBloc(i, bloc):
    if i >= 0:
        print("Bloc numero: " + str(i//16))

    #bloc es un bloc de 16 bytes (128 bits)
    hexNumber = bloc.hex()
    matriu = [[0 for x in range(4)] for y in range(4)]

    for i in range(4):
        for j in range(4):
            matriu[j][i] = hexNumber[i*8+j*2] + hexNumber[i*8+j*2+1];

    for i in range(4):
        for j in range(4):
            print(matriu[i][j], end=' ')
        print()

def escriuBlocFile(file, bloc, missatge):
    #bloc es un bloc de 16 bytes (128 bits)
    hexNumber = bloc.hex()
    matriu = [[0 for x in range(4)] for y in range(4)]

    for i in range(4):
        for j in range(4):
            matriu[j][i] = hexNumber[i*8+j*2] + hexNumber[i*8+j*2+1];
    file.write(missatge + "\n")
    for i in range(4):
        for j in range(4):
            file.write(str(matriu[i][j]) + " ")
        file.write("\n")
    file.write("\n")

def emplenaRandom(bloc):
    #nomes emplena blocs de 4x4
    for i in range(4):
        bloc[i][0] = randint(0,255)
        bloc[i][1] = randint(0,255)
        bloc[i][2] = randint(0,255)
        bloc[i][3] = randint(0,255)

def canviaLetraString(string, index, lletra):
    string = list(string)
    string[index] = lletra
    return("".join(string))


def canviabit(num, index):
    numBinari = format(num,'08b')
    b = numBinari[index]
    if (b == "0"):
        b = "1"
    else:
        b = "0"
    numeroEnBinari = canviaLetraString(numBinari, index, b)
    return int(numeroEnBinari,base=2)

#Canviem la funcio ShiftRows per la identitat. Quins efectes te aquest canvi al xifrar un bloc?
#(Xifreu diferents M i els corresponents Mi amb la mateixa clau K i compareu C amb Ci.)
def exercici():
    key = 91988770966827344886319470096581337551
    key = key.to_bytes(16, byteorder='big', signed=True)
    missatgeBloc = [[None]*4 for _ in range(4)]
    file = open("shift_rows.txt","w")
    print("Escrivint ...")

    #generem 10 missatges aleatoris de mida d'un bloc
    for l in range(10):
        emplenaRandom(missatgeBloc)

        workload=100000
        salt = os.urandom(SALT_SIZE)
        key, hmac_key, iv = get_key_iv(key, salt, workload)
        AESObject = AES(key)
        encryptedFile = AESObject.encrypt_cbc(matrix2bytes(missatgeBloc), iv)

        escriuBlocFile(file,encryptedFile,"bloc original numero # " + str(l+1) + " encriptat: \n")

        for i in range(4):
            for j in range(4):
                originalValue = missatgeBloc[i][j]
                for k in range(8):
                    num = canviabit(missatgeBloc[i][j],k)
                    missatgeBloc[i][j] = num
                    encryptedFile = AESObject.encrypt_cbc(matrix2bytes(missatgeBloc), iv)
                    missatge = "#"+str(l+1) + " bloc encriptat despres de canviar el bit numero " + str(127-i*32-j*8-k)
                    escriuBlocFile(file,encryptedFile,missatge+"\n")
                    missatgeBloc[i][j] = originalValue


#exercici 2.1.2
def main():

    #exercici()
    plaintext = [[138, 138, 138, 138],[138, 138, 138, 138],[138, 138, 138, 138],[138, 138, 138, 138]]
    mix_columns(plaintext)
    escriuBloc(-1,matrix2bytes(plaintext))
    
main()
