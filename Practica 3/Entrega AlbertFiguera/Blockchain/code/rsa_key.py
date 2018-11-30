import random
import time
from rsa_public_key import rsa_public_key

class rsa_key:


#SIGN   ->  "DESENCRIPTAR CON TU PROPIA CLAVE PRIVADA"
#VERIFY ->  "ENCRIPTAR" CON LA CLAVE PUBLICA DE QUIEN LO HAYA FIRMADO

    def __init__(self,bits_modulo = 2048,e = 2**16+1):
        # genera una clau RSA (de 2048 bits i amb exponent public 2**16+1 per defecte)

        self.primeP = 0
        self.primeQ = 0

        #print("generando primos")
        while self.primeP == self.primeQ:
            self.primeP = self.generateLargePrime(int(bits_modulo/2)) # p nombre primer
            self.primeQ = self.generateLargePrime(int(bits_modulo/2)) # q nombre primer
        #print("primos generados")

        self.publicExponent = e
        self.privateExponent = self.findModInverse(self.publicExponent, (self.primeP - 1) * (self.primeQ - 1)) # d * e = 1 mod (phi(n))
        self.modulus = self.primeP * self.primeQ # n ==> n = p*q
        #print("private expoonent")
        #print(self.privateExponent)
        # print("fin exponent\n\n")

        self.privateExponentModulusPhiP = self.privateExponent % (self.primeP - 1) #d1 ==> d1 = d mod (p-1)
        self.privateExponentModulusPhiQ = self.privateExponent % (self.primeQ - 1) #d2 ==> d2 = d mod (q-1)
        self.inverseQModulusP = self.findModInverse(self.primeQ, self.primeP)

    def sign(self,message):
        # retorna un enter que es la signatura de "message" feta amb la clau RSA fent servir el TXR
        mp = pow(message, self.privateExponentModulusPhiP, self.primeP)
        mq = pow(message, self.privateExponentModulusPhiQ, self.primeQ)

        h = (mp - mq)*self.inverseQModulusP % self.primeP
        message = mq + self.primeQ * h
        return message

    def sign_slow(self,message):
        # retorna un enter que es la signatura de "message" feta amb la clau RSA sense fer servir el TXR
        return pow(message, self.privateExponent, self.modulus)

    def calculatePublicExponent(self, phiN):
        trobat = False
        while not trobat:
            e = random.randrange(1, phiN)
            # e ha de ser primer entre phi(n) on phi(n) = (p-1)*(q-1)
            if self.gcd(e, (self.primeP - 1) * (self.primeQ - 1)) == 1:
                trobat = True
                return e

    def generateLargePrime(self, bits_modulo):
        trobat = False
        while not trobat:
            prime = random.randrange(2**(bits_modulo-1), 2**(bits_modulo))
            if self.isPrime(prime):
                trobat = True
                return prime

    def isPrime(self, prime):
        return self.rabinMiller(prime)

    def rabinMiller(self,num):
        if num % 2 == 0 or num < 2:
            return False
        if num == 3:
            return True
        s = num - 1
        t = 0
        while s % 2 == 0:
            s = s // 2
            t += 1
        for trials in range(5):
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1:
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
        return True

    def findModInverse(self, a, m):
        if self.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m

    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def sign_timer(self,message):
        # igual que el metode sign, excepte que aquesta executa l'algorisme 200 cops en comptes d'1 i
        # no retorna cap resultat perque no ens importa

        t1 = time.clock() #A UNIX, retorna time de cpu

        for i in range(20):
            mp = pow(message, self.privateExponentModulusPhiP, self.primeP)
            mq = pow(message, self.privateExponentModulusPhiQ, self.primeQ)
            h = (mp - mq)*self.inverseQModulusP % self.primeP
            message = mq + self.primeQ * h

        t2 = time.clock()
        print(t2-t1)

    def sign_slow_timer(self,message):
        # igual que el metode sign_slow, excepte que aquesta executa l'algorisme 200 cops en comptes d'1 i
        # no retorna cap resultat perquè no ens importa

        t1 = time.clock() #A UNIX, retorna time de cpu
        for i in range(20):
            message = pow(message, self.privateExponent, self.modulus)

        t2 = time.clock()
        print(t2-t1)
