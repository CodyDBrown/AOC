def readInput(filePath):
    # Read in the numbers
    file = open(filePath, "r")
    
    numbers = file.read()
    
    file.close()
    return numbers

def nextCheck(numbers):
    answer = 0
    for n in range(len(numbers)-1):
        if(numbers[n] == numbers[n+1]):
            answer += int(numbers[n])
    # List is circular so I need to check first and last numbers
    if(numbers[0] == numbers[-1]):
        answer += int(numbers[0])
    
    return answer

def rightInTwo(numbers):
    size = len(numbers)
    numbersOne = numbers[:size//2]
    numbersTwo = numbers[size//2:]
    return numbersOne, numbersTwo
       
def halfCheck(numbers):
    answer = 0
    first, second, = rightInTwo(numbers)
    for n, m in zip(first, second):
        if(n == m):
            answer += int(n)*2
    return answer
    

def partOneMain():
    numbers = readInput("input.txt")
    
    print("Answer for part one: ", nextCheck(numbers))
 
def partTwoMain():
    numbers = readInput("input.txt")
    print("Answer for part two: ", halfCheck(numbers))

if __name__ == "__main__":
    partOneMain()
    partTwoMain()