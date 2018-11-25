import random

class rsa_key:

    def __init__(self,bits_modulo = 2048,e = 2**16+1):
        # genera una clau RSA (de 2048 bits i amb exponent public 2**16+1 per defecte)

        self.primeP = 0
        self.primeQ = 0

        print('calculant primers per RSA...')

        while self.primeP == self.primeQ:
            self.primeP = self.generateLargePrime(bits_modulo) # p nombre primer
            self.primeQ = self.generateLargePrime(bits_modulo) # q nombre primer

        print('Sha calculat P:')
        print(self.primeP)
        print('Sha calculat Q:')
        print(self.primeQ)

        self.publicExponent = self.calculatePublicExponent((self.primeP - 1)*(self.primeQ - 1)) # e on 1 < e < phi(n) e i phi(n) primers entre ells

        print('Sha calculat publicExponent:')
        print(self.publicExponent)

        self.privateExponent = self.findModInverse(self.publicExponent, (self.primeP - 1) * (self.primeQ - 1)) # d

        print('Sha calculat privateExponent:')
        print(self.privateExponent)

        self.modulus = self.primeP * self.primeQ # n ==> n = p*q

        print('Sha calculat modulus:')
        print(self.modulus)

        self.privateExponentModulusPhiP = self.privateExponent % (self.primeP - 1) #d1 ==> d1 = d mod (p-1)
        self.privateExponentModulusPhiQ = self.privateExponent % (self.primeQ - 1) #d2 ==> d2 = d mod (q-1)
        self.inverseQModulusP = pow(self.primeQ, -1) % self.primeP #q1 ==> q1 = q^-1 mod p
        #AMB EL SEGON METODE NO ES NECESSARI self.inversePModulusQ = pow(self.primeP, -1) % self.primeQ #p1 ==> p1 = p^-1 mod q

        #CLAU PUBLICA (e,n)
        #CLAU PRIVADA (d,p,q,d1,d2,q1)

        print('Sha calculat tot')

        #CIFRAR c = m^e mod(n)

        #DESCIFRAR m = c^d mod n

        # DESCIFRAR METODE XINÈS
        # calcular cp = c mod p              cq = c mod q
        # calcular c1 = cp ^ d1 mod p        c2 = cq ^ d2 mod q
        # m = c1 * q1 * q + c2 * p1 * p mod n

        # DESCIFRAR PDF RSA METODE XINÈS. USAREM AQUEST
        # M = c1 * q1 * q + c2 * p1 * p mod n
        # h = (c1 - c2)q1 mod p
        # M = c2 + q * h

        print('anem a encriptar: ')
        missatge = 5
        print(missatge)
        missatgeEncriptat = (pow(missatge, self.publicExponent) % self.modulus)
        #NO FUNCIONA PERO HAURIA? (pow(missatge, self.publicExponent) % self.primeP) + (pow(missatge, self.publicExponent) % self.primeQ)
        print(missatgeEncriptat)
        missatgeDesencriptat = (pow(missatgeEncriptat, self.privateExponent) % self.modulus)
        print(missatgeDesencriptat)

    def sign(self,message):
        # retorma un enter que es la signatura de "message" feta amb la clau RSA fent servir el TXR
        a=5

    def sign_slow(self,message):
        # retorma un enter que es la signatura de "message" feta amb la clau RSA sense fer servir el TXR
        a=5

    def calculatePublicExponent(self, phiN):
        trobat = False
        while not trobat:
            e = random.randrange(1, phiN)
            print("POSSIBLE PUBLIC EXPONENT")
            print(e)
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
        # Returns True if num is a prime number.
        if num % 2 == 0 or num < 2:
            return False # Rabin-Miller doesn't work on even integers.
        if num == 3:
            return True
        s = num - 1
        t = 0
        while s % 2 == 0:
            # Keep halving s until it is odd (and use t
            # to count how many times we halve s):
            s = s // 2
            t += 1
        for trials in range(5): # Try to falsify num's primality 5 times.
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1: # This test does not apply if v is 1.
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
        return True

    def findModInverse(self, a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

        if self.gcd(a, m) != 1:
            return None # no mod inverse if a & m aren't relatively prime
        # Calculate using the Extended Euclidean Algorithm:
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3 # // is the integer division operator
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m

    def gcd(self, a, b):
    # Return the GCD of a and b using Euclid's Algorithm
        while a != 0:
            a, b = b % a, a
        return b
