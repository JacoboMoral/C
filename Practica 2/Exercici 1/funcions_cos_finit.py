import time
import random

#taules com a variables globals sinizialitzen a GF_tables()
tableOfExp = [None]*256
tableOfLog = [None]*256

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap


def GF_product_p(a, b):
    result = 0

    for i in range(8):
        a &= 255
        if b & 1 == 1:
            result ^= a
        maxBit = a & 128   #128 = 0x80
        a <<= 1
        if maxBit == 128:
            a ^= 27 #27 = 0x1B
        b >>= 1
    return result

def GF_tables():
    global tableOfExp
    global tableOfLog

    tableOfExp[0] = 1;

    for i in range (1,256):
        tableOfExp[i] = GF_product_p(tableOfExp[i-1], 3) #no fa falta calcular potencies a cada posicio perque basta amb calcular el nombre de la posicio anterior per 3
        tableOfLog[tableOfExp[i-1] & 255] = (i-1)
    return

def GF_product_t(a, b):
    if a == 0 or b == 0:  #qualsevol a o b multiplicat per 0 retorna 0
        return 0
    pos = (tableOfLog[a & 255] & 255) + (tableOfLog[b & 255] & 255)
    if(pos > 255):
        return tableOfExp[pos-255]
    return tableOfExp[pos]

@timing
def GF_product_p_x(x):
    for i in range (0,5000000):
        GF_product_p(i%256,x)
    return

@timing
def GF_product_t_x(x):
    for i in range (0,5000000):
        GF_product_t(i%256,x)
    return

@timing
def GF_product_t_vs():
    for i in range (0, 5000000):
        GF_product_t(random.randint(0,255), random.randint(0,255))

@timing
def GF_product_p_vs():
    for i in range (0, 5000000):
        GF_product_t(random.randint(0,255), random.randint(0,255))


def GF_generador():
    generadors = []
    for i in range (256):
        result = 1
        aux = None
        for j in range (1,256):
            result = GF_product_p(i,result)
            if result == 1 and aux is None:
                aux = j
        if aux == 255: #si result == 255 significa que result = 1
            generadors.append(i)
    return generadors

def GF_invers(a):
    if (a == 0): return 0
    return (tableOfExp[255-tableOfLog[a & 255] & 255])


def main():
    GF_tables()
    # print(tableOfExp)
    # print(tableOfLog)

    print(GF_generador())

    #GF_product_p vs GF_product_t
    GF_product_p_vs()
    GF_product_t_vs()

    #GF_product_p(a,0x02) vs GF_product_t(a,0x02)
    GF_product_p_x(2)
    GF_product_t_x(2)

    #GF_product_p(a,0x03) vs GF_product_t(a,0x03)
    GF_product_p_x(3)
    GF_product_t_x(3)

    #GF_product_p(a,0x09) vs GF_product_t(a,0x09)
    GF_product_p_x(9)
    GF_product_t_x(9)

    #GF_product_p(a,0x0B) vs GF_product_t(a,0x0B)
    GF_product_p_x(11)
    GF_product_t_x(11)

    #GF_product_p(a,0x0D) vs GF_product_t(a,0x0D)
    GF_product_p_x(13)
    GF_product_t_x(13)

    #GF_product_p(a,0x0E) vs GF_product_t(a,0x0E)
    GF_product_p_x(15)
    GF_product_t_x(15)


main()
