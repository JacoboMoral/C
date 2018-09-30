import pprint
import operator
pp = pprint.PrettyPrinter(indent=4)

def getTripletes():
    f = open("2018_09_10_12_57_11_jacobo.moral.Hill", "r")
    text = f.read()
    tripletes = {}
    for i in range(0,len(text),3):
        triplete = "";
        triplete = triplete + text[i] + text[i+1] + text[i+2];
        if triplete in tripletes:
            tripletes[triplete] = tripletes[triplete] + 1
        else:
            tripletes[triplete] = 1;
    tripletes = sorted(tripletes.items(), key=operator.itemgetter(1))
    return tripletes
def main():
    pp.pprint(getTripletes())







main()
