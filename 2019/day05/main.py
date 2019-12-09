from IntcodeComputer import IntcodeComputer

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
    numbers = fileToList("input.txt")
    # print(numbers)
    #numbers = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    IntcodeComputer(numbers)


if __name__ == "__main__":
    partOneMain()