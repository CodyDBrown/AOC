from IntcodeComputerV6 import IntcodeComputer

def fileToList(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split(',')
    numberList = []
    for n in text:
        numberList.append(int(n))
    return numberList

def addMemory(numbers):
    for _ in range(len(numbers)*100):
        numbers.append(0)
    return numbers
def partOneMain():
    numbers = fileToList("input.txt")
    #numbers = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    numbers = addMemory(numbers)
    IntcodeComputer(numbers)
def partTwoMain():
    pass

if __name__ == "__main__":
    partOneMain()
    partTwoMain()
