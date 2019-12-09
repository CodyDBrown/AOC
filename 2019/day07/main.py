from AmplifierConrollerSoftware import AmplifierConrollerSoftware
from AmplifierConrollerSoftwareV2 import AmplifierConrollerSoftwareV2
import itertools

def fileToList(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split(',')
    numberList = []
    for n in text:
        numberList.append(int(n))
    return numberList

def partOneMain():
    Phases = [0,1,2,3,4]
    test = fileToList('input.txt')
    allPhases = list(itertools.permutations(Phases))
    MAX_OUTPUT = 0
    MAX_PHASES = []
    for phases in allPhases:
        ampOut = AmplifierConrollerSoftware(test, phases)
        if ampOut > MAX_OUTPUT:
            MAX_OUTPUT = ampOut
            MAX_PHASES = phases
    print("Max output is {}, and the phase list is {}".format(MAX_OUTPUT, MAX_PHASES))
     

def partTwoMain():
    Phases = [9,8,7,6,5]
    #test = fileToList('input.txt')
    test = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    #allPhases = list(itertools.permutations(Phases))
    MAX_OUTPUT = 0
    MAX_PHASES = []
    """
    for phases in allPhases:
        ampOut = AmplifierConrollerSoftwareV2(test, phases)
        if ampOut > MAX_OUTPUT:
            MAX_OUTPUT = ampOut
            MAX_PHASES = phases
            """
    ampOut = AmplifierConrollerSoftwareV2(test, Phases)
    print("Max output is {}, and the phase list is {}".format(ampOut, Phases))

if __name__ == "__main__":
    partOneMain()
    #partTwoMain()