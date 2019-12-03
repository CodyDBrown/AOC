INDEX = 0

def fileToList(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split(',')
    numberList = []
    for n in text:
        numberList.append(int(n))
    return numberList

def InputCorrection(One, Two, numbers):
    numbers[1] = One
    numbers[2] = Two
    return numbers

def Check(numbers):
    global INDEX
    while(True):
        if numbers[INDEX] == 1:
            indexOne = numbers[INDEX + 1]
            indexTwo = numbers[INDEX + 2]
            outPut = numbers[INDEX + 3]
         
            numbers[outPut] = numbers[indexOne] + numbers[indexTwo]
         
            INDEX += 4
        elif numbers[INDEX] == 2:
            indexOne = numbers[INDEX + 1]
            indexTwo = numbers[INDEX + 2]
            outPut = numbers[INDEX + 3]
            numbers[outPut] = numbers[indexOne] * numbers[indexTwo]
            INDEX += 4
          
        elif numbers[INDEX] == 99:
            
            return numbers[0]
        else:
            print("ERROR", numbers[INDEX])
            return None

def partOneMain():
    global INDEX
    INDEX = 0
    numbers = fileToList("input.txt")
    numbers = InputCorrection(12, 2, numbers)
    answer = Check(numbers)
    print("Answer to part one is:", answer)
    

def partTwoMain():
    global INDEX
    answer = 0
    
    for noun in range(100):
        for verb in range(100):
            numbers = fileToList("input.txt")
            INDEX = 0
            numbers = InputCorrection(noun, verb, numbers)
            answer = Check(numbers)
            #print(answer, noun, verb)
            if (answer == 19690720):
                print(100*noun+verb)
                return answer
    
                

if __name__ == "__main__":
    partOneMain()
    partTwoMain()