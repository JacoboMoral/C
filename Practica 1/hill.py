import pprint
import operator
import numpy as np
pp = pprint.PrettyPrinter(indent=4)
characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def trigramToString(trigram):
    charList = [characters[trigram[0]], characters[trigram[1]], characters[trigram[2]]]
    string = "".join(charList)
    return string

def stringToTrigram(string):
    return [characters.index(string[0]), characters.index(string[1]), characters.index(string[2])]


def getTrigramas():
    f = open("2018_09_10_12_57_11_jacobo.moral.Hill", "r")
    text = f.read()
    trigramas = {}
    for i in range(0,len(text),3):
        trigrama = "";
        trigrama = trigrama + text[i] + text[i+1] + text[i+2];
        if trigrama in trigramas:
            trigramas[trigrama] = trigramas[trigrama] + 1
        else:
            trigramas[trigrama] = 1;
    trigramas = sorted(trigramas.items(), key=operator.itemgetter(1))
    return trigramas

def multKeyInverseWithTrigram(keyInverse, trigram):
    multResult = np.matmul(keyInverse, trigram)
    for i in range(0,len(multResult)):
        multResult[i] = multResult[i]%26
    return multResult

def main():
    f = open("2018_09_10_12_57_11_jacobo.moral.Hill", "r")
    cypheredText = f.read()
    trigramas = getTrigramas()
    inverseKey = np.array([[5, 7, 8], [2, 16, 9], [4, 15, 20]])
    text = ""

    for i in range(0,len(cypheredText),3):
        cypheredTrigram = cypheredText[i] + cypheredText[i+1] + cypheredText[i+2]
        text = text + trigramToString(multKeyInverseWithTrigram(inverseKey,stringToTrigram(cypheredTrigram)))
        #print (trigramToString(multKeyInverseWithTrigram(inverseKey,stringToTrigram(trigramas[i][0]))))

    #pp.pprint(getTrigramas())
    print(text)






main()
