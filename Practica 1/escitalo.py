
f = open("2018_09_10_12_57_11_jacobo.moral.Escitalo", "r")
text = f.read()
#text = "IryyatbHmvaEhedLurlP"
k = 1;
name = "yes"
while name != "no":
    desencriptat = " ";
    for i in range(0, k):
        for j in range(i,len(text),k):
            desencriptat += text[j]

    print(desencriptat)
    k = k+1;
    name = input("Do you wish to continue? ")
