
f = open("2018_09_10_12_57_11_jacobo.moral.Escitalo", "r")
text = f.read()
#text = "IryyatbHmvaEhedLurlP" #4
#text = "itaLavdPmel hry uyH rbE" #4
#text = "ivlaeymrHhyEubLraPtd" #3
k = 114;
name = "yes"
while name != "no":
    desencriptat = " ";
    for i in range(0, k):
        for j in range(i,len(text),k):
            desencriptat += text[j]

    print(desencriptat)
    print(k)
    #if " ﻿The Project Gutenberg" in desencriptat:
    #    print(desencriptat)
    #    name = "no"
    #print(k)
    k = k+1;
    name = input("Do you wish to continue? ")
w = open("JacoboMoralBuendia_114.escital","w")
w.write(desencriptat)
